import pandas as pd

def transformar_datos_socios(data_frame_limpio_socios):

    df = data_frame_limpio_socios.copy()

    # =========================
    # LIMPIEZA CRÍTICA
    # =========================

    # Convertir estado a string seguro
    if "estado" in df.columns:
        df["estado"] = df["estado"].astype(str).str.lower().str.strip()

    # Convertir mmembresia a número (EXTRAE valor si es dict)
    if "mmembresia" in df.columns:

        def extraer_valor(x):
            if isinstance(x, dict):
                return x.get("valor", 0)
            return x

        df["mmembresia"] = df["mmembresia"].apply(extraer_valor)
        df["mmembresia"] = pd.to_numeric(df["mmembresia"], errors="coerce")

    # =========================
    # FILTRO 1: ACTIVOS
    # =========================
    filtro1 = df[df["estado"] == "activo"]

    agrupacion1 = (
        filtro1.groupby("nombre")["id_socio"]
        .count()
        .reset_index(name="cuenta")
    )

    # =========================
    # FILTRO 2: MEMBRESIAS ALTAS
    # =========================
    if "mmembresia" in df.columns:

        filtro2 = df[df["mmembresia"] >= 300]

        agrupacion2 = (
            filtro2.groupby("estado")["id_socio"]
            .count()
            .reset_index(name="cuenta")
        )
    else:
        agrupacion2 = pd.DataFrame(columns=["estado", "cuenta"])

    # =========================
    # FILTRO 3: THOMAS
    # =========================
    filtro3 = df[df["nombre"] == "thomas rodriguez"]

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