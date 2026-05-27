import pandas as pd

def transformar_datos(data_frame_limpio_clases):

    df = data_frame_limpio_clases.copy()

    # =========================
    # FILTRO 1: CLASES VIRTUALES
    # =========================
    filtro1 = df.query("estado == 'virtual'")

    agrupacion1 = (
        filtro1.groupby("nivel")["id_clase"]
        .count()
        .reset_index(name="cuenta")
    )

    # =========================
    # FILTRO 2: CUPOS ALTOS
    # =========================
    filtro2 = df.query("cupos_maximos >= 25")

    agrupacion2 = (
        filtro2.groupby("estado")["id_clase"]
        .count()
        .reset_index(name="cuenta")
    )

    # =========================
    # FILTRO 3: NIVEL 1
    # =========================
    filtro3 = df.query("nivel == 'nivel 1'")

    agrupacion3 = (
        filtro3.groupby("estado")["id_clase"]
        .count()
        .reset_index(name="cantidad")
    )

    # =========================
    # FILTRO 4: ENTRENADORES
    # =========================
    filtro4 = df.query("mentrenador >= 300")

    agrupacion4 = (
        filtro4.groupby("mentrenador")["id_clase"]
        .count()
        .reset_index(name="cuenta")
    )

    # =========================
    # FILTRO 5: FECHAS
    # =========================
    filtro5 = df[df["horario"].notnull()]

    agrupacion5 = (
        filtro5.groupby(filtro5["horario"].dt.date)["id_clase"]
        .count()
        .reset_index(name="cuenta")
    )

    # =========================
    # RESULTADO FINAL
    # =========================
    resultado = {
        "clasesVirtuales": agrupacion1,
        "clasesConMuchosCupos": agrupacion2,
        "clasesNivel1": agrupacion3,
        "clasesPorEntrenador": agrupacion4,
        "clasesPorFecha": agrupacion5
    }

    return resultado