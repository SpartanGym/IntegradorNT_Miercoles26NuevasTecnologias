import pandas as pd

def transformar_datos(data_frame_limpio_clases):

    df = data_frame_limpio_clases.copy()

    # =========================
    # NORMALIZAR COLUMNAS
    # =========================
    if "niveles" in df.columns:
        df["nivel"] = df["niveles"].astype(str).str.lower().str.strip()
    elif "nivel" in df.columns:
        df["nivel"] = df["nivel"].astype(str).str.lower().str.strip()

    if "cupos" in df.columns:
        df["cupos_maximos"] = pd.to_numeric(df["cupos"], errors="coerce")
    elif "cupos_maximos" in df.columns:
        df["cupos_maximos"] = pd.to_numeric(df["cupos_maximos"], errors="coerce")

    if "id_entrenadores" in df.columns:
        df["mentrenador"] = pd.to_numeric(df["id_entrenadores"], errors="coerce")
    elif "mentrenador" in df.columns:
        df["mentrenador"] = pd.to_numeric(df["mentrenador"], errors="coerce")

    df["estado"] = df["estado"].astype(str).str.lower().str.strip()

    # =========================
    # FILTRO 1: CLASES VIRTUALES
    # =========================
    filtro1 = df[df["estado"] == "virtual"]
    agrupacion1 = (
        filtro1.groupby("nivel")["id_clase"]
        .count()
        .reset_index(name="cuenta")
    )

    # =========================
    # FILTRO 2: CUPOS ALTOS
    # =========================
    filtro2 = df[df["cupos_maximos"] >= 25]
    agrupacion2 = (
        filtro2.groupby("estado")["id_clase"]
        .count()
        .reset_index(name="cuenta")
    )

    # =========================
    # FILTRO 3: NIVEL 1
    # =========================
    filtro3 = df[df["nivel"] == "nivel 1"]
    agrupacion3 = (
        filtro3.groupby("estado")["id_clase"]
        .count()
        .reset_index(name="cantidad")
    )

    # =========================
    # FILTRO 4: ENTRENADORES
    # =========================
    filtro4 = df[df["mentrenador"] >= 300]
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

    return {
        "clasesVirtuales": agrupacion1,
        "clasesConMuchosCupos": agrupacion2,
        "clasesNivel1": agrupacion3,
        "clasesPorEntrenador": agrupacion4,
        "clasesPorFecha": agrupacion5
    }