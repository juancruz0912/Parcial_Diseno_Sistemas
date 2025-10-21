"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\factory
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\factory\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\factory\cultivo_factory.py
# ================================================================================

from typing import Dict, Callable
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import PINO_DEFAULT_VARIEDAD, OLIVO_DEFAULT_TIPO_ACEITUNA, LECHUGA_DEFAULT_VARIEDAD, ZANAHORIA_DEFAULT_ES_BABY_CARROT

class CultivoFactory:
    """Fábrica para la creación de objetos Cultivo utilizando el patrón Factory Method.

    Permite la creación de diferentes tipos de cultivos (Pino, Olivo, Lechuga, Zanahoria)
    sin exponer la lógica de instanciación al cliente.
    """
    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        """Crea una instancia de un cultivo basado en la especie proporcionada.

        Args:
            especie (str): El nombre de la especie del cultivo a crear.

        Returns:
            Cultivo: Una instancia del cultivo solicitado.

        Raises:
            ValueError: Si la especie de cultivo no es reconocida.
        """
        factories: Dict[str, Callable[[], Cultivo]] = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie de cultivo desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> Pino:
        """Crea una instancia de Pino con valores por defecto."""
        return Pino(variedad=PINO_DEFAULT_VARIEDAD)

    @staticmethod
    def _crear_olivo() -> Olivo:
        """Crea una instancia de Olivo con valores por defecto."""
        return Olivo(tipo_aceituna=OLIVO_DEFAULT_TIPO_ACEITUNA)

    @staticmethod
    def _crear_lechuga() -> Lechuga:
        """Crea una instancia de Lechuga con valores por defecto."""
        return Lechuga(variedad=LECHUGA_DEFAULT_VARIEDAD)

    @staticmethod
    def _crear_zanahoria() -> Zanahoria:
        """Crea una instancia de Zanahoria con valores por defecto."""
        return Zanahoria(is_baby=ZANAHORIA_DEFAULT_ES_BABY_CARROT)


