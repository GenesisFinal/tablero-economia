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

def adjust_series_to_constant(dates, nominal_prices, ipc_dict):
    """Adjusts historical nominal values to constant purchasing power of the latest date using official IPC."""
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

def reconstruct_real_dataset():
    print("==========================================================================")
    print("ACTUALIZANDO TABLERO CON CANASTAS AJUSTADAS POR IPC A PRECIOS DE HOY...")
    print("==========================================================================")

    ref_file = r'g:\Mi unidad\IA\Valores Financieros\master_dataset_PUNTO_RESTAURACION_BALANCES_UNIFICADOS_COMPLETO.json'
    with open(ref_file, 'r', encoding='utf-8', errors='ignore') as f:
        ref_data = json.load(f)

    root = ref_data.get('final_data', ref_data)
    ref_cats = root.get('economic_categories', [])
    ref_hdb = root.get('historical_db', {})

    print(f"[1] Base de referencia: {len(ref_cats)} categorías y {len(ref_hdb)} series históricas reales.")

    # Live APIs for verified latest points
    print("[2] Consultando APIs oficiales para últimas publicaciones verificadas...")
    
    # 1. IPC Mensual INDEC (ArgentinaDatos)
    try:
        r = requests.get("https://api.argentinadatos.com/v1/finanzas/indices/inflacion", timeout=8).json()
        ipc_dates = [x["fecha"] for x in r if "fecha" in x and "valor" in x]
        ipc_prices = [float(x["valor"]) for x in r if "fecha" in x and "valor" in x]
        if ipc_dates:
            ref_hdb["ipc_mensual"] = {"dates": ipc_dates, "prices": ipc_prices}
            print(f"  -> IPC Mensual verificado: {len(ipc_dates)} pts (Último: {ipc_prices[-1]}% - {ipc_dates[-1]})")
    except Exception as e:
        print("[WARN] IPC:", e)

    # 2. IPC Interanual INDEC (ArgentinaDatos)
    try:
        r = requests.get("https://api.argentinadatos.com/v1/finanzas/indices/inflacionInteranual", timeout=8).json()
        ia_dates = [x["fecha"] for x in r if "fecha" in x and "valor" in x]
        ia_prices = [float(x["valor"]) for x in r if "fecha" in x and "valor" in x]
        if ia_dates:
            ref_hdb["ipc_interanual"] = {"dates": ia_dates, "prices": ia_prices}
            print(f"  -> IPC Interanual verificado: {len(ia_dates)} pts (Último: {ia_prices[-1]}% - {ia_dates[-1]})")
    except Exception as e:
        print("[WARN] IPC Interanual:", e)

    # 3. Riesgo País JP Morgan (ArgentinaDatos)
    try:
        r = requests.get("https://api.argentinadatos.com/v1/finanzas/indices/riesgo-pais", timeout=8).json()
        rp_dates = [x["fecha"] for x in r if "fecha" in x and "valor" in x]
        rp_prices = [float(x["valor"]) for x in r if "fecha" in x and "valor" in x]
        if rp_dates:
            ref_hdb["riesgo_pais"] = {"dates": rp_dates, "prices": rp_prices}
            print(f"  -> Riesgo País verificado: {len(rp_dates)} pts (Último: {rp_prices[-1]} bps - {rp_dates[-1]})")
    except Exception as e:
        print("[WARN] Riesgo País:", e)

    # 4. UVA BCRA (ArgentinaDatos)
    try:
        r = requests.get("https://api.argentinadatos.com/v1/finanzas/indices/uva", timeout=8).json()
        uva_dates = [x["fecha"] for x in r if "fecha" in x and "valor" in x]
        uva_prices = [float(x["valor"]) for x in r if "fecha" in x and "valor" in x]
        if uva_dates:
            ref_hdb["uva_val"] = {"dates": uva_dates, "prices": uva_prices}
            print(f"  -> UVA verificado: {len(uva_dates)} pts (Último: ${uva_prices[-1]:,.2f} - {uva_dates[-1]})")
    except Exception as e:
        print("[WARN] UVA:", e)

    # Build IPC dictionary for deflating
    ipc_dict = {}
    ipc_series = ref_hdb.get("ipc_mensual", {})
    if ipc_series:
        for d, p in zip(ipc_series.get("dates", []), ipc_series.get("prices", [])):
            ipc_dict[d[:7]] = float(p)

    # Compute Constant Series for Canastas
    canastas_to_adjust = [
        ("canasta_alimentaria_val", "canasta_alimentaria_constante", "Canasta Básica Alimentaria a Precios Constantes", "Mide el costo histórico de la CBA ajustado por inflación (IPC) a pesos del último dato disponible. Refleja la variación real de la línea de indigencia."),
        ("canasta_total_val", "canasta_total_constante", "Canasta Básica Total a Precios Constantes", "Mide el costo histórico de la CBT ajustado por inflación (IPC) a pesos del último dato disponible. Refleja la variación real de la línea de pobreza."),
        ("canasta_alimentaria_hogar2", "canasta_alimentaria_hogar2_constante", "CBA Familiar (Hogar 2) a Precios Constantes", "Costo histórico de la CBA para un hogar de 4 integrantes ajustado por inflación (IPC) a pesos del último dato disponible."),
        ("canasta_total_hogar2", "canasta_total_hogar2_constante", "CBT Familiar (Hogar 2) a Precios Constantes", "Costo histórico de la CBT para un hogar de 4 integrantes ajustado por inflación (IPC) a pesos del último dato disponible.")
    ]

    for nom_key, const_key, const_name, const_desc in canastas_to_adjust:
        if nom_key in ref_hdb:
            nom_s = ref_hdb[nom_key]
            dates = nom_s.get("dates") or (nom_s.get("daily") or {}).get("dates") or (nom_s.get("monthly") or {}).get("dates") or []
            prices = nom_s.get("prices") or (nom_s.get("daily") or {}).get("prices") or (nom_s.get("monthly") or {}).get("prices") or []
            if dates and prices:
                const_prices = adjust_series_to_constant(dates, prices, ipc_dict)
                ref_hdb[const_key] = {"dates": dates, "prices": const_prices}
                print(f"  -> Calculada serie constante: {const_name} ({len(const_prices)} pts, último: ${const_prices[-1]:,.2f})")

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

    print("\n[3] Estructurando tarjetas de cada categoría...")

    for cat in ref_cats:
        cat_name = cat.get("name") or cat.get("category")
        cards = list(cat.get("cards") or cat.get("indicators") or [])

        # If Precios y Costo de Vida, inject constant canasta cards if not already present
        if "Precios" in cat_name:
            existing_keys = [c.get("key") or c.get("id") for c in cards]
            for nom_key, const_key, const_name, const_desc in canastas_to_adjust:
                if const_key not in existing_keys and const_key in ref_hdb:
                    cards.append({
                        "key": const_key,
                        "name": const_name,
                        "desc": const_desc,
                        "source": "INDEC / Ajuste IPC",
                        "freq": "Mensual",
                        "time_range": "Mensual"
                    })

        enhanced_cards = []
        for card in cards:
            key = card.get("key") or card.get("id")
            name = card.get("name") or card.get("title")
            desc = card.get("desc") or card.get("meaning") or f"Indicador económico oficial de {name}."
            source = card.get("source") or "INDEC / BCRA / Min. Economía"
            freq = card.get("time_range") or card.get("freq") or "Mensual"

            series = ref_hdb.get(key, {})
            dates = series.get("dates") or (series.get("daily") or {}).get("dates") or (series.get("monthly") or {}).get("dates") or []
            prices = series.get("prices") or (series.get("daily") or {}).get("prices") or (series.get("monthly") or {}).get("prices") or []

            # Clean and sanitize prices (remove NaNs / None)
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

            # Sparkline slice (last 24 real points)
            spark_slice = prices[-24:] if len(prices) >= 24 else prices
            spark_dates = dates[-len(spark_slice):]
            final_spark_db[key] = {"dates": spark_dates, "prices": spark_slice}

            # Display value
            display_val = card.get("display_value")
            if not display_val or key.endswith("_constante"):
                if "%" in name or "Tasa" in name or "Variación" in name or "Porcentaje" in name:
                    display_val = f"{latest_val:.2f}%"
                elif "USD" in name or "MEP" in name:
                    display_val = f"USD {latest_val:,.2f}"
                elif latest_val > 1_000_000_000:
                    display_val = f"${latest_val / 1_000_000_000:,.2f} B"
                elif latest_val > 1_000_000:
                    display_val = f"${latest_val:,.2f}"
                else:
                    display_val = f"${latest_val:,.2f}" if "$" not in str(latest_val) else f"{latest_val:,.2f}"

            # Period variation
            if len(prices) >= 2:
                p_curr = prices[-1]
                p_prev = prices[-2]
                if p_prev != 0:
                    chg_pct = ((p_curr - p_prev) / abs(p_prev)) * 100
                    prefix = "+" if chg_pct > 0 else ""
                    suffix = " real" if key.endswith("_constante") else ""
                    if freq == "Trimestral":
                        display_change = f"{prefix}{chg_pct:.2f}% t/t{suffix}"
                    elif freq == "Diario":
                        display_change = f"{prefix}{chg_pct:.2f}% diario"
                    else:
                        display_change = f"{prefix}{chg_pct:.2f}% m/m{suffix}"
                else:
                    display_change = "0.00%"
            else:
                display_change = card.get("display_change") or "0.00%"

            # YoY variation
            if len(prices) >= 13:
                p_curr = prices[-1]
                p_yoy = prices[-13]
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

            p_min = min(prices)
            p_max = max(prices)

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
                "latest_date_raw": latest_date_raw,
                "latest_date": latest_date_formatted,
                "range_min": p_min,
                "range_max": p_max,
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
            "version": "2.2.0",
            "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_categories": len(enhanced_categories),
            "total_indicators": total_cards
        },
        "categories": enhanced_categories,
        "historical_db": final_hdb,
        "sparklines_db": final_spark_db
    }

    workspace = os.path.dirname(os.path.abspath(__file__))
    master_path = os.path.join(workspace, "master_dataset.json")
    if not os.path.exists(os.path.dirname(master_path)):
        master_path = r"g:\Mi unidad\IA\Tablero-Economía\master_dataset.json"

    with open(master_path, "w", encoding="utf-8") as f:
        json.dump(master_output, f, ensure_ascii=False, indent=2)

    print(f"\n[SUCCESS] master_dataset.json actualizado con {len(enhanced_categories)} categorías, {total_cards} indicadores y canastas ajustadas por IPC.")
    return master_output

if __name__ == "__main__":
    reconstruct_real_dataset()
