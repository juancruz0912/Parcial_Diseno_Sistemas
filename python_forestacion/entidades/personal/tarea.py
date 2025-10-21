from datetime import date

class Tarea:
    def __init__(self, id_tarea: int, fecha_programada: date, descripcion: str):
        self._id_tarea = id_tarea
        self._fecha_programada = fecha_programada
        self._descripcion = descripcion
        self._completada = False

    def get_id_tarea(self) -> int:
        return self._id_tarea

    def set_id_tarea(self, id_tarea: int) -> None:
        self._id_tarea = id_tarea

    def get_fecha_programada(self) -> date:
        return self._fecha_programada

    def set_fecha_programada(self, fecha_programada: date) -> None:
        self._fecha_programada = fecha_programada

    def get_descripcion(self) -> str:
        return self._descripcion

    def set_descripcion(self, descripcion: str) -> None:
        self._descripcion = descripcion

    def is_completada(self) -> bool:
        return self._completada

    def set_completada(self, completada: bool) -> None:
        self._completada = completada
