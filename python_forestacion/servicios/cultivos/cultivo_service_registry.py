from typing import Callable, Dict
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
    def __init__(self, pino_service: PinoService,
                 olivo_service: OlivoService,
                 lechuga_service: LechugaService,
                 zanahoria_service: ZanahoriaService):
        self._pino_service = pino_service
        self._olivo_service = olivo_service
        self._lechuga_service = lechuga_service
        self._zanahoria_service = zanahoria_service

        self._absorber_agua_handlers: Dict[type, Callable[[Cultivo], int]] = {}
        self._mostrar_datos_handlers: Dict[type, Callable[[Cultivo], None]] = {}

        # Register handlers for absorbing water
        self._absorber_agua_handlers[Pino] = lambda c: self._pino_service.absorver_agua(c)
        self._absorber_agua_handlers[Olivo] = lambda c: self._olivo_service.absorver_agua(c)
        self._absorber_agua_handlers[Lechuga] = lambda c: self._lechuga_service.absorver_agua(c)
        self._absorber_agua_handlers[Zanahoria] = lambda c: self._zanahoria_service.absorver_agua(c)

        # Register handlers for displaying data
        self._mostrar_datos_handlers[Pino] = lambda c: self._pino_service.mostrar_datos(c)
        self._mostrar_datos_handlers[Olivo] = lambda c: self._olivo_service.mostrar_datos(c)
        self._mostrar_datos_handlers[Lechuga] = lambda c: self._lechuga_service.mostrar_datos(c)
        self._mostrar_datos_handlers[Zanahoria] = lambda c: self._zanahoria_service.mostrar_datos(c)

    def absorber_agua(self, cultivo: Cultivo) -> int:
        handler = self._absorber_agua_handlers.get(cultivo.__class__)
        if handler is None:
            raise ValueError(f"No hay servicio registrado para: {cultivo.__class__.__name__}")
        return handler(cultivo)

    def mostrar_datos(self, cultivo: Cultivo) -> None:
        handler = self._mostrar_datos_handlers.get(cultivo.__class__)
        if handler is None:
            raise ValueError(f"No hay servicio registrado para: {cultivo.__class__.__name__}")
        handler(cultivo)
