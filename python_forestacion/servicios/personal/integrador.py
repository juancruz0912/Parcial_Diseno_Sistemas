"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\personal
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\personal\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\personal\trabajador_service.py
# ================================================================================

from datetime import date
from typing import List
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea

class TrabajadorService:
    @staticmethod
    def _obtener_id_tarea(tarea: Tarea) -> int:
        """Obtiene el ID de una tarea para ordenamiento."""
        return tarea.get_id_tarea()

    def trabajar(self, trabajador: Trabajador, fecha: date, herramienta: Herramienta) -> bool:
        if not trabajador.get_apto_medico().esta_apto():
            print(f"El trabajador {trabajador.get_nombre()} no puede trabajar - apto médico inválido")
            return False

        tareas_ordenadas: List[Tarea] = sorted(
            trabajador.get_tareas(), 
            key=TrabajadorService._obtener_id_tarea, 
            reverse=True
        )

        tarea_ejecutada = False
        for tarea in tareas_ordenadas:
            if tarea.get_fecha_programada() == fecha:
                print(f"El trabajador {trabajador.get_nombre()} realizó la tarea {tarea.get_id_tarea()} {tarea.get_descripcion()} con herramienta: {herramienta.get_nombre()}")
                tarea.set_completada(True)
                tarea_ejecutada = True
        return tarea_ejecutada

    def asignar_apto_medico(self, trabajador: Trabajador, apto: bool, fecha_emision: date, observaciones: str) -> None:
        trabajador.asignar_apto_medico(apto, fecha_emision, observaciones)
        print(f"Apto médico actualizado para: {trabajador.get_nombre()}")


