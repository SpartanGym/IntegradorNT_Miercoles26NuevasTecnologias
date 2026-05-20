import pandas as pd

#zona para importar simulaciones

from utils.simulaciónDatosSocios import generar_socios
from utils.simulacionClases import generar_clases

#zona para importar limpiezas 

from notebook.limpiezaDatosSocios import limpiar_socios
from notebook.limpiezaDatosClases import limpiar_clases


#Creando las simulaciones
simulaciones_socios=generar_socios(1000)
simulaciones_clases=generar_clases(1000)

print(simulaciones_socios)
print(simulaciones_clases)

#Ordenando las simulaciones
simulaciones_socios_ordenadas=pd.DataFrame(simulaciones_socios)
simulaciones_clases_ordenadas=pd.DataFrame(simulaciones_clases)

#limpiando el set de datos
simulaciones_socios_limpias=limpiar_socios(simulaciones_socios_ordenadas)
simulaciones_clases_limpias=limpiar_clases(simulaciones_clases_ordenadas)

print(simulaciones_socios_limpias)
print(simulaciones_clases_limpias)