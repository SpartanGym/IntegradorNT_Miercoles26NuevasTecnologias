import pandas as pd

def transformar_datos(data_frame_limpio_clases):

    #filtro 1
    filtro1 = data_frame_limpio_clases.query(
        "estado=='virtual'"
    )

    agrupacion1 = (
        filtro1.groupby("niveles")["id_clase"]
        .count()
        .reset_index(name="cuenta")
    )


    #filtro 2
    filtro2 = data_frame_limpio_clases.query(
        "cupos>=25"
    )

    agrupacion2 = (
        filtro2.groupby("estado")["id_clase"]
        .count()
        .reset_index(name="cuenta")
    )


    #filtro 3
    filtro3 = data_frame_limpio_clases.query(
        "niveles=='nivel 1'"
    )

    agrupacion3 = (
        filtro3.groupby("estado")["id_clase"]
        .count()
        .reset_index(name="cantidad")
    )


    #filtro 4
    filtro4 = data_frame_limpio_clases.query(
        "id_entrenadores>=300"
    )

    agrupacion4 = (
        filtro4.groupby("id_entrenadores")["id_clase"]
        .count()
        .reset_index(name="cuenta")
    )


    #filtro 5
    filtro5 = data_frame_limpio_clases.query(
        "horario.notnull()",
        engine="python"
    )

    agrupacion5 = (
        filtro5.groupby(
            filtro5["horario"].dt.date
        )["id_clase"]
        .count()
        .reset_index(name="cuenta")
    )


    resultado = {

        "clasesVirtuales": agrupacion1,

        "clasesConMuchosCupos": agrupacion2,

        "clasesNivel1": agrupacion3,

        "clasesPorEntrenador": agrupacion4,

        "clasesPorFecha": agrupacion5
    }

    return resultado