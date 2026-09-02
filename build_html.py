import json
import os

def build_index_html():
    print("Building index.html with 85% min and 115% max Y-scale padding across all charts and sparklines...")

    workspace = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(workspace, 'master_dataset.json')
    if not os.path.exists(dataset_path):
        dataset_path = r'g:\Mi unidad\IA\Tablero-Economía\master_dataset.json'

    with open(dataset_path, 'r', encoding='utf-8') as f:
        master_dataset = json.load(f)

    json_str = json.dumps(master_dataset, ensure_ascii=False)

    html_content = f'''<!DOCTYPE html>
<html lang="es" class="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tablero de Indicadores Económicos | Economía</title>
  
  <!-- Favicons (Embedded Data-URI + Static Fallbacks) -->
  <link rel="icon" type="image/png" href="data:image/png;base64,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">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="data:image/png;base64,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">
  <link rel="shortcut icon" href="favicon.ico">

  <!-- Cache Control -->
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">

  <!-- Google Fonts: Sora & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <!-- Chart.js -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Sora"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace']
          }},
          colors: {{
            brand: {{
              red: '#E20039',
              redHover: '#B8002E',
              blue: '#0284C7',
              navy: '#0F172A',
              cardDark: '#1E293B',
              cardLight: '#FFFFFF',
              borderDark: '#334155',
              borderLight: '#E2E8F0',
              green: '#10B981',
              gold: '#F59E0B',
              purple: '#8B5CF6'
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{
      font-family: 'Sora', sans-serif;
      background-color: #F8FAFC;
      color: #0F172A;
      overflow-x: hidden;
      transition: background-color 0.2s ease, color 0.2s ease;
    }}
    .dark body {{
      background-color: #0B1120;
      color: #F1F5F9;
    }}
    .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}

    .glass-card {{
      background-color: #FFFFFF;
      border: 1px solid #E2E8F0;
      box-shadow: 0 2px 8px -1px rgba(0, 0, 0, 0.06), 0 1px 3px rgba(0, 0, 0, 0.04);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .dark .glass-card {{
      background-color: rgba(30, 41, 59, 0.75);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(51, 65, 85, 0.6);
      box-shadow: 0 4px 14px -2px rgba(0, 0, 0, 0.3);
    }}
    .glass-card:hover {{
      transform: translateY(-2px);
      border-color: rgba(226, 0, 57, 0.4);
      box-shadow: 0 10px 20px -3px rgba(226, 0, 57, 0.12), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }}
    .dark .glass-card:hover {{
      border-color: rgba(226, 0, 57, 0.5);
      box-shadow: 0 12px 24px -6px rgba(226, 0, 57, 0.2);
    }}

    .sidebar-item.active {{
      background: linear-gradient(90deg, rgba(226, 0, 57, 0.12) 0%, rgba(226, 0, 57, 0.02) 100%);
      border-left: 4px solid #E20039;
      color: #E20039 !important;
      font-weight: 700;
    }}
    .dark .sidebar-item.active {{
      background: linear-gradient(90deg, rgba(226, 0, 57, 0.25) 0%, rgba(226, 0, 57, 0.05) 100%);
      border-left: 4px solid #E20039;
      color: #FFFFFF !important;
      font-weight: 700;
    }}

    .top-tab-btn.active {{
      background-color: #E20039 !important;
      color: #FFFFFF !important;
      box-shadow: 0 4px 14px rgba(226, 0, 57, 0.35);
    }}

    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #F1F5F9;
    }}
    .dark ::-webkit-scrollbar-track {{
      background: #0F172A;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #CBD5E1;
      border-radius: 4px;
    }}
    .dark ::-webkit-scrollbar-thumb {{
      background: #334155;
    }}

    .sparkline-canvas {{
      width: 100% !important;
      height: 48px !important;
    }}
    .modal-backdrop {{
      background-color: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(8px);
    }}
    .dark .modal-backdrop {{
      background-color: rgba(11, 17, 32, 0.85);
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col selection:bg-brand-red selection:text-white">

  <!-- TOP HEADER -->
  <header class="sticky top-0 z-40 bg-white/95 dark:bg-[#0F172A]/95 backdrop-blur-md border-b border-slate-200 dark:border-[#334155]/60 transition-colors shadow-sm">
    <div class="max-w-[1900px] mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      
      <!-- Left: Logo -->
      <div class="flex items-center gap-3 shrink-0">
        <button onclick="toggleMobileSidebar()" class="lg:hidden p-2 rounded-xl bg-slate-100 dark:bg-[#1E293B] text-slate-700 dark:text-slate-300 hover:text-black dark:hover:text-white border border-slate-300 dark:border-[#334155]">
          <i class="fas fa-bars text-sm"></i>
        </button>

        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-brand-red to-[#9B0024] flex items-center justify-center text-white shadow-lg shadow-brand-red/30">
          <i class="fas fa-chart-pie text-base"></i>
        </div>
        <div>
          <div class="flex items-center gap-2 mb-0.5">
            <span class="text-xs font-bold uppercase tracking-wider text-brand-red">ECONOMÍA</span>
          </div>
          <h1 class="text-base sm:text-lg font-bold text-slate-900 dark:text-slate-100 tracking-tight leading-tight">
            Tablero de Indicadores Económicos
          </h1>
        </div>
      </div>

      <!-- Center: Search Bar -->
      <div class="flex-1 max-w-lg hidden md:block">
        <div class="relative">
          <i class="fas fa-search absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
          <input 
            type="text" 
            id="global-search-input"
            placeholder="Buscar indicador (ej. Jubilación, AUH, PUAM, IPC, Reservas, Deuda)... (Ctrl + K)"
            oninput="handleSearch(this.value)"
            class="w-full bg-slate-100 dark:bg-[#1E293B]/80 text-xs text-slate-900 dark:text-slate-100 placeholder:text-slate-500 dark:placeholder:text-slate-400 rounded-xl pl-9 pr-8 py-2 border border-slate-300 dark:border-[#334155]/60 focus:outline-none focus:border-brand-red focus:ring-1 focus:ring-brand-red transition-all font-medium"
          >
          <button id="search-clear-btn" onclick="clearSearch()" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 text-xs">
            <i class="fas fa-times"></i>
          </button>
        </div>
      </div>

      <!-- Right: Controls -->
      <div class="flex items-center gap-2">
        <div class="hidden sm:flex items-center p-1 rounded-xl bg-slate-100 dark:bg-[#1E293B] border border-slate-300 dark:border-[#334155] text-xs font-semibold">
          <button 
            onclick="setNavLayout('sidebar')" 
            id="layout-btn-sidebar"
            class="px-2.5 py-1 rounded-lg transition-all flex items-center gap-1.5 bg-brand-red text-white shadow-sm font-bold"
            title="Menú lateral izquierdo fijo"
          >
            <i class="fas fa-table-columns"></i>
            <span>Menú Lateral</span>
          </button>
          <button 
            onclick="setNavLayout('topgrid')" 
            id="layout-btn-topgrid"
            class="px-2.5 py-1 rounded-lg transition-all flex items-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-black dark:hover:text-white"
            title="Menú superior en 2 filas sin scroll"
          >
            <i class="fas fa-grip-lines"></i>
            <span>Menú 2 Filas</span>
          </button>
        </div>

        <button onclick="exportAllCSV()" title="Exportar indicadores a CSV" class="p-2 rounded-xl bg-slate-100 dark:bg-[#1E293B] text-slate-700 dark:text-slate-300 hover:text-black dark:hover:text-white border border-slate-300 dark:border-[#334155] text-xs font-semibold flex items-center gap-1.5 transition-colors">
          <i class="fas fa-file-csv text-brand-red"></i>
          <span class="hidden xl:inline">Exportar CSV</span>
        </button>

        <button onclick="toggleTheme()" id="theme-toggle-btn" title="Cambiar Tema (Oscuro / Claro)" class="p-2 w-9 h-9 rounded-xl bg-slate-100 dark:bg-[#1E293B] text-slate-700 dark:text-slate-300 hover:text-black dark:hover:text-white border border-slate-300 dark:border-[#334155] flex items-center justify-center text-sm transition-colors">
          <i class="fas fa-moon dark:hidden text-slate-700"></i>
          <i class="fas fa-sun hidden dark:inline text-amber-400"></i>
        </button>
      </div>

    </div>
  </header>

  <!-- TOP HIGHLIGHTS / KPIS BANNER -->
  <section class="bg-slate-100/90 dark:bg-[#0F172A]/60 border-b border-slate-200 dark:border-[#334155]/40 py-3 transition-colors">
    <div class="max-w-[1900px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3" id="top-kpis-container">
        <!-- Rendered dynamically -->
      </div>
    </div>
  </section>

  <!-- TOP 2-ROW CATEGORY GRID -->
  <nav id="top-categories-grid-nav" class="hidden bg-[#F8FAFC]/95 dark:bg-[#0B1120]/95 border-b border-slate-200 dark:border-[#334155]/50 py-3 transition-colors">
    <div class="max-w-[1900px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-[11px] font-bold uppercase tracking-wider text-slate-600 dark:text-slate-400 mb-2 flex items-center justify-between">
        <span>Categorías Macroeconómicas</span>
        <span class="text-[10px] text-brand-red font-mono font-bold">12 Secciones</span>
      </div>
      <div class="flex flex-wrap gap-2 text-xs font-semibold" id="top-grid-tabs-container">
        <!-- Rendered dynamically -->
      </div>
    </div>
  </nav>

  <!-- MAIN APP WRAPPER -->
  <div class="max-w-[1900px] mx-auto px-4 sm:px-6 lg:px-8 py-6 w-full flex-grow flex items-start gap-6">
    
    <!-- LEFT SIDEBAR -->
    <aside id="left-sidebar" class="w-64 xl:w-72 shrink-0 sticky top-20 flex flex-col gap-4 max-h-[calc(100vh-100px)] overflow-y-auto pr-1">
      <div class="glass-card rounded-2xl p-3 border border-slate-200 dark:border-[#334155]/60">
        <div class="px-3 py-2 border-b border-slate-200 dark:border-[#334155]/50 flex items-center justify-between mb-2">
          <span class="text-xs font-bold uppercase tracking-wider text-slate-800 dark:text-slate-300 flex items-center gap-1.5">
            <i class="fas fa-layer-group text-brand-red"></i>
            <span>Categorías</span>
          </span>
          <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-400" id="sidebar-total-badge">123</span>
        </div>
        <div class="flex flex-col gap-1 text-xs font-medium" id="sidebar-category-list">
          <!-- Rendered dynamically -->
        </div>
      </div>

      <div class="glass-card rounded-2xl p-4 border border-slate-200 dark:border-[#334155]/50 text-xs flex flex-col gap-2">
        <div class="flex items-center gap-2 text-emerald-600 dark:text-emerald-400 font-bold">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span>Datos 100% Verificados</span>
        </div>
        <p class="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed font-medium">
          Series oficiales extraídas de ANSES, BCRA, INDEC, Secretaría de Finanzas y Trabajo sin interpolaciones ni datos inventados.
        </p>
        <div class="text-[10px] text-slate-500 dark:text-slate-400 font-mono mt-1 pt-2 border-t border-slate-200 dark:border-[#334155]/40">
          Act: <span id="sidebar-update-time" class="text-slate-800 dark:text-slate-300 font-bold">...</span>
        </div>
      </div>
    </aside>

    <!-- MOBILE DRAWER -->
    <div id="mobile-sidebar-backdrop" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm hidden opacity-0 transition-opacity duration-200" onclick="toggleMobileSidebar()">
      <div id="mobile-sidebar-drawer" class="w-72 max-w-[85vw] h-full bg-white dark:bg-[#0F172A] p-4 shadow-2xl flex flex-col gap-4 overflow-y-auto transform -translate-x-full transition-transform duration-250 ease-out" onclick="event.stopPropagation()">
        <div class="flex items-center justify-between pb-3 border-b border-slate-200 dark:border-slate-700">
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-brand-red"></span>
            <span class="font-bold text-sm text-slate-900 dark:text-white">Categorías Económicas</span>
          </div>
          <button onclick="toggleMobileSidebar()" class="p-1.5 rounded-lg text-slate-500 hover:text-black dark:text-slate-400 dark:hover:text-white">
            <i class="fas fa-times"></i>
          </button>
        </div>
        <div class="flex flex-col gap-1 text-xs" id="mobile-sidebar-category-list">
          <!-- Rendered dynamically -->
        </div>
      </div>
    </div>

    <!-- MAIN CONTENT -->
    <main class="flex-1 w-full min-w-0">
      <div id="search-status-banner" class="hidden mb-6 p-4 rounded-2xl bg-brand-red/10 border border-brand-red/30 flex items-center justify-between">
        <div class="flex items-center gap-2 text-sm text-slate-800 dark:text-slate-200">
          <i class="fas fa-search text-brand-red"></i>
          <span>Resultados para: <strong id="search-query-text" class="text-black dark:text-white font-bold"></strong></span>
          <span id="search-count-badge" class="px-2 py-0.5 rounded-full bg-brand-red text-white text-xs font-bold"></span>
        </div>
        <button onclick="clearSearch()" class="text-xs text-brand-red hover:underline font-bold">
          Mostrar todas las categorías
        </button>
      </div>

      <div id="categories-root" class="flex flex-col gap-10">
        <!-- Rendered dynamically -->
      </div>
    </main>

  </div>

  <!-- FOOTER -->
  <footer class="bg-slate-100 dark:bg-[#0F172A] border-t border-slate-200 dark:border-[#334155]/60 py-6 mt-12 transition-colors">
    <div class="max-w-[1900px] mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-600 dark:text-slate-400">
      <div class="flex items-center gap-2 font-medium">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
        <span class="text-slate-900 dark:text-slate-200 font-bold">Sistema de Monitoreo Macroeconómico</span>
      </div>
      <div class="flex items-center gap-4">
        <span>Última Actualización: <strong id="footer-update-time" class="text-slate-900 dark:text-slate-200 font-mono font-bold"></strong></span>
        <span>•</span>
        <span>Fuentes: ANSES, INDEC, BCRA, Secretaría de Finanzas, Min. Capital Humano, ArgentinaDatos</span>
      </div>
    </div>
  </footer>

  <!-- DETAIL & REGRESSION MODAL -->
  <div id="indicator-modal" class="fixed inset-0 z-50 modal-backdrop hidden items-center justify-center p-4 sm:p-6 opacity-0 transition-opacity duration-250 ease-out" onclick="handleModalBackdropClick(event)">
    <div class="glass-card rounded-3xl w-full max-w-5xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl border border-brand-red/30 relative animate-in fade-in zoom-in-95 duration-200 bg-white dark:bg-[#1E293B]" onclick="event.stopPropagation()">
      
      <!-- Modal Header -->
      <div class="p-6 pb-4 border-b border-slate-200 dark:border-[#334155]/60 flex items-start justify-between gap-4">
        <div class="flex items-start gap-3">
          <div class="w-11 h-11 rounded-2xl bg-brand-red/10 border border-brand-red/30 flex items-center justify-center text-brand-red text-lg shrink-0 mt-0.5">
            <i class="fas fa-chart-line" id="modal-icon"></i>
          </div>
          <div>
            <div class="flex items-center gap-2 mb-1 flex-wrap">
              <span id="modal-category-badge" class="px-2 py-0.5 rounded-md text-[11px] font-bold uppercase tracking-wider bg-slate-200 dark:bg-slate-800 text-slate-800 dark:text-slate-300"></span>
              <span id="modal-freq-badge" class="px-2 py-0.5 rounded-md text-[11px] font-bold bg-blue-50 dark:bg-blue-500/10 text-blue-700 dark:text-blue-400 border border-blue-200 dark:border-blue-500/20"></span>
              <span id="modal-source-badge" class="px-2 py-0.5 rounded-md text-[11px] font-bold bg-emerald-50 dark:bg-emerald-500/10 text-emerald-700 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-500/20"></span>
              <span id="modal-ratio-badge" class="hidden px-2.5 py-0.5 rounded-md text-[11px] font-bold bg-purple-50 dark:bg-purple-500/15 text-purple-700 dark:text-purple-300 border border-purple-200 dark:border-purple-500/30"></span>
              <span id="modal-date-badge" class="px-2.5 py-0.5 rounded-md text-[11px] font-black bg-rose-50 dark:bg-brand-red/20 text-brand-red border border-rose-200 dark:border-brand-red/30 font-mono"></span>
            </div>
            <h2 id="modal-title" class="text-lg sm:text-xl font-bold text-slate-950 dark:text-slate-100 tracking-tight"></h2>
            <p id="modal-desc" class="text-xs text-slate-600 dark:text-slate-400 mt-1 max-w-2xl leading-relaxed font-medium"></p>
          </div>
        </div>

        <button onclick="closeModal()" class="w-9 h-9 rounded-full bg-slate-100 dark:bg-slate-800/80 text-slate-500 hover:text-black dark:text-slate-400 dark:hover:text-white flex items-center justify-center transition-colors shrink-0">
          <i class="fas fa-times text-sm"></i>
        </button>
      </div>

      <!-- Modal Body -->
      <div class="p-6 overflow-y-auto flex-grow flex flex-col gap-5">
        
        <!-- Summary Stat Pills -->
        <div class="grid grid-cols-2 sm:grid-cols-5 gap-3">
          <div class="p-3 rounded-2xl bg-slate-50 dark:bg-[#0F172A]/70 border border-slate-200 dark:border-[#334155]/50">
            <div class="text-[10px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Último Dato Real</div>
            <div id="modal-stat-latest" class="text-base sm:text-lg font-black font-mono text-slate-950 dark:text-slate-100 mt-0.5"></div>
            <div id="modal-stat-date" class="text-[10px] text-brand-red font-bold font-mono"></div>
          </div>

          <div class="p-3 rounded-2xl bg-slate-50 dark:bg-[#0F172A]/70 border border-slate-200 dark:border-[#334155]/50">
            <div class="text-[10px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Var. Período</div>
            <div id="modal-stat-mom" class="text-base sm:text-lg font-black font-mono mt-0.5"></div>
            <div class="text-[10px] text-slate-500 dark:text-slate-400 font-medium">Mes / Trimestre</div>
          </div>

          <div class="p-3 rounded-2xl bg-slate-50 dark:bg-[#0F172A]/70 border border-slate-200 dark:border-[#334155]/50">
            <div class="text-[10px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Var. Interanual</div>
            <div id="modal-stat-yoy" class="text-base sm:text-lg font-black font-mono mt-0.5"></div>
            <div class="text-[10px] text-slate-500 dark:text-slate-400 font-medium">Últimos 12 meses</div>
          </div>

          <div class="p-3 rounded-2xl bg-slate-50 dark:bg-[#0F172A]/70 border border-slate-200 dark:border-[#334155]/50">
            <div class="text-[10px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Mín / Máx Período</div>
            <div id="modal-stat-range" class="text-xs sm:text-sm font-bold font-mono text-slate-900 dark:text-slate-200 mt-1"></div>
            <div id="modal-stat-pts" class="text-[10px] text-slate-500 dark:text-slate-400 font-mono font-medium"></div>
          </div>

          <div class="p-3 rounded-2xl bg-slate-50 dark:bg-[#0F172A]/70 border border-slate-200 dark:border-[#334155]/50">
            <div class="text-[10px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Tendencia Real</div>
            <div id="modal-stat-trend" class="text-sm font-black font-mono mt-1"></div>
            <div id="modal-stat-slope" class="text-[10px] text-slate-500 dark:text-slate-400 font-mono font-medium"></div>
          </div>
        </div>

        <!-- Controls -->
        <div class="flex flex-wrap items-center justify-between gap-3 bg-slate-100/80 dark:bg-[#0F172A]/40 p-2.5 rounded-2xl border border-slate-200 dark:border-[#334155]/40">
          <div class="flex items-center gap-1 text-xs font-semibold">
            <span class="text-slate-600 dark:text-slate-400 mr-1 text-[11px] font-bold">Rango:</span>
            <button onclick="setModalPeriod('1A')" id="btn-period-1A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-200 dark:hover:bg-slate-800">1A</button>
            <button onclick="setModalPeriod('2A')" id="btn-period-2A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-200 dark:hover:bg-slate-800">2A</button>
            <button onclick="setModalPeriod('3A')" id="btn-period-3A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-200 dark:hover:bg-slate-800">3A</button>
            <button onclick="setModalPeriod('5A')" id="btn-period-5A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-200 dark:hover:bg-slate-800">5A</button>
            <button onclick="setModalPeriod('ALL')" id="btn-period-ALL" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-200 dark:hover:bg-slate-800">Histórico</button>
          </div>

          <div class="flex items-center gap-2">
            <button 
              onclick="toggleRegressionLine()" 
              id="btn-toggle-regression" 
              class="px-3 py-1 text-xs font-bold rounded-xl border transition-all flex items-center gap-1.5 bg-slate-200 dark:bg-slate-800/80 border-slate-300 dark:border-slate-700 text-slate-800 dark:text-slate-300 hover:border-brand-red"
            >
              <i class="fas fa-chart-line text-brand-red"></i>
              <span>Recta de Regresión</span>
              <span id="regression-badge" class="w-2 h-2 rounded-full bg-slate-500"></span>
            </button>

            <button onclick="exportModalChartPNG()" title="Descargar Gráfico en PNG" class="p-1.5 px-2.5 rounded-xl bg-slate-200 dark:bg-slate-800/80 text-slate-800 dark:text-slate-300 hover:text-black dark:hover:text-white border border-slate-300 dark:border-slate-700 text-xs font-semibold">
              <i class="fas fa-camera"></i>
            </button>
          </div>
        </div>

        <!-- Chart Canvas -->
        <div class="relative w-full h-[360px] min-h-[300px] bg-white dark:bg-[#0F172A]/40 rounded-2xl p-3 border border-slate-200 dark:border-[#334155]/40 flex items-center justify-center">
          <canvas id="modal-main-chart"></canvas>
        </div>

      </div>

    </div>
  </div>

  <!-- EMBEDDED DATASET -->
  <script>
    window.DATASET = {json_str};
  </script>

  <!-- APPLICATION LOGIC -->
  <script>
    let currentCategory = 'all';
    let searchQuery = '';
    let isDarkMode = false;
    let navLayout = localStorage.getItem('navLayout') || 'sidebar';
    let sparklineCharts = {{}};
    let modalChart = null;

    let modalState = {{
      key: null,
      card: null,
      series: null,
      period: '2A',
      showRegression: true
    }};

    // Compute 85% min and 115% max Y-scale padding to prevent visual exaggeration on low-variance series
    function computeScaleBounds(prices) {{
      if (!prices || !prices.length) return {{ min: undefined, max: undefined }};
      const pMin = Math.min(...prices);
      const pMax = Math.max(...prices);

      let sMin, sMax;
      if (pMin >= 0 && pMax >= 0) {{
        sMin = pMin * 0.85;
        sMax = pMax * 1.15;
        if (sMin < 0) sMin = 0;
      }} else if (pMin < 0 && pMax > 0) {{
        sMin = pMin * 1.15;
        sMax = pMax * 1.15;
      }} else if (pMax <= 0) {{
        sMin = pMin * 1.15;
        sMax = pMax * 0.85;
      }} else {{
        sMin = pMin * 0.85;
        sMax = pMax * 1.15;
      }}
      return {{ min: sMin, max: sMax }};
    }}

    function isBarChartIndicator(card) {{
      if (!card) return false;
      const k = (card.key || '').toLowerCase();
      const n = (card.name || '').toLowerCase();
      return (
        card.chart_type === 'bar' ||
        k.startsWith('resultado_') ||
        k.startsWith('saldo_') ||
        k.startsWith('balanza_') ||
        k.includes('_interanual') ||
        k.includes('interanual') ||
        k === 'supermercados_ventas' ||
        k === 'isac_general' ||
        n.includes('resultado fiscal') ||
        n.includes('resultado financiero') ||
        n.includes('resultado primario') ||
        n.includes('saldo comercial') ||
        n.includes('interanual') ||
        n.includes('variación') ||
        n.includes('variacion')
      );
    }}

    function getUnitMeta(card) {{
      const k = (card.key || '').toLowerCase();
      const n = (card.name || '').toLowerCase();

      if (k === 'riesgo_pais') {{
        return {{ type: 'bps', prefix: '', suffix: ' bps', decimals: 0 }};
      }}

      if (k === 'relacion_activo_pasivo') {{
        return {{ type: 'ratio', prefix: '', suffix: ' act/pas', decimals: 2 }};
      }}

      if (k === 'pbi_corriente' || k === 'pbi_constante_hoy') {{
        return {{ type: 'currency_ars_m', prefix: '$ ', suffix: ' M', decimals: 2 }};
      }}

      if (k === 'supermercados_ventas_usd') {{
        return {{ type: 'currency_usd_m', prefix: 'USD ', suffix: ' M', decimals: 2 }};
      }}

      if (k === 'supermercados_ventas_valor') {{
        return {{ type: 'currency_ars_const', prefix: '$ ', suffix: ' M (Dic-16)', decimals: 2 }};
      }}

      // Check Percentage & Ratios
      if (k.endsWith('_pbi') || k.startsWith('ratio_') || k.startsWith('cobertura_') || k.startsWith('tasa_') || 
          k === 'capacidad_instalada_industria' ||
          k.includes('cobertura') || n.includes('cobertura') ||
          k.includes('interanual') || n.includes('interanual') || 
          n.includes('tasa') || n.includes('variación') || n.includes('variacion') || n.includes('porcentaje') || 
          k.includes('desocupacion') || k.includes('actividad') || k.includes('indigencia') || k.includes('pobreza') || 
          k.includes('empleo_val') || k.includes('salarios_indice') || k.includes('isac_general') || 
          k.includes('ipc') || k.includes('ipi') || k.includes('emae_interanual') || k === 'supermercados_ventas' || 
          k.includes('pbi_interanual') || k.includes('emae_agro') || n.includes('%')) {{
        return {{ type: 'percent', prefix: '', suffix: '%', decimals: 2 }};
      }}

      // Debt, Reserves, FGS, CIARA, MOA, PP in USD Millions
      if ((k.includes('deuda_') && !k.endsWith('_pbi')) || k === 'reservas_brutas' || k === 'reservas_bcra' || 
          k === 'fgs_total_usd' || k === 'liquidacion_divisas_ciara' || k === 'exportaciones_moa' || 
          k === 'exportaciones_pp' || k === 'exportaciones_totales' || k === 'importaciones_totales' ||
          k === 'moa_exportaciones') {{
        return {{ type: 'currency_usd', prefix: 'USD ', suffix: ' M', decimals: 2 }};
      }}

      // Check General USD
      if (k.endsWith('_usd') || k.includes('usd') || n.includes('usd') || n.includes('dólares') || n.includes('dolares')) {{
        return {{ type: 'currency_usd', prefix: 'USD ', suffix: '', decimals: 2 }};
      }}

      // Quantities & Specific Units
      if (k === 'gas_produccion') {{
        return {{ type: 'quantity', prefix: '', suffix: ' MM m³/mes', decimals: 2 }};
      }}
      if (k === 'petroleo_produccion') {{
        return {{ type: 'quantity', prefix: '', suffix: ' miles m³/mes', decimals: 2 }};
      }}
      if (k === 'produccion_automotriz') {{
        return {{ type: 'quantity', prefix: '', suffix: ' unid./mes', decimals: 0 }};
      }}
      if (k === 'generacion_electrica_total') {{
        return {{ type: 'quantity', prefix: '', suffix: ' GWh/mes', decimals: 1 }};
      }}
      if (k === 'faena_bovina') {{
        return {{ type: 'quantity', prefix: '', suffix: ' mil cab./mes', decimals: 1 }};
      }}
      if (k === 'molienda_oleaginosas') {{
        return {{ type: 'quantity', prefix: '', suffix: ' mil Tn/mes', decimals: 1 }};
      }}
      if (k === 'cosecha_granos_total') {{
        return {{ type: 'quantity', prefix: '', suffix: ' MM Tn', decimals: 1 }};
      }}

      // Quantities & Indices
      if (k.includes('poblacion') || k.includes('beneficios_sipa')) {{
        return {{ type: 'quantity', prefix: '', suffix: ' hab.', decimals: 0 }};
      }}
      if (k.includes('empleo_privado') || k.includes('empleo_total')) {{
        return {{ type: 'quantity', prefix: '', suffix: ' mil', decimals: 1 }};
      }}
      if (k.includes('cemento_total')) {{
        return {{ type: 'quantity', prefix: '', suffix: ' Tn', decimals: 1 }};
      }}
      if (k.includes('isac_') || k.includes('icc_') || k.includes('indice_salarios_ipc') || k.includes('emae_construccion') || k === 'ipi_manufacturero_nivel') {{
        return {{ type: 'index', prefix: '', suffix: ' pts', decimals: 2 }};
      }}

      // Currency ARS
      return {{ type: 'currency_ars', prefix: '$', suffix: '', decimals: 2 }};
    }}

    function formatValueWithMeta(val, meta, compact = false) {{
      if (val === null || val === undefined || isNaN(val)) return 'N/D';
      const num = Number(val);
      const dec = meta.decimals !== undefined ? meta.decimals : 2;

      let formattedNumber = '';
      if (compact && Math.abs(num) >= 1_000_000_000) {{
        formattedNumber = (num / 1_000_000_000).toLocaleString('es-AR', {{ minimumFractionDigits: 1, maximumFractionDigits: 2 }}) + ' B';
      }} else if (compact && Math.abs(num) >= 1_000_000) {{
        formattedNumber = (num / 1_000_000).toLocaleString('es-AR', {{ minimumFractionDigits: 1, maximumFractionDigits: 2 }}) + ' M';
      }} else {{
        formattedNumber = num.toLocaleString('es-AR', {{ minimumFractionDigits: dec, maximumFractionDigits: dec }});
      }}

      return `${{meta.prefix}}${{formattedNumber}}${{meta.suffix}}`;
    }}

    // Clean Spanish Date Formatter for Chart X-Axis and Tooltips
    function formatDateSpanish(dateStr, formatType = 'short') {{
      if (!dateStr || dateStr.length < 4) return dateStr;
      const months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'];
      const monthsFull = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];

      try {{
        const parts = dateStr.split('-');
        if (parts.length >= 2) {{
          const y = parts[0];
          const m = parseInt(parts[1], 10);
          const mStr = (m >= 1 && m <= 12) ? months[m - 1] : parts[1];
          const mFullStr = (m >= 1 && m <= 12) ? monthsFull[m - 1] : parts[1];

          if (parts.length === 3 && parts[2] !== '01') {{
            const d = parseInt(parts[2], 10);
            if (formatType === 'full') return `${{d}} de ${{mFullStr}} de ${{y}}`;
            return `${{d}} ${{mStr}} ${{y.slice(-2)}}`;
          }}

          if (formatType === 'full') return `${{mFullStr}} de ${{y}}`;
          return `${{mStr}} ${{y}}`;
        }}
      }} catch (e) {{}}
      return dateStr;
    }}

    // Real Calendar Date Filter
    function filterSeriesByCalendar(dates, prices, period) {{
      if (!dates || !dates.length || period === 'ALL') {{
        return {{ dates, prices }};
      }}

      const lastDateStr = dates[dates.length - 1];
      let cutoffStr = '';

      try {{
        const parts = lastDateStr.split('-');
        const y = parseInt(parts[0], 10);
        const m = parts[1] || '01';
        const d = parts[2] || '01';

        const yearsBack = {{ '1A': 1, '2A': 2, '3A': 3, '5A': 5 }}[period] || 2;
        const targetYear = y - yearsBack;

        cutoffStr = `${{targetYear}}-${{m}}-${{d}}`;
        if (parts.length === 2) cutoffStr = `${{targetYear}}-${{m}}`;
      }} catch (e) {{
        const count = {{ '1A': 12, '2A': 24, '3A': 36, '5A': 60 }}[period] || 24;
        return {{ dates: dates.slice(-count), prices: prices.slice(-count) }};
      }}

      const filtered = [];
      for (let i = 0; i < dates.length; i++) {{
        if (dates[i] >= cutoffStr) {{
          filtered.push({{ d: dates[i], p: prices[i] }});
        }}
      }}

      if (filtered.length < 2) {{
        return {{ dates: dates.slice(-12), prices: prices.slice(-12) }};
      }}

      return {{
        dates: filtered.map(x => x.d),
        prices: filtered.map(x => x.p)
      }};
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      initTheme();
      initNavLayout();
      renderTopKPIs();
      renderSidebarNavigation();
      renderTopGridNavigation();
      renderAllCategories();
      setupKeyboardShortcuts();

      if (window.DATASET && window.DATASET.metadata) {{
        const updateTimeEl = document.getElementById('footer-update-time');
        const sidebarUpdateEl = document.getElementById('sidebar-update-time');
        const totalBadgeEl = document.getElementById('sidebar-total-badge');
        if (updateTimeEl) updateTimeEl.innerText = window.DATASET.metadata.last_updated;
        if (sidebarUpdateEl) sidebarUpdateEl.innerText = window.DATASET.metadata.last_updated.slice(0, 10);
        if (totalBadgeEl) totalBadgeEl.innerText = window.DATASET.metadata.total_indicators || 123;
      }}
    }});

    function initNavLayout() {{
      setNavLayout(navLayout);
    }}

    function setNavLayout(mode) {{
      navLayout = mode;
      localStorage.setItem('navLayout', mode);

      const sidebarEl = document.getElementById('left-sidebar');
      const topGridEl = document.getElementById('top-categories-grid-nav');
      const btnSidebar = document.getElementById('layout-btn-sidebar');
      const btnTopGrid = document.getElementById('layout-btn-topgrid');

      if (mode === 'topgrid') {{
        if (sidebarEl) sidebarEl.classList.add('hidden');
        if (topGridEl) topGridEl.classList.remove('hidden');
        if (btnTopGrid) btnTopGrid.className = "px-2.5 py-1 rounded-lg transition-all flex items-center gap-1.5 bg-brand-red text-white shadow-sm font-bold";
        if (btnSidebar) btnSidebar.className = "px-2.5 py-1 rounded-lg transition-all flex items-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-black dark:hover:text-white";
      }} else {{
        if (sidebarEl) sidebarEl.classList.remove('hidden');
        if (topGridEl) topGridEl.classList.add('hidden');
        if (btnSidebar) btnSidebar.className = "px-2.5 py-1 rounded-lg transition-all flex items-center gap-1.5 bg-brand-red text-white shadow-sm font-bold";
        if (btnTopGrid) btnTopGrid.className = "px-2.5 py-1 rounded-lg transition-all flex items-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-black dark:hover:text-white";
      }}
    }}

    function toggleMobileSidebar() {{
      const backdrop = document.getElementById('mobile-sidebar-backdrop');
      const drawer = document.getElementById('mobile-sidebar-drawer');
      if (!backdrop || !drawer) return;

      if (backdrop.classList.contains('hidden')) {{
        backdrop.classList.remove('hidden');
        setTimeout(() => {{
          backdrop.classList.remove('opacity-0');
          drawer.classList.remove('-translate-x-full');
        }}, 10);
      }} else {{
        backdrop.classList.add('opacity-0');
        drawer.classList.add('-translate-x-full');
        setTimeout(() => {{
          backdrop.classList.add('hidden');
        }}, 250);
      }}
    }}

    function initTheme() {{
      const savedTheme = localStorage.getItem('theme') || 'light';
      if (savedTheme === 'dark') {{
        document.documentElement.classList.remove('light');
        document.documentElement.classList.add('dark');
        isDarkMode = true;
      }} else {{
        document.documentElement.classList.remove('dark');
        document.documentElement.classList.add('light');
        isDarkMode = false;
      }}
    }}

    function toggleTheme() {{
      if (document.documentElement.classList.contains('dark')) {{
        document.documentElement.classList.remove('dark');
        document.documentElement.classList.add('light');
        localStorage.setItem('theme', 'light');
        isDarkMode = false;
      }} else {{
        document.documentElement.classList.remove('light');
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
        isDarkMode = true;
      }}
      renderAllCategories();
      if (modalState.key) updateModalChart();
    }}

    function renderTopKPIs() {{
      const container = document.getElementById('top-kpis-container');
      if (!container || !window.DATASET) return;

      const kpiKeys = [
        {{ key: 'ipc_mensual', label: 'IPC Mensual', icon: 'fa-percentage', color: 'text-amber-600 dark:text-amber-400' }},
        {{ key: 'jubilacion_minima_bono', label: 'Jub. Mínima + Bono', icon: 'fa-hands-holding-circle', color: 'text-purple-600 dark:text-purple-400' }},
        {{ key: 'auh_val', label: 'AUH por Hijo', icon: 'fa-child', color: 'text-blue-600 dark:text-blue-400' }},
        {{ key: 'riesgo_pais', label: 'Riesgo País', icon: 'fa-arrow-trend-down', color: 'text-blue-600 dark:text-blue-400' }},
        {{ key: 'reservas_brutas', label: 'Reservas BCRA', icon: 'fa-vault', color: 'text-emerald-600 dark:text-emerald-400' }},
        {{ key: 'resultado_fiscal_primario', label: 'Resultado Primario', icon: 'fa-scale-balanced', color: 'text-cyan-600 dark:text-cyan-400' }}
      ];

      let html = '';
      kpiKeys.forEach(k => {{
        let cardData = findCardByKey(k.key);
        if (!cardData && k.key === 'jubilacion_minima_bono') cardData = findCardByKey('jubilacion_minima');
        if (!cardData && k.key === 'reservas_brutas') cardData = findCardByKey('reservas_bcra');

        if (cardData) {{
          const meta = getUnitMeta(cardData);
          const formattedVal = formatValueWithMeta(cardData.value, meta);
          const isPos = String(cardData.display_change).includes('+');
          const isNeg = String(cardData.display_change).includes('-');
          const colorClass = isPos ? 'text-emerald-700 dark:text-emerald-400 font-bold' : (isNeg ? 'text-rose-700 dark:text-rose-400 font-bold' : 'text-slate-600 dark:text-slate-300');

          html += `
            <div onclick="openModalByKey('${{cardData.key}}')" class="glass-card p-3 rounded-2xl cursor-pointer hover:border-brand-red flex flex-col justify-between">
              <div class="flex items-center justify-between text-[11px] text-slate-600 dark:text-slate-400 font-bold">
                <span>${{k.label}}</span>
                <span class="text-[10px] text-brand-red font-mono font-bold">${{cardData.latest_date}}</span>
              </div>
              <div class="text-base sm:text-lg font-black font-mono text-slate-950 dark:text-slate-100 mt-1 tracking-tight">
                ${{formattedVal}}
              </div>
              <div class="flex items-center justify-between text-[10px] font-mono mt-0.5">
                <span class="${{colorClass}}">${{cardData.display_change}}</span>
                <span class="text-slate-500 dark:text-slate-400 font-semibold">${{cardData.var_ia}}</span>
              </div>
            </div>
          `;
        }}
      }});
      container.innerHTML = html;
    }}

    function renderSidebarNavigation() {{
      const sidebarContainer = document.getElementById('sidebar-category-list');
      const mobileContainer = document.getElementById('mobile-sidebar-category-list');
      if (!sidebarContainer || !window.DATASET) return;

      const categories = window.DATASET.categories || [];
      const totalCount = window.DATASET.metadata.total_indicators || 123;

      let html = `
        <button 
          onclick="selectCategory('all')" 
          id="sidebar-item-all"
          class="sidebar-item active w-full px-3 py-2 rounded-xl text-left transition-all flex items-center justify-between text-slate-800 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800/60"
        >
          <span class="flex items-center gap-2 font-semibold">
            <i class="fas fa-layer-group text-brand-red w-4 text-center"></i>
            <span>Todas las Categorías</span>
          </span>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-slate-200 dark:bg-slate-800 font-mono font-bold">${{totalCount}}</span>
        </button>
      `;

      categories.forEach(cat => {{
        const count = cat.cards ? cat.cards.length : 0;
        html += `
          <button 
            onclick="selectCategory('${{cat.id}}')" 
            id="sidebar-item-${{cat.id}}"
            class="sidebar-item w-full px-3 py-2 rounded-xl text-left transition-all flex items-center justify-between text-slate-700 dark:text-slate-400 hover:text-black dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/60"
          >
            <span class="flex items-center gap-2 truncate">
              <i class="fas ${{cat.icon}} text-brand-red w-4 text-center"></i>
              <span class="truncate font-semibold">${{cat.name}}</span>
            </span>
            <span class="text-[10px] px-1.5 py-0.5 rounded-full bg-slate-200 dark:bg-slate-800/80 font-mono font-bold shrink-0">${{count}}</span>
          </button>
        `;
      }});

      sidebarContainer.innerHTML = html;
      if (mobileContainer) mobileContainer.innerHTML = html;
    }}

    function renderTopGridNavigation() {{
      const container = document.getElementById('top-grid-tabs-container');
      if (!container || !window.DATASET) return;

      const categories = window.DATASET.categories || [];
      const totalCount = window.DATASET.metadata.total_indicators || 123;

      let html = `
        <button 
          onclick="selectCategory('all')" 
          id="top-grid-item-all"
          class="top-tab-btn active px-3 py-1.5 rounded-xl border border-slate-300 dark:border-transparent transition-all flex items-center gap-1.5 text-slate-800 dark:text-slate-300 font-bold"
        >
          <i class="fas fa-layer-group"></i>
          <span>Todas (${{totalCount}})</span>
        </button>
      `;

      categories.forEach(cat => {{
        const count = cat.cards ? cat.cards.length : 0;
        html += `
          <button 
            onclick="selectCategory('${{cat.id}}')" 
            id="top-grid-item-${{cat.id}}"
            class="top-tab-btn px-3 py-1.5 rounded-xl border border-slate-300 dark:border-transparent transition-all flex items-center gap-1.5 text-slate-700 dark:text-slate-400 hover:text-black dark:hover:text-white bg-slate-100 dark:bg-[#1E293B] font-semibold"
          >
            <i class="fas ${{cat.icon}} text-brand-red"></i>
            <span>${{cat.name}}</span>
            <span class="text-[10px] px-1.5 py-0.2 rounded-full bg-slate-200 dark:bg-slate-800 font-mono font-bold">${{count}}</span>
          </button>
        `;
      }});

      container.innerHTML = html;
    }}

    function selectCategory(catId) {{
      currentCategory = catId;

      document.querySelectorAll('.sidebar-item').forEach(btn => {{
        btn.classList.remove('active');
        btn.classList.add('text-slate-700', 'dark:text-slate-400');
      }});
      const activeSidebar = document.getElementById(`sidebar-item-${{catId}}`);
      if (activeSidebar) activeSidebar.classList.add('active');

      document.querySelectorAll('.top-tab-btn').forEach(btn => {{
        btn.classList.remove('active', 'bg-brand-red', 'text-white');
        btn.classList.add('bg-slate-100', 'dark:bg-[#1E293B]', 'text-slate-700', 'dark:text-slate-400');
      }});
      const activeTop = document.getElementById(`top-grid-item-${{catId}}`);
      if (activeTop) {{
        activeTop.classList.add('active', 'bg-brand-red', 'text-white');
        activeTop.classList.remove('bg-slate-100', 'dark:bg-[#1E293B]', 'text-slate-700', 'dark:text-slate-400');
      }}

      const backdrop = document.getElementById('mobile-sidebar-backdrop');
      if (backdrop && !backdrop.classList.contains('hidden')) {{
        toggleMobileSidebar();
      }}

      renderAllCategories();
    }}

    function renderAllCategories() {{
      const root = document.getElementById('categories-root');
      if (!root || !window.DATASET) return;

      const categories = window.DATASET.categories || [];
      let html = '';
      let totalVisibleCards = 0;

      categories.forEach(cat => {{
        if (currentCategory !== 'all' && cat.id !== currentCategory) return;

        const filteredCards = (cat.cards || []).filter(c => {{
          if (!searchQuery) return true;
          const q = searchQuery.toLowerCase();
          return (
            (c.name && c.name.toLowerCase().includes(q)) ||
            (c.desc && c.desc.toLowerCase().includes(q)) ||
            (c.category && c.category.toLowerCase().includes(q)) ||
            (c.source && c.source.toLowerCase().includes(q)) ||
            (c.key && c.key.toLowerCase().includes(q)) ||
            (c.ratio_badge && c.ratio_badge.toLowerCase().includes(q))
          );
        }});

        if (filteredCards.length === 0) return;
        totalVisibleCards += filteredCards.length;

        html += `
          <section id="sec-${{cat.id}}" class="flex flex-col gap-4 scroll-mt-24">
            <div class="flex items-center justify-between border-b border-slate-200 dark:border-[#334155]/60 pb-3">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-xl bg-brand-red/10 border border-brand-red/30 flex items-center justify-center text-brand-red text-sm">
                  <i class="fas ${{cat.icon}}"></i>
                </div>
                <div>
                  <h2 class="text-lg sm:text-xl font-extrabold text-slate-950 dark:text-slate-100 tracking-tight">
                    ${{cat.name}}
                  </h2>
                </div>
              </div>
              <span class="text-xs font-bold px-2.5 py-1 rounded-lg bg-slate-200 dark:bg-[#1E293B] text-slate-800 dark:text-slate-300 font-mono">
                ${{filteredCards.length}} indicadores
              </span>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
              ${{filteredCards.map(c => renderIndicatorCardHTML(c)).join('')}}
            </div>
          </section>
        `;
      }});

      if (totalVisibleCards === 0) {{
        html = `
          <div class="p-12 text-center flex flex-col items-center justify-center glass-card rounded-3xl">
            <i class="fas fa-search text-4xl text-slate-400 dark:text-slate-500 mb-3"></i>
            <h3 class="text-lg font-bold text-slate-900 dark:text-slate-200">No se encontraron indicadores</h3>
            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1 font-medium">Intenta con otros términos de búsqueda como "Jubilación", "AUH", "PUAM", "IPC", o "Reservas".</p>
            <button onclick="clearSearch()" class="mt-4 px-4 py-2 rounded-xl bg-brand-red text-white text-xs font-bold hover:bg-brand-redHover transition-all shadow-lg shadow-brand-red/30">
              Limpiar Búsqueda
            </button>
          </div>
        `;
      }}

      root.innerHTML = html;

      setTimeout(() => {{
        categories.forEach(cat => {{
          (cat.cards || []).forEach(c => {{
            const isBar = isBarChartIndicator(c);
            drawSparkline(c.key, c.sparkline, isBar);
          }});
        }});
      }}, 50);
    }}

    function renderIndicatorCardHTML(card) {{
      const meta = getUnitMeta(card);
      const formattedVal = formatValueWithMeta(card.value, meta);

      const isPos = String(card.display_change).includes('+');
      const isNeg = String(card.display_change).includes('-');
      
      const momBadgeColor = isPos 
        ? 'bg-emerald-50 text-emerald-800 border-emerald-300 dark:bg-emerald-500/10 dark:text-emerald-400 dark:border-emerald-500/20' 
        : (isNeg 
            ? 'bg-rose-50 text-rose-800 border-rose-300 dark:bg-rose-500/10 dark:text-rose-400 dark:border-rose-500/20' 
            : 'bg-slate-100 text-slate-700 border-slate-300 dark:bg-slate-800 dark:text-slate-400 dark:border-slate-700');
            
      const momIcon = isPos 
        ? '<i class="fas fa-arrow-trend-up text-[10px] mr-1 text-emerald-600 dark:text-emerald-400"></i>' 
        : (isNeg 
            ? '<i class="fas fa-arrow-trend-down text-[10px] mr-1 text-rose-600 dark:text-rose-400"></i>' 
            : '');

      const ratioBadgeHTML = card.ratio_badge ? `
        <span class="text-[9px] font-bold px-1.5 py-0.5 rounded bg-purple-50 dark:bg-purple-500/20 text-purple-700 dark:text-purple-300 border border-purple-200 dark:border-purple-500/30 truncate max-w-[130px]" title="Ratio: ${{card.ratio_badge}}">
          <i class="fas fa-link text-[8px] mr-0.5"></i>${{card.ratio_badge}}
        </span>
      ` : '';

      return `
        <div 
          onclick="openModalByKey('${{card.key}}')"
          class="glass-card rounded-2xl p-4 flex flex-col justify-between cursor-pointer group relative overflow-hidden"
          title="Click para ver serie histórica verificada (${{card.total_points || 0}} pts) y regresión"
        >
          <div>
            <div class="flex items-center justify-between gap-1 mb-2.5 flex-wrap">
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/60 font-mono">
                ${{card.freq}}
              </span>

              ${{ratioBadgeHTML}}

              <span class="text-[10px] font-black font-mono px-2 py-0.5 rounded-md bg-rose-50 dark:bg-brand-red/15 text-brand-red border border-rose-200 dark:border-brand-red/30 flex items-center gap-1 shadow-2xs" title="Fecha del último dato oficial publicado">
                <i class="far fa-calendar-check text-[9px]"></i>
                <span>${{card.latest_date}}</span>
              </span>
            </div>

            <h3 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-slate-100 group-hover:text-brand-red transition-colors line-clamp-2 leading-snug">
              ${{card.name}}
            </h3>
          </div>

          <div class="my-3">
            <div class="text-xl sm:text-2xl font-black font-mono text-slate-950 dark:text-slate-50 tracking-tight">
              ${{formattedVal}}
            </div>

            <div class="flex items-center gap-2 mt-2 flex-wrap">
              <span class="px-2 py-0.5 rounded-lg border text-[11px] font-mono font-bold ${{momBadgeColor}} flex items-center" title="Variación de período">
                ${{momIcon}} ${{card.display_change}}
              </span>

              <span class="px-2 py-0.5 rounded-lg bg-slate-100 dark:bg-slate-800/90 text-slate-800 dark:text-slate-200 border border-slate-300 dark:border-slate-700/60 text-[11px] font-mono font-bold" title="Variación Interanual">
                ${{card.var_ia}}
              </span>
            </div>
          </div>

          <div class="pt-2 border-t border-slate-200 dark:border-slate-700/40 flex items-center justify-between gap-2">
            <div class="flex-1 h-10 relative">
              <canvas id="sparkline-${{card.key}}" class="sparkline-canvas"></canvas>
            </div>
            <div class="flex items-center gap-1">
              <span class="text-[9px] text-slate-400 font-mono" title="Puntos históricos verificados">${{card.total_points || 0}}p</span>
              <div class="w-7 h-7 rounded-lg bg-brand-red/10 border border-brand-red/20 group-hover:bg-brand-red group-hover:text-white text-brand-red flex items-center justify-center text-xs transition-all shrink-0 shadow-sm">
                <i class="fas fa-expand-alt"></i>
              </div>
            </div>
          </div>
        </div>
      `;
    }}

    function drawSparkline(key, prices, isBar = false) {{
      const canvas = document.getElementById(`sparkline-${{key}}`);
      if (!canvas || !prices || prices.length < 2) return;

      const ctx = canvas.getContext('2d');

      if (sparklineCharts[key]) {{
        sparklineCharts[key].destroy();
      }}

      const scaleBounds = computeScaleBounds(prices);

      if (isBar) {{
        const bgColors = prices.map(p => p >= 0 ? '#10B981' : '#E20039');
        const borderColors = prices.map(p => p >= 0 ? '#059669' : '#BE123C');

        sparklineCharts[key] = new Chart(ctx, {{
          type: 'bar',
          data: {{
            labels: prices.map((_, i) => i),
            datasets: [{{
              data: prices,
              backgroundColor: bgColors,
              borderColor: borderColors,
              borderWidth: 1,
              borderRadius: 2,
              barPercentage: 0.9,
              categoryPercentage: 0.9
            }}]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{ legend: {{ display: false }}, tooltip: {{ enabled: false }} }},
            scales: {{
              x: {{ display: false }},
              y: {{ 
                display: false,
                min: scaleBounds.min,
                max: scaleBounds.max
              }}
            }},
            animation: false
          }}
        }});
      }} else {{
        const isUp = prices[prices.length - 1] >= prices[0];
        const strokeColor = isUp ? '#059669' : '#E20039';
        const fillColor = isUp ? 'rgba(5, 150, 105, 0.15)' : 'rgba(226, 0, 57, 0.15)';

        sparklineCharts[key] = new Chart(ctx, {{
          type: 'line',
          data: {{
            labels: prices.map((_, i) => i),
            datasets: [{{
              data: prices,
              borderColor: strokeColor,
              borderWidth: 2,
              pointRadius: 0,
              pointHoverRadius: 0,
              tension: 0.35,
              fill: true,
              backgroundColor: fillColor
            }}]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{ legend: {{ display: false }}, tooltip: {{ enabled: false }} }},
            scales: {{
              x: {{ display: false }},
              y: {{ 
                display: false,
                min: scaleBounds.min,
                max: scaleBounds.max
              }}
            }},
            animation: false
          }}
        }});
      }}
    }}

    function handleSearch(val) {{
      searchQuery = val.trim();
      const banner = document.getElementById('search-status-banner');
      const queryText = document.getElementById('search-query-text');
      const clearBtn = document.getElementById('search-clear-btn');

      if (searchQuery) {{
        if (banner) banner.classList.remove('hidden');
        if (queryText) queryText.innerText = searchQuery;
        if (clearBtn) clearBtn.classList.remove('hidden');
      }} else {{
        if (banner) banner.classList.add('hidden');
        if (clearBtn) clearBtn.classList.add('hidden');
      }}

      renderAllCategories();
    }}

    function clearSearch() {{
      searchQuery = '';
      const input = document.getElementById('global-search-input');
      if (input) input.value = '';
      const banner = document.getElementById('search-status-banner');
      const clearBtn = document.getElementById('search-clear-btn');
      if (banner) banner.classList.add('hidden');
      if (clearBtn) clearBtn.classList.add('hidden');
      renderAllCategories();
    }}

    function openModalByKey(key) {{
      const card = findCardByKey(key);
      if (!card) return;

      const meta = getUnitMeta(card);
      const histDB = window.DATASET.historical_db || {{}};
      const hist = histDB[key];

      let dates = [];
      let prices = [];

      if (hist) {{
        if (hist.dates && hist.prices) {{
          dates = hist.dates;
          prices = hist.prices;
        }} else if (hist.daily) {{
          dates = hist.daily.dates || [];
          prices = hist.daily.prices || [];
        }} else if (hist.monthly) {{
          dates = hist.monthly.dates || [];
          prices = hist.monthly.prices || [];
        }}
      }}

      if (dates.length === 0 && card.sparkline) {{
        prices = card.sparkline;
        dates = prices.map((_, i) => `T-${{prices.length - i}}`);
      }}

      modalState.key = key;
      modalState.card = card;
      modalState.meta = meta;
      modalState.isBar = isBarChartIndicator(card);
      modalState.series = {{ dates, prices }};
      modalState.period = '2A';
      modalState.showRegression = true;

      // Populate Header
      document.getElementById('modal-title').innerText = card.name;
      document.getElementById('modal-desc').innerText = card.desc;
      document.getElementById('modal-category-badge').innerText = card.category;
      document.getElementById('modal-freq-badge').innerText = card.freq;
      document.getElementById('modal-source-badge').innerText = card.source;
      document.getElementById('modal-date-badge').innerText = `Último Dato: ${{card.latest_date}}`;

      const ratioBadgeEl = document.getElementById('modal-ratio-badge');
      if (ratioBadgeEl) {{
        if (card.ratio_badge) {{
          ratioBadgeEl.innerText = `Ratio: ${{card.ratio_badge}}`;
          ratioBadgeEl.classList.remove('hidden');
        }} else {{
          ratioBadgeEl.classList.add('hidden');
        }}
      }}

      // Icon
      const iconEl = document.getElementById('modal-icon');
      if (iconEl) {{
        iconEl.className = modalState.isBar ? "fas fa-chart-column" : "fas fa-chart-line";
      }}

      // Populate Stats
      const formattedLatest = formatValueWithMeta(card.value, meta);
      document.getElementById('modal-stat-latest').innerText = formattedLatest;
      document.getElementById('modal-stat-date').innerText = `Publicación: ${{card.latest_date}}`;

      const isPos = String(card.display_change).includes('+');
      const isNeg = String(card.display_change).includes('-');
      const momEl = document.getElementById('modal-stat-mom');
      momEl.innerText = card.display_change;
      momEl.className = `text-base sm:text-lg font-black font-mono mt-0.5 ${{isPos ? 'text-emerald-700 dark:text-emerald-400' : (isNeg ? 'text-rose-700 dark:text-rose-400' : 'text-slate-800 dark:text-slate-300')}}`;

      const yoyEl = document.getElementById('modal-stat-yoy');
      yoyEl.innerText = card.var_ia;
      yoyEl.className = `text-base sm:text-lg font-black font-mono mt-0.5 ${{String(card.var_ia).includes('+') ? 'text-emerald-700 dark:text-emerald-400' : (String(card.var_ia).includes('-') ? 'text-rose-700 dark:text-rose-400' : 'text-slate-800 dark:text-slate-300')}}`;

      const pMin = Math.min(...prices);
      const pMax = Math.max(...prices);
      const minStr = formatValueWithMeta(pMin, meta);
      const maxStr = formatValueWithMeta(pMax, meta);

      document.getElementById('modal-stat-range').innerText = `${{minStr}} / ${{maxStr}}`;
      document.getElementById('modal-stat-pts').innerText = `${{prices.length}} registros históricos`;

      const modalEl = document.getElementById('indicator-modal');
      modalEl.classList.remove('hidden');
      modalEl.classList.add('flex');
      setTimeout(() => {{
        modalEl.classList.remove('opacity-0');
        updateModalChart();
      }}, 10);
    }}

    function closeModal() {{
      const modalEl = document.getElementById('indicator-modal');
      modalEl.classList.add('opacity-0');
      setTimeout(() => {{
        modalEl.classList.add('hidden');
        modalEl.classList.remove('flex');
        if (modalChart) {{
          modalChart.destroy();
          modalChart = null;
        }}
      }}, 200);
    }}

    function handleModalBackdropClick(e) {{
      if (e.target.id === 'indicator-modal') {{
        closeModal();
      }}
    }}

    function setModalPeriod(p) {{
      modalState.period = p;
      updateModalChart();
    }}

    function toggleRegressionLine() {{
      modalState.showRegression = !modalState.showRegression;
      updateModalChart();
    }}

    function updateModalChart() {{
      if (!modalState.series || !modalState.series.prices.length) return;

      const meta = modalState.meta || getUnitMeta(modalState.card);
      const isBar = modalState.isBar;
      const {{ dates: rawDates, prices: rawPrices }} = modalState.series;

      // Real Calendar Filter
      const {{ dates: filteredDates, prices: filteredPrices }} = filterSeriesByCalendar(rawDates, rawPrices, modalState.period);
      const targetLen = filteredPrices.length;

      // Calculate 85% min and 115% max Y-scale padding for realistic, non-distorted visualization
      const scaleBounds = computeScaleBounds(filteredPrices);

      // Period buttons highlight
      ['1A', '2A', '3A', '5A', 'ALL'].forEach(p => {{
        const btn = document.getElementById(`btn-period-${{p}}`);
        if (btn) {{
          if (p === modalState.period) {{
            btn.className = "px-2.5 py-1 rounded-lg transition-colors border border-brand-red bg-brand-red text-white font-bold shadow-md shadow-brand-red/30";
          }} else {{
            btn.className = "px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-200 dark:hover:bg-slate-800 text-slate-800 dark:text-slate-300 font-semibold";
          }}
        }}
      }});

      // Regression button
      const regBtn = document.getElementById('btn-toggle-regression');
      const regBadge = document.getElementById('regression-badge');
      if (regBtn && regBadge) {{
        if (modalState.showRegression) {{
          regBtn.className = "px-3 py-1 text-xs font-bold rounded-xl border transition-all flex items-center gap-1.5 bg-brand-red/10 dark:bg-brand-red/20 border-brand-red text-brand-red shadow-sm";
          regBadge.className = "w-2 h-2 rounded-full bg-brand-red animate-pulse";
        }} else {{
          regBtn.className = "px-3 py-1 text-xs font-bold rounded-xl border transition-all flex items-center gap-1.5 bg-slate-200 dark:bg-slate-800/80 border-slate-300 dark:border-slate-700 text-slate-800 dark:text-slate-300";
          regBadge.className = "w-2 h-2 rounded-full bg-slate-400";
        }}
      }}

      // Calculate Linear Regression
      const n = filteredPrices.length;
      let sumX = 0, sumY = 0, sumXY = 0, sumXX = 0;
      for (let i = 0; i < n; i++) {{
        sumX += i;
        sumY += filteredPrices[i];
        sumXY += i * filteredPrices[i];
        sumXX += i * i;
      }}

      const slope = (n * sumXY - sumX * sumY) / ((n * sumXX - sumX * sumX) || 1);
      const intercept = (sumY - slope * sumX) / (n || 1);
      const regressionPrices = filteredPrices.map((_, i) => slope * i + intercept);

      const trendEl = document.getElementById('modal-stat-trend');
      const slopeEl = document.getElementById('modal-stat-slope');
      if (slope > 0.001) {{
        trendEl.innerText = "Alcista \u2191";
        trendEl.className = "text-sm font-black font-mono mt-1 text-emerald-700 dark:text-emerald-400";
      }} else if (slope < -0.001) {{
        trendEl.innerText = "Bajista \u2193";
        trendEl.className = "text-sm font-black font-mono mt-1 text-rose-700 dark:text-rose-400";
      }} else {{
        trendEl.innerText = "Estable \u2192";
        trendEl.className = "text-sm font-black font-mono mt-1 text-slate-800 dark:text-slate-300";
      }}

      const slopeUnit = meta.type === 'percent' ? 'p.p. / per' : (meta.suffix ? `${{meta.suffix.trim()}} / per` : (meta.prefix ? `${{meta.prefix.trim()}} / per` : '/ per'));
      slopeEl.innerText = `Pendiente: ${{slope.toFixed(2)}} ${{slopeUnit}}`;

      const canvas = document.getElementById('modal-main-chart');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');

      if (modalChart) {{
        modalChart.destroy();
      }}

      const isDark = document.documentElement.classList.contains('dark');
      const textColor = isDark ? '#CBD5E1' : '#334155';
      const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.07)';

      let datasets = [];

      if (isBar) {{
        const bgColors = filteredPrices.map(p => p >= 0 ? 'rgba(16, 185, 129, 0.85)' : 'rgba(226, 0, 57, 0.85)');
        const borderColors = filteredPrices.map(p => p >= 0 ? '#059669' : '#BE123C');

        datasets.push({{
          type: 'bar',
          label: modalState.card.name,
          data: filteredPrices,
          backgroundColor: bgColors,
          borderColor: borderColors,
          borderWidth: 1.5,
          borderRadius: 4,
          barPercentage: 0.85
        }});
      }} else {{
        datasets.push({{
          type: 'line',
          label: modalState.card.name,
          data: filteredPrices,
          borderColor: '#E20039',
          borderWidth: 2.5,
          pointBackgroundColor: '#E20039',
          pointBorderColor: '#FFFFFF',
          pointBorderWidth: 1.5,
          pointRadius: targetLen > 60 ? 0 : (targetLen > 30 ? 1.5 : 3),
          pointHoverRadius: 6,
          fill: true,
          backgroundColor: isDark ? 'rgba(226, 0, 57, 0.15)' : 'rgba(226, 0, 57, 0.08)',
          tension: 0.25
        }});
      }}

      if (modalState.showRegression) {{
        datasets.push({{
          type: 'line',
          label: 'Recta de Regresión (Tendencia)',
          data: regressionPrices,
          borderColor: '#0284C7',
          borderWidth: 2,
          borderDash: [6, 4],
          pointRadius: 0,
          fill: false,
          tension: 0
        }});
      }}

      modalChart = new Chart(ctx, {{
        type: isBar ? 'bar' : 'line',
        data: {{
          labels: filteredDates,
          datasets: datasets
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          interaction: {{
            mode: 'index',
            intersect: false
          }},
          plugins: {{
            legend: {{
              display: true,
              position: 'top',
              labels: {{
                color: textColor,
                font: {{ family: 'Sora', size: 11, weight: '700' }}
              }}
            }},
            tooltip: {{
              backgroundColor: isDark ? '#0F172A' : '#FFFFFF',
              titleColor: isDark ? '#F1F5F9' : '#0F172A',
              bodyColor: isDark ? '#CBD5E1' : '#1E293B',
              borderColor: '#E20039',
              borderWidth: 1.5,
              padding: 10,
              displayColors: true,
              callbacks: {{
                title: function(context) {{
                  const rawD = context[0].label;
                  return formatDateSpanish(rawD, 'full');
                }},
                label: function(context) {{
                  const val = context.raw || 0;
                  const formatted = formatValueWithMeta(val, meta);
                  if (isBar && context.dataset.type === 'bar') {{
                    const isPct = meta.type === 'percent';
                    const prefixState = val >= 0 
                      ? (isPct ? '🟢 Crecimiento: +' : '🟢 Superávit: ') 
                      : (isPct ? '🔴 Caída: ' : '🔴 Déficit: ');
                    return `${{prefixState}}${{formatted}}`;
                  }}
                  return `${{context.dataset.label}}: ${{formatted}}`;
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              grid: {{ color: gridColor }},
              ticks: {{
                color: textColor,
                font: {{ family: 'JetBrains Mono', size: 10, weight: '600' }},
                maxTicksLimit: 8,
                maxRotation: 30,
                callback: function(val, index) {{
                  const rawD = this.getLabelForValue(val);
                  return formatDateSpanish(rawD, 'short');
                }}
              }}
            }},
            y: {{
              min: scaleBounds.min,
              max: scaleBounds.max,
              grid: {{ color: gridColor }},
              ticks: {{
                color: textColor,
                font: {{ family: 'JetBrains Mono', size: 10, weight: '600' }},
                callback: function(val) {{
                  return formatValueWithMeta(val, meta, true);
                }}
              }}
            }}
          }}
        }}
      }});
    }}

    function exportModalChartPNG() {{
      const chartCanvas = document.getElementById('modal-main-chart');
      if (!chartCanvas || !modalState.card) return;

      const card = modalState.card;
      const meta = modalState.meta || getUnitMeta(card);
      const formattedVal = formatValueWithMeta(card.value, meta);
      const isDark = document.documentElement.classList.contains('dark');

      // High DPI 2x retina export canvas
      const exportCanvas = document.createElement('canvas');
      const dpr = 2;
      const width = 1200;
      const height = 750;
      exportCanvas.width = width * dpr;
      exportCanvas.height = height * dpr;

      const ctx = exportCanvas.getContext('2d');
      ctx.scale(dpr, dpr);

      // Theme Colors
      const bgColor = isDark ? '#0F172A' : '#FFFFFF';
      const cardBgColor = isDark ? '#1E293B' : '#F8FAFC';
      const textColor = isDark ? '#F8FAFC' : '#0F172A';
      const subTextColor = isDark ? '#94A3B8' : '#475569';
      const borderColor = isDark ? '#334155' : '#E2E8F0';
      const brandRed = '#E20039';

      // 1. Fill Solid Canvas Background (NO TRANSPARENCY - GUARANTEED WHITE IN LIGHT MODE)
      ctx.fillStyle = bgColor;
      ctx.fillRect(0, 0, width, height);

      // 2. Header Box
      ctx.fillStyle = cardBgColor;
      ctx.fillRect(24, 20, width - 48, 115);
      ctx.strokeStyle = borderColor;
      ctx.lineWidth = 1.5;
      ctx.strokeRect(24, 20, width - 48, 115);

      // Top Subheader
      ctx.fillStyle = brandRed;
      ctx.font = 'bold 12px "Sora", sans-serif';
      ctx.fillText('ECONOMÍA  •  TABLERO DE INDICADORES ECONÓMICOS', 44, 44);

      // Indicator Title
      ctx.fillStyle = textColor;
      ctx.font = 'bold 20px "Sora", sans-serif';
      let title = card.name;
      if (title.length > 55) title = title.slice(0, 52) + '...';
      ctx.fillText(title, 44, 72);

      // Metadata info line
      ctx.fillStyle = subTextColor;
      ctx.font = '600 12px "Sora", sans-serif';
      let metaInfo = `Categoría: ${{card.category}}   |   Frecuencia: ${{card.freq}}   |   Último Dato: ${{card.latest_date}}`;
      if (card.ratio_badge) metaInfo += `   |   Ratio: ${{card.ratio_badge}}`;
      ctx.fillText(metaInfo, 44, 100);

      // Value & Changes on the Right
      ctx.textAlign = 'right';
      ctx.fillStyle = textColor;
      ctx.font = 'bold 26px "JetBrains Mono", monospace';
      ctx.fillText(formattedVal, width - 44, 62);

      ctx.font = 'bold 13px "JetBrains Mono", monospace';
      const isPos = String(card.display_change).includes('+');
      const isNeg = String(card.display_change).includes('-');
      ctx.fillStyle = isPos ? '#10B981' : (isNeg ? '#E20039' : subTextColor);
      ctx.fillText(`${{card.display_change}}   ${{card.var_ia}}`, width - 44, 90);
      ctx.textAlign = 'left';

      // 3. Chart Container
      const chartX = 24;
      const chartY = 150;
      const chartW = width - 48;
      const chartH = height - 200;

      ctx.fillStyle = isDark ? '#1E293B' : '#FFFFFF';
      ctx.fillRect(chartX, chartY, chartW, chartH);
      ctx.strokeStyle = borderColor;
      ctx.strokeRect(chartX, chartY, chartW, chartH);

      // Draw Chart
      ctx.drawImage(chartCanvas, chartX + 10, chartY + 10, chartW - 20, chartH - 20);

      // 4. Footer Line
      ctx.fillStyle = subTextColor;
      ctx.font = '500 11px "Sora", sans-serif';
      ctx.fillText(`Fuente oficial: ${{card.source}}  •  Generado el ${{new Date().toLocaleDateString('es-AR')}}  •  Datos 100% Verificados`, 30, height - 18);

      ctx.textAlign = 'right';
      ctx.fillText('https://genesisfinal.github.io/tablero-economia/', width - 30, height - 18);
      ctx.textAlign = 'left';

      // 5. Trigger Download
      const themeTag = isDark ? 'oscuro' : 'claro';
      const dateTag = new Date().toISOString().slice(0, 10);
      const link = document.createElement('a');
      link.download = `${{card.key}}_${{themeTag}}_${{dateTag}}.png`;
      link.href = exportCanvas.toDataURL('image/png');
      link.click();
    }}

    function exportAllCSV() {{
      if (!window.DATASET || !window.DATASET.categories) return;

      let csv = 'Categoria,Indicador,Clave,Frecuencia,Fuente,Fecha_Publicacion,Valor_Actual,Var_Periodo,Var_Interanual,Ratio_Badge\\n';
      window.DATASET.categories.forEach(cat => {{
        (cat.cards || []).forEach(c => {{
          const meta = getUnitMeta(c);
          const formattedVal = formatValueWithMeta(c.value, meta);
          const row = [
            `"${{cat.name}}"`,
            `"${{c.name}}"`,
            `"${{c.key}}"`,
            `"${{c.freq}}"`,
            `"${{c.source}}"`,
            `"${{c.latest_date}}"`,
            `"${{formattedVal}}"`,
            `"${{c.display_change}}"`,
            `"${{c.var_ia}}"`,
            `"${{c.ratio_badge || ''}}"`
          ].join(',');
          csv += row + '\\n';
        }});
      }});

      const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', `tablero_indicadores_economicos_${{new Date().toISOString().slice(0,10)}}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }}

    function findCardByKey(key) {{
      if (!window.DATASET || !window.DATASET.categories) return null;
      for (const cat of window.DATASET.categories) {{
        for (const card of (cat.cards || [])) {{
          if (card.key === key) return card;
        }}
      }}
      return null;
    }}

    function setupKeyboardShortcuts() {{
      document.addEventListener('keydown', (e) => {{
        if (e.key === 'Escape') {{
          closeModal();
        }}
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {{
          e.preventDefault();
          const search = document.getElementById('global-search-input');
          if (search) search.focus();
        }}
      }});
    }}
  </script>

</body>
</html>
'''

    out_file = os.path.join(workspace, 'index.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"[SUCCESS] Wrote index.html with 85% min and 115% max Y-scale padding ({len(html_content)} bytes)!")

if __name__ == "__main__":
    build_index_html()
