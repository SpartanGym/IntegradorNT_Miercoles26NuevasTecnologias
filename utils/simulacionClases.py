import random
from datetime import datetime,timedelta

def generar_clases(numero_clases):
    nombres=["andrea","camilo","sebastian","catalina","laura"]
    descripcion=["En esta clase se ve musica de salsa","en esta clase se ve musica de bachata","en esat clase se ve musica mixta"]
    horario=datetime(2026,4,15)
    cupos_maximos=["cupos maximos para esta clase 20"]
    niveles=["nivel 1","nivel 2","nivel 3"]
    estado=["fisico","virtual"]

    simulaciones=[]
    for _ in range(numero_clases):

        clases={
            "id_clase":random.randint(0,200),
            "nombre ususario":random.choice(nombres),
            "descripcion":random.choice(descripcion),
            "horario":horario+timedelta(days=random.randint(0,60)),
            "cupos":random.choice(cupos_maximos),
            "niveles":random.choice(niveles),
            "id_entrenadores":random.randint(200,400),
            "estado":random.choice(estado)
        }

        probabilidadError=random.random()
        if(probabilidadError<0.2):
            clases["id_clase"]=None
        elif(probabilidadError<0.3):
            clases["nombre ususario"]=random.choice(["carla","estefania","carlos","sandra","juan"])
        elif(probabilidadError<0.4):
            clases["descripcion"]=random.choice(["una joya las clases mi papacho"])
        elif(probabilidadError<0.5):
            clases["horario"]=None
        elif(probabilidadError<0.6):
            clases["cupos"]=random.choice(["no se demore que se queda sin cupo"])
        elif(probabilidadError<0.7):
             clases["niveles"]=random.choice(["su nivel es 3"])
        elif(probabilidadError<0.8):
            clases["id_entrenadores"]=None
        elif(probabilidadError<0.9):
            clases["estado"]=random.choice(["fisico","virtual"])
        simulaciones.append(clases)
    return simulaciones
         

