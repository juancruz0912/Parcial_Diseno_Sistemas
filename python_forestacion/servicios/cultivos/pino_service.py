from datetime import date
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class PinoService(ArbolService):
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

    def cosechar(self, pino: Pino) -> bool:
        # Pino can be harvested all year round
        print("Se ha cosechado este pino")
        return True

    def secretar_resina(self, pino: Pino) -> None:
        print("Estoy secretando resina")

    def florecer(self, pino: Pino) -> bool:
        mes = date.today().month
        return 9 <= mes <= 12

    def absorver_agua(self, pino: Pino) -> int:
        mes = date.today().month
        agua_absorvida = 0

        if mes in [1, 2, 3, 4, 9, 10, 11, 12]:
            agua_absorvida = 2

        pino.set_agua(pino.get_agua() + agua_absorvida)
        return agua_absorvida

    def consumir_agua(self, pino: Pino) -> int:
        mes = date.today().month
        agua_consumida = 0

        if mes in [1, 2, 3, 4, 9, 10, 11, 12]:
            agua_consumida = 2
            self.crecer(pino, 0.10)
        elif mes in [5, 6, 7, 8]:
            agua_consumida = 1

        pino.set_agua(pino.get_agua() - agua_consumida)
        return agua_consumida

    def mostrar_datos(self, pino: Pino) -> None:
        print(f"Cultivo {pino.__class__.__name__}")
        print(f"Variedad: {pino.get_variedad()}")
        print(f"Altura: {pino.get_altura()}")
