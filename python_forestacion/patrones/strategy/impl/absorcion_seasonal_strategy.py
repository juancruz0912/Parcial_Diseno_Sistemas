from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import ABSORCION_SEASONAL_VERANO, ABSORCION_SEASONAL_INVIERNO, MES_INICIO_VERANO, MES_FIN_VERANO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Implementación de la estrategia de absorción de agua estacional.

    La cantidad de agua absorbida por el cultivo varía según la estación del año.
    """
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """Calcula la absorción de agua basándose en la estación (mes).

        Args:
            fecha (date): La fecha actual para determinar el mes.
            temperatura (float): La temperatura ambiental actual (no usada en esta estrategia).
            humedad (float): La humedad ambiental actual (no usada en esta estrategia).
            cultivo (Cultivo): El cultivo para el cual se calcula la absorción (no usado en esta estrategia).

        Returns:
            int: La cantidad de agua absorbida, que varía según si es verano o invierno.
        """
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO
