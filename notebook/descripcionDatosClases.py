import pandas as pd

def describir_datos(data_frame_limpio_clases):

    print("\n*** DESCRIPCION DEL DATASET ***")

    # 1. Filas y columnas
    print(f"Numero de filas del dataset: {data_frame_limpio_clases.shape[0]}")
    print(f"Numero de columnas del dataset: {data_frame_limpio_clases.shape[1]}")

    # 2. Columnas disponibles
    print(f"Lista de columnas disponibles: {list(data_frame_limpio_clases.columns)}")

    # 3. Tipos de datos
    print(f"Tipos de dato de cada atributo:\n{data_frame_limpio_clases.dtypes}")

    # =========================
    # ESTADISTICAS NUMERICAS
    # =========================
    print("\n*** ESTADISTICAS ***")

    columnas_numericas = data_frame_limpio_clases.select_dtypes(include=["number"]).columns

    if len(columnas_numericas) > 0:
        print(data_frame_limpio_clases[columnas_numericas].describe())
    else:
        print("No hay columnas numericas para describir")

    # =========================
    # CONTEOS
    # =========================
    print("\n*** CONTEOS ***")

    if "estado" in data_frame_limpio_clases.columns:
        print("\nEstado:")
        print(data_frame_limpio_clases["estado"].value_counts())

    if "nivel" in data_frame_limpio_clases.columns:
        print("\nNivel:")
        print(data_frame_limpio_clases["nivel"].value_counts())

    # =========================
    # FECHAS
    # =========================
    print("\n*** DESCRIPCION DE FECHAS ***")

    if "horario" in data_frame_limpio_clases.columns:
        print(f"Fecha mas antigua: {data_frame_limpio_clases['horario'].min()}")
        print(f"Fecha mas reciente: {data_frame_limpio_clases['horario'].max()}")
    else:
        print("No hay columna de fechas para analizar")