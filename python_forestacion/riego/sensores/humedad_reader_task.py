import threading
import time
import random

class HumedadReaderTask(threading.Thread):
    def __init__(self):
        super().__init__()
        self._ultima_humedad = float('nan')
        self._ejecutando = True

    def run(self):
        while self._ejecutando:
            try:
                self._ultima_humedad = self._leer_sensor()
                print(f"[Humedad] {self._ultima_humedad:.2f} % ")
                time.sleep(3)  # simula muestreo
            except Exception as e:
                print(f"Error inesperado en HumedadReaderTask: {e}")
                break

    def _leer_sensor(self) -> float:
        return random.uniform(0, 100)  # entre 0% y 100%

    def get_ultima_humedad(self) -> float:
        return self._ultima_humedad

    def detener(self):
        self._ejecutando = False
