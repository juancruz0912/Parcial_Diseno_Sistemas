"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\constantes.py
# ================================================================================

from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

# Agua
AGUA_MINIMA = 10
AGUA_INICIAL_PLANTACION = 500

# Riego
TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50
MES_INICIO_VERANO = 12
MES_FIN_VERANO = 2

# Absorcion
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2

# Cultivos
SUPERFICIE_PINO = 2.0
AGUA_INICIAL_PINO = 2
PINO_DEFAULT_VARIEDAD = "cedro"
PINO_INITIAL_ALTURA = 1.0

AGUA_INICIAL_OLIVO = 5
SUPERFICIE_OLIVO = 3.0
OLIVO_DEFAULT_TIPO_ACEITUNA = TipoAceituna.NEGRA
OLIVO_INITIAL_ALTURA = 0.5

AGUA_INICIAL_ZANAHORIA = 0
SUPERFICIE_ZANAHORIA = 0.15
ZANAHORIA_DEFAULT_ES_BABY_CARROT = True

AGUA_INICIAL_LECHUGA = 1
SUPERFICIE_LECHUGA = 0.2
LECHUGA_DEFAULT_VARIEDAD = "Mantecosa"


