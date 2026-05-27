import pandas as pd

def describir_datos(data_frame_limpio_socios):

    print("*** DESCRIPCION DEL DATASET ***")

    # 1. Número de filas
    print(f"Numero de filas del dataset: {data_frame_limpio_socios.shape[0]}")

    # 2. Número de columnas
    print(f"Numero de columnas del dataset: {data_frame_limpio_socios.shape[1]}")

    # 3. Lista de columnas
    print(f"Lista de columnas disponibles: {list(data_frame_limpio_socios.columns)}")

    # 4. Tipos de datos
    print(f"Tipos de dato de cada atributo:\n{data_frame_limpio_socios.dtypes}")


    # =========================
    # ESTADÍSTICAS NUMÉRICAS
    # =========================
    print("\n*** ESTADISTICAS ***")

    columnas_numericas = data_frame_limpio_socios.select_dtypes(include=["number"]).columns

    if len(columnas_numericas) > 0:
        print(data_frame_limpio_socios[columnas_numericas].describe())
    else:
        print("No hay columnas numéricas para describir")


    # =========================
    # CONTEOS
    # =========================
    print("\n*** CONTEOS ***")

    if "estado" in data_frame_limpio_socios.columns:
        print("\nEstado:")
        print(data_frame_limpio_socios["estado"].value_counts())

    if "nombre" in data_frame_limpio_socios.columns:
        print("\nNombre:")
        print(data_frame_limpio_socios["nombre"].value_counts())


    # =========================
    # FECHAS
    # =========================
    print("\n*** DESCRIPCION DE FECHAS ***")

    if "fecha_inscripcion" in data_frame_limpio_socios.columns:

        print(f"Fecha mas antigua: {data_frame_limpio_socios['fecha_inscripcion'].min()}")
        print(f"Fecha mas reciente: {data_frame_limpio_socios['fecha_inscripcion'].max()}")

    else:
        print("No hay columna de fechas para analizar")