import pandas as pd


# ==========================================
# IMPORTAR CONSUMOS
# ==========================================

from notebook.consumoDatosSocios import consumir_socios
from notebook.consumoDatosClases import consumir_clases


# ==========================================
# IMPORTAR LIMPIEZAS
# ==========================================

from notebook.limpiezaDatosSocios import limpiar_socios
from notebook.limpiezaDatosClases import limpiar_clases


# ==========================================
# IMPORTAR TRANSFORMACIONES
# ==========================================

from notebook.transformacionDatosSocios import transformar_datos_socios
from notebook.transformacionDatosClases import transformar_datos


# ==========================================
# IMPORTAR DESCRIPCIONES
# ==========================================

from notebook.descripcionDatosSocios import describir_datos as describir_socios
from notebook.descripcionDatosClases import describir_datos as describir_clases


# ==========================================
# IMPORTAR GRAFICACION
# ==========================================

from notebook.graficacionSocios import (
    graficar_socios_por_nombre,
    graficar_socios_por_estado,
    graficar_socios_thomas,
    graficar_membresias_altas
)
from notebook.graficacionClases import (
    graficar_clases_por_nivel,
    graficar_clases_virtual_vs_fisico,
    graficar_clases_con_muchos_cupos
)


# ==========================================
# CONSUMIR DATOS DESDE LA API
# ==========================================

datos_socios = consumir_socios()
datos_clases = consumir_clases()


# ==========================================
# CONVERTIR A DATAFRAME
# ==========================================

dataFrameSocios = pd.DataFrame(datos_socios)
dataFrameClases = pd.DataFrame(datos_clases)


# ==========================================
# LIMPIAR DATOS
# ==========================================

dataFrameSociosLimpio = limpiar_socios(dataFrameSocios)
dataFrameClasesLimpio = limpiar_clases(dataFrameClases)


# ==========================================
# DESCRIBIR DATOS
# ==========================================

print("\n========== SOCIOS ==========\n")
describir_socios(dataFrameSociosLimpio)

print("\n========== CLASES ==========\n")
describir_clases(dataFrameClasesLimpio)


# ==========================================
# TRANSFORMAR DATOS
# ==========================================

resultadoSocios = transformar_datos_socios(dataFrameSociosLimpio)
resultadoClases = transformar_datos(dataFrameClasesLimpio)


# ==========================================
# MOSTRAR RESULTADOS
# ==========================================

print("\n========== RESULTADOS SOCIOS ==========\n")
print(resultadoSocios["usuariosActivos"])
print(resultadoSocios["membresiasAltas"])
print(resultadoSocios["sociosThomas"])

print("\n========== RESULTADOS CLASES ==========\n")
print(resultadoClases["clasesVirtuales"])
print(resultadoClases["clasesConMuchosCupos"])
print(resultadoClases["clasesNivel1"])


# ==========================================
# GRAFICAR SOCIOS
# ==========================================

print("\n========== GRAFICANDO SOCIOS ==========\n")

graficar_socios_por_nombre(resultadoSocios["usuariosActivos"])
graficar_socios_por_estado(resultadoSocios["membresiasAltas"])
graficar_socios_thomas(resultadoSocios["sociosThomas"])
graficar_membresias_altas(resultadoSocios["membresiasAltas"])


# ==========================================
# GRAFICAR CLASES
# ==========================================

print("\n========== GRAFICANDO CLASES ==========\n")

graficar_clases_por_nivel(resultadoClases["clasesVirtuales"])
graficar_clases_virtual_vs_fisico(resultadoClases["clasesVirtuales"])
graficar_clases_con_muchos_cupos(resultadoClases["clasesConMuchosCupos"])