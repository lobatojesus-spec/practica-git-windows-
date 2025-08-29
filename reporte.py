cat > reporte.py << 'EOF'
# coding: utf-8
def generar_reporte(datos):
    """
    Genera un reporte simple con el número de registros y columnas.
    """
    n = len(datos) if hasattr(datos, "__len__") else 0
    cols = list(datos[0].keys()) if n and isinstance(datos[0], dict) else []
    return {"registros": n, "columnas": cols}

if __name__ == "__main__":
    muestra = [{"id": 1, "valor": 10}, {"id": 2, "valor": 15}]
    print(generar_reporte(muestra))
EOF

