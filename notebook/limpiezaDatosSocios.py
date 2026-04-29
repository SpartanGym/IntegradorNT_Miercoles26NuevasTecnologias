import pandas as pd 

def limpiar_socios(data_frame_sucio_socios):
    
    data_frame_limpio_socios = data_frame_sucio_socios.copy()
    # LIMPIEZA DE TEXTOS

    data_frame_limpio_socios["Nombre_usuario"] = data_frame_limpio_socios["Nombre_usuario"].astype("string").str.strip().str.lower()
    data_frame_limpio_socios["estado"] = data_frame_limpio_socios["estado"].astype("string").str.strip().str.lower()

    # Valores esperados
    valores_esperados_nombres = ["thomas","jose","alberto","santiago","camilo"]
    data_frame_limpio_socios["Nombre_usuario"] = data_frame_limpio_socios["Nombre_usuario"].where(
        data_frame_limpio_socios["Nombre_usuario"].isin(valores_esperados_nombres),
        pd.NA
    )

    valores_esperados_estado = ["usuario activo","usuario bloqueado"]
    data_frame_limpio_socios["estado"] = data_frame_limpio_socios["estado"].where(
        data_frame_limpio_socios["estado"].isin(valores_esperados_estado),
        pd.NA
    )

    # LIMPIEZA NUMÉRICA

    data_frame_limpio_socios["id_socio"] = pd.to_numeric(data_frame_limpio_socios["id_socio"], errors="coerce")
    data_frame_limpio_socios["id_membresia"] = pd.to_numeric(data_frame_limpio_socios["id_membresia"], errors="coerce")

    data_frame_limpio_socios = data_frame_limpio_socios[data_frame_limpio_socios["id_socio"] > 0]
    data_frame_limpio_socios = data_frame_limpio_socios[data_frame_limpio_socios["id_membresia"] >= 200]

    # LIMPIEZA DE FECHAS

    data_frame_limpio_socios["fecha_inscripcion"] = pd.to_datetime(data_frame_limpio_socios["fecha_inscripcion"], errors="coerce")

    fecha_default = pd.to_datetime("2026-01-01")
    data_frame_limpio_socios["fecha_inscripcion"] = data_frame_limpio_socios["fecha_inscripcion"].fillna(fecha_default)

    # ELIMINAR NULOS IMPORTANTES

    columnas_obligatorias = ["id_socio","Nombre_usuario","estado","id_membresia"]
    data_frame_limpio_socios = data_frame_limpio_socios.dropna(subset=columnas_obligatorias)

    return data_frame_limpio_socios