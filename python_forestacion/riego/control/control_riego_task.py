import threading
import time
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUMEDAD_MAX_RIEGO
from python_forestacion.patrones.observer.observable import Observer
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

class ControlRiegoTask(threading.Thread, Observer[EventoSensor]):
    """Tarea en segundo plano que controla el sistema de riego de forma automática.

    Actúa como un Observer, reaccionando a las actualizaciones de temperatura y humedad
    para decidir cuándo regar la plantación.
    """
    def __init__(self, temp_task, hum_task, finca: Plantacion, plantacion_service):
        """Inicializa una nueva instancia de ControlRiegoTask.

        Args:
            temp_task: La tarea de lectura de temperatura (Observable).
            hum_task: La tarea de lectura de humedad (Observable).
            finca (Plantacion): La plantación a controlar.
            plantacion_service: El servicio de plantación para realizar el riego.
        """
        threading.Thread.__init__(self)
        Observer.__init__(self)
        self.daemon = True # Set as daemon thread
        self._temp_task = temp_task
        self._hum_task = hum_task
        self._finca = finca
        self._plantacion_service = plantacion_service
        self._stop_event = threading.Event() # Event for graceful shutdown
        self._ultima_temperatura = float('nan')
        self._ultima_humedad = float('nan')

        # Register as observer to sensor tasks
        self._temp_task.agregar_observador(self)
        self._hum_task.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """Actualiza la última temperatura o humedad recibida de un sensor.

        Este método es llamado por los Observables (sensores) cuando hay una nueva lectura.

        Args:
            evento (float): El valor de la temperatura o humedad notificado.
        """
        # This method will be called by the Observable (sensor tasks)
        # We need to determine if the event is temperature or humidity
        # A more robust solution would involve a custom Event object or separate observers
        # For now, we'll assume the last updated value is the one we care about.
        # This is a simplification for the current context.
        # A better approach would be to pass a tuple (sensor_type, value) or use a dedicated event class.
        # For this implementation, we'll check if the event matches the last known value from each sensor.
        if self._temp_task.get_ultima_temperatura() == evento: # Check if it's a temperature update
            self._ultima_temperatura = evento
        elif self._hum_task.get_ultima_humedad() == evento: # Check if it's a humidity update
            self._ultima_humedad = evento

    def run(self):
        """Método principal del hilo que evalúa las condiciones y activa el riego.
        """
        while not self._stop_event.is_set():
            try:
                # Use the last updated values from the sensors
                temp = self._ultima_temperatura
                hum = self._ultima_humedad

                if not (temp == float('nan') or hum == float('nan')):
                    if TEMP_MIN_RIEGO <= temp <= TEMP_MAX_RIEGO and hum < HUMEDAD_MAX_RIEGO:
                        self._plantacion_service.regar(self._finca)

                self._stop_event.wait(2.5)  # Check conditions every 2.5 seconds, allows faster shutdown
            except AguaAgotadaException as e:
                print(e.get_full_message())
                print("Sistema de riego detenido automáticamente por falta de agua.")
                self._stop_event.set()
                break
            except Exception as e:
                print(f"Error inesperado en ControlRiegoTask: {e}")
                self._stop_event.set()
                break

    def detener(self):
        """Detiene la ejecución del hilo de control de riego de forma segura.
        """
        self._stop_event.set()
        # Unregister from observers to clean up
        self._temp_task.eliminar_observador(self)
        self._hum_task.eliminar_observador(self)
