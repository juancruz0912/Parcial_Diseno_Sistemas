from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

class LechugaService(CultivoService):
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(1))

    def cosechar(self, lechuga: Lechuga) -> bool:
        # Lechuga can be harvested all year round
        print("Se ha cosechado esta lechuga")
        return True
        print("Desarrollando semilla de lechuga")

    def absorver_agua(self, lechuga: Lechuga) -> int:
        lechuga.set_agua(lechuga.get_agua() + 1)
        return 1

    def consumir_agua(self, lechuga: Lechuga) -> int:
        lechuga.set_agua(lechuga.get_agua() - 1)
        return 1

    def mostrar_datos(self, lechuga: Lechuga) -> None:
        print(f"Cultivo: {lechuga.__class__.__name__}")
        print(f"Variedad: {lechuga.get_variedad()}")
