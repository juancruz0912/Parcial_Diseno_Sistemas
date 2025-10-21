from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones import mensajes_exception

class PersistenciaException(ForestacionException):
    def __init__(self, error_code: str, message: str, user_message: str = None, cause: Exception = None, tipo_operacion: str = "Desconocida"):
        super().__init__(error_code, message, user_message, cause)
        self._tipo_operacion = tipo_operacion

    def get_tipo_operacion(self) -> str:
        return self._tipo_operacion
