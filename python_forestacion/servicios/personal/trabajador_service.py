from datetime import date
from typing import List
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea

class TrabajadorService:
    def trabajar(self, trabajador: Trabajador, fecha: date, util: Herramienta) -> bool:
        if not trabajador.get_apto_medico().esta_apto():
            print(f"El trabajador {trabajador.get_nombre()} no puede trabajar - apto médico inválido")
            return False

        tareas_ordenadas: List[Tarea] = sorted(trabajador.get_tareas(), key=lambda t: t.get_id_tarea(), reverse=True)

        tarea_ejecutada = False
        for tarea in tareas_ordenadas:
            if tarea.get_fecha_programada() == fecha:
                print(f"El trabajador {trabajador.get_nombre()} realizó la tarea {tarea.get_id_tarea()} {tarea.get_descripcion()} con herramienta: {util.get_nombre()}")
                tarea.set_completada(True)
                tarea_ejecutada = True
        return tarea_ejecutada

    def asignar_apto_medico(self, trabajador: Trabajador, apto: bool, fecha_emision: date, observaciones: str) -> None:
        trabajador.asignar_apto_medico(apto, fecha_emision, observaciones)
        print(f"Apto médico actualizado para: {trabajador.get_nombre()}")
