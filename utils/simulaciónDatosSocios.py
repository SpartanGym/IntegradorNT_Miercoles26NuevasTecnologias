import random

from datetime import datetime,timedelta

def generar_socios(numeroSimulaciones):

    nombres=["Thomas","Jose","Alberto","Santiago","Camilo"]
    estado=["usuario activo","usuario bloqueado"]
    telefono=["30168898","3122581896","3082225555","3086741767"]
    correo=["r.eb.e.cca.9.7.10@gmail.com","theobald2798+paz@gmail.com","tayahschwarz257+mcmullin@googlemail.com","s.v.bd.j.ek.sh.s.kv@gmail.com"]
    fechaInicio=datetime(2026,1,2)

    simulaciones=[]
    for _ in range(numeroSimulaciones):

        Socio={
            "id_socio":random.randint(0,200),
            "Nombre_usuario":random.choice(nombres),
            "correo":random.choice(correo),
            "telefono":random.choice(telefono),
            "fecha_inscripcion":fechaInicio+timedelta(days=random.randint(0,60)),
            "estado":random.choice(estado),
            "id_membresia":random.randint(200,400),
            "created_at":fechaInicio+timedelta(days=random.randint(0,60)),
            "updated_at":fechaInicio+timedelta(days=random.randint(0,60))
        }

        #Inyectando errores controlados
        probabilidadError=random.random()
        if(probabilidadError<0.2):
            Socio["id_socio"]=None
        elif(probabilidadError<0.3):
            Socio["Nombre_usuario"]=random.choice(["Maria","Yaruis","Rodolfa"])
        elif(probabilidadError<0.4):
            Socio["correo"]=random.choice(["rolo07@gmail.com","thomasrolo07@gmail.com","albertofans@gmail.com"])
        elif(probabilidadError<0.5):
            Socio["telefono"]=random.choice(["3012244612","318191157","3018181919"])
        elif(probabilidadError<0.6):
            Socio["fecha_inscripcion"]=None
        elif(probabilidadError<0.7):
            Socio["estado"]=random.choice(["REACTIVO","REBLOQUEADO"])
        elif(probabilidadError<0.8):
            Socio["id_membresia"]=None
        elif(probabilidadError<0.9):
            Socio["created_at"]=None
        elif(probabilidadError<0.9):
            Socio["updated_at"]=None

        simulaciones.append(Socio)
    return simulaciones 