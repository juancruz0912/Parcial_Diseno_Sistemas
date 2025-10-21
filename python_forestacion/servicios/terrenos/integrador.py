"""
Archivo integrador generado automaticamente
Directorio: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\terrenos
Fecha: 2025-10-21 19:37:21
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\terrenos\plantacion_service.py
# ================================================================================

from typing import List, Type, TypeVar
from datetime import date

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.terrenos.plantacion import Plantacion

from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException

from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory

from python_forestacion.constantes import AGUA_MINIMA

T = TypeVar('T', bound=Cultivo)

class PlantacionService:
    """Servicio para la gestión de plantaciones y sus cultivos.

    Encapsula la lógica de negocio relacionada con la plantación, riego y consumo de cultivos.
    """
    def __init__(self, cultivo_service_registry: CultivoServiceRegistry):
        """Inicializa una nueva instancia de PlantacionService.

        Args:
            cultivo_service_registry (CultivoServiceRegistry): El registro de servicios de cultivo para el dispatch polimórfico.
        """
        self._cultivo_service_registry = cultivo_service_registry

    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int) -> bool:
        """Planta una cantidad específica de cultivos de una especie dada en una plantación.

        Args:
            plantacion (Plantacion): La plantación donde se realizará la siembra.
            especie (str): La especie del cultivo a plantar (e.g., "Pino", "Lechuga").
            cantidad (int): La cantidad de cultivos a plantar.

        Returns:
            bool: True si la plantación fue exitosa.

        Raises:
            ValueError: Si la especie de cultivo no es reconocida por la fábrica.
            SuperficieInsuficienteException: Si no hay suficiente superficie disponible en la plantación.
        """
        superficie_ocupada = sum(c.get_superficie() for c in plantacion.get_cultivos_interno())
        sup_disponible = plantacion.get_situada_en().get_superficie() - superficie_ocupada

        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)

            superficie_requerida = cultivo.get_superficie()
            sup_disponible -= superficie_requerida

            if sup_disponible >= 0:
                plantacion.get_cultivos_interno().append(cultivo)
                print(f"Se plantó un/a: {cultivo.__class__.__name__}")
            else:
                raise SuperficieInsuficienteException(
                    cultivo.__class__.__name__,
                    superficie_requerida,
                    sup_disponible + superficie_requerida
                )
        return True

    def regar(self, plantacion: Plantacion) -> bool:
        """Riega todos los cultivos en una plantación, distribuyendo agua según la estrategia de cada cultivo.

        Args:
            plantacion (Plantacion): La plantación a regar.

        Returns:
            bool: True si el riego fue exitoso.

        Raises:
            AguaAgotadaException: Si no hay suficiente agua disponible en la plantación para el riego.
        """
        print(f"Regando finca: {plantacion.get_nombre()}")

        # For now, use dummy values for temperature and humidity
        # In a real scenario, these would come from the ControlRiegoTask or directly from sensors
        current_date = date.today()
        current_temperature = 25.0 # Dummy value
        current_humidity = 60.0 # Dummy value

        for cultivo in plantacion.get_cultivos_interno():
            agua_actual = plantacion.get_agua_disponible()

            if agua_actual > AGUA_MINIMA:
                agua_absorvida = self._absorver_agua_cultivo(cultivo, current_date, current_temperature, current_humidity)
                plantacion.set_agua_disponible(agua_actual - agua_absorvida)
            else:
                raise AguaAgotadaException(agua_actual, AGUA_MINIMA)
        return True

    def _absorver_agua_cultivo(self, cultivo: Cultivo, fecha: date, temperatura: float, humedad: float) -> int:
        """Delega la absorción de agua a la estrategia de absorción del cultivo a través del registro de servicios.

        Args:
            cultivo (Cultivo): El cultivo que absorberá el agua.
            fecha (date): La fecha actual para cálculos estacionales.
            temperatura (float): La temperatura actual.
            humedad (float): La humedad actual.

        Returns:
            int: La cantidad de agua absorbida por el cultivo.
        """
        return self._cultivo_service_registry.absorber_agua(cultivo, fecha, temperatura, humedad)

    def consumir(self, plantacion: Plantacion, tipo_cultivo: Type[T]) -> bool:
        """Consume (elimina) todos los cultivos de un tipo específico de la plantación.

        Args:
            plantacion (Plantacion): La plantación de la cual consumir cultivos.
            tipo_cultivo (Type[T]): El tipo de cultivo a consumir.

        Returns:
            bool: True si se consumió al menos un cultivo, False en caso contrario.
        """
        # Create a new list to hold crops that are not consumed
        cultivos_restantes = []
        consumidos = False
        for cult in plantacion.get_cultivos_interno():
            if not isinstance(cult, tipo_cultivo):
                cultivos_restantes.append(cult)
            else:
                consumidos = True
        plantacion.set_cultivos(cultivos_restantes)
        return consumidos


# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ================================================================================

import os
import pickle
from typing import Type

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.excepciones import mensajes_exception
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

class RegistroForestalService:
    def __init__(self, cultivo_service_registry: CultivoServiceRegistry):
        self._cultivo_service_registry = cultivo_service_registry

    def mostrar_datos(self, registro: RegistroForestal) -> None:
        print("REGISTRO FORESTAL")
        print("=================")
        print(f"Padrón:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avalúo:      {registro.get_avaluo()}")
        print(f"Domicilio:   {registro.get_tierra().get_domicilio()}")
        print(f"Superficie: {registro.get_tierra().get_superficie()}")
        print(f"Cantidad de cultivos plantados: {len(registro.get_plantacion().get_cultivos())}")
        print("Listado de Cultivos plantados")
        print("____________________________")

        for cultivo in registro.get_plantacion().get_cultivos():
            self._mostrar_datos_cultivo(cultivo)

    def _mostrar_datos_cultivo(self, cultivo: Cultivo) -> None:
        self._cultivo_service_registry.mostrar_datos(cultivo)

    def persistir(self, registro: RegistroForestal) -> None:
        data_dir = "data"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        nombre_archivo = os.path.join(data_dir, f"{registro.get_propietario()}.dat")

        try:
            with open(nombre_archivo, 'wb') as f:
                pickle.dump(registro, f)
            print(mensajes_exception.get_persistencia_exitosa_message(registro.get_propietario()))
        except FileNotFoundError as e:
            raise PersistenciaException(
                mensajes_exception.ERROR_CODE_03,
                mensajes_exception.ERROR_03_ARCHIVO_NO_ENCONTRADO_ESCRITURA,
                tipo_operacion="ESCRITURA",
                cause=e
            ) from e
        except IOError as e:
            raise PersistenciaException(
                mensajes_exception.ERROR_CODE_04,
                mensajes_exception.ERROR_04_IO_ESCRITURA,
                tipo_operacion="ESCRITURA",
                cause=e
            ) from e
        except Exception as e:
            raise PersistenciaException(
                mensajes_exception.ERROR_CODE_00,
                mensajes_exception.ERROR_00_NO_IDENTIFICADO,
                tipo_operacion="ESCRITURA",
                cause=e
            ) from e

    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        if not propietario or propietario.strip() == "":
            raise ValueError("El nombre del propietario no puede ser nulo o vacío")

        data_dir = "data"
        nombre_archivo = os.path.join(data_dir, f"{propietario}.dat")

        try:
            with open(nombre_archivo, 'rb') as f:
                registro = pickle.load(f)
            print(mensajes_exception.get_lectura_exitosa_message(propietario))
            return registro
        except FileNotFoundError as e:
            raise PersistenciaException(
                mensajes_exception.ERROR_CODE_05,
                mensajes_exception.ERROR_05_ARCHIVO_NO_ENCONTRADO_LECTURA,
                tipo_operacion="LECTURA",
                cause=e
            ) from e
        except (IOError, EOFError, pickle.UnpicklingError) as e:
            raise PersistenciaException(
                mensajes_exception.ERROR_CODE_06,
                mensajes_exception.ERROR_06_IO_LECTURA,
                tipo_operacion="LECTURA",
                cause=e
            ) from e
        except Exception as e:
            raise PersistenciaException(
                mensajes_exception.ERROR_CODE_00,
                mensajes_exception.ERROR_00_NO_IDENTIFICADO,
                tipo_operacion="LECTURA",
                cause=e
            ) from e


# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\terrenos\tierra_service.py
# ================================================================================

from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.tierra import Tierra

class TierraService:
    def crear_tierra_con_plantacion(self, id_padron_catastral: int, superficie: float,
                                   domicilio: str, nombre_plantacion: str) -> Tierra:
        tierra = Tierra(id_padron_catastral, superficie, domicilio)

        # Crear plantación asociada automáticamente
        # Hardcoded values for Plantacion as in Java example
        plantacion = Plantacion(1, nombre_plantacion, 100000, tierra)
        tierra.set_finca(plantacion)

        print(f"Tierra creada: {domicilio} con plantación: {nombre_plantacion}")
        return tierra


