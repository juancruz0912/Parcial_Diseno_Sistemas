"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\arbol.py
# ================================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    _cant_arboles = 0

    def __init__(self, agua: int, superficie: float, altura: float):
        super().__init__(agua, superficie)
        Arbol._cant_arboles += 1
        self._id = Arbol._cant_arboles
        self._altura = altura

    def get_id(self) -> int:
        return self._id

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        self._altura = altura

    @staticmethod
    def get_cant_arboles() -> int:
        return Arbol._cant_arboles


# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\cultivo.py
# ================================================================================

from abc import ABC

class Cultivo(ABC):
    EDAD_MAXIMA = 20

    def __init__(self, agua: int, superficie: float):
        self._agua = agua
        self._superficie = superficie

    def get_agua(self) -> int:
        return self._agua
    
    def set_agua(self, agua: int) -> None:
        self._agua = agua

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        self._superficie = superficie


# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\hortaliza.py
# ================================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo):
    def __init__(self, agua: int, superficie: float, invernadero: bool):
        super().__init__(agua, superficie)
        self._invernadero = invernadero

    def is_invernadero(self) -> bool:
        return self._invernadero

    def set_invernadero(self, invernadero: bool) -> None:
        self._invernadero = invernadero


# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\lechuga.py
# ================================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA

class Lechuga(Hortaliza):
    def __init__(self, variedad: str):
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad


# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\olivo.py
# ================================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO, OLIVO_INITIAL_ALTURA

class Olivo(Arbol):
    def __init__(self, tipo_aceituna: TipoAceituna):
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=OLIVO_INITIAL_ALTURA
        )
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna


# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\pino.py
# ================================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO, PINO_INITIAL_ALTURA

class Pino(Arbol):
    """Representa un tipo de cultivo de pino, heredando de Arbol.

    Attributes:
        _variedad (str): La variedad específica del pino.
    """
    def __init__(self, variedad: str):
        """Inicializa una nueva instancia de Pino.

        Args:
            variedad (str): La variedad del pino (e.g., "Parana", "Elliott").
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=PINO_INITIAL_ALTURA
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Obtiene la variedad del pino.

        Returns:
            str: La variedad del pino.
        """
        return self._variedad


# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ================================================================================

from enum import Enum

class TipoAceituna(Enum):
    NEGRA = "Negra"
    VERDE = "Verde"
    ROJA = "Roja"


# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\zanahoria.py
# ================================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA

class Zanahoria(Hortaliza):
    def __init__(self, is_baby: bool):
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._is_baby = is_baby

    def is_baby_carrot(self) -> bool:
        return self._is_baby

    def set_is_baby(self, is_baby: bool) -> None:
        self._is_baby = is_baby


