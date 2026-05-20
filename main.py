import pandas as pd

from utils.simulacionDatosClases import generar_clases

from notebook.limpiezaDatosClases import limpiar_clases
from notebook.descripcionDatosClases import describir_datos
from notebook.transformacionDatosClases import transformar_datos


# GENERAR DATOS
simulaciones = generar_clases(1000)

# convertir a dataframe
data_frame_sucio = pd.DataFrame(simulaciones)



# LIMPIAR DATOS
data_frame_limpio = limpiar_clases(data_frame_sucio)



# DESCRIBIR DATOS
describir_datos(data_frame_limpio)



# TRANSFORMAR DATOS
resultados = transformar_datos(data_frame_limpio)


# MOSTRAR RESULTADOS
print(resultados["clasesVirtuales"])

print(resultados["clasesConMuchosCupos"])

print(resultados["clasesNivel1"])

print(resultados["clasesPorEntrenador"])

print(resultados["clasesPorFecha"])