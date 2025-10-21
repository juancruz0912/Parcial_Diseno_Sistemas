"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy\absorcion_agua_strategy.py
# ================================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """Interfaz abstracta para las estrategias de cálculo de absorción de agua de cultivos.

    Define el contrato que deben seguir todas las implementaciones de estrategias de absorción.
    """
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """Calcula la cantidad de agua que un cultivo debe absorber.

        Args:
            fecha (date): La fecha actual, utilizada para cálculos estacionales.
            temperatura (float): La temperatura ambiental actual.
            humedad (float): La humedad ambiental actual.
            cultivo (Cultivo): El cultivo para el cual se calcula la absorción.

        Returns:
            int: La cantidad de agua absorbida por el cultivo en litros.
        """
        pass


