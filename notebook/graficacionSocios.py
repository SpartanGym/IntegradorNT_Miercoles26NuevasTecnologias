import matplotlib.pyplot as plt
import os

RUTA_ASSETS = os.path.join(
    os.path.dirname(__file__), "..", "spartan-elite", "src", "assets", "graficos"
)

def crear_ruta_si_no_existe(ruta):
    os.makedirs(ruta, exist_ok=True)


# =========================
# GRAFICO 1: SOCIOS POR NOMBRE
# =========================
def graficar_socios_por_nombre(datos, nombre_archivo="socios_por_nombre.png", ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    if "nombre" not in datos.columns or "cuenta" not in datos.columns:
        print("No hay datos para graficar socios por nombre")
        return

    figura, area = plt.subplots(figsize=(10, 5))

    area.bar(
        datos["nombre"],
        datos["cuenta"],
        color="#c0392b",
        edgecolor="black"
    )

    area.set_title("Socios por nombre")
    area.set_xlabel("Nombre")
    area.set_ylabel("Cantidad")

    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico guardado en: {ruta_completa}")


# =========================
# GRAFICO 2: SOCIOS POR ESTADO
# =========================
def graficar_socios_por_estado(datos, nombre_archivo="socios_por_estado.png", ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    if "estado" not in datos.columns or "cuenta" not in datos.columns:
        print("No hay datos para graficar socios por estado")
        return

    figura, area = plt.subplots(figsize=(8, 8))

    area.pie(
        datos["cuenta"],
        labels=datos["estado"],
        autopct="%1.1f%%",
        colors=["#c0392b", "#1a1a1a"],
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5}
    )

    area.set_title("Socios activos vs bloqueados")

    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico guardado en: {ruta_completa}")


# =========================
# GRAFICO 3: THOMAS
# =========================
def graficar_socios_thomas(datos, nombre_archivo="socios_thomas.png", ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    if "estado" not in datos.columns or "cantidad" not in datos.columns:
        print("No hay datos para graficar Thomas")
        return

    figura, area = plt.subplots(figsize=(8, 5))

    colores = [
        "#c0392b" if e == "activo" else "#1a1a1a"
        for e in datos["estado"]
    ]

    area.bar(
        datos["estado"],
        datos["cantidad"],
        color=colores,
        edgecolor="black"
    )

    area.set_title("Socios Thomas: activos vs bloqueados")
    area.set_xlabel("Estado")
    area.set_ylabel("Cantidad")

    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico guardado en: {ruta_completa}")


# =========================
# GRAFICO 4: MEMBRESIAS ALTAS
# =========================
def graficar_membresias_altas(datos, nombre_archivo="membresias_altas.png", ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    if "estado" not in datos.columns or "cuenta" not in datos.columns:
        print("No hay datos para graficar membresias")
        return

    figura, area = plt.subplots(figsize=(8, 8))

    area.pie(
        datos["cuenta"],
        labels=datos["estado"],
        autopct="%1.1f%%",
        colors=["#c0392b", "#666666"],
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5}
    )

    area.set_title("Socios con membresías altas por estado")

    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico guardado en: {ruta_completa}")