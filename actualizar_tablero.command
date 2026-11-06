#!/bin/zsh
cd "$(dirname "$0")"

echo "========================================================="
echo "   ACTUALIZANDO TABLERO DE DATOS ECONÓMICOS"
echo "   LA SEGUNDA SEGUROS - SISTEMA DE MONITOREO (macOS)"
echo "========================================================="
echo ""

echo "[1/3] Extrayendo y actualizando series macroeconómicas..."
python3 actualizar_datos.py
if [ $? -ne 0 ]; then
    echo "[ERROR] Falló la actualización de datos."
    read -k 1 "?Presiona cualquier tecla para salir..."
    exit 1
fi

echo ""
echo "[2/3] Ensamblando y regenerando index.html..."
python3 build_html.py
if [ $? -ne 0 ]; then
    echo "[ERROR] Falló la construcción del tablero HTML."
    read -k 1 "?Presiona cualquier tecla para salir..."
    exit 1
fi

echo ""
echo "[3/3] Sincronizando con la nube (GitHub Pages)..."
if [ -f "deploy_to_github.py" ]; then
    python3 deploy_to_github.py
fi

echo ""
echo "[OK] ¡Tablero de Indicadores Económicos actualizado con éxito!"
echo "Abriendo en el navegador..."
open "index.html"
sleep 2
exit 0
