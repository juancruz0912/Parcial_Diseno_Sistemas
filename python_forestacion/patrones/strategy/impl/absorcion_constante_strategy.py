from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Implementación de la estrategia de absorción de agua constante.

    El cultivo absorbe una cantidad fija de agua, independientemente de factores externos.
    """
    def __init__(self, cantidad_constante: int):
        """Inicializa una nueva instancia de AbsorcionConstanteStrategy.

        Args:
            cantidad_constante (int): La cantidad fija de agua a absorber.
        """
        self._cantidad = cantidad_constante

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """Calcula la absorción de agua, retornando la cantidad constante predefinida.

        Args:
            fecha (date): La fecha actual (no usada en esta estrategia).
            temperatura (float): La temperatura ambiental actual (no usada en esta estrategia).
            humedad (float): La humedad ambiental actual (no usada en esta estrategia).
            cultivo (Cultivo): El cultivo para el cual se calcula la absorción (no usado en esta estrategia).

        Returns:
            int: La cantidad constante de agua a absorber.
        """
        return self._cantidad
