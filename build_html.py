import json
import os

def build_index_html():
    print("Building index.html with embedded dataset...")

    dataset_path = r'g:\Mi unidad\IA\Tablero-Economía\master_dataset.json'
    with open(dataset_path, 'r', encoding='utf-8') as f:
        master_dataset = json.load(f)

    json_str = json.dumps(master_dataset, ensure_ascii=False)

    html_content = f'''<!DOCTYPE html>
<html lang="es" class="dark">
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
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

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
              card: '#1E293B',
              cardLight: '#FFFFFF',
              border: '#334155',
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
    body {{
      font-family: 'Sora', sans-serif;
      background-color: #0B1120;
      color: #F1F5F9;
      overflow-x: hidden;
    }}
    html.light body {{
      background-color: #F8FAFC;
      color: #0F172A;
    }}
    .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}
    .glass-card {{
      background: rgba(30, 41, 59, 0.7);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(51, 65, 85, 0.6);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    html.light .glass-card {{
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      box-shadow: 0 4px 12px -2px rgba(0, 0, 0, 0.05);
    }}
    .glass-card:hover {{
      transform: translateY(-2px);
      border-color: rgba(226, 0, 57, 0.5);
      box-shadow: 0 12px 24px -6px rgba(226, 0, 57, 0.15);
    }}
    html.light .glass-card:hover {{
      border-color: rgba(226, 0, 57, 0.5);
      box-shadow: 0 12px 24px -6px rgba(0, 0, 0, 0.1);
    }}
    .tab-btn.active {{
      background-color: #E20039;
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(226, 0, 57, 0.4);
    }}
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0F172A;
    }}
    html.light ::-webkit-scrollbar-track {{
      background: #F1F5F9;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #334155;
      border-radius: 4px;
    }}
    html.light ::-webkit-scrollbar-thumb {{
      background: #CBD5E1;
    }}
    .sparkline-canvas {{
      width: 100% !important;
      height: 48px !important;
    }}
    .modal-backdrop {{
      background-color: rgba(11, 17, 32, 0.85);
      backdrop-filter: blur(8px);
    }}
    html.light .modal-backdrop {{
      background-color: rgba(15, 23, 42, 0.6);
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col selection:bg-brand-red selection:text-white">

  <!-- HEADER -->
  <header class="sticky top-0 z-40 bg-[#0F172A]/90 dark:bg-[#0F172A]/90 light:bg-white/90 backdrop-blur-md border-b border-[#334155]/60 light:border-slate-200 transition-colors">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      
      <!-- Brand & Title -->
      <div class="flex items-center gap-3 shrink-0">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-brand-red to-[#9B0024] flex items-center justify-center text-white shadow-lg shadow-brand-red/30">
          <i class="fas fa-chart-pie text-base"></i>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-bold uppercase tracking-wider text-brand-red">LA SEGUNDA</span>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-brand-red/10 text-brand-red font-semibold border border-brand-red/20">ECONOMÍA</span>
          </div>
          <h1 class="text-base sm:text-lg font-bold text-slate-100 light:text-slate-900 tracking-tight leading-tight">
            Tablero de Indicadores Económicos
          </h1>
        </div>
      </div>

      <!-- Quick Search Bar -->
      <div class="flex-1 max-w-md hidden md:block">
        <div class="relative">
          <i class="fas fa-search absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
          <input 
            type="text" 
            id="global-search-input"
            placeholder="Buscar indicador (ej. IPC, Reservas, Salarios, Deuda, PBI)..."
            oninput="handleSearch(this.value)"
            class="w-full bg-[#1E293B]/80 light:bg-slate-100 text-xs text-slate-200 light:text-slate-800 rounded-xl pl-9 pr-8 py-2 border border-[#334155]/60 light:border-slate-300 focus:outline-none focus:border-brand-red focus:ring-1 focus:ring-brand-red transition-all"
          >
          <button id="search-clear-btn" onclick="clearSearch()" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-200 text-xs">
            <i class="fas fa-times"></i>
          </button>
        </div>
      </div>

      <!-- Actions & Theme Toggle -->
      <div class="flex items-center gap-2">
        <button onclick="exportAllCSV()" title="Exportar indicadores a CSV" class="p-2 rounded-xl bg-[#1E293B] light:bg-slate-100 text-slate-300 light:text-slate-700 hover:text-white light:hover:text-black border border-[#334155] light:border-slate-300 text-xs font-semibold flex items-center gap-1.5 transition-colors">
          <i class="fas fa-file-csv text-brand-red"></i>
          <span class="hidden sm:inline">Exportar CSV</span>
        </button>

        <button onclick="toggleTheme()" id="theme-toggle-btn" title="Cambiar Tema" class="p-2 w-9 h-9 rounded-xl bg-[#1E293B] light:bg-slate-100 text-slate-300 light:text-slate-700 hover:text-white light:hover:text-black border border-[#334155] light:border-slate-300 flex items-center justify-center text-sm transition-colors">
          <i class="fas fa-moon dark:hidden"></i>
          <i class="fas fa-sun hidden dark:inline text-amber-400"></i>
        </button>
      </div>

    </div>
  </header>

  <!-- TOP HIGHLIGHTS / KPIS BANNER -->
  <section class="bg-[#0F172A]/50 light:bg-slate-100/70 border-b border-[#334155]/40 light:border-slate-200 py-3 transition-colors">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3" id="top-kpis-container">
        <!-- Rendered dynamically -->
      </div>
    </div>
  </section>

  <!-- CATEGORY NAVIGATION BAR -->
  <nav class="sticky top-16 z-30 bg-[#0B1120]/95 light:bg-[#F8FAFC]/95 backdrop-blur-md border-b border-[#334155]/50 light:border-slate-200 py-2.5 transition-colors">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1 text-xs font-semibold" id="category-tabs-container">
        <!-- Rendered dynamically -->
      </div>
    </div>
  </nav>

  <!-- MAIN CONTENT CONTAINER -->
  <main class="flex-grow max-w-[1700px] mx-auto px-4 sm:px-6 lg:px-8 py-6 w-full">
    
    <!-- Search Results Status Banner (When searching) -->
    <div id="search-status-banner" class="hidden mb-6 p-4 rounded-2xl bg-brand-red/10 border border-brand-red/30 flex items-center justify-between">
      <div class="flex items-center gap-2 text-sm text-slate-200 light:text-slate-800">
        <i class="fas fa-search text-brand-red"></i>
        <span>Resultados para: <strong id="search-query-text" class="text-white light:text-black"></strong></span>
        <span id="search-count-badge" class="px-2 py-0.5 rounded-full bg-brand-red text-white text-xs font-bold"></span>
      </div>
      <button onclick="clearSearch()" class="text-xs text-brand-red hover:underline font-semibold">
        Mostrar todas las categorías
      </button>
    </div>

    <!-- CATEGORIES SECTION -->
    <div id="categories-root" class="flex flex-col gap-10">
      <!-- Rendered dynamically -->
    </div>

  </main>

  <!-- FOOTER -->
  <footer class="bg-[#0F172A] light:bg-slate-100 border-t border-[#334155]/60 light:border-slate-200 py-6 mt-12 transition-colors">
    <div class="max-w-[1700px] mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-400 light:text-slate-600">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
        <span>Sistema de Monitoreo Macroeconómico • <strong>La Segunda Seguros</strong></span>
      </div>
      <div class="flex items-center gap-4">
        <span>Última Actualización: <strong id="footer-update-time" class="text-slate-200 light:text-slate-800 font-mono"></strong></span>
        <span>•</span>
        <span>Fuentes: INDEC, BCRA, Min. Economía, AFIP/ARCA, ArgentinaDatos</span>
      </div>
    </div>
  </footer>

  <!-- DETAIL & REGRESSION MODAL -->
  <div id="indicator-modal" class="fixed inset-0 z-50 modal-backdrop hidden items-center justify-center p-4 sm:p-6 opacity-0 transition-opacity duration-250 ease-out" onclick="handleModalBackdropClick(event)">
    <div class="glass-card rounded-3xl w-full max-w-5xl max-h-[92vh] flex flex-col overflow-hidden shadow-2xl border border-brand-red/30 relative animate-in fade-in zoom-in-95 duration-200" onclick="event.stopPropagation()">
      
      <!-- Modal Header -->
      <div class="p-6 pb-4 border-b border-[#334155]/60 light:border-slate-200 flex items-start justify-between gap-4">
        <div class="flex items-start gap-3">
          <div class="w-11 h-11 rounded-2xl bg-brand-red/10 border border-brand-red/30 flex items-center justify-center text-brand-red text-lg shrink-0 mt-0.5">
            <i class="fas fa-chart-line" id="modal-icon"></i>
          </div>
          <div>
            <div class="flex items-center gap-2 mb-1 flex-wrap">
              <span id="modal-category-badge" class="px-2 py-0.5 rounded-md text-[11px] font-bold uppercase tracking-wider bg-slate-800 light:bg-slate-200 text-slate-300 light:text-slate-700"></span>
              <span id="modal-freq-badge" class="px-2 py-0.5 rounded-md text-[11px] font-semibold bg-blue-500/10 text-blue-400 light:text-blue-600 border border-blue-500/20"></span>
              <span id="modal-source-badge" class="px-2 py-0.5 rounded-md text-[11px] font-semibold bg-emerald-500/10 text-emerald-400 light:text-emerald-600 border border-emerald-500/20"></span>
            </div>
            <h2 id="modal-title" class="text-lg sm:text-xl font-bold text-slate-100 light:text-slate-900 tracking-tight"></h2>
            <p id="modal-desc" class="text-xs text-slate-400 light:text-slate-600 mt-1 max-w-2xl leading-relaxed"></p>
          </div>
        </div>

        <button onclick="closeModal()" class="w-9 h-9 rounded-full bg-slate-800/80 light:bg-slate-200 text-slate-400 hover:text-white light:hover:text-black flex items-center justify-center transition-colors shrink-0">
          <i class="fas fa-times text-sm"></i>
        </button>
      </div>

      <!-- Modal Body (Stats + Chart + Controls) -->
      <div class="p-6 overflow-y-auto flex-grow flex flex-col gap-5">
        
        <!-- Summary Stat Pills -->
        <div class="grid grid-cols-2 sm:grid-cols-5 gap-3">
          <div class="p-3 rounded-2xl bg-[#0F172A]/70 light:bg-slate-100 border border-[#334155]/50 light:border-slate-200">
            <div class="text-[10px] font-semibold uppercase tracking-wider text-slate-400 light:text-slate-500">Último Dato</div>
            <div id="modal-stat-latest" class="text-base sm:text-lg font-bold font-mono text-slate-100 light:text-slate-900 mt-0.5"></div>
            <div id="modal-stat-date" class="text-[10px] text-slate-400 light:text-slate-500"></div>
          </div>

          <div class="p-3 rounded-2xl bg-[#0F172A]/70 light:bg-slate-100 border border-[#334155]/50 light:border-slate-200">
            <div class="text-[10px] font-semibold uppercase tracking-wider text-slate-400 light:text-slate-500">Var. Período</div>
            <div id="modal-stat-mom" class="text-base sm:text-lg font-bold font-mono mt-0.5"></div>
            <div class="text-[10px] text-slate-400 light:text-slate-500">Mes / Trimestre</div>
          </div>

          <div class="p-3 rounded-2xl bg-[#0F172A]/70 light:bg-slate-100 border border-[#334155]/50 light:border-slate-200">
            <div class="text-[10px] font-semibold uppercase tracking-wider text-slate-400 light:text-slate-500">Var. Interanual</div>
            <div id="modal-stat-yoy" class="text-base sm:text-lg font-bold font-mono mt-0.5"></div>
            <div class="text-[10px] text-slate-400 light:text-slate-500">Últimos 12 meses</div>
          </div>

          <div class="p-3 rounded-2xl bg-[#0F172A]/70 light:bg-slate-100 border border-[#334155]/50 light:border-slate-200">
            <div class="text-[10px] font-semibold uppercase tracking-wider text-slate-400 light:text-slate-500">Mínimo / Máximo</div>
            <div id="modal-stat-range" class="text-xs sm:text-sm font-bold font-mono text-slate-200 light:text-slate-800 mt-1"></div>
            <div id="modal-stat-avg" class="text-[10px] text-slate-400 light:text-slate-500 font-mono"></div>
          </div>

          <div class="p-3 rounded-2xl bg-[#0F172A]/70 light:bg-slate-100 border border-[#334155]/50 light:border-slate-200">
            <div class="text-[10px] font-semibold uppercase tracking-wider text-slate-400 light:text-slate-500">Tendencia</div>
            <div id="modal-stat-trend" class="text-sm font-bold font-mono mt-1"></div>
            <div id="modal-stat-slope" class="text-[10px] text-slate-400 light:text-slate-500 font-mono"></div>
          </div>
        </div>

        <!-- Chart Controls (Time Range & Regression Line Switch) -->
        <div class="flex flex-wrap items-center justify-between gap-3 bg-[#0F172A]/40 light:bg-slate-100/60 p-2.5 rounded-2xl border border-[#334155]/40 light:border-slate-200">
          
          <!-- Period Selector -->
          <div class="flex items-center gap-1 text-xs font-semibold">
            <span class="text-slate-400 mr-1 text-[11px]">Rango:</span>
            <button onclick="setModalPeriod('1A')" id="btn-period-1A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-800 light:hover:bg-slate-200">1A</button>
            <button onclick="setModalPeriod('2A')" id="btn-period-2A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-800 light:hover:bg-slate-200">2A</button>
            <button onclick="setModalPeriod('3A')" id="btn-period-3A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-800 light:hover:bg-slate-200">3A</button>
            <button onclick="setModalPeriod('5A')" id="btn-period-5A" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-800 light:hover:bg-slate-200">5A</button>
            <button onclick="setModalPeriod('ALL')" id="btn-period-ALL" class="px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-800 light:hover:bg-slate-200">Histórico</button>
          </div>

          <!-- Regression Line Toggle & Download PNG -->
          <div class="flex items-center gap-2">
            <button 
              onclick="toggleRegressionLine()" 
              id="btn-toggle-regression" 
              class="px-3 py-1 text-xs font-bold rounded-xl border transition-all flex items-center gap-1.5 bg-slate-800/80 light:bg-slate-200 border-slate-700 light:border-slate-300 text-slate-300 light:text-slate-700 hover:border-brand-red"
            >
              <i class="fas fa-chart-line text-brand-red"></i>
              <span>Recta de Regresión</span>
              <span id="regression-badge" class="w-2 h-2 rounded-full bg-slate-500"></span>
            </button>

            <button onclick="exportModalChartPNG()" title="Descargar Gráfico en PNG" class="p-1.5 px-2.5 rounded-xl bg-slate-800/80 light:bg-slate-200 text-slate-300 light:text-slate-700 hover:text-white border border-slate-700 light:border-slate-300 text-xs">
              <i class="fas fa-camera"></i>
            </button>
          </div>

        </div>

        <!-- Main Interactive Chart Canvas -->
        <div class="relative w-full h-[360px] min-h-[300px] bg-[#0F172A]/40 light:bg-white rounded-2xl p-3 border border-[#334155]/40 light:border-slate-200 flex items-center justify-center">
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
    let isDarkMode = true;
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
      renderTopKPIs();
      renderCategoryTabs();
      renderAllCategories();
      setupKeyboardShortcuts();

      if (window.DATASET && window.DATASET.metadata) {{
        const updateTimeEl = document.getElementById('footer-update-time');
        if (updateTimeEl) updateTimeEl.innerText = window.DATASET.metadata.last_updated;
      }}
    }});

    // Theme Switcher
    function initTheme() {{
      const savedTheme = localStorage.getItem('theme') || 'dark';
      if (savedTheme === 'light') {{
        document.documentElement.classList.remove('dark');
        document.documentElement.classList.add('light');
        isDarkMode = false;
      }} else {{
        document.documentElement.classList.remove('light');
        document.documentElement.classList.add('dark');
        isDarkMode = true;
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
      // Re-render charts with correct theme colors
      if (modalState.key) updateModalChart();
    }}

    // Top Highlight KPIs
    function renderTopKPIs() {{
      const container = document.getElementById('top-kpis-container');
      if (!container || !window.DATASET) return;

      const kpiKeys = [
        {{ key: 'ipc_mensual', label: 'IPC Mensual', icon: 'fa-percentage', color: 'text-amber-400' }},
        {{ key: 'ipc_interanual', label: 'IPC Interanual', icon: 'fa-chart-simple', color: 'text-rose-400' }},
        {{ key: 'riesgo_pais', label: 'Riesgo País', icon: 'fa-arrow-trend-down', color: 'text-blue-400' }},
        {{ key: 'reservas_brutas', label: 'Reservas BCRA', icon: 'fa-vault', color: 'text-emerald-400' }},
        {{ key: 'base_monetaria', label: 'Base Monetaria', icon: 'fa-money-bill-wave', color: 'text-cyan-400' }},
        {{ key: 'salario_minimo', label: 'Salario Mínimo (SMVM)', icon: 'fa-wallet', color: 'text-purple-400' }}
      ];

      let html = '';
      kpiKeys.forEach(k => {{
        let cardData = findCardByKey(k.key);
        if (!cardData && k.key === 'salario_minimo') cardData = findCardByKey('smvm_val');
        if (!cardData && k.key === 'reservas_brutas') cardData = findCardByKey('reservas_bcra');

        if (cardData) {{
          const isPos = String(cardData.display_change).includes('+');
          const isNeg = String(cardData.display_change).includes('-');
          const colorClass = isPos ? 'text-emerald-400' : (isNeg ? 'text-rose-400' : 'text-slate-300');

          html += `
            <div onclick="openModalByKey('${{cardData.key}}')" class="glass-card p-3 rounded-2xl cursor-pointer hover:border-brand-red flex flex-col justify-between">
              <div class="flex items-center justify-between text-[11px] text-slate-400 light:text-slate-500 font-semibold">
                <span>${{k.label}}</span>
                <i class="fas ${{k.icon}} ${{k.color}}"></i>
              </div>
              <div class="text-sm sm:text-base font-bold font-mono text-slate-100 light:text-slate-900 mt-1">
                ${{cardData.display_value}}
              </div>
              <div class="flex items-center justify-between text-[10px] font-mono mt-0.5">
                <span class="${{colorClass}} font-semibold">${{cardData.display_change}}</span>
                <span class="text-slate-400 light:text-slate-500">${{cardData.var_ia}}</span>
              </div>
            </div>
          `;
        }}
      }});
      container.innerHTML = html;
    }}

    // Category Tabs Navigation
    function renderCategoryTabs() {{
      const container = document.getElementById('category-tabs-container');
      if (!container || !window.DATASET) return;

      const categories = window.DATASET.categories || [];
      const totalCount = window.DATASET.metadata.total_indicators || 0;

      let html = `
        <button 
          onclick="selectCategory('all')" 
          id="tab-btn-all"
          class="tab-btn active shrink-0 px-3.5 py-1.5 rounded-xl border border-transparent transition-all flex items-center gap-2 text-slate-300 light:text-slate-700 hover:text-white"
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
            id="tab-btn-${{cat.id}}"
            class="tab-btn shrink-0 px-3.5 py-1.5 rounded-xl border border-transparent transition-all flex items-center gap-2 text-slate-400 light:text-slate-600 hover:text-white light:hover:text-black bg-slate-900/60 light:bg-slate-200/70"
          >
            <i class="fas ${{cat.icon}} text-brand-red"></i>
            <span>${{cat.name}}</span>
            <span class="text-[10px] px-1.5 py-0.2 rounded-full bg-slate-800 light:bg-slate-300 text-slate-300 light:text-slate-700 font-mono font-bold">${{count}}</span>
          </button>
        `;
      }});

      container.innerHTML = html;
    }}

    function selectCategory(catId) {{
      currentCategory = catId;
      document.querySelectorAll('.tab-btn').forEach(btn => {{
        btn.classList.remove('active');
        btn.classList.add('bg-slate-900/60', 'light:bg-slate-200/70', 'text-slate-400', 'light:text-slate-600');
      }});

      const activeBtn = document.getElementById(`tab-btn-${{catId}}`);
      if (activeBtn) {{
        activeBtn.classList.add('active');
        activeBtn.classList.remove('bg-slate-900/60', 'light:bg-slate-200/70', 'text-slate-400', 'light:text-slate-600');
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
          <section id="sec-${{cat.id}}" class="flex flex-col gap-4">
            
            <!-- Category Header -->
            <div class="flex items-center justify-between border-b border-[#334155]/60 light:border-slate-200 pb-3">
              <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-xl bg-brand-red/10 border border-brand-red/30 flex items-center justify-center text-brand-red text-sm">
                  <i class="fas ${{cat.icon}}"></i>
                </div>
                <div>
                  <h2 class="text-base sm:text-lg font-bold text-slate-100 light:text-slate-900 tracking-tight">
                    ${{cat.name}}
                  </h2>
                </div>
              </div>
              <span class="text-xs font-semibold px-2.5 py-1 rounded-lg bg-[#1E293B] light:bg-slate-200 text-slate-300 light:text-slate-700 font-mono">
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
            <i class="fas fa-search text-4xl text-slate-500 mb-3"></i>
            <h3 class="text-lg font-bold text-slate-200 light:text-slate-800">No se encontraron indicadores</h3>
            <p class="text-xs text-slate-400 light:text-slate-500 mt-1">Intenta con otros términos de búsqueda como "IPC", "Reservas", "Salarios", o "PBI".</p>
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

    // Indicator Card Template
    function renderIndicatorCardHTML(card) {{
      const isPos = String(card.display_change).includes('+');
      const isNeg = String(card.display_change).includes('-');
      const momColor = isPos ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' : (isNeg ? 'bg-rose-500/10 text-rose-400 border-rose-500/20' : 'bg-slate-800 text-slate-400 border-slate-700');
      const momIcon = isPos ? '<i class="fas fa-arrow-trend-up text-[10px] mr-1"></i>' : (isNeg ? '<i class="fas fa-arrow-trend-down text-[10px] mr-1"></i>' : '');

      return `
        <div 
          onclick="openModalByKey('${{card.key}}')"
          class="glass-card rounded-2xl p-4 flex flex-col justify-between cursor-pointer group relative overflow-hidden"
          title="Click para ver gráfico interactivo y regresión"
        >
          <!-- Top row: Name & Badges -->
          <div>
            <div class="flex items-start justify-between gap-2 mb-2">
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 light:text-slate-500 px-2 py-0.5 rounded bg-slate-800/80 light:bg-slate-200/80 border border-slate-700/60 light:border-slate-300">
                ${{card.freq}}
              </span>
              <span class="text-[10px] text-slate-400 light:text-slate-500 font-semibold" title="Fuente oficial">
                ${{card.source.split('/')[0]}}
              </span>
            </div>

            <h3 class="text-xs sm:text-sm font-bold text-slate-200 light:text-slate-800 group-hover:text-brand-red transition-colors line-clamp-2 leading-snug">
              ${{card.name}}
            </h3>
          </div>

          <!-- Mid row: Value & Variations -->
          <div class="my-3">
            <div class="text-xl sm:text-2xl font-extrabold font-mono text-slate-100 light:text-slate-950 tracking-tight">
              ${{card.display_value}}
            </div>

            <div class="flex items-center gap-2 mt-2 flex-wrap">
              <span class="px-2 py-0.5 rounded-lg border text-[11px] font-mono font-bold ${{momColor}} flex items-center" title="Variación de período">
                ${{momIcon}} ${{card.display_change}}
              </span>

              <span class="px-2 py-0.5 rounded-lg bg-slate-800/80 light:bg-slate-100 text-slate-300 light:text-slate-700 border border-slate-700/60 light:border-slate-300 text-[11px] font-mono font-semibold" title="Variación Interanual">
                ${{card.var_ia}}
              </span>
            </div>
          </div>

          <!-- Bottom: Sparkline Canvas & Action Trigger -->
          <div class="pt-2 border-t border-slate-700/40 light:border-slate-200/80 flex items-center justify-between gap-2">
            <div class="flex-1 h-10 relative">
              <canvas id="sparkline-${{card.key}}" class="sparkline-canvas"></canvas>
            </div>
            <div class="w-7 h-7 rounded-lg bg-brand-red/10 border border-brand-red/20 group-hover:bg-brand-red group-hover:text-white text-brand-red flex items-center justify-center text-xs transition-all shrink-0 shadow-sm">
              <i class="fas fa-expand-alt"></i>
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
      const strokeColor = isUp ? '#10B981' : '#E20039';
      const fillColor = isUp ? 'rgba(16, 185, 129, 0.12)' : 'rgba(226, 0, 57, 0.12)';

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
            borderWidth: 1.75,
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

      // Populate Stats
      document.getElementById('modal-stat-latest').innerText = card.display_value;
      document.getElementById('modal-stat-date').innerText = `Fecha: ${{card.latest_date}}`;

      const isPos = String(card.display_change).includes('+');
      const isNeg = String(card.display_change).includes('-');
      const momEl = document.getElementById('modal-stat-mom');
      momEl.innerText = card.display_change;
      momEl.className = `text-base sm:text-lg font-bold font-mono mt-0.5 ${{isPos ? 'text-emerald-400' : (isNeg ? 'text-rose-400' : 'text-slate-300')}}`;

      const yoyEl = document.getElementById('modal-stat-yoy');
      yoyEl.innerText = card.var_ia;
      yoyEl.className = `text-base sm:text-lg font-bold font-mono mt-0.5 ${{String(card.var_ia).includes('+') ? 'text-emerald-400' : (String(card.var_ia).includes('-') ? 'text-rose-400' : 'text-slate-300')}}`;

      const pMin = Math.min(...prices);
      const pMax = Math.max(...prices);
      const pAvg = prices.reduce((a, b) => a + b, 0) / (prices.length || 1);

      document.getElementById('modal-stat-range').innerText = `${{pMin.toLocaleString('es-AR')}} / ${{pMax.toLocaleString('es-AR')}}`;
      document.getElementById('modal-stat-avg').innerText = `Promedio: ${{pAvg.toLocaleString('es-AR', {{ maximumFractionDigits: 2 }})}}`;

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
            btn.className = "px-2.5 py-1 rounded-lg transition-colors border border-transparent hover:bg-slate-800 light:hover:bg-slate-200 text-slate-300 light:text-slate-700";
          }}
        }}
      }});

      // Update Regression Button State
      const regBtn = document.getElementById('btn-toggle-regression');
      const regBadge = document.getElementById('regression-badge');
      if (regBtn && regBadge) {{
        if (modalState.showRegression) {{
          regBtn.className = "px-3 py-1 text-xs font-bold rounded-xl border transition-all flex items-center gap-1.5 bg-brand-red/20 border-brand-red text-brand-red shadow-sm";
          regBadge.className = "w-2 h-2 rounded-full bg-brand-red animate-pulse";
        }} else {{
          regBtn.className = "px-3 py-1 text-xs font-bold rounded-xl border transition-all flex items-center gap-1.5 bg-slate-800/80 light:bg-slate-200 border-slate-700 light:border-slate-300 text-slate-300 light:text-slate-700";
          regBadge.className = "w-2 h-2 rounded-full bg-slate-500";
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
        trendEl.className = "text-sm font-bold font-mono mt-1 text-emerald-400";
      }} else if (slope < -0.001) {{
        trendEl.innerText = "Bajista \u2193";
        trendEl.className = "text-sm font-bold font-mono mt-1 text-rose-400";
      }} else {{
        trendEl.innerText = "Estable \u2192";
        trendEl.className = "text-sm font-bold font-mono mt-1 text-slate-300";
      }}
      slopeEl.innerText = `Pendiente: ${{slope.toFixed(3)}}/per`;

      // Render Chart.js
      const canvas = document.getElementById('modal-main-chart');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');

      if (modalChart) {{
        modalChart.destroy();
      }}

      const isLight = document.documentElement.classList.contains('light');
      const textColor = isLight ? '#334155' : '#94A3B8';
      const gridColor = isLight ? 'rgba(0,0,0,0.06)' : 'rgba(255,255,255,0.06)';

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
          backgroundColor: isLight ? 'rgba(226, 0, 57, 0.08)' : 'rgba(226, 0, 57, 0.15)',
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
                font: {{ family: 'Sora', size: 11, weight: '600' }}
              }}
            }},
            tooltip: {{
              backgroundColor: isLight ? '#FFFFFF' : '#0F172A',
              titleColor: isLight ? '#0F172A' : '#F1F5F9',
              bodyColor: isLight ? '#334155' : '#CBD5E1',
              borderColor: '#E20039',
              borderWidth: 1,
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
                font: {{ family: 'JetBrains Mono', size: 10 }},
                maxRotation: 45
              }}
            }},
            y: {{
              grid: {{ color: gridColor }},
              ticks: {{
                color: textColor,
                font: {{ family: 'JetBrains Mono', size: 10 }},
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

      let csv = 'Categoria,Indicador,Clave,Frecuencia,Fuente,Valor_Actual,Var_Periodo,Var_Interanual,Fecha\\n';
      window.DATASET.categories.forEach(cat => {{
        (cat.cards || []).forEach(c => {{
          const row = [
            `"${{cat.name}}"`,
            `"${{c.name}}"`,
            `"${{c.key}}"`,
            `"${{c.freq}}"`,
            `"${{c.source}}"`,
            `"${{c.display_value}}"`,
            `"${{c.display_change}}"`,
            `"${{c.var_ia}}"`,
            `"${{c.latest_date}}"`
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

    out_file = r'g:\Mi unidad\IA\Tablero-Economía\index.html'
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"[SUCCESS] Wrote index.html successfully ({len(html_content)} bytes)!")

if __name__ == "__main__":
    build_index_html()
