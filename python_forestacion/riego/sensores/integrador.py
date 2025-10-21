"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\riego\sensores
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\riego\sensores\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\riego\sensores\humedad_reader_task.py
# ================================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor


class HumedadReaderTask(threading.Thread, Observable[EventoSensor]):
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


# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\riego\sensores\temperatura_reader_task.py
# ================================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor


class TemperaturaReaderTask(threading.Thread, Observable[EventoSensor]):
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


