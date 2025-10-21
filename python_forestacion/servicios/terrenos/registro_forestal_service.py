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
