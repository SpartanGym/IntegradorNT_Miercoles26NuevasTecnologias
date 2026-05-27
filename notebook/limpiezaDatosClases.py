import pandas as pd

def limpiar_clases(data_frame_sucio_clases):

    data_frame_limpio_clases = data_frame_sucio_clases.copy()

    # MOSTRAR COLUMNAS (DEBUG)
    print("COLUMNAS DEL DATAFRAME:")
    print(data_frame_limpio_clases.columns)

    # =========================
    # LIMPIEZA DE TEXTOS
    # =========================

    if "nombre" in data_frame_limpio_clases.columns:
        data_frame_limpio_clases["nombre"] = (
            data_frame_limpio_clases["nombre"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    if "descripcion" in data_frame_limpio_clases.columns:
        data_frame_limpio_clases["descripcion"] = (
            data_frame_limpio_clases["descripcion"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    if "nivel" in data_frame_limpio_clases.columns:
        data_frame_limpio_clases["nivel"] = (
            data_frame_limpio_clases["nivel"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    if "estado" in data_frame_limpio_clases.columns:
        data_frame_limpio_clases["estado"] = (
            data_frame_limpio_clases["estado"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    # =========================
    # LIMPIEZA NUMÉRICA
    # =========================

    if "id_clase" in data_frame_limpio_clases.columns:
        data_frame_limpio_clases["id_clase"] = pd.to_numeric(
            data_frame_limpio_clases["id_clase"], errors="coerce"
        )

        data_frame_limpio_clases = data_frame_limpio_clases[
            data_frame_limpio_clases["id_clase"] > 0
        ]

    if "mentrenador" in data_frame_limpio_clases.columns:
        data_frame_limpio_clases["mentrenador"] = pd.to_numeric(
            data_frame_limpio_clases["mentrenador"], errors="coerce"
        )

        data_frame_limpio_clases = data_frame_limpio_clases[
            data_frame_limpio_clases["mentrenador"] >= 200
        ]

    if "cupos_maximos" in data_frame_limpio_clases.columns:
        data_frame_limpio_clases["cupos_maximos"] = pd.to_numeric(
            data_frame_limpio_clases["cupos_maximos"], errors="coerce"
        )

        data_frame_limpio_clases = data_frame_limpio_clases[
            data_frame_limpio_clases["cupos_maximos"] > 0
        ]

    # =========================
    # FECHAS
    # =========================

    if "horario" in data_frame_limpio_clases.columns:
        data_frame_limpio_clases["horario"] = pd.to_datetime(
            data_frame_limpio_clases["horario"], errors="coerce"
        )

        data_frame_limpio_clases["horario"] = data_frame_limpio_clases[
            "horario"
        ].fillna(pd.to_datetime("2026-01-01"))

    # =========================
    # NULOS IMPORTANTES
    # =========================

    columnas_obligatorias = ["id_clase", "nombre", "nivel", "estado", "mentrenador"]

    columnas_existentes = [
        col for col in columnas_obligatorias
        if col in data_frame_limpio_clases.columns
    ]

    data_frame_limpio_clases = data_frame_limpio_clases.dropna(
        subset=columnas_existentes
    )

    return data_frame_limpio_clases