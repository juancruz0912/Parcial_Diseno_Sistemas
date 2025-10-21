from typing import List
from datetime import date
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico

class Trabajador:
    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas.copy() if tareas else []
        self._apto_medico: AptoMedico = AptoMedico(True, date.today(), "Estado de salud: bueno")

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def get_tareas(self) -> List[Tarea]:
        return self._tareas.copy()

    def set_tareas(self, tareas: List[Tarea]) -> None:
        self._tareas = tareas.copy() if tareas else []

    def get_apto_medico(self) -> AptoMedico:
        return self._apto_medico

    def set_apto_medico(self, apto_medico: AptoMedico) -> None:
        self._apto_medico = apto_medico

    def asignar_apto_medico(self, apto: bool, fecha_emision: date, observaciones: str) -> None:
        self._apto_medico = AptoMedico(apto, fecha_emision, observaciones)
