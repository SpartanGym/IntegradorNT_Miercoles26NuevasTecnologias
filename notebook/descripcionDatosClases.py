import pandas as pd

def describir_datos(data_frame_limpio_clases):

    print("*** DESCRIPCION DEL DATASET ***")

    print(f"Numero de filas del dataset: {data_frame_limpio_clases.shape[0]}")

    print(f"Numero de columnas del dataset: {data_frame_limpio_clases.shape[1]}")

    print(f"Lista de columnas disponibles: {list(data_frame_limpio_clases.columns)}")

    print(f"Tipos de dato de cada atributo: {data_frame_limpio_clases.dtypes}")


    #Estadisticas (SOLO APLICA PARA DATOS NUMERICOS)
    print("*** ESTADISTICAS ***")

    print(
        f"{data_frame_limpio_clases[['id_clase','cupos','id_entrenadores']].describe()}"
    )


    #Informacion de conteos valiosos
    print("*** CONTEOS ***")

    print(
        f"{data_frame_limpio_clases['estado'].value_counts()}"
    )

    print(
        f"{data_frame_limpio_clases['niveles'].value_counts()}"
    )


    #Describiendo las fechas
    print("*** DESCRIPCION DE FECHAS ***")

    print(
        f"{data_frame_limpio_clases['horario'].min()}"
    )

    print(
        f"{data_frame_limpio_clases['horario'].max()}"
    )