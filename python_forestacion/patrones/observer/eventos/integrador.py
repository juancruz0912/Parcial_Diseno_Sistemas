"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\observer\eventos
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\observer\eventos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: evento_plantacion.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\observer\eventos\evento_plantacion.py
# ================================================================================

from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventoPlantacion:
    """
    Representa un evento que ocurre en una plantación.
    """
    mensaje: str
    timestamp: datetime

# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\observer\eventos\evento_sensor.py
# ================================================================================

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

