# ============================================
# CÓDIGOS DE ERROR
# ============================================

ERROR_CODE_00 = "ERROR 00"
ERROR_CODE_01 = "ERROR 01"
ERROR_CODE_02 = "ERROR 02"
ERROR_CODE_03 = "ERROR 03"
ERROR_CODE_04 = "ERROR 04"
ERROR_CODE_05 = "ERROR 05"
ERROR_CODE_06 = "ERROR 06"
ERROR_CODE_07 = "ERROR 07"

# ============================================
# ERRORES GENERALES
# ============================================

ERROR_00_NO_IDENTIFICADO = "Se produjo un error no identificado en el sistema"

# ============================================
# ERRORES DE RIEGO Y AGUA
# ============================================

ERROR_01_AGUA_AGOTADA = "Se agotó el agua disponible en la finca"
ERROR_01_AGUA_AGOTADA_USER_MESSAGE = "No hay suficiente agua disponible para continuar el riego. Nivel de agua crítico."

def get_agua_agotada_detallado_message(agua_disponible: float, agua_minima: float) -> str:
    return f"Agua insuficiente para riego. Disponible: {agua_disponible:.2f} L, Mínimo requerido: {agua_minima:.2f} L"

# ============================================
# ERRORES DE SUPERFICIE Y PLANTACIÓN
# ============================================

ERROR_02_SUPERFICIE_INSUFICIENTE_PREFIX = "No se pudo plantar: "
ERROR_02_SUPERFICIE_INSUFICIENTE_SUFFIX = " porque no queda superficie disponible en la finca"

def get_superficie_insuficiente_message(cultivo: str) -> str:
    return ERROR_02_SUPERFICIE_INSUFICIENTE_PREFIX + cultivo + \
           ERROR_02_SUPERFICIE_INSUFICIENTE_SUFFIX

def get_superficie_insuficiente_user_message(cultivo: str) -> str:
    return f"No hay suficiente espacio en la plantación para cultivar {cultivo}"

def get_superficie_insuficiente_detallado_message(cultivo: str, superficie_requerida: float, superficie_disponible: float) -> str:
    return f"No se puede plantar {cultivo}. Requiere: {superficie_requerida:.2f} m², Disponible: {superficie_disponible:.2f} m²"

# ============================================
# ERRORES DE PERSISTENCIA - ESCRITURA
# ============================================

ERROR_03_ARCHIVO_NO_ENCONTRADO_ESCRITURA = "No se encontró la ruta del archivo para escritura"
ERROR_04_IO_ESCRITURA = "Se produjo un error de entrada/salida durante la escritura"

# ============================================
# ERRORES DE PERSISTENCIA - LECTURA
# ============================================

ERROR_05_ARCHIVO_NO_ENCONTRADO_LECTURA = "No se encontró el archivo para lectura"
ERROR_06_IO_LECTURA = "Se produjo un error de entrada/salida durante la lectura"
ERROR_07_CLASS_NOT_FOUND = "Error de conversión de clase durante la deserialización"

def get_archivo_no_encontrado_message(nombre_archivo: str) -> str:
    return f"No se encontró el archivo: {nombre_archivo}"

def get_io_error_message(nombre_archivo: str) -> str:
    return f"Error de entrada/salida al procesar el archivo: {nombre_archivo}"

def get_class_not_found_message(nombre_archivo: str) -> str:
    return f"Error de deserialización. Verifique la versión de las clases en: {nombre_archivo}"

# ============================================
# MENSAJES DE OPERACIONES EXITOSAS
# ============================================

def get_persistencia_exitosa_message(propietario: str) -> str:
    return f"Registro persistido exitosamente: {propietario}"

def get_lectura_exitosa_message(propietario: str) -> str:
    return f"Registro leído exitosamente: {propietario}"
