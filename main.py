import pandas as pd

#zona para importar simulaciones

from utils.simulaciónDatosSocios  import generar_socios

#zona para importar limpiezas 

from notebook.limpiezaDatosSocios import limpiar_socios


#Creando las simulaciones
simulaciones=generar_socios(100)
print(simulaciones)

#Ordenando las simulaciones
simulaciones_ordenadas=pd.DataFrame(simulaciones)

#limpiando el set de datos
simulaciones_limpias=limpiar_socios(simulaciones_ordenadas)
print(simulaciones_limpias)