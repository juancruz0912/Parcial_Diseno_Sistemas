"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\agua_agotada_exception.py
# ================================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones import mensajes_exception

class AguaAgotadaException(ForestacionException):
    def __init__(self, agua_disponible: float = 0.0, agua_minima: float = 10.0):
        if agua_disponible == 0.0 and agua_minima == 10.0: # Default constructor
            super().__init__(
                mensajes_exception.ERROR_CODE_01,
                mensajes_exception.ERROR_01_AGUA_AGOTADA,
                mensajes_exception.ERROR_01_AGUA_AGOTADA_USER_MESSAGE
            )
        else:
            super().__init__(
                mensajes_exception.ERROR_CODE_01,
                mensajes_exception.ERROR_01_AGUA_AGOTADA,
                mensajes_exception.get_agua_agotada_detallado_message(agua_disponible, agua_minima)
            )
        self._agua_disponible = agua_disponible
        self._agua_minima = agua_minima

    def get_agua_disponible(self) -> float:
        return self._agua_disponible

    def get_agua_minima(self) -> float:
        return self._agua_minima


# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\forestacion_exception.py
# ================================================================================

class ForestacionException(Exception):
    """Excepción base para todos los errores específicos de la aplicación de forestación.

    Permite encapsular un código de error, un mensaje técnico, un mensaje para el usuario
    y la causa original de la excepción.
    """
    def __init__(self, error_code: str, message: str, user_message: str = None, cause: Exception = None):
        """Inicializa una nueva instancia de ForestacionException.

        Args:
            error_code (str): Código único que identifica el tipo de error.
            message (str): Mensaje técnico detallado de la excepción.
            user_message (str, optional): Mensaje amigable para el usuario. Si no se provee, usa `message`.
            cause (Exception, optional): La excepción original que causó esta excepción.
        """
        super().__init__(message)
        self._error_code = error_code
        self._user_message = user_message if user_message is not None else message
        self._cause = cause

    def get_error_code(self) -> str:
        """Obtiene el código de error de la excepción.

        Returns:
            str: El código de error.
        """
        return self._error_code

    def get_user_message(self) -> str:
        """Obtiene el mensaje amigable para el usuario de la excepción.

        Returns:
            str: El mensaje para el usuario.
        """
        return self._user_message

    def get_full_message(self) -> str:
        """Obtiene el mensaje completo de la excepción, incluyendo el código de error y el mensaje de usuario.

        Returns:
            str: El mensaje completo.
        """
        return f"{self._error_code} - {self._user_message}"

    def __str__(self) -> str:
        """Retorna la representación en cadena de la excepción.

        Returns:
            str: La representación en cadena de la excepción.
        """
        base_str = self.get_full_message()
        if self._cause:
            return f"{base_str} | Causa: {self._cause}"
        return base_str

    @property
    def cause(self) -> Exception:
        """Propiedad para acceder a la excepción original que causó esta excepción.

        Returns:
            Exception: La excepción original.
        """
        return self._cause


# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\mensajes_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\persistencia_exception.py
# ================================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones import mensajes_exception

class PersistenciaException(ForestacionException):
    def __init__(self, error_code: str, message: str, user_message: str = None, cause: Exception = None, tipo_operacion: str = "Desconocida"):
        super().__init__(error_code, message, user_message, cause)
        self._tipo_operacion = tipo_operacion

    def get_tipo_operacion(self) -> str:
        return self._tipo_operacion


# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ================================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones import mensajes_exception

class SuperficieInsuficienteException(ForestacionException):
    def __init__(self, tipo_cultivo: str, superficie_requerida: float = 0.0, superficie_disponible: float = 0.0):
        if superficie_requerida == 0.0 and superficie_disponible == 0.0: # Basic constructor
            super().__init__(
                mensajes_exception.ERROR_CODE_02,
                mensajes_exception.get_superficie_insuficiente_message(tipo_cultivo),
                mensajes_exception.get_superficie_insuficiente_user_message(tipo_cultivo)
            )
        else:
            super().__init__(
                mensajes_exception.ERROR_CODE_02,
                mensajes_exception.get_superficie_insuficiente_message(tipo_cultivo),
                mensajes_exception.get_superficie_insuficiente_detallado_message(tipo_cultivo, superficie_requerida, superficie_disponible)
            )
        self._tipo_cultivo = tipo_cultivo
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    def get_tipo_cultivo(self) -> str:
        return self._tipo_cultivo

    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible


