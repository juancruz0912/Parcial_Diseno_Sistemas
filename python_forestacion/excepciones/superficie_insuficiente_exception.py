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
