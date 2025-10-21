from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class ArbolService(CultivoService):
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        super().__init__(estrategia_absorcion)

    def crecer(self, arbol: Arbol, incremento: float) -> bool:
        if 0 < incremento < 1:
            arbol.set_altura(arbol.get_altura() + incremento)
            self._consumir_agua_por_crecimiento(arbol)
            return True
        return False

    def _consumir_agua_por_crecimiento(self, arbol: Arbol) -> None:
        if arbol.get_agua() > 0:
            arbol.set_agua(arbol.get_agua() - 1)
