from datetime import date
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class CultivoService:
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia_absorcion

    def mostrar_datos(self, cultivo: Cultivo):
        print(f"Cultivo: {cultivo.__class__.__name__}")
        print(f"Superficie: {cultivo.get_superficie():.2f} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")

    def absorver_agua(self, cultivo: Cultivo, fecha: date, temperatura: float, humedad: float) -> int:
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(fecha, temperatura, humedad, cultivo)
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida
