from python_forestacion.entidades.cultivos.lechuga import Lechuga

class LechugaService:
    def desarrollar_semilla(self, lechuga: Lechuga) -> None:
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
