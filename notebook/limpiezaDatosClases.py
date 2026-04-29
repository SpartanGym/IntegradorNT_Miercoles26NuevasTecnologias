import pandas as pd 

def limpiar_clases(data_frame_sucio_clases):
    
    data_frame_limpio_clases = data_frame_sucio_clases.copy()

    # LIMPIEZA DE TEXTOS

    data_frame_limpio_clases["nombre_usuario"] = data_frame_limpio_clases["nombre_usuario"].astype("string").str.strip().str.lower()
    data_frame_limpio_clases["descripcion"] = data_frame_limpio_clases["descripcion"].astype("string").str.strip().str.lower()
    data_frame_limpio_clases["niveles"] = data_frame_limpio_clases["niveles"].astype("string").str.strip().str.lower()
    data_frame_limpio_clases["estado"] = data_frame_limpio_clases["estado"].astype("string").str.strip().str.lower()

    # Valores esperados
    valores_esperados_nombres = ["andrea","camilo","sebastian","catalina","laura"]
    data_frame_limpio_clases["nombre_usuario"] = data_frame_limpio_clases["nombre_usuario"].where(
        data_frame_limpio_clases["nombre_usuario"].isin(valores_esperados_nombres),
        pd.NA
    )

    valores_esperados_niveles = ["nivel 1","nivel 2","nivel 3"]
    data_frame_limpio_clases["niveles"] = data_frame_limpio_clases["niveles"].where(
        data_frame_limpio_clases["niveles"].isin(valores_esperados_niveles),
        pd.NA
    )

    valores_esperados_estado = ["fisico","virtual"]
    data_frame_limpio_clases["estado"] = data_frame_limpio_clases["estado"].where(
        data_frame_limpio_clases["estado"].isin(valores_esperados_estado),
        pd.NA
    )

    # LIMPIEZA NUMÉRICA

    data_frame_limpio_clases["id_clase"] = pd.to_numeric(data_frame_limpio_clases["id_clase"], errors="coerce")
    data_frame_limpio_clases["id_entrenadores"] = pd.to_numeric(data_frame_limpio_clases["id_entrenadores"], errors="coerce")
    data_frame_limpio_clases["cupos"] = pd.to_numeric(data_frame_limpio_clases["cupos"], errors="coerce")

    data_frame_limpio_clases = data_frame_limpio_clases[data_frame_limpio_clases["id_clase"] > 0]
    data_frame_limpio_clases = data_frame_limpio_clases[data_frame_limpio_clases["id_entrenadores"] >= 200]
    data_frame_limpio_clases = data_frame_limpio_clases[data_frame_limpio_clases["cupos"] > 0]

    # LIMPIEZA DE FECHAS

    data_frame_limpio_clases["horario"] = pd.to_datetime(data_frame_limpio_clases["horario"], errors="coerce")

    fecha_default = pd.to_datetime("2026-01-01")
    data_frame_limpio_clases["horario"] = data_frame_limpio_clases["horario"].fillna(fecha_default)

    # ELIMINAR NULOS IMPORTANTES

    columnas_obligatorias = ["id_clase","nombre_usuario","niveles","estado","id_entrenadores"]
    data_frame_limpio_clases = data_frame_limpio_clases.dropna(subset=columnas_obligatorias)

    return data_frame_limpio_clases