from typing import Callable, Dict
from threading import Lock
from datetime import date

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

class CultivoServiceRegistry:
    """Implementa el patrón Singleton para gestionar y despachar servicios de cultivo.

    Este registro centraliza la lógica para obtener el servicio correcto para un tipo de cultivo
    dado, eliminando la necesidad de cascadas de `isinstance()`.
    """
    _instance = None
    _lock = Lock()

    def __new__(cls):
        """Controla la creación de la instancia única del Singleton.

        Garantiza que solo se cree una instancia de `CultivoServiceRegistry` de forma thread-safe.
        """
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    def _inicializar_servicios(self):
        """Inicializa los servicios de cultivo y registra sus handlers.

        Este método se llama una única vez durante la creación de la instancia Singleton.
        """
        # Crear servicios de cultivos individuales
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        self._absorber_agua_handlers: Dict[type, Callable[[Cultivo, date, float, float], int]] = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }
        self._mostrar_datos_handlers: Dict[type, Callable[[Cultivo], None]] = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

    @classmethod
    def get_instance(cls):
        """Obtiene la instancia única de CultivoServiceRegistry.

        Returns:
            CultivoServiceRegistry: La instancia única del registro de servicios.
        """
        if cls._instance is None:
            cls() # This will call __new__ and initialize the instance
        return cls._instance

    def absorber_agua(self, cultivo: Cultivo, fecha: date, temperatura: float, humedad: float) -> int:
        """Despacha la llamada para que un cultivo absorba agua al servicio correspondiente.

        Args:
            cultivo (Cultivo): El cultivo que absorberá el agua.
            fecha (date): La fecha actual para cálculos estacionales.
            temperatura (float): La temperatura actual.
            humedad (float): La humedad actual.

        Returns:
            int: La cantidad de agua absorbida por el cultivo.

        Raises:
            ValueError: Si no hay un servicio registrado para el tipo de cultivo dado.
        """
        handler = self._absorber_agua_handlers.get(cultivo.__class__)
        if handler is None:
            raise ValueError(f"No hay servicio registrado para: {cultivo.__class__.__name__}")
        return handler(cultivo, fecha, temperatura, humedad)

    def mostrar_datos(self, cultivo: Cultivo) -> None:
        """Despacha la llamada para mostrar los datos de un cultivo al servicio correspondiente.

        Args:
            cultivo (Cultivo): El cultivo cuyos datos se mostrarán.

        Raises:
            ValueError: Si no hay un servicio registrado para el tipo de cultivo dado.
        """
        handler = self._mostrar_datos_handlers.get(cultivo.__class__)
        if handler is None:
            raise ValueError(f"No hay servicio registrado para: {cultivo.__class__.__name__}")
        handler(cultivo)

    # Dedicated handlers for absorber_agua (replacing lambdas)
    def _absorber_agua_pino(self, cultivo: Pino, fecha: date, temperatura: float, humedad: float) -> int:
        """Maneja la absorción de agua para un Pino."""
        return self._pino_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def _absorber_agua_olivo(self, cultivo: Olivo, fecha: date, temperatura: float, humedad: float) -> int:
        """Maneja la absorción de agua para un Olivo."""
        return self._olivo_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def _absorber_agua_lechuga(self, cultivo: Lechuga, fecha: date, temperatura: float, humedad: float) -> int:
        """Maneja la absorción de agua para una Lechuga."""
        return self._lechuga_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def _absorber_agua_zanahoria(self, cultivo: Zanahoria, fecha: date, temperatura: float, humedad: float) -> int:
        """Maneja la absorción de agua para una Zanahoria."""
        return self._zanahoria_service.absorver_agua(cultivo, fecha, temperatura, humedad)

    # Dedicated handlers for mostrar_datos (replacing lambdas)
    def _mostrar_datos_pino(self, cultivo: Pino) -> None:
        """Maneja la visualización de datos para un Pino."""
        self._pino_service.mostrar_datos(cultivo)

    def _mostrar_datos_olivo(self, cultivo: Olivo) -> None:
        """Maneja la visualización de datos para un Olivo."""
        self._olivo_service.mostrar_datos(cultivo)

    def _mostrar_datos_lechuga(self, cultivo: Lechuga) -> None:
        """Maneja la visualización de datos para una Lechuga."""
        self._lechuga_service.mostrar_datos(cultivo)

    def _mostrar_datos_zanahoria(self, cultivo: Zanahoria) -> None:
        """Maneja la visualización de datos para una Zanahoria."""
        self._zanahoria_service.mostrar_datos(cultivo)


    # The __init__ method is not needed for a Singleton that initializes in __new__
    # but if it exists, it should be a no-op or raise an error to prevent re-initialization.
    # For simplicity, we'll omit it as __new__ handles everything.
    # def __init__(self, *args, **kwargs):
    #     pass

