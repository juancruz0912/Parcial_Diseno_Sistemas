import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable

class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """Tarea en segundo plano para leer la temperatura ambiental de forma continua.

    Actúa como un Observable en el patrón Observer, notificando a sus observadores
    cada vez que se lee una nueva temperatura.
    """
    def __init__(self):
        """Inicializa una nueva instancia de TemperaturaReaderTask.
        """
        threading.Thread.__init__(self)
        Observable.__init__(self)
        self.daemon = True # Set as daemon thread
        self._ultima_temperatura = float('nan')
        self._stop_event = threading.Event() # Event for graceful shutdown

    def run(self):
        """Método principal del hilo que lee la temperatura y notifica a los observadores.
        """
        while not self._stop_event.is_set():
            try:
                self._ultima_temperatura = self._leer_sensor()
                print(f"[Temperatura] {self._ultima_temperatura:.2f} °C")
                self.notificar_observadores(self._ultima_temperatura) # Notify observers
                time.sleep(2)  # simula muestreo
            except Exception as e:
                print(f"Error inesperado en TemperaturaReaderTask: {e}")
                break

    def _leer_sensor(self) -> float:
        """Simula la lectura de un sensor de temperatura.

        Returns:
            float: Un valor de temperatura aleatorio entre -25 y 50 °C.
        """
        return random.uniform(-25, 50)  # entre -25 y 50 °C

    def get_ultima_temperatura(self) -> float:
        """Obtiene la última temperatura leída por el sensor.

        Returns:
            float: La última temperatura leída.
        """
        return self._ultima_temperatura

    def detener(self):
        """Detiene la ejecución del hilo de lectura de temperatura de forma segura.
        """
        self._stop_event.set()
