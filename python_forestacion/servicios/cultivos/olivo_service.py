from datetime import date
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.servicios.cultivos.arbol_service import ArbolService

class OlivoService(ArbolService):
    def cosechar(self, olivo: Olivo) -> bool:
        mes = date.today().month
        if 5 <= mes <= 7:
            print("Se ha cosechado este olivo")
            return True
        return False

    def florecer(self, olivo: Olivo) -> bool:
        mes = date.today().month
        return 9 <= mes <= 12

    def absorver_agua(self, olivo: Olivo) -> int:
        mes = date.today().month
        agua_absorvida = 0

        if mes in [1, 2, 3, 4, 9, 10, 11, 12]:
            agua_absorvida = 1

        olivo.set_agua(olivo.get_agua() + agua_absorvida)
        return agua_absorvida

    def consumir_agua(self, olivo: Olivo) -> int:
        mes = date.today().month
        agua_consumida = 0

        if mes in [1, 2, 3, 4, 9, 10, 11, 12]:
            agua_consumida = 2
            self.crecer(olivo, 0.01)
        elif mes in [5, 6, 7, 8]:
            agua_consumida = 1

        olivo.set_agua(olivo.get_agua() - agua_consumida)
        return agua_consumida

    def mostrar_datos(self, olivo: Olivo) -> None:
        print(f"Cultivo {olivo.__class__.__name__}")
        print(f"Fruto: {olivo.get_fruto().name}")
        print(f"Altura: {olivo.get_altura()}")
