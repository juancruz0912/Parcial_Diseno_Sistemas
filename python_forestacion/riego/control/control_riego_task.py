import threading
import time
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUMEDAD_MAX_RIEGO

# Forward declarations for type hinting to avoid circular imports
# These will be resolved at runtime when the actual classes are imported
# from servicios.terrenos.plantacion_service import PlantacionService
# from riego.sensores.humedad_reader_task import HumedadReaderTask
# from riego.sensores.temperatura_reader_task import TemperaturaReaderTask

class ControlRiegoTask(threading.Thread):
    def __init__(self, temp_task, hum_task, finca: Plantacion, plantacion_service):
        super().__init__()
        self._temp_task = temp_task
        self._hum_task = hum_task
        self._finca = finca
        self._plantacion_service = plantacion_service
        self._ejecutando = True

    def run(self):
        while self._ejecutando:
            try:
                temp = self._temp_task.get_ultima_temperatura()
                hum = self._hum_task.get_ultima_humedad()

                if temp is not None and hum is not None:
                    if TEMP_MIN_RIEGO <= temp <= TEMP_MAX_RIEGO and hum < HUMEDAD_MAX_RIEGO:
                        self._plantacion_service.regar(self._finca)

                time.sleep(2.5)  # 2500 ms = 2.5 segundos
            except AguaAgotadaException as e:
                print(e.get_full_message())
                print("Sistema de riego detenido automáticamente por falta de agua.")
                self._ejecutando = False
                break
            except Exception as e:
                print(f"Error inesperado en ControlRiegoTask: {e}")
                self._ejecutando = False
                break

    def detener(self):
        self._ejecutando = False
