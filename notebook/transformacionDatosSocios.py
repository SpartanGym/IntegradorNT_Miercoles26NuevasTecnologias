import pandas as pd

def transformar_datos_socios(data_frame_limpio_socios):

    df = data_frame_limpio_socios.copy()

    # =========================
    # NORMALIZAR COLUMNA NOMBRE
    # =========================
    if "Nombre_usuario" in df.columns:
        df["nombre"] = df["Nombre_usuario"].astype(str).str.lower().str.strip()
    elif "nombre" in df.columns:
        df["nombre"] = df["nombre"].astype(str).str.lower().str.strip()

    # =========================
    # NORMALIZAR ESTADO
    # =========================
    if "estado" in df.columns:
        df["estado"] = df["estado"].astype(str).str.lower().str.strip()

    # =========================
    # FILTRO 1: ACTIVOS POR NOMBRE
    # =========================
    filtro1 = df[df["estado"] == "usuario activo"]
    if filtro1.empty:
        filtro1 = df[df["estado"] == "activo"]

    agrupacion1 = (
        filtro1.groupby("nombre")["id_socio"]
        .count()
        .reset_index(name="cuenta")
    )
    agrupacion1.rename(columns={"nombre": "Nombre_usuario"}, inplace=True)

    # =========================
    # FILTRO 2: MEMBRESIAS ALTAS
    # =========================
    if "id_membresia" in df.columns:
        filtro2 = df[pd.to_numeric(df["id_membresia"], errors="coerce") >= 300]
        agrupacion2 = (
            filtro2.groupby("estado")["id_socio"]
            .count()
            .reset_index(name="cuenta")
        )
    else:
        agrupacion2 = df.groupby("estado")["id_socio"].count().reset_index(name="cuenta")

    # =========================
    # FILTRO 3: THOMAS
    # =========================
    filtro3 = df[df["nombre"].str.contains("thomas", na=False)]
    agrupacion3 = (
        filtro3.groupby("estado")["id_socio"]
        .count()
        .reset_index(name="cantidad")
    )

    # =========================
    # FILTRO 4: FECHAS
    # =========================
    if "fecha_inscripcion" in df.columns:
        filtro4 = df[df["fecha_inscripcion"].notnull()]
        agrupacion4 = (
            filtro4.groupby(filtro4["fecha_inscripcion"].dt.date)["id_socio"]
            .count()
            .reset_index(name="cuenta")
        )
    else:
        agrupacion4 = pd.DataFrame()

    # =========================
    # FILTRO 5: BLOQUEADOS
    # =========================
    filtro5 = df[df["estado"] == "usuario bloqueado"]
    if filtro5.empty:
        filtro5 = df[df["estado"] == "bloqueado"]

    agrupacion5 = (
        filtro5.groupby("nombre")["id_socio"]
        .count()
        .reset_index(name="cuenta")
    )

    return {
        "usuariosActivos": agrupacion1,
        "membresiasAltas": agrupacion2,
        "sociosThomas": agrupacion3,
        "inscripcionesPorFecha": agrupacion4,
        "usuariosBloqueados": agrupacion5
    }