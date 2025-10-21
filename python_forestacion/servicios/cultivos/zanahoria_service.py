from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

class ZanahoriaService(CultivoService):
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))

    def cosechar(self, zanahoria: Zanahoria) -> bool:
        # Zanahoria can be harvested all year round
        print("Se ha cosechado esta zanahoria")
        return True
