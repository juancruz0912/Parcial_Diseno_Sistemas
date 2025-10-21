from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA

class Zanahoria(Hortaliza):
    def __init__(self, is_baby: bool):
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._is_baby = is_baby

    def is_baby_carrot(self) -> bool:
        return self._is_baby

    def set_is_baby(self, is_baby: bool) -> None:
        self._is_baby = is_baby
