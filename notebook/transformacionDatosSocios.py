import pandas as pd

def transformar_datos_socios(data_frame_limpio_socios):

    # filtro 1
    filtro1 = data_frame_limpio_socios.query(
        "estado=='usuario activo'"
    )

    agrupacion1 = (
        filtro1.groupby("Nombre_usuario")["id_socio"]
        .count()
        .reset_index(name="cuenta")
    )


    # filtro 2
    filtro2 = data_frame_limpio_socios.query(
        "id_membresia>=300"
    )

    agrupacion2 = (
        filtro2.groupby("estado")["id_socio"]
        .count()
        .reset_index(name="cuenta")
    )


    # filtro 3
    filtro3 = data_frame_limpio_socios.query(
        "Nombre_usuario=='thomas'"
    )

    agrupacion3 = (
        filtro3.groupby("estado")["id_socio"]
        .count()
        .reset_index(name="cantidad")
    )


    # filtro 4
    filtro4 = data_frame_limpio_socios.query(
        "fecha_inscripcion.notnull()",
        engine="python"
    )

    agrupacion4 = (
        filtro4.groupby(
            filtro4["fecha_inscripcion"].dt.date
        )["id_socio"]
        .count()
        .reset_index(name="cuenta")
    )


    # filtro 5
    filtro5 = data_frame_limpio_socios.query(
        "estado=='usuario bloqueado'"
    )

    agrupacion5 = (
        filtro5.groupby("Nombre_usuario")["id_socio"]
        .count()
        .reset_index(name="cuenta")
    )


    resultado = {

        "usuariosActivos": agrupacion1,

        "membresiasAltas": agrupacion2,

        "sociosThomas": agrupacion3,

        "inscripcionesPorFecha": agrupacion4,

        "usuariosBloqueados": agrupacion5
    }

    return resultado