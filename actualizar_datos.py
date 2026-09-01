import json
import os
import requests
import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def format_date_es(date_str):
    if not date_str or date_str == 'N/D':
        return 'N/D'
    try:
        parts = date_str.split('-')
        if len(parts) >= 2:
            year = parts[0]
            month = int(parts[1])
            months_es = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
            m_str = months_es[month - 1]
            if len(parts) == 3 and parts[2] not in ['01', '30', '31']:
                day = int(parts[2])
                return f"{day} {m_str} {year}"
            return f"{m_str} {year}"
    except Exception:
        pass
    return date_str

def get_indicator_unit_meta(key, name, cat_name):
    k = key.lower()
    n = name.lower()

    if k == 'riesgo_pais':
        return {'type': 'bps', 'prefix': '', 'suffix': ' bps', 'decimals': 0}

    # Percentages (%)
    if (k.endswith('_pbi') or k.startswith('ratio_') or 'cobertura' in k or 'cobertura' in n or
        'interanual' in k or 'interanual' in n or 
        'tasa' in n or 'variación' in n or 'variacion' in n or 'porcentaje' in n or 
        'desocupacion' in k or 'actividad' in k or 'indigencia' in k or 'pobreza' in k or 
        'empleo_val' in k or 'salarios_indice' in k or 'isac_general' in k or 
        'ipc' in k or 'ipi' in k or 'emae_interanual' in k or k == 'supermercados_ventas' or 
        'pbi_interanual' in k or 'emae_agro' in k or '%' in n):
        return {'type': 'percent', 'prefix': '', 'suffix': '%', 'decimals': 2}

    # Debt and Reserves in USD Millions
    if ('deuda_' in k and not k.endswith('_pbi')) or k == 'reservas_brutas' or k == 'reservas_bcra':
        return {'type': 'currency_usd', 'prefix': 'USD ', 'suffix': ' M', 'decimals': 2}

    # Standard USD
    if k.endswith('_usd') or 'usd' in k or 'en usd' in n or 'en dólares' in n or 'en dolares' in n:
        return {'type': 'currency_usd', 'prefix': 'USD ', 'suffix': '', 'decimals': 2}

    # Quantities & Indices
    if 'poblacion' in k:
        return {'type': 'quantity', 'prefix': '', 'suffix': ' hab.', 'decimals': 0}
    if 'empleo_privado' in k or 'empleo_total' in k:
        return {'type': 'quantity', 'prefix': '', 'suffix': ' mil', 'decimals': 1}
    if 'gas_produccion' in k:
        return {'type': 'quantity', 'prefix': '', 'suffix': ' MM m³/d', 'decimals': 2}
    if 'petroleo_produccion' in k:
        return {'type': 'quantity', 'prefix': '', 'suffix': ' m³/d', 'decimals': 2}
    if 'cemento_total' in k:
        return {'type': 'quantity', 'prefix': '', 'suffix': ' Tn', 'decimals': 1}
    if 'isac_' in k or 'icc_' in k or 'indice_salarios_ipc' in k or 'emae_construccion' in k or 'supermercados_ventas_valor' in k:
        return {'type': 'index', 'prefix': '', 'suffix': ' pts', 'decimals': 2}

    # Currency ARS ($)
    return {'type': 'currency_ars', 'prefix': '$', 'suffix': '', 'decimals': 2}

def format_value_with_meta(val, meta, compact=False):
    if val is None or (isinstance(val, float) and val != val):
        return 'N/D'
    num = float(val)
    dec = meta.get('decimals', 2)

    if compact and abs(num) >= 1_000_000_000:
        formatted = f"{num / 1_000_000_000:,.1f} B"
    elif compact and abs(num) >= 1_000_000:
        formatted = f"{num / 1_000_000:,.1f} M"
    else:
        formatted = f"{num:,.{dec}f}"

    return f"{meta.get('prefix', '')}{formatted}{meta.get('suffix', '')}"

def adjust_series_to_constant(dates, nominal_prices, ipc_dict):
    n = len(dates)
    if n == 0 or len(nominal_prices) == 0:
        return []

    indices = [1.0] * n
    for i in range(1, n):
        ym = dates[i][:7]
        m_rate = ipc_dict.get(ym, 0.0)
        indices[i] = indices[i-1] * (1.0 + m_rate / 100.0)

    final_idx = indices[-1] if indices else 1.0
    constant_prices = []
    for i in range(n):
        factor = (final_idx / indices[i]) if indices[i] > 0 else 1.0
        constant_prices.append(round(nominal_prices[i] * factor, 2))

    return constant_prices

def compute_aggregate_to_pbi(dates, prices, pbi_dict, mode='billones'):
    ratio_dates = []
    ratio_prices = []
    for d, p in zip(dates, prices):
        ym = d[:7]
        if ym in pbi_dict:
            pbi_val = pbi_dict[ym]
            if pbi_val > 0:
                if mode == 'billones':
                    agg_m = p * 1_000_000
                elif mode == 'miles':
                    agg_m = p / 1_000
                else:
                    agg_m = p
                r = round((agg_m / pbi_val) * 100, 2)
                ratio_dates.append(d)
                ratio_prices.append(r)
    return ratio_dates, ratio_prices

def build_ratio_series(num_series, den_dict, is_pct=True):
    r_dates = []
    r_prices = []
    dates = num_series.get('dates', [])
    prices = num_series.get('prices', [])
    for d, num_val in zip(dates, prices):
        ym = d[:7]
        if ym in den_dict and den_dict[ym] > 0:
            den_val = den_dict[ym]
            mult = 100.0 if is_pct else 1.0
            r = round((num_val / den_val) * mult, 2)
            r_dates.append(d)
            r_prices.append(r)
    return r_dates, r_prices

def sample_sparkline_series(dates, prices, freq):
    if not dates or not prices:
        return []
    if freq == "Diario" and len(prices) > 60:
        step = max(1, len(prices[-250:]) // 24)
        sample = prices[-250:][::step]
        if prices[-1] not in sample:
            sample.append(prices[-1])
        return sample[-24:]
    return prices[-24:] if len(prices) >= 24 else prices

def reconstruct_and_order_dataset():
    print("==========================================================================")
    print("ACTUALIZANDO DATASET CON JUBILACIONES CONSTANTES (AJUSTADAS POR IPC)...")
    print("==========================================================================")

    master_path = r'g:\Mi unidad\IA\Tablero-Economía\master_dataset.json'
    with open(master_path, 'r', encoding='utf-8') as f:
        master_data = json.load(f)

    ref_cats = master_data.get('categories', [])
    ref_hdb = master_data.get('historical_db', {})

    # Live APIs
    try:
        r = requests.get("https://api.argentinadatos.com/v1/finanzas/indices/inflacion", timeout=8).json()
        ipc_dates = [x["fecha"] for x in r if "fecha" in x and "valor" in x]
        ipc_prices = [float(x["valor"]) for x in r if "fecha" in x and "valor" in x]
        if ipc_dates:
            ref_hdb["ipc_mensual"] = {"dates": ipc_dates, "prices": ipc_prices}
    except Exception as e:
        print("[WARN] IPC:", e)

    try:
        r = requests.get("https://api.argentinadatos.com/v1/finanzas/indices/inflacionInteranual", timeout=8).json()
        ia_dates = [x["fecha"] for x in r if "fecha" in x and "valor" in x]
        ia_prices = [float(x["valor"]) for x in r if "fecha" in x and "valor" in x]
        if ia_dates:
            ref_hdb["ipc_interanual"] = {"dates": ia_dates, "prices": ia_prices}
    except Exception as e:
        print("[WARN] IPC Interanual:", e)

    try:
        r = requests.get("https://api.argentinadatos.com/v1/finanzas/indices/riesgo-pais", timeout=8).json()
        rp_dates = [x["fecha"] for x in r if "fecha" in x and "valor" in x]
        rp_prices = [float(x["valor"]) for x in r if "fecha" in x and "valor" in x]
        if rp_dates:
            ref_hdb["riesgo_pais"] = {"dates": rp_dates, "prices": rp_prices}
    except Exception as e:
        print("[WARN] Riesgo País:", e)

    try:
        r = requests.get("https://api.argentinadatos.com/v1/finanzas/indices/uva", timeout=8).json()
        uva_dates = [x["fecha"] for x in r if "fecha" in x and "valor" in x]
        uva_prices = [float(x["valor"]) for x in r if "fecha" in x and "valor" in x]
        if uva_dates:
            ref_hdb["uva_val"] = {"dates": uva_dates, "prices": uva_prices}
    except Exception as e:
        print("[WARN] UVA:", e)

    # 1. CANASTAS A PRECIOS CONSTANTES
    ipc_dict = {}
    ipc_series = ref_hdb.get("ipc_mensual", {})
    if ipc_series:
        for d, p in zip(ipc_series.get("dates", []), ipc_series.get("prices", [])):
            ipc_dict[d[:7]] = float(p)

    canastas_to_adjust = [
        ("canasta_alimentaria_val", "canasta_alimentaria_constante", "Canasta Básica Alimentaria a Precios Constantes", "Mide el costo histórico de la CBA ajustado por inflación (IPC) a pesos del último dato disponible. Refleja la variación real de la línea de indigencia."),
        ("canasta_alimentaria_hogar2", "canasta_alimentaria_hogar2_constante", "CBA Familiar (Hogar 2) a Precios Constantes", "Costo histórico de la CBA para un hogar de 4 integrantes ajustado por inflación (IPC) a pesos del último dato disponible."),
        ("canasta_total_val", "canasta_total_constante", "Canasta Básica Total a Precios Constantes", "Mide el costo histórico de la CBT ajustado por inflación (IPC) a pesos del último dato disponible. Refleja la variación real de la línea de pobreza."),
        ("canasta_total_hogar2", "canasta_total_hogar2_constante", "CBT Familiar (Hogar 2) a Precios Constantes", "Costo histórico de la CBT para un hogar de 4 integrantes ajustado por inflación (IPC) a pesos del último dato disponible.")
    ]

    for nom_key, const_key, const_name, const_desc in canastas_to_adjust:
        if nom_key in ref_hdb:
            nom_s = ref_hdb[nom_key]
            dates = nom_s.get("dates", [])
            prices = nom_s.get("prices", [])
            if dates and prices:
                const_prices = adjust_series_to_constant(dates, prices, ipc_dict)
                ref_hdb[const_key] = {"dates": dates, "prices": const_prices}

    # 2. JUBILACIONES A PRECIOS CONSTANTES (AJUSTADAS POR IPC)
    jubilaciones_to_adjust = [
        ("jubilacion_minima", "jubilacion_minima_constante", "Jubilación Mínima a Precios Constantes", "Monto histórico del haber mínimo de ANSES ajustado por inflación (IPC) a pesos del último dato disponible. Refleja la evolución del poder adquisitivo real."),
        ("jubilacion_maxima", "jubilacion_maxima_constante", "Jubilación Máxima a Precios Constantes", "Monto histórico del haber máximo previsional ajustado por inflación (IPC) a pesos del último dato disponible."),
        ("jubilacion_promedio", "jubilacion_promedio_constante", "Jubilación Promedio a Precios Constantes", "Haber previsional medio del SIPA ajustado por inflación (IPC) a pesos del último dato disponible.")
    ]

    for nom_key, const_key, const_name, const_desc in jubilaciones_to_adjust:
        if nom_key in ref_hdb:
            nom_s = ref_hdb[nom_key]
            dates = nom_s.get("dates", [])
            prices = nom_s.get("prices", [])
            if dates and prices:
                const_prices = adjust_series_to_constant(dates, prices, ipc_dict)
                ref_hdb[const_key] = {"dates": dates, "prices": const_prices}

    # 3. AGREGADOS MONETARIOS / PBI
    pbi_dict = {}
    pbi_s = ref_hdb.get("pbi_corriente", {})
    if pbi_s:
        for d, p in zip(pbi_s.get("dates", []), pbi_s.get("prices", [])):
            pbi_dict[d[:7]] = float(p)

    monetary_pbi_specs = [
        ("agregado_b1", "agregado_b1_pbi", "Agregado Monetario B1 (M1) / PBI", "Mide la relación entre el Agregado B1 (circulante + depósitos a la vista en pesos y USD) y el PBI corriente. Refleja la liquidez transaccional sobre el producto.", "billones"),
        ("agregado_b2", "agregado_b2_pbi", "Agregado Monetario B2 (M2) / PBI", "Mide la relación entre el Agregado B2 (B1 + depósitos en cajas de ahorro en pesos y USD) y el PBI corriente.", "billones"),
        ("agregado_b3", "agregado_b3_pbi", "Agregado Monetario B3 (M3) / PBI", "Mide la relación entre el Agregado B3 (M3 amplio: B2 + plazos fijos en pesos y USD) y el PBI corriente. Indica el grado de profundidad financiera total.", "billones"),
        ("base_monetaria", "base_monetaria_pbi", "Base Monetaria / PBI", "Mide la relación entre la Base Monetaria (circulante + encajes) y el PBI corriente. Refleja la monetización básica de la economía.", "billones"),
        ("billetes_circulacion", "billetes_circulacion_pbi", "Billetes en Circulación / PBI", "Mide la relación entre el dinero físico en poder del público y el PBI corriente.", "miles")
    ]

    for agg_key, pbi_key, pbi_name, pbi_desc, mode in monetary_pbi_specs:
        if agg_key in ref_hdb and pbi_dict:
            agg_s = ref_hdb[agg_key]
            dates = agg_s.get("dates", [])
            prices = agg_s.get("prices", [])
            if dates and prices:
                rd, rp = compute_aggregate_to_pbi(dates, prices, pbi_dict, mode)
                if rd and rp:
                    ref_hdb[pbi_key] = {"dates": rd, "prices": rp}

    # 4. RESERVAS Y DEUDA COMPARATIVAS / RATIOS
    pbi_usd_s = ref_hdb.get("pbi_usd_mep", {})
    pbi_usd_dict = {d[:7]: p for d, p in zip(pbi_usd_s.get("dates", []), pbi_usd_s.get("prices", []))}
    res_s = ref_hdb.get("reservas_brutas", {})
    deuda_tot_s = ref_hdb.get("deuda_publica_total", {})
    deuda_ext_s = ref_hdb.get("deuda_externa", {})
    deuda_pub_ext_s = ref_hdb.get("deuda_publica_externa", {})
    deuda_fmi_s = ref_hdb.get("deuda_publica_fmi", {})

    deuda_ratios_specs = [
        ("deuda_publica_total_pbi", "Deuda Pública Total / PBI", "Mide la relación porcentual entre el stock total de deuda pública bruta del Estado Nacional y el Producto Bruto Interno expresado en USD.", deuda_tot_s, pbi_usd_dict, "Secretaría de Finanzas / INDEC", "Mensual"),
        ("deuda_externa_pbi", "Deuda Externa Total / PBI", "Ratio entre la Deuda Externa Bruta Total (sectores público y privado) y el PBI anualizado.", deuda_ext_s, pbi_usd_dict, "INDEC / Min. Economía", "Trimestral"),
        ("deuda_publica_externa_pbi", "Deuda Pública Externa / PBI", "Ratio entre los títulos y compromisos públicos en moneda extranjera y el PBI.", deuda_pub_ext_s, pbi_usd_dict, "Secretaría de Finanzas", "Mensual"),
        ("deuda_publica_fmi_pbi", "Deuda Pública con el FMI / PBI", "Porcentaje que representa el pasivo soberano con el Fondo Monetario Internacional respecto al PBI.", deuda_fmi_s, pbi_usd_dict, "Secretaría de Finanzas / FMI", "Mensual"),
        ("reservas_pbi", "Reservas Internacionales / PBI", "Mide el stock de reservas brutas del Banco Central como porcentaje del Producto Bruto Interno.", res_s, pbi_usd_dict, "BCRA / INDEC", "Diario"),
        ("ratio_reservas_deuda_externa", "Cobertura de Reservas / Deuda Externa", "Porcentaje de la Deuda Externa Total cubierto por las Reservas Internacionales Brutas del BCRA.", res_s, {d[:7]: p for d, p in zip(deuda_ext_s.get('dates', []), deuda_ext_s.get('prices', []))}, "BCRA / INDEC", "Mensual"),
        ("ratio_reservas_deuda_fmi", "Cobertura de Reservas / Deuda FMI", "Relación porcentual entre las Reservas Brutas del BCRA y los vencimientos de deuda con el FMI.", res_s, {d[:7]: p for d, p in zip(deuda_fmi_s.get('dates', []), deuda_fmi_s.get('prices', []))}, "BCRA / Min. Economía", "Mensual")
    ]

    for r_key, r_name, r_desc, num_s, den_d, r_src, r_freq in deuda_ratios_specs:
        rd, rp = build_ratio_series(num_s, den_d, is_pct=True)
        if rd and rp:
            ref_hdb[r_key] = {"dates": rd, "prices": rp}

    # Ensure Riesgo País is in ref_hdb
    if "riesgo_pais" not in ref_hdb:
        try:
            r = requests.get("https://api.argentinadatos.com/v1/finanzas/indices/riesgo-pais", timeout=8).json()
            rp_dates = [x["fecha"] for x in r if "fecha" in x and "valor" in x]
            rp_prices = [float(x["valor"]) for x in r if "fecha" in x and "valor" in x]
            if rp_dates:
                ref_hdb["riesgo_pais"] = {"dates": rp_dates, "prices": rp_prices}
        except Exception:
            pass

    precios_ordered_keys = [
        "canasta_alimentaria_val", "canasta_alimentaria_constante", "canasta_alimentaria_usd",
        "canasta_alimentaria_hogar2", "canasta_alimentaria_hogar2_constante", "canasta_alimentaria_hogar2_usd",
        "canasta_total_val", "canasta_total_constante", "canasta_total_usd",
        "canasta_total_hogar2", "canasta_total_hogar2_constante", "canasta_total_hogar2_usd",
        "ipc_mensual", "ipc_interanual", "ipc_nucleo_mensual", "ipc_nucleo_interanual",
        "ipc_mayorista_mensual", "ipc_mayorista_interanual", "uva_val"
    ]

    monetario_ordered_keys = [
        "agregado_b1", "agregado_b1_pbi", "agregado_b1_usd",
        "agregado_b2", "agregado_b2_pbi", "agregado_b2_usd",
        "agregado_b3", "agregado_b3_pbi", "agregado_b3_usd",
        "base_monetaria", "base_monetaria_pbi", "base_monetaria_usd",
        "billetes_circulacion", "billetes_circulacion_pbi", "billetes_circulacion_usd"
    ]

    reservas_deuda_ordered_keys = [
        "reservas_brutas", "reservas_pbi", "ratio_reservas_deuda_externa", "ratio_reservas_deuda_fmi",
        "deuda_publica_total", "deuda_publica_total_pbi",
        "deuda_externa", "deuda_externa_pbi",
        "deuda_publica_externa", "deuda_publica_externa_pbi",
        "deuda_publica_fmi", "deuda_publica_fmi_pbi",
        "deuda_publica_pesos", "riesgo_pais"
    ]

    jubilaciones_ordered_keys = [
        "jubilacion_minima", "jubilacion_minima_constante", "jubilacion_minima_usd",
        "jubilacion_maxima", "jubilacion_maxima_constante", "jubilacion_maxima_usd",
        "jubilacion_promedio", "jubilacion_promedio_constante", "jubilacion_promedio_usd"
    ]

    category_icons = {
        "Precios y Costo de Vida": "fa-tags",
        "Agregados Monetarios": "fa-money-bill-wave",
        "Sector Fiscal": "fa-landmark",
        "Comercio Internacional": "fa-ship",
        "Reservas y Deuda": "fa-vault",
        "Empleo y Salarios": "fa-user-tie",
        "Datos Demográficos": "fa-users",
        "Jubilaciones y Social": "fa-hands-holding-circle",
        "Actividad y Consumo": "fa-chart-line",
        "Industria y Energía": "fa-industry",
        "Campo y Bioeconomía": "fa-wheat-awn",
        "Construcción e Inmobiliario": "fa-trowel-bricks"
    }

    category_slugs = {
        "Precios y Costo de Vida": "precios",
        "Agregados Monetarios": "monetario",
        "Sector Fiscal": "fiscal",
        "Comercio Internacional": "comercio",
        "Reservas y Deuda": "reservas-deuda",
        "Empleo y Salarios": "empleo-salarios",
        "Datos Demográficos": "demografia",
        "Jubilaciones y Social": "jubilaciones",
        "Actividad y Consumo": "actividad",
        "Industria y Energía": "industria",
        "Campo y Bioeconomía": "agro",
        "Construcción e Inmobiliario": "construccion"
    }

    enhanced_categories = []
    final_hdb = {}
    final_spark_db = {}
    total_cards = 0

    for cat in ref_cats:
        cat_name = cat.get("name") or cat.get("category")
        raw_cards = list(cat.get("cards") or cat.get("indicators") or [])

        cards_dict = {}
        for c in raw_cards:
            k = c.get("key") or c.get("id")
            if "Monetario" in cat_name and "canasta" in k:
                continue
            cards_dict[k] = c

        if "Precios" in cat_name:
            for nom_key, const_key, const_name, const_desc in canastas_to_adjust:
                cards_dict[const_key] = {
                    "key": const_key,
                    "name": const_name,
                    "desc": const_desc,
                    "source": "INDEC / Ajuste IPC",
                    "freq": "Mensual",
                    "time_range": "Mensual"
                }

        if "Jubilaciones" in cat_name:
            for nom_key, const_key, const_name, const_desc in jubilaciones_to_adjust:
                cards_dict[const_key] = {
                    "key": const_key,
                    "name": const_name,
                    "desc": const_desc,
                    "source": "ANSES / Ajuste IPC",
                    "freq": "Mensual",
                    "time_range": "Mensual"
                }

        if "Monetario" in cat_name:
            for agg_key, pbi_key, pbi_name, pbi_desc, mode in monetary_pbi_specs:
                cards_dict[pbi_key] = {
                    "key": pbi_key,
                    "name": pbi_name,
                    "desc": pbi_desc,
                    "source": "BCRA / INDEC",
                    "freq": "Trimestral",
                    "time_range": "Trimestral"
                }

        if "Reservas" in cat_name:
            for r_key, r_name, r_desc, num_s, den_d, r_src, r_freq in deuda_ratios_specs:
                cards_dict[r_key] = {
                    "key": r_key,
                    "name": r_name,
                    "desc": r_desc,
                    "source": r_src,
                    "freq": r_freq,
                    "time_range": r_freq
                }

            cards_dict["riesgo_pais"] = {
                "key": "riesgo_pais",
                "name": "Riesgo País (EMBI+ Argentina)",
                "desc": "Diferencial de tasa de rendimiento exigida a los bonos soberanos argentinos sobre los bonos del Tesoro de EE.UU., medido por J.P. Morgan.",
                "source": "J.P. Morgan / Rava",
                "freq": "Diario",
                "time_range": "Diario"
            }

        if "Precios" in cat_name:
            ordered_cards = [cards_dict[k] for k in precios_ordered_keys if k in cards_dict]
        elif "Monetario" in cat_name:
            ordered_cards = [cards_dict[k] for k in monetario_ordered_keys if k in cards_dict]
        elif "Reservas" in cat_name:
            ordered_cards = [cards_dict[k] for k in reservas_deuda_ordered_keys if k in cards_dict]
        elif "Jubilaciones" in cat_name:
            ordered_cards = [cards_dict[k] for k in jubilaciones_ordered_keys if k in cards_dict]
        else:
            ordered_cards = list(cards_dict.values())

        enhanced_cards = []
        for card in ordered_cards:
            key = card.get("key") or card.get("id")
            name = card.get("name") or card.get("title")
            desc = card.get("desc") or card.get("meaning") or f"Indicador económico oficial de {name}."
            source = card.get("source") or "INDEC / BCRA / ANSES / Min. Economía"
            freq = card.get("time_range") or card.get("freq") or "Mensual"

            series = ref_hdb.get(key, {})
            dates = series.get("dates") or (series.get("daily") or {}).get("dates") or (series.get("monthly") or {}).get("dates") or []
            prices = series.get("prices") or (series.get("daily") or {}).get("prices") or (series.get("monthly") or {}).get("prices") or []

            clean_pairs = [(d, float(p)) for d, p in zip(dates, prices) if p is not None and not (isinstance(p, float) and p != p)]
            dates = [x[0] for x in clean_pairs]
            prices = [x[1] for x in clean_pairs]

            if not dates or not prices:
                c_date = card.get("date") or "2026-07-01"
                c_val = card.get("value") or 0
                dates = [c_date]
                prices = [float(c_val)]

            final_hdb[key] = {"dates": dates, "prices": prices}

            latest_val = prices[-1]
            latest_date_raw = dates[-1]
            latest_date_formatted = format_date_es(latest_date_raw)

            spark_slice = sample_sparkline_series(dates, prices, freq)
            spark_dates = dates[-len(spark_slice):]
            final_spark_db[key] = {"dates": spark_dates, "prices": spark_slice}

            meta = get_indicator_unit_meta(key, name, cat_name)
            display_val = format_value_with_meta(latest_val, meta)

            if len(prices) >= 2:
                p_curr = prices[-1]
                p_prev = prices[-2]
                if p_prev != 0:
                    chg_pct = ((p_curr - p_prev) / abs(p_prev)) * 100
                    prefix = "+" if chg_pct > 0 else ""
                    suffix = " real" if key.endswith("_constante") else ""
                    if freq == "Trimestral" or key.endswith("_pbi"):
                        display_change = f"{prefix}{chg_pct:.2f}% t/t{suffix}"
                    elif freq == "Diario":
                        display_change = f"{prefix}{chg_pct:.2f}% diario"
                    else:
                        display_change = f"{prefix}{chg_pct:.2f}% m/m{suffix}"
                else:
                    display_change = "0.00%"
            else:
                display_change = card.get("display_change") or "0.00%"

            yoy_step = 5 if (freq == "Trimestral" or key.endswith("_pbi")) else (252 if freq == "Diario" else 13)
            if len(prices) >= yoy_step:
                p_curr = prices[-1]
                p_yoy = prices[-yoy_step]
                if p_yoy != 0:
                    yoy_pct = ((p_curr - p_yoy) / abs(p_yoy)) * 100
                    prefix = "+" if yoy_pct > 0 else ""
                    suffix = " Real" if key.endswith("_constante") else ""
                    var_ia = f"{prefix}{yoy_pct:.2f}% i.a.{suffix}"
                else:
                    var_ia = "0.00% i.a."
            elif card.get("var_ia") and card.get("var_ia") != "N/D":
                var_ia = card.get("var_ia")
            elif "Interanual" in name:
                var_ia = display_val
            else:
                var_ia = display_change.replace("m/m", "i.a.").replace("t/t", "i.a.")

            enhanced_card = {
                "key": key,
                "name": name,
                "category": cat_name,
                "desc": desc,
                "source": source,
                "freq": freq,
                "value": latest_val,
                "display_value": display_val,
                "display_change": display_change,
                "var_ia": var_ia,
                "unit_type": meta['type'],
                "unit_prefix": meta['prefix'],
                "unit_suffix": meta['suffix'],
                "decimals": meta['decimals'],
                "latest_date_raw": latest_date_raw,
                "latest_date": latest_date_formatted,
                "range_min": min(prices),
                "range_max": max(prices),
                "total_points": len(prices),
                "sparkline": spark_slice
            }
            enhanced_cards.append(enhanced_card)
            total_cards += 1

        cat_slug = category_slugs.get(cat_name, cat_name.lower().replace(" ", "-"))
        cat_icon = category_icons.get(cat_name, "fa-chart-bar")

        enhanced_categories.append({
            "id": cat_slug,
            "name": cat_name,
            "icon": cat_icon,
            "cards": enhanced_cards
        })

    master_output = {
        "metadata": {
            "title": "Tablero de Indicadores Económicos - La Segunda",
            "version": "2.9.0",
            "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_categories": len(enhanced_categories),
            "total_indicators": total_cards
        },
        "categories": enhanced_categories,
        "historical_db": final_hdb,
        "sparklines_db": final_spark_db
    }

    with open(master_path, "w", encoding="utf-8") as f:
        json.dump(master_output, f, ensure_ascii=False, indent=2)

    print(f"\n[SUCCESS] master_dataset.json actualizado con {len(enhanced_categories)} categorías y {total_cards} indicadores.")
    return master_output

if __name__ == "__main__":
    reconstruct_and_order_dataset()
