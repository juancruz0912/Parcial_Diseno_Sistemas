import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable

class HumedadReaderTask(threading.Thread, Observable[float]):
    """Tarea en segundo plano para leer la humedad ambiental de forma continua.

    Actúa como un Observable en el patrón Observer, notificando a sus observadores
    cada vez que se lee una nueva humedad.
    """
    def __init__(self):
        """Inicializa una nueva instancia de HumedadReaderTask.
        """
        threading.Thread.__init__(self)
        Observable.__init__(self)
        self.daemon = True # Set as daemon thread
        self._ultima_humedad = float('nan')
        self._stop_event = threading.Event() # Event for graceful shutdown

    def run(self):
        """Método principal del hilo que lee la humedad y notifica a los observadores.
        """
        while not self._stop_event.is_set():
            try:
                self._ultima_humedad = self._leer_sensor()
                print(f"[Humedad] {self._ultima_humedad:.2f} % ")
                self.notificar_observadores(self._ultima_humedad) # Notify observers
                time.sleep(3)  # simula muestreo
            except Exception as e:
                print(f"Error inesperado en HumedadReaderTask: {e}")
                break

    def _leer_sensor(self) -> float:
        """Simula la lectura de un sensor de humedad.

        Returns:
            float: Un valor de humedad aleatorio entre 0 y 100 %.
        """
        return random.uniform(0, 100)  # entre 0% y 100%

    def get_ultima_humedad(self) -> float:
        """Obtiene la última humedad leída por el sensor.

        Returns:
            float: La última humedad leída.
        """
        return self._ultima_humedad

    def detener(self):
        """Detiene la ejecución del hilo de lectura de humedad de forma segura.
        """
        self._stop_event.set()
