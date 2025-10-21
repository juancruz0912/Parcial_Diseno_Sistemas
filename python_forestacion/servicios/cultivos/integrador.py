"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\arbol_service.py
# ================================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class ArbolService(CultivoService):
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        super().__init__(estrategia_absorcion)

    def crecer(self, arbol: Arbol, incremento: float) -> bool:
        if 0 < incremento < 1:
            arbol.set_altura(arbol.get_altura() + incremento)
            self._consumir_agua_por_crecimiento(arbol)
            return True
        return False

    def _consumir_agua_por_crecimiento(self, arbol: Arbol) -> None:
        if arbol.get_agua() > 0:
            arbol.set_agua(arbol.get_agua() - 1)


# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\cultivo_service.py
# ================================================================================

from datetime import date
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class CultivoService:
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        self._estrategia_absorcion = estrategia_absorcion

    def mostrar_datos(self, cultivo: Cultivo):
        print(f"Cultivo: {cultivo.__class__.__name__}")
        print(f"Superficie: {cultivo.get_superficie():.2f} m²")
        print(f"Agua almacenada: {cultivo.get_agua()} L")

    def absorver_agua(self, cultivo: Cultivo, fecha: date, temperatura: float, humedad: float) -> int:
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(fecha, temperatura, humedad, cultivo)
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida


# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ================================================================================

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



# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\lechuga_service.py
# ================================================================================

from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

class LechugaService(CultivoService):
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(1))

    def cosechar(self, lechuga: Lechuga) -> bool:
        # Lechuga can be harvested all year round
        print("Se ha cosechado esta lechuga")
        return True
        print("Desarrollando semilla de lechuga")

    def absorver_agua(self, lechuga: Lechuga) -> int:
        lechuga.set_agua(lechuga.get_agua() + 1)
        return 1

    def consumir_agua(self, lechuga: Lechuga) -> int:
        lechuga.set_agua(lechuga.get_agua() - 1)
        return 1

    def mostrar_datos(self, lechuga: Lechuga) -> None:
        print(f"Cultivo: {lechuga.__class__.__name__}")
        print(f"Variedad: {lechuga.get_variedad()}")


# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\olivo_service.py
# ================================================================================

from datetime import date
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class OlivoService(ArbolService):
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

    def cosechar(self, olivo: Olivo) -> bool:
        mes = date.today().month
        if 5 <= mes <= 7:
            print("Se ha cosechado este olivo")
            return True
        return False

    def florecer(self, olivo: Olivo) -> bool:
        mes = date.today().month
        return 9 <= mes <= 12

    def absorver_agua(self, olivo: Olivo) -> int:
        mes = date.today().month
        agua_absorvida = 0

        if mes in [1, 2, 3, 4, 9, 10, 11, 12]:
            agua_absorvida = 1

        olivo.set_agua(olivo.get_agua() + agua_absorvida)
        return agua_absorvida

    def consumir_agua(self, olivo: Olivo) -> int:
        mes = date.today().month
        agua_consumida = 0

        if mes in [1, 2, 3, 4, 9, 10, 11, 12]:
            agua_consumida = 2
            self.crecer(olivo, 0.01)
        elif mes in [5, 6, 7, 8]:
            agua_consumida = 1

        olivo.set_agua(olivo.get_agua() - agua_consumida)
        return agua_consumida

    def mostrar_datos(self, olivo: Olivo) -> None:
        print(f"Cultivo {olivo.__class__.__name__}")
        print(f"Fruto: {olivo.get_tipo_aceituna().name}")
        print(f"Altura: {olivo.get_altura()}")


# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\pino_service.py
# ================================================================================

from datetime import date
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy

class PinoService(ArbolService):
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

    def cosechar(self, pino: Pino) -> bool:
        # Pino can be harvested all year round
        print("Se ha cosechado este pino")
        return True

    def secretar_resina(self, pino: Pino) -> None:
        print("Estoy secretando resina")

    def florecer(self, pino: Pino) -> bool:
        mes = date.today().month
        return 9 <= mes <= 12

    def absorver_agua(self, pino: Pino) -> int:
        mes = date.today().month
        agua_absorvida = 0

        if mes in [1, 2, 3, 4, 9, 10, 11, 12]:
            agua_absorvida = 2

        pino.set_agua(pino.get_agua() + agua_absorvida)
        return agua_absorvida

    def consumir_agua(self, pino: Pino) -> int:
        mes = date.today().month
        agua_consumida = 0

        if mes in [1, 2, 3, 4, 9, 10, 11, 12]:
            agua_consumida = 2
            self.crecer(pino, 0.10)
        elif mes in [5, 6, 7, 8]:
            agua_consumida = 1

        pino.set_agua(pino.get_agua() - agua_consumida)
        return agua_consumida

    def mostrar_datos(self, pino: Pino) -> None:
        print(f"Cultivo {pino.__class__.__name__}")
        print(f"Variedad: {pino.get_variedad()}")
        print(f"Altura: {pino.get_altura()}")


# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\zanahoria_service.py
# ================================================================================

from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

class ZanahoriaService(CultivoService):
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))

    def cosechar(self, zanahoria: Zanahoria) -> bool:
        # Zanahoria can be harvested all year round
        print("Se ha cosechado esta zanahoria")
        return True


