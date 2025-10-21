"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy\impl
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy\impl\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy\impl\absorcion_constante_strategy.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy\impl\absorcion_seasonal_strategy.py
# ================================================================================

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


