import json
import os

def build_index_html():
    print("Building index.html with real historical series and visible date badges on every card...")

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
  <title>Tablero de Indicadores Económicos | La Segunda Seguros</title>
  
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
              gold: '#F59E0B'
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    /* Base Theme Styles */
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

    /* High Contrast Glass Cards */
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

    /* Sidebar Active States */
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

    /* Scrollbars */
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
      
      <!-- Left: Mobile Menu Toggle & Brand Logo -->
      <div class="flex items-center gap-3 shrink-0">
        <button onclick="toggleMobileSidebar()" class="lg:hidden p-2 rounded-xl bg-slate-100 dark:bg-[#1E293B] text-slate-700 dark:text-slate-300 hover:text-black dark:hover:text-white border border-slate-300 dark:border-[#334155]">
          <i class="fas fa-bars text-sm"></i>
        </button>

        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-brand-red to-[#9B0024] flex items-center justify-center text-white shadow-lg shadow-brand-red/30">
          <i class="fas fa-chart-pie text-base"></i>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-bold uppercase tracking-wider text-brand-red">LA SEGUNDA</span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-brand-red/10 text-brand-red font-semibold border border-brand-red/20">ECONOMÍA</span>
          </div>
          <h1 class="text-base sm:text-lg font-bold text-slate-900 dark:text-slate-100 tracking-tight leading-tight">
            Tablero de Indicadores Económicos
          </h1>
        </div>
      </div>

      <!-- Center: Quick Search Bar -->
      <div class="flex-1 max-w-lg hidden md:block">
        <div class="relative">
          <i class="fas fa-search absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
          <input 
            type="text" 
            id="global-search-input"
            placeholder="Buscar indicador (ej. IPC, Reservas, Salarios, Deuda, PBI)... (Ctrl + K)"
            oninput="handleSearch(this.value)"
            class="w-full bg-slate-100 dark:bg-[#1E293B]/80 text-xs text-slate-900 dark:text-slate-100 placeholder:text-slate-500 dark:placeholder:text-slate-400 rounded-xl pl-9 pr-8 py-2 border border-slate-300 dark:border-[#334155]/60 focus:outline-none focus:border-brand-red focus:ring-1 focus:ring-brand-red transition-all font-medium"
          >
          <button id="search-clear-btn" onclick="clearSearch()" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 text-xs">
            <i class="fas fa-times"></i>
          </button>
        </div>
      </div>

      <!-- Right: Layout Switcher & Theme Toggle -->
      <div class="flex items-center gap-2">
        
        <!-- Navigation Layout Mode Toggle (Sidebar vs 2-Row Top Menu) -->
        <div class="hidden sm:flex items-center p-1 rounded-xl bg-slate-100 dark:bg-[#1E293B] border border-slate-300 dark:border-[#334155] text-xs font-semibold">
          <button 
            onclick="setNavLayout('sidebar')" 
            id="layout-btn-sidebar"
            class="px-2.5 py-1 rounded-lg transition-all flex items-center gap-1.5 bg-brand-red text-white shadow-sm"
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

  <!-- TOP 2-ROW CATEGORY GRID (Shown when NavLayout is 'topgrid') -->
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

  <!-- MAIN APP WRAPPER (SIDEBAR + CONTENT) -->
  <div class="max-w-[1900px] mx-auto px-4 sm:px-6 lg:px-8 py-6 w-full flex-grow flex items-start gap-6">
    
    <!-- LEFT SIDEBAR NAVIGATION -->
    <aside id="left-sidebar" class="w-64 xl:w-72 shrink-0 sticky top-20 flex flex-col gap-4 max-h-[calc(100vh-100px)] overflow-y-auto pr-1">
      
      <!-- Sidebar Box -->
      <div class="glass-card rounded-2xl p-3 border border-slate-200 dark:border-[#334155]/60">
        
        <!-- Sidebar Header -->
        <div class="px-3 py-2 border-b border-slate-200 dark:border-[#334155]/50 flex items-center justify-between mb-2">
          <span class="text-xs font-bold uppercase tracking-wider text-slate-800 dark:text-slate-300 flex items-center gap-1.5">
            <i class="fas fa-layer-group text-brand-red"></i>
            <span>Categorías</span>
          </span>
          <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-full bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-400" id="sidebar-total-badge">88</span>
        </div>

        <!-- Sidebar Category Links List -->
        <div class="flex flex-col gap-1 text-xs font-medium" id="sidebar-category-list">
          <!-- Rendered dynamically -->
        </div>

      </div>

      <!-- Quick Info Box -->
      <div class="glass-card rounded-2xl p-4 border border-slate-200 dark:border-[#334155]/50 text-xs flex flex-col gap-2">
        <div class="flex items-center gap-2 text-emerald-600 dark:text-emerald-400 font-bold">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span>Datos 100% Verificados</span>
        </div>
        <p class="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed font-medium">
          Series oficiales extraídas directamente de BCRA, INDEC y ArgentinaDatos sin interpolación.
        </p>
        <div class="text-[10px] text-slate-500 dark:text-slate-400 font-mono mt-1 pt-2 border-t border-slate-200 dark:border-[#334155]/40">
          Act: <span id="sidebar-update-time" class="text-slate-800 dark:text-slate-300 font-bold">...</span>
        </div>
      </div>

    </aside>

    <!-- MOBILE OFF-CANVAS SIDEBAR BACKDROP & DRAWER -->
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

    <!-- MAIN CONTENT AREA -->
    <main class="flex-1 w-full min-w-0">
      
      <!-- Search Results Status Banner (When searching) -->
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

      <!-- CATEGORIES SECTION -->
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
        <span>Sistema de Monitoreo Macroeconómico • <strong class="text-slate-900 dark:text-slate-200">La Segunda Seguros</strong></span>
      </div>
      <div class="flex items-center gap-4">
        <span>Última Actualización: <strong id="footer-update-time" class="text-slate-900 dark:text-slate-200 font-mono font-bold"></strong></span>
        <span>•</span>
        <span>Fuentes: INDEC, BCRA, Min. Economía, AFIP/ARCA, ArgentinaDatos</span>
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

      <!-- Modal Body (Stats + Chart + Controls) -->
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

        <!-- Chart Controls (Time Range & Regression Line Switch) -->
        <div class="flex flex-wrap items-center justify-between gap-3 bg-slate-100/80 dark:bg-[#0F172A]/40 p-2.5 rounded-2xl border border-slate-200 dark:border-[#334155]/40">
          
          <!-- Period Selector -->
          <div class="flex items-center gap-1 text-xs font-semibold">
            <span class="text-slate-600 dark:text-slate-400 mr-1 text-[11px] font-bold">Rango:</span>
            <button onclick="setModalPeriod('1A')" id="btn-period-1A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-200 dark:hover:bg-slate-800">1A</button>
            <button onclick="setModalPeriod('2A')" id="btn-period-2A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-200 dark:hover:bg-slate-800">2A</button>
            <button onclick="setModalPeriod('3A')" id="btn-period-3A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-200 dark:hover:bg-slate-800">3A</button>
            <button onclick="setModalPeriod('5A')" id="btn-period-5A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-200 dark:hover:bg-slate-800">5A</button>
            <button onclick="setModalPeriod('ALL')" id="btn-period-ALL" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-200 dark:hover:bg-slate-800">Histórico</button>
          </div>

          <!-- Regression Line Toggle & Download PNG -->
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

        <!-- Main Interactive Chart Canvas -->
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
    // State Management
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

    // Initialization
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
        if (totalBadgeEl) totalBadgeEl.innerText = window.DATASET.metadata.total_indicators || 88;
      }}
    }});

    // Layout Switcher (Sidebar vs 2-Row Top Menu)
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

        if (btnTopGrid) {{
          btnTopGrid.className = "px-2.5 py-1 rounded-lg transition-all flex items-center gap-1.5 bg-brand-red text-white shadow-sm font-bold";
        }}
        if (btnSidebar) {{
          btnSidebar.className = "px-2.5 py-1 rounded-lg transition-all flex items-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-black dark:hover:text-white";
        }}
      }} else {{
        // Sidebar Mode
        if (sidebarEl) sidebarEl.classList.remove('hidden');
        if (topGridEl) topGridEl.classList.add('hidden');

        if (btnSidebar) {{
          btnSidebar.className = "px-2.5 py-1 rounded-lg transition-all flex items-center gap-1.5 bg-brand-red text-white shadow-sm font-bold";
        }}
        if (btnTopGrid) {{
          btnTopGrid.className = "px-2.5 py-1 rounded-lg transition-all flex items-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-black dark:hover:text-white";
        }}
      }}
    }}

    // Mobile Sidebar Drawer Toggle
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

    // Theme Switcher
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

    // Top Highlight KPIs
    function renderTopKPIs() {{
      const container = document.getElementById('top-kpis-container');
      if (!container || !window.DATASET) return;

      const kpiKeys = [
        {{ key: 'ipc_mensual', label: 'IPC Mensual', icon: 'fa-percentage', color: 'text-amber-600 dark:text-amber-400' }},
        {{ key: 'ipc_interanual', label: 'IPC Interanual', icon: 'fa-chart-simple', color: 'text-rose-600 dark:text-rose-400' }},
        {{ key: 'riesgo_pais', label: 'Riesgo País', icon: 'fa-arrow-trend-down', color: 'text-blue-600 dark:text-blue-400' }},
        {{ key: 'reservas_brutas', label: 'Reservas BCRA', icon: 'fa-vault', color: 'text-emerald-600 dark:text-emerald-400' }},
        {{ key: 'base_monetaria', label: 'Base Monetaria', icon: 'fa-money-bill-wave', color: 'text-cyan-600 dark:text-cyan-400' }},
        {{ key: 'smvm_val', label: 'Salario Mínimo (SMVM)', icon: 'fa-wallet', color: 'text-purple-600 dark:text-purple-400' }}
      ];

      let html = '';
      kpiKeys.forEach(k => {{
        let cardData = findCardByKey(k.key);
        if (!cardData && k.key === 'smvm_val') cardData = findCardByKey('salario_minimo');
        if (!cardData && k.key === 'reservas_brutas') cardData = findCardByKey('reservas_bcra');

        if (cardData) {{
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
                ${{cardData.display_value}}
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

    // Sidebar Category Navigation
    function renderSidebarNavigation() {{
      const sidebarContainer = document.getElementById('sidebar-category-list');
      const mobileContainer = document.getElementById('mobile-sidebar-category-list');
      if (!sidebarContainer || !window.DATASET) return;

      const categories = window.DATASET.categories || [];
      const totalCount = window.DATASET.metadata.total_indicators || 88;

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

    // Top 2-Row Category Grid Navigation
    function renderTopGridNavigation() {{
      const container = document.getElementById('top-grid-tabs-container');
      if (!container || !window.DATASET) return;

      const categories = window.DATASET.categories || [];
      const totalCount = window.DATASET.metadata.total_indicators || 88;

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

      // Update Sidebar Items
      document.querySelectorAll('.sidebar-item').forEach(btn => {{
        btn.classList.remove('active');
        btn.classList.add('text-slate-700', 'dark:text-slate-400');
      }});
      const activeSidebar = document.getElementById(`sidebar-item-${{catId}}`);
      if (activeSidebar) activeSidebar.classList.add('active');

      // Update Top Grid Items
      document.querySelectorAll('.top-tab-btn').forEach(btn => {{
        btn.classList.remove('active', 'bg-brand-red', 'text-white');
        btn.classList.add('bg-slate-100', 'dark:bg-[#1E293B]', 'text-slate-700', 'dark:text-slate-400');
      }});
      const activeTop = document.getElementById(`top-grid-item-${{catId}}`);
      if (activeTop) {{
        activeTop.classList.add('active', 'bg-brand-red', 'text-white');
        activeTop.classList.remove('bg-slate-100', 'dark:bg-[#1E293B]', 'text-slate-700', 'dark:text-slate-400');
      }}

      // Close mobile drawer if open
      const backdrop = document.getElementById('mobile-sidebar-backdrop');
      if (backdrop && !backdrop.classList.contains('hidden')) {{
        toggleMobileSidebar();
      }}

      renderAllCategories();
    }}

    // Render Categories & Indicator Cards
    function renderAllCategories() {{
      const root = document.getElementById('categories-root');
      if (!root || !window.DATASET) return;

      const categories = window.DATASET.categories || [];
      let html = '';
      let totalVisibleCards = 0;

      categories.forEach(cat => {{
        if (currentCategory !== 'all' && cat.id !== currentCategory) return;

        // Filter cards by search query if applicable
        const filteredCards = (cat.cards || []).filter(c => {{
          if (!searchQuery) return true;
          const q = searchQuery.toLowerCase();
          return (
            (c.name && c.name.toLowerCase().includes(q)) ||
            (c.desc && c.desc.toLowerCase().includes(q)) ||
            (c.category && c.category.toLowerCase().includes(q)) ||
            (c.source && c.source.toLowerCase().includes(q)) ||
            (c.key && c.key.toLowerCase().includes(q))
          );
        }});

        if (filteredCards.length === 0) return;
        totalVisibleCards += filteredCards.length;

        html += `
          <section id="sec-${{cat.id}}" class="flex flex-col gap-4 scroll-mt-24">
            
            <!-- Category Header with High Contrast -->
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

            <!-- Cards Grid -->
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
            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1 font-medium">Intenta con otros términos de búsqueda como "IPC", "Reservas", "Salarios", o "PBI".</p>
            <button onclick="clearSearch()" class="mt-4 px-4 py-2 rounded-xl bg-brand-red text-white text-xs font-bold hover:bg-brand-redHover transition-all shadow-lg shadow-brand-red/30">
              Limpiar Búsqueda
            </button>
          </div>
        `;
      }}

      root.innerHTML = html;

      // Draw all sparklines in DOM
      setTimeout(() => {{
        categories.forEach(cat => {{
          (cat.cards || []).forEach(c => {{
            drawSparkline(c.key, c.sparkline);
          }});
        }});
      }}, 50);
    }}

    // Indicator Card Template with Visible Date Badge & High Contrast
    function renderIndicatorCardHTML(card) {{
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

      return `
        <div 
          onclick="openModalByKey('${{card.key}}')"
          class="glass-card rounded-2xl p-4 flex flex-col justify-between cursor-pointer group relative overflow-hidden"
          title="Click para ver serie histórica verificada (${{card.total_points || 0}} pts) y regresión"
        >
          <!-- Top row: Frequency, Date Badge & Source -->
          <div>
            <div class="flex items-center justify-between gap-1 mb-2.5">
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/60 font-mono">
                ${{card.freq}}
              </span>

              <!-- PROMINENT LAST UPDATED DATE BADGE -->
              <span class="text-[10px] font-black font-mono px-2 py-0.5 rounded-md bg-rose-50 dark:bg-brand-red/15 text-brand-red border border-rose-200 dark:border-brand-red/30 flex items-center gap-1 shadow-2xs" title="Fecha del último dato oficial publicado">
                <i class="far fa-calendar-check text-[9px]"></i>
                <span>${{card.latest_date}}</span>
              </span>

              <span class="text-[10px] text-slate-500 dark:text-slate-400 font-bold truncate max-w-[75px]" title="Fuente: ${{card.source}}">
                ${{card.source.split('/')[0].trim()}}
              </span>
            </div>

            <!-- Indicator Title: High Contrast Text -->
            <h3 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-slate-100 group-hover:text-brand-red transition-colors line-clamp-2 leading-snug">
              ${{card.name}}
            </h3>
          </div>

          <!-- Mid row: Big Bold Value & Dual Variation Badges -->
          <div class="my-3">
            <div class="text-xl sm:text-2xl font-black font-mono text-slate-950 dark:text-slate-50 tracking-tight">
              ${{card.display_value}}
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

          <!-- Bottom: Real Sparkline Canvas & Points Counter -->
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

    // Draw Smooth Canvas Sparkline
    function drawSparkline(key, prices) {{
      const canvas = document.getElementById(`sparkline-${{key}}`);
      if (!canvas || !prices || prices.length < 2) return;

      const ctx = canvas.getContext('2d');
      const isUp = prices[prices.length - 1] >= prices[0];
      const strokeColor = isUp ? '#059669' : '#E20039';
      const fillColor = isUp ? 'rgba(5, 150, 105, 0.15)' : 'rgba(226, 0, 57, 0.15)';

      if (sparklineCharts[key]) {{
        sparklineCharts[key].destroy();
      }}

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
            y: {{ display: false }}
          }},
          animation: false
        }}
      }});
    }}

    // Search Filtering
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

    // Modal & Interactive Regression Chart Logic
    function openModalByKey(key) {{
      const card = findCardByKey(key);
      if (!card) return;

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
      modalState.series = {{ dates, prices }};
      modalState.period = '2A';
      modalState.showRegression = true;

      // Populate Header & Info
      document.getElementById('modal-title').innerText = card.name;
      document.getElementById('modal-desc').innerText = card.desc;
      document.getElementById('modal-category-badge').innerText = card.category;
      document.getElementById('modal-freq-badge').innerText = card.freq;
      document.getElementById('modal-source-badge').innerText = card.source;
      document.getElementById('modal-date-badge').innerText = `Último Dato: ${{card.latest_date}}`;

      // Populate Stats
      document.getElementById('modal-stat-latest').innerText = card.display_value;
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

      document.getElementById('modal-stat-range').innerText = `${{pMin.toLocaleString('es-AR')}} / ${{pMax.toLocaleString('es-AR')}}`;
      document.getElementById('modal-stat-pts').innerText = `${{prices.length}} registros históricos`;

      // Open Modal DOM
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

      const {{ dates, prices }} = modalState.series;
      let targetLen = prices.length;

      if (modalState.period === '1A') targetLen = Math.min(12, prices.length);
      else if (modalState.period === '2A') targetLen = Math.min(24, prices.length);
      else if (modalState.period === '3A') targetLen = Math.min(36, prices.length);
      else if (modalState.period === '5A') targetLen = Math.min(60, prices.length);
      else if (modalState.period === 'ALL') targetLen = prices.length;

      const filteredDates = dates.slice(-targetLen);
      const filteredPrices = prices.slice(-targetLen);

      // Highlight Period Buttons
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

      // Update Regression Button State
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

      // Calculate Linear Regression (y = mx + b)
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

      // Trend label
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
      slopeEl.innerText = `Pendiente: ${{slope.toFixed(3)}}/per`;

      // Render Chart.js
      const canvas = document.getElementById('modal-main-chart');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');

      if (modalChart) {{
        modalChart.destroy();
      }}

      const isDark = document.documentElement.classList.contains('dark');
      const textColor = isDark ? '#CBD5E1' : '#334155';
      const gridColor = isDark ? 'rgba(255,255,255,0.06)' : 'rgba(0,0,0,0.07)';

      const datasets = [
        {{
          label: modalState.card.name,
          data: filteredPrices,
          borderColor: '#E20039',
          borderWidth: 2.5,
          pointBackgroundColor: '#E20039',
          pointBorderColor: '#FFFFFF',
          pointBorderWidth: 1.5,
          pointRadius: targetLen > 40 ? 1 : 3,
          pointHoverRadius: 6,
          fill: true,
          backgroundColor: isDark ? 'rgba(226, 0, 57, 0.15)' : 'rgba(226, 0, 57, 0.08)',
          tension: 0.25
        }}
      ];

      if (modalState.showRegression) {{
        datasets.push({{
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
        type: 'line',
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
                label: function(context) {{
                  const val = context.raw || 0;
                  return `${{context.dataset.label}}: ${{val.toLocaleString('es-AR')}}`;
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
                maxRotation: 45
              }}
            }},
            y: {{
              grid: {{ color: gridColor }},
              ticks: {{
                color: textColor,
                font: {{ family: 'JetBrains Mono', size: 10, weight: '600' }},
                callback: function(val) {{
                  return val.toLocaleString('es-AR');
                }}
              }}
            }}
          }}
        }}
      }});
    }}

    // Export Modal Chart Image
    function exportModalChartPNG() {{
      const canvas = document.getElementById('modal-main-chart');
      if (!canvas || !modalState.card) return;

      const link = document.createElement('a');
      link.download = `${{modalState.card.key}}_grafico.png`;
      link.href = canvas.toDataURL('image/png');
      link.click();
    }}

    // Export Complete Dataset as CSV
    function exportAllCSV() {{
      if (!window.DATASET || !window.DATASET.categories) return;

      let csv = 'Categoria,Indicador,Clave,Frecuencia,Fuente,Fecha_Publicacion,Valor_Actual,Var_Periodo,Var_Interanual\\n';
      window.DATASET.categories.forEach(cat => {{
        (cat.cards || []).forEach(c => {{
          const row = [
            `"${{cat.name}}"`,
            `"${{c.name}}"`,
            `"${{c.key}}"`,
            `"${{c.freq}}"`,
            `"${{c.source}}"`,
            `"${{c.latest_date}}"`,
            `"${{c.display_value}}"`,
            `"${{c.display_change}}"`,
            `"${{c.var_ia}}"`
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

    // Helper: Find Card in Master Dataset
    function findCardByKey(key) {{
      if (!window.DATASET || !window.DATASET.categories) return null;
      for (const cat of window.DATASET.categories) {{
        for (const card of (cat.cards || [])) {{
          if (card.key === key) return card;
        }}
      }}
      return null;
    }}

    // Keyboard Shortcuts
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

    print(f"[SUCCESS] Wrote index.html with visible date badges & verified series ({len(html_content)} bytes)!")

if __name__ == "__main__":
    build_index_html()
