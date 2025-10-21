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
