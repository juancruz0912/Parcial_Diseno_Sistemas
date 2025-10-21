"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\terrenos
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\terrenos\plantacion.py
# ================================================================================

from typing import List
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.terrenos.tierra import Tierra

class Plantacion:
    def __init__(self, id: int, nombre: str, agua: int, tierra: Tierra):
        self._id = id
        self._nombre = nombre
        self._agua_disponible = agua
        self._situada_en = tierra
        self._cultivos: List[Cultivo] = []
        self._trabajadores: List[Trabajador] = []

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def get_id(self) -> int:
        return self._id

    def set_id(self, id: int) -> None:
        self._id = id

    def get_agua_disponible(self) -> int:
        return self._agua_disponible

    def set_agua_disponible(self, agua_disponible: int) -> None:
        if agua_disponible < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua_disponible = agua_disponible

    def get_situada_en(self) -> Tierra:
        return self._situada_en

    def set_situada_en(self, situada_en: Tierra) -> None:
        self._situada_en = situada_en

    def get_cultivos(self) -> List[Cultivo]:
        return self._cultivos.copy()

    def set_cultivos(self, cultivos: List[Cultivo]) -> None:
        self._cultivos = cultivos.copy() if cultivos else []

    def get_trabajadores(self) -> List[Trabajador]:
        return self._trabajadores.copy()

    def set_trabajadores(self, trabajadores: List[Trabajador]) -> None:
        self._trabajadores = trabajadores.copy() if trabajadores else []

    def get_cultivos_interno(self) -> List[Cultivo]:
        return self._cultivos

    def get_trabajadores_interno(self) -> List[Trabajador]:
        return self._trabajadores


# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\terrenos\registro_forestal.py
# ================================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    def __init__(self, id_padron: int, tierra: Tierra, plantacion: Plantacion, propietario: str, avaluo: float):
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_padron(self) -> int:
        return self._id_padron

    def set_id_padron(self, id_padron: int) -> None:
        self._id_padron = id_padron

    def get_tierra(self) -> Tierra:
        return self._tierra

    def get_plantacion(self) -> Plantacion:
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def set_propietario(self, propietario: str) -> None:
        self._propietario = propietario

    def get_avaluo(self) -> float:
        return self._avaluo

    def set_avaluo(self, avaluo: float) -> None:
        self._avaluo = avaluo


# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\terrenos\tierra.py
# ================================================================================

class Tierra:
    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = None

    def get_id_padron_catastral(self) -> int:
        return self._id_padron_catastral

    def set_id_padron_catastral(self, id_padron_catastral: int) -> None:
        self._id_padron_catastral = id_padron_catastral

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def set_domicilio(self, domicilio: str) -> None:
        self._domicilio = domicilio

    def get_finca(self):
        return self._finca

    def set_finca(self, finca) -> None:
        self._finca = finca


