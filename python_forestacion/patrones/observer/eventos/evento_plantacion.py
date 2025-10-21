from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventoPlantacion:
    """
    Representa un evento que ocurre en una plantación.
    """
    mensaje: str
    timestamp: datetime