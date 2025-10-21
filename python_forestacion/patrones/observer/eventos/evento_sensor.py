from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventoSensor:
    """
    Representa un evento de lectura de un sensor.
    """
    tipo_sensor: str
    valor: float
    timestamp: datetime