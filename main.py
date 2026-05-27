import pandas as pd


# ==========================================
# IMPORTAR SIMULACIONES
# ==========================================
from utils.simulaciónDatosSocios import generar_socios
from utils.simulacionClases import generar_clases


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
# IMPORTAR GRAFICACION SOCIOS
# ==========================================
from notebook.graficacionSocios import (
    graficar_socios_por_nombre,
    graficar_socios_por_estado,
    graficar_socios_thomas,
    graficar_membresias_altas
)


# ==========================================
# IMPORTAR GRAFICACION CLASES
# ==========================================
from notebook.graficacionClases import (
    graficar_clases_por_nivel,
    graficar_clases_virtual_vs_fisico,
    graficar_clases_con_muchos_cupos
)


# ==========================================
# GENERAR DATOS
# ==========================================
datos_socios = generar_socios(1000)
datos_clases = generar_clases(1000)


# ==========================================
# DATAFRAMES
# ==========================================
dataFrameSocios = pd.DataFrame(datos_socios)
dataFrameClases = pd.DataFrame(datos_clases)


# ==========================================
# LIMPIEZA
# ==========================================
dataFrameSociosLimpio = limpiar_socios(dataFrameSocios)
dataFrameClasesLimpio = limpiar_clases(dataFrameClases)


# ==========================================
# DESCRIPCIÓN
# ==========================================
print("\n========== SOCIOS ==========\n")
describir_socios(dataFrameSociosLimpio)

print("\n========== CLASES ==========\n")
describir_clases(dataFrameClasesLimpio)


# ==========================================
# TRANSFORMACIÓN
# ==========================================
resultadoSocios = transformar_datos_socios(dataFrameSociosLimpio)
resultadoClases = transformar_datos(dataFrameClasesLimpio)


# ==========================================
# RESULTADOS
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

graficar_clases_por_nivel(resultadoClases["clasesNivel1"])
graficar_clases_virtual_vs_fisico(resultadoClases["clasesVirtuales"])
graficar_clases_con_muchos_cupos(resultadoClases["clasesConMuchosCupos"])