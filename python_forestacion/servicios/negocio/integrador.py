"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\negocio
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\negocio\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\negocio\fincas_service.py
# ================================================================================

import time
from typing import List, TypeVar, Type

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Forward declaration for PlantacionService to avoid circular imports
# from servicios.terrenos.plantacion_service import PlantacionService

T = TypeVar('T', bound=Cultivo)

class FincasService:
    def __init__(self, plantacion_service, cultivo_service_registry: CultivoServiceRegistry):
        self._fincas: List[RegistroForestal] = []
        self._plantacion_service = plantacion_service
        self._cultivo_service_registry = cultivo_service_registry

    def add_finca(self, finca: RegistroForestal) -> None:
        self._fincas.append(finca)

    def remover_finca(self, finca: RegistroForestal) -> None:
        self._fincas.remove(finca)

    def fumigar(self, id_finca: int, insecticida: str) -> None:
        for finca_registro in self._fincas:
            if finca_registro.get_plantacion().get_id() == id_finca:
                for cultivo in finca_registro.get_plantacion().get_cultivos():
                    print("Se esta fumigando el cultivo:")
                    self._mostrar_datos_cultivo(cultivo)
                    print(f"Con el insecticida: {insecticida}")

    def regar(self) -> None:
        for finca_registro in self._fincas:
            temp_task = TemperaturaReaderTask()
            hum_task = HumedadReaderTask()
            control_task = ControlRiegoTask(
                temp_task, hum_task, finca_registro.get_plantacion(), self._plantacion_service
            )

            temp_task.start()
            hum_task.start()
            control_task.start()

            # Let it run for a while (e.g., 20 seconds as in Java example)
            time.sleep(20)

            # Stop all threads
            temp_task.detener()
            hum_task.detener()
            control_task.detener()

            # Wait for threads to finish (optional, but good practice)
            temp_task.join()
            hum_task.join()
            control_task.join()

    def cosechar_y_empaquetar(self, tipo_cultivo: Type[T]) -> Paquete[T]:
        caja = Paquete[tipo_cultivo]()

        for finca_registro in self._fincas:
            for cultivo in finca_registro.get_plantacion().get_cultivos():
                if isinstance(cultivo, tipo_cultivo):
                    caja.add_item(cultivo)
            # Assuming plantacionService.consumir removes the harvested crops from the plantation
            self._plantacion_service.consumir(finca_registro.get_plantacion(), tipo_cultivo)
            print(f"Se cosecharon los/las {tipo_cultivo.__name__}s de la finca {finca_registro.get_plantacion().get_nombre()}")
        return caja

    def _mostrar_datos_cultivo(self, cultivo: Cultivo) -> None:
        self._cultivo_service_registry.mostrar_datos(cultivo)


# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\negocio\paquete.py
# ================================================================================

from typing import List, Generic, TypeVar
from python_forestacion.entidades.cultivos.cultivo import Cultivo

T = TypeVar('T', bound=Cultivo)

class Paquete(Generic[T]):
    def __init__(self):
        self._id = None  # Java's id was not initialized in constructor, so making it optional
        self._productos: List[T] = []

    def add_item(self, producto: T) -> None:
        self._productos.append(producto)

    def get_items(self) -> List[T]:
        return self._productos

    def mostrar_contenido_caja(self) -> None:
        print("CONTENIDO DE LA CAJA")
        print("____________________")
        for c in self.get_items():
            print(f"Cultivo: {c.__class__.__name__}")


