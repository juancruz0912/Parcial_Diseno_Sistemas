from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService:
    def desarrollar_semilla(self, zanahoria: Zanahoria) -> None:
        print("Desarrollando semilla de zanahoria")

    def absorver_agua(self, zanahoria: Zanahoria) -> int:
        zanahoria.set_agua(zanahoria.get_agua() + 2)
        return 2

    def consumir_agua(self, zanahoria: Zanahoria) -> int:
        zanahoria.set_agua(zanahoria.get_agua() - 1)
        return 1

    def mostrar_datos(self, zanahoria: Zanahoria) -> None:
        print(f"Cultivo: {zanahoria.__class__.__name__}")
        if zanahoria.is_baby_carrot():
            print("Es baby carrot")
