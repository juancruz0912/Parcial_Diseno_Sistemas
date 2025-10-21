import threading
import time
import random

class TemperaturaReaderTask(threading.Thread):
    def __init__(self):
        super().__init__()
        self._ultima_temperatura = float('nan')
        self._ejecutando = True

    def run(self):
        while self._ejecutando:
            try:
                self._ultima_temperatura = self._leer_sensor()
                print(f"[Temperatura] {self._ultima_temperatura:.2f} °C")
                time.sleep(2)  # simula muestreo
            except Exception as e:
                print(f"Error inesperado en TemperaturaReaderTask: {e}")
                break

    def _leer_sensor(self) -> float:
        return random.uniform(-25, 50)  # entre -25 y 50 °C

    def get_ultima_temperatura(self) -> float:
        return self._ultima_temperatura

    def detener(self):
        self._ejecutando = False
