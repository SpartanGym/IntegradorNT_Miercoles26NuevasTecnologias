import matplotlib.pyplot as plt
import os

RUTA_ASSETS = os.path.join(
    os.path.dirname(__file__), "..", "spartan-elite", "src", "assets", "graficos"
)

def crear_ruta_si_no_existe(ruta):
    os.makedirs(ruta, exist_ok=True)


# =========================
# CLASES POR NIVEL
# =========================
def graficar_clases_por_nivel(datos, nombre_archivo="clases_por_nivel.png", ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    if "nivel" not in datos.columns or "cuenta" not in datos.columns:
        print("No hay datos para graficar niveles")
        return

    figura, area = plt.subplots(figsize=(10, 5))

    area.bar(
        datos["nivel"],
        datos["cuenta"],
        color="#c0392b",
        edgecolor="black"
    )

    area.set_title("Clases por nivel")
    area.set_xlabel("Nivel")
    area.set_ylabel("Cantidad")

    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico guardado en: {ruta_completa}")


# =========================
# VIRTUAL VS FÍSICO
# =========================
def graficar_clases_virtual_vs_fisico(datos, nombre_archivo="clases_virtual_fisico.png", ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    if "estado" not in datos.columns or "cuenta" not in datos.columns:
        print("No hay datos para graficar virtual vs físico")
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

    area.set_title("Clases virtuales vs físicas")

    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico guardado en: {ruta_completa}")


# =========================
# CUPOS
# =========================
def graficar_clases_con_muchos_cupos(datos, nombre_archivo="clases_cupos.png", ruta_destino=RUTA_ASSETS):

    crear_ruta_si_no_existe(ruta_destino)

    if "estado" not in datos.columns or "cuenta" not in datos.columns:
        print("No hay datos para graficar cupos")
        return

    figura, area = plt.subplots(figsize=(10, 5))

    area.bar(
        datos["estado"],
        datos["cuenta"],
        color="#c0392b",
        edgecolor="black"
    )

    area.set_title("Clases con muchos cupos por estado")
    area.set_xlabel("Estado")
    area.set_ylabel("Cantidad")

    plt.tight_layout()

    ruta_completa = os.path.join(ruta_destino, nombre_archivo)
    figura.savefig(ruta_completa)
    plt.close(figura)

    print(f"Gráfico guardado en: {ruta_completa}")