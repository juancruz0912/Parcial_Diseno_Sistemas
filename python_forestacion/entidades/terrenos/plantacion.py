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
