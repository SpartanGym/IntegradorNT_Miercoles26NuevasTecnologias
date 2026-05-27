import pandas as pd

def limpiar_socios(data_frame_sucio_socios):

    data_frame_limpio_socios = data_frame_sucio_socios.copy()

    # LIMPIEZA DE TEXTOS
    data_frame_limpio_socios["nombre"] = (
        data_frame_limpio_socios["nombre"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    data_frame_limpio_socios["estado"] = (
        data_frame_limpio_socios["estado"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    # Valores esperados
    valores_esperados_estado = ["activo", "bloqueado"]

    data_frame_limpio_socios["estado"] = data_frame_limpio_socios["estado"].where(
        data_frame_limpio_socios["estado"].isin(valores_esperados_estado),
        pd.NA
    )

    # LIMPIEZA NUMÉRICA
    data_frame_limpio_socios["id_socio"] = pd.to_numeric(
        data_frame_limpio_socios["id_socio"], errors="coerce"
    )

    data_frame_limpio_socios = data_frame_limpio_socios[
        data_frame_limpio_socios["id_socio"] > 0
    ]

    # LIMPIEZA FECHAS
    data_frame_limpio_socios["fecha_inscripcion"] = pd.to_datetime(
        data_frame_limpio_socios["fecha_inscripcion"], errors="coerce"
    )

    data_frame_limpio_socios["fecha_inscripcion"] = data_frame_limpio_socios[
        "fecha_inscripcion"
    ].fillna(pd.to_datetime("2026-01-01"))

    # ELIMINAR NULOS IMPORTANTES
    columnas_obligatorias = ["id_socio", "nombre", "estado"]

    data_frame_limpio_socios = data_frame_limpio_socios.dropna(
        subset=columnas_obligatorias
    )

    return data_frame_limpio_socios