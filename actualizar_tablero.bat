@echo off
chcp 65001 > nul
echo =========================================================
echo    ACTUALIZANDO TABLERO DE DATOS ECONÓMICOS
echo    LA SEGUNDA SEGUROS - SISTEMA DE MONITOREO
echo =========================================================
echo.

echo [1/2] Extrayendo y actualizando series macroeconómicas...
python actualizar_datos.py
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Falló la actualización de datos.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [2/2] Ensamblando y regenerando index.html...
python build_html.py
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Falló la construcción del tablero HTML.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [3/3] Sincronizando con la nube (GitHub Pages)...
if exist "deploy_to_github.py" (
    python deploy_to_github.py
)

echo.
echo [OK] ¡Tablero de Indicadores Económicos actualizado con éxito!
echo Abriendo en el navegador...
start "" "index.html"
timeout /t 3 > nul
exit
