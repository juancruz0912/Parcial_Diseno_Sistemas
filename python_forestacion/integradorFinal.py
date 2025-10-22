"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion
Fecha de generacion: 2025-10-21 19:37:21
Total de archivos integrados: 67
Total de directorios procesados: 22
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================
# DIRECTORIO: ..
#   1. main.py

# DIRECTORIO: .
#   2. __init__.py
#   3. constantes.py
#
# DIRECTORIO: entidades
#   4. __init__.py
#
# DIRECTORIO: entidades\cultivos
#   5. __init__.py
#   6. arbol.py
#   7. cultivo.py
#   8. hortaliza.py
#   9. lechuga.py
#   10. olivo.py
#   11. pino.py
#   12. tipo_aceituna.py
#   13. zanahoria.py
#
# DIRECTORIO: entidades\personal
#   14. __init__.py
#   15. apto_medico.py
#   16. herramienta.py
#   17. tarea.py
#   18. trabajador.py
#
# DIRECTORIO: entidades\terrenos
#   19. __init__.py
#   20. plantacion.py
#   21. registro_forestal.py
#   22. tierra.py
#
# DIRECTORIO: excepciones
#   23. __init__.py
#   24. agua_agotada_exception.py
#   25. forestacion_exception.py
#   26. mensajes_exception.py
#   27. persistencia_exception.py
#   28. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   29. __init__.py
#
# DIRECTORIO: patrones\factory
#   30. __init__.py
#   31. cultivo_factory.py
#
# DIRECTORIO: patrones\observer
#   32. __init__.py
#   33. observable.py
#   34. observer.py
#
# DIRECTORIO: patrones\observer\eventos
#   35. __init__.py
#   36. evento_plantacion.py
#   37. evento_sensor.py
#
# DIRECTORIO: patrones\singleton
#   38. __init__.py
#
# DIRECTORIO: patrones\strategy
#   39. __init__.py
#   40. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones\strategy\impl
#   41. __init__.py
#   42. absorcion_constante_strategy.py
#   43. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   44. __init__.py
#
# DIRECTORIO: riego\control
#   45. __init__.py
#   46. control_riego_task.py
#
# DIRECTORIO: riego\sensores
#   47. __init__.py
#   48. humedad_reader_task.py
#   49. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   50. __init__.py
#
# DIRECTORIO: servicios\cultivos
#   51. __init__.py
#   52. arbol_service.py
#   53. cultivo_service.py
#   54. cultivo_service_registry.py
#   55. lechuga_service.py
#   56. olivo_service.py
#   57. pino_service.py
#   58. zanahoria_service.py
#
# DIRECTORIO: servicios\negocio
#   59. __init__.py
#   60. fincas_service.py
#   61. paquete.py
#
# DIRECTORIO: servicios\personal
#   62. __init__.py
#   63. trabajador_service.py
#
# DIRECTORIO: servicios\terrenos
#   64. __init__.py
#   65. plantacion_service.py
#   66. registro_forestal_service.py
#   67. tierra_service.py
#

################################################################################
# DIRECTORIO: ..
################################################################################

# ==============================================================================
# ARCHIVO 1/67: main.py
# Directorio: .
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\main.py
# ==============================================================================

import time
from datetime import date
from typing import List

# Entidades
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.terrenos.tierra import Tierra

# Excepciones
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException

# Riego
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask

# Servicios
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.terrenos.tierra_service import TierraService

def main():
    try:
        print("==============================================")
        print("EJEMPLO: PATRÓN ENTITY-SERVICE")
        print("==============================================\n")

        # ============================================
        # INICIALIZAR SERVICIOS (REFACTORIZADO: Dependency Injection)
        # ============================================

        # Obtener la instancia única del Registry Pattern (Singleton)
        cultivo_service_registry = CultivoServiceRegistry.get_instance()

        # Inyectar dependencias en servicios
        tierra_service = TierraService()
        plantacion_service = PlantacionService(cultivo_service_registry)
        registro_service = RegistroForestalService(cultivo_service_registry)
        trabajador_service = TrabajadorService()
        fincas_service = FincasService(plantacion_service, cultivo_service_registry)

        # ============================================
        # 1. CREAR TIERRA Y PLANTACIÓN (usando servicio)
        # ============================================
        print("1. Creando tierra con plantación...")

        terreno = tierra_service.crear_tierra_con_plantacion(
            1, 10000.0, "Agrelo, Mendoza", "Finca del Madero")
        plantacion = terreno.get_finca()

        # ============================================
        # 2. CREAR REGISTRO FORESTAL
        # ============================================
        print("\n2. Creando registro forestal...")
        registro = RegistroForestal(
            1, terreno, plantacion, "Juan Perez", 50309233.55)

        # ============================================
        # 3. PLANTAR CULTIVOS (usando servicio)
        # ============================================
        print("\n3. Plantando cultivos...")
        plantacion_service.plantar(plantacion, "Pino", 5)
        plantacion_service.plantar(plantacion, "Olivo", 5)
        plantacion_service.plantar(plantacion, "Lechuga", 5)
        plantacion_service.plantar(plantacion, "Zanahoria", 5)

        # ============================================
        # 4. SISTEMA DE RIEGO AUTOMATIZADO
        # ============================================
        print("\n4. Iniciando sistema de riego automatizado...")
        tarea_temp = TemperaturaReaderTask()
        tarea_hum = HumedadReaderTask()
        tarea_control = ControlRiegoTask(tarea_temp, tarea_hum, plantacion, plantacion_service)

        # Start threads
        tarea_temp.start()
        tarea_hum.start()
        tarea_control.start()

        # Allow irrigation to run for a bit (e.g., 5 seconds)
        time.sleep(5)

        # Detener sistema de riego
        print("\nDeteniendo sistema de riego...")
        tarea_temp.detener()
        tarea_hum.detener()
        tarea_control.detener()

        # Wait for threads to finish
        tarea_temp.join()
        tarea_hum.join()
        tarea_control.join()

        # ============================================
        # 5. GESTIÓN DE TRABAJADORES (usando servicio)
        # ============================================
        print("\n5. Gestionando trabajadores...")
        tareas: List[Tarea] = []
        tareas.append(Tarea(1, date.today(), "Desmalezar"))
        tareas.append(Tarea(2, date.today(), "Abonar"))
        tareas.append(Tarea(3, date.today(), "Marcar surcos"))

        trabajadores: List[Trabajador] = []
        trabajadores.append(Trabajador(43888734, "Juan Perez", tareas))
        trabajadores.append(Trabajador(40222333, "María López", tareas))

        plantacion.set_trabajadores(trabajadores)

        # Asignar apto médico explícitamente (usando servicio)
        print("\n5.1. Asignando apto médico a trabajadores...")
        trabajador_service.asignar_apto_medico(
            trabajadores[0],
            True,
            date.today(),
            "Estado de salud: excelente"
        )

        # Trabajador ejecuta tareas (usando servicio)
        print("\n5.2. Ejecutando tareas del trabajador...")
        trabajador_service.trabajar(
            trabajadores[0],
            date.today(),
            Herramienta(1, "Pala", True)
        )

        # ============================================
        # 6. SERVICIOS DE FINCAS (usando servicio)
        # ============================================
        print("\n6. Usando servicios de fincas...")
        fincas_service.add_finca(registro)

        # Fumigar
        fincas_service.fumigar(1, "insecto organico")

        # Cosechar y empaquetar (tipo-seguro)
        print("\n7. Cosechando cultivos...")
        caja1 = fincas_service.cosechar_y_empaquetar(Lechuga)
        caja1.mostrar_contenido_caja()

        caja2 = fincas_service.cosechar_y_empaquetar(Pino)
        caja2.mostrar_contenido_caja()

        # ============================================
        # 8. PERSISTENCIA (usando servicio)
        # ============================================
        print("\n8. Persistiendo registro...")
        registro_service.persistir(registro)

        # Leer registro
        print("\n9. Leyendo registro persistido...")
        registro_leido = RegistroForestalService.leer_registro("Juan Perez")
        registro_service.mostrar_datos(registro_leido)

        print("\n==============================================")
        print("EJEMPLO COMPLETADO EXITOSAMENTE")
        print("==============================================")

    except SuperficieInsuficienteException as e:
        print(f"\n{e.get_full_message()}")
        print(f"Detalles: {e.get_user_message()}")
        if e.get_superficie_requerida() > 0:
            print(f"  - Superficie requerida: {e.get_superficie_requerida():.2f} m²")
            print(f"  - Superficie disponible: {e.get_superficie_disponible():.2f} m²")
    except PersistenciaException as e:
        print(f"\n{e.get_full_message()}")
        print(f"Detalles: {e.get_user_message()}")
        print(f"Tipo de operación: {e.get_tipo_operacion()}")
        if e.cause is not None:
            print(f"Causa: {e.cause}")
    except ValueError as e:
        print(f"\nError de validación: {e}")
    except Exception as e:
        print("\nError inesperado del sistema")
        print(f"Mensaje: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 2/67: __init__.py
# Directorio: .
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 3/67: constantes.py
# Directorio: .
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\constantes.py
# ==============================================================================

from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

# Agua
AGUA_MINIMA = 10
AGUA_INICIAL_PLANTACION = 500

# Riego
TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50
MES_INICIO_VERANO = 12
MES_FIN_VERANO = 2

# Absorcion
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2

# Cultivos
SUPERFICIE_PINO = 2.0
AGUA_INICIAL_PINO = 2
PINO_DEFAULT_VARIEDAD = "cedro"
PINO_INITIAL_ALTURA = 1.0

AGUA_INICIAL_OLIVO = 5
SUPERFICIE_OLIVO = 3.0
OLIVO_DEFAULT_TIPO_ACEITUNA = TipoAceituna.NEGRA
OLIVO_INITIAL_ALTURA = 0.5

AGUA_INICIAL_ZANAHORIA = 0
SUPERFICIE_ZANAHORIA = 0.15
ZANAHORIA_DEFAULT_ES_BABY_CARROT = True

AGUA_INICIAL_LECHUGA = 1
SUPERFICIE_LECHUGA = 0.2
LECHUGA_DEFAULT_VARIEDAD = "Mantecosa"



################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 4/67: __init__.py
# Directorio: entidades
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 5/67: __init__.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 6/67: arbol.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\arbol.py
# ==============================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    _cant_arboles = 0

    def __init__(self, agua: int, superficie: float, altura: float):
        super().__init__(agua, superficie)
        Arbol._cant_arboles += 1
        self._id = Arbol._cant_arboles
        self._altura = altura

    def get_id(self) -> int:
        return self._id

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        self._altura = altura

    @staticmethod
    def get_cant_arboles() -> int:
        return Arbol._cant_arboles


# ==============================================================================
# ARCHIVO 7/67: cultivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\cultivo.py
# ==============================================================================

from abc import ABC

class Cultivo(ABC):
    EDAD_MAXIMA = 20

    def __init__(self, agua: int, superficie: float):
        self._agua = agua
        self._superficie = superficie

    def get_agua(self) -> int:
        return self._agua
    
    def set_agua(self, agua: int) -> None:
        self._agua = agua

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        self._superficie = superficie


# ==============================================================================
# ARCHIVO 8/67: hortaliza.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\hortaliza.py
# ==============================================================================

from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Hortaliza(Cultivo):
    def __init__(self, agua: int, superficie: float, invernadero: bool):
        super().__init__(agua, superficie)
        self._invernadero = invernadero

    def is_invernadero(self) -> bool:
        return self._invernadero

    def set_invernadero(self, invernadero: bool) -> None:
        self._invernadero = invernadero


# ==============================================================================
# ARCHIVO 9/67: lechuga.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\lechuga.py
# ==============================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA

class Lechuga(Hortaliza):
    def __init__(self, variedad: str):
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad


# ==============================================================================
# ARCHIVO 10/67: olivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\olivo.py
# ==============================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO, OLIVO_INITIAL_ALTURA

class Olivo(Arbol):
    def __init__(self, tipo_aceituna: TipoAceituna):
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=OLIVO_INITIAL_ALTURA
        )
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        return self._tipo_aceituna


# ==============================================================================
# ARCHIVO 11/67: pino.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\pino.py
# ==============================================================================

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO, PINO_INITIAL_ALTURA

class Pino(Arbol):
    """Representa un tipo de cultivo de pino, heredando de Arbol.

    Attributes:
        _variedad (str): La variedad específica del pino.
    """
    def __init__(self, variedad: str):
        """Inicializa una nueva instancia de Pino.

        Args:
            variedad (str): La variedad del pino (e.g., "Parana", "Elliott").
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=PINO_INITIAL_ALTURA
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Obtiene la variedad del pino.

        Returns:
            str: La variedad del pino.
        """
        return self._variedad


# ==============================================================================
# ARCHIVO 12/67: tipo_aceituna.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ==============================================================================

from enum import Enum

class TipoAceituna(Enum):
    NEGRA = "Negra"
    VERDE = "Verde"
    ROJA = "Roja"


# ==============================================================================
# ARCHIVO 13/67: zanahoria.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\cultivos\zanahoria.py
# ==============================================================================

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA

class Zanahoria(Hortaliza):
    def __init__(self, is_baby: bool):
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._is_baby = is_baby

    def is_baby_carrot(self) -> bool:
        return self._is_baby

    def set_is_baby(self, is_baby: bool) -> None:
        self._is_baby = is_baby



################################################################################
# DIRECTORIO: entidades\personal
################################################################################

# ==============================================================================
# ARCHIVO 14/67: __init__.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 15/67: apto_medico.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\personal\apto_medico.py
# ==============================================================================

from datetime import date

class AptoMedico:
    def __init__(self, apto: bool, fecha_emision: date, observaciones: str):
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def esta_apto(self) -> bool:
        return self._apto

    def set_apto(self, apto: bool) -> None:
        self._apto = apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def set_fecha_emision(self, fecha_emision: date) -> None:
        self._fecha_emision = fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones

    def set_observaciones(self, observaciones: str) -> None:
        self._observaciones = observaciones

    def get_resumen(self) -> str:
        return f"Apto: {self._apto} | Fecha: {self._fecha_emision} | Obs: {self._observaciones}"


# ==============================================================================
# ARCHIVO 16/67: herramienta.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\personal\herramienta.py
# ==============================================================================

class Herramienta:
    def __init__(self, id_herramienta: int, nombre: str, certificado_hys: bool):
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    def get_id_herramienta(self) -> int:
        return self._id_herramienta

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def is_certificado_hys(self) -> bool:
        return self._certificado_hys

    def set_certificado_hys(self, certificado_hys: bool) -> None:
        self._certificado_hys = certificado_hys


# ==============================================================================
# ARCHIVO 17/67: tarea.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\personal\tarea.py
# ==============================================================================

from datetime import date

class Tarea:
    def __init__(self, id_tarea: int, fecha_programada: date, descripcion: str):
        self._id_tarea = id_tarea
        self._fecha_programada = fecha_programada
        self._descripcion = descripcion
        self._completada = False

    def get_id_tarea(self) -> int:
        return self._id_tarea

    def set_id_tarea(self, id_tarea: int) -> None:
        self._id_tarea = id_tarea

    def get_fecha_programada(self) -> date:
        return self._fecha_programada

    def set_fecha_programada(self, fecha_programada: date) -> None:
        self._fecha_programada = fecha_programada

    def get_descripcion(self) -> str:
        return self._descripcion

    def set_descripcion(self, descripcion: str) -> None:
        self._descripcion = descripcion

    def is_completada(self) -> bool:
        return self._completada

    def set_completada(self, completada: bool) -> None:
        self._completada = completada


# ==============================================================================
# ARCHIVO 18/67: trabajador.py
# Directorio: entidades\personal
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\personal\trabajador.py
# ==============================================================================

from typing import List
from datetime import date
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico

class Trabajador:
    def __init__(self, dni: int, nombre: str, tareas: List[Tarea]):
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas.copy() if tareas else []
        self._apto_medico: AptoMedico = AptoMedico(True, date.today(), "Estado de salud: bueno")

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def get_tareas(self) -> List[Tarea]:
        return self._tareas.copy()

    def set_tareas(self, tareas: List[Tarea]) -> None:
        self._tareas = tareas.copy() if tareas else []

    def get_apto_medico(self) -> AptoMedico:
        return self._apto_medico

    def set_apto_medico(self, apto_medico: AptoMedico) -> None:
        self._apto_medico = apto_medico

    def asignar_apto_medico(self, apto: bool, fecha_emision: date, observaciones: str) -> None:
        self._apto_medico = AptoMedico(apto, fecha_emision, observaciones)



################################################################################
# DIRECTORIO: entidades\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 19/67: __init__.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 20/67: plantacion.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\terrenos\plantacion.py
# ==============================================================================

from typing import List
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.terrenos.tierra import Tierra

class Plantacion:
    def __init__(self, id: int, nombre: str, agua: int, tierra: Tierra):
        self._id = id
        self._nombre = nombre
        self._agua_disponible = agua
        self._situada_en = tierra
        self._cultivos: List[Cultivo] = []
        self._trabajadores: List[Trabajador] = []

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def get_id(self) -> int:
        return self._id

    def set_id(self, id: int) -> None:
        self._id = id

    def get_agua_disponible(self) -> int:
        return self._agua_disponible

    def set_agua_disponible(self, agua_disponible: int) -> None:
        if agua_disponible < 0:
            raise ValueError("El agua no puede ser negativa")
        self._agua_disponible = agua_disponible

    def get_situada_en(self) -> Tierra:
        return self._situada_en

    def set_situada_en(self, situada_en: Tierra) -> None:
        self._situada_en = situada_en

    def get_cultivos(self) -> List[Cultivo]:
        return self._cultivos.copy()

    def set_cultivos(self, cultivos: List[Cultivo]) -> None:
        self._cultivos = cultivos.copy() if cultivos else []

    def get_trabajadores(self) -> List[Trabajador]:
        return self._trabajadores.copy()

    def set_trabajadores(self, trabajadores: List[Trabajador]) -> None:
        self._trabajadores = trabajadores.copy() if trabajadores else []

    def get_cultivos_interno(self) -> List[Cultivo]:
        return self._cultivos

    def get_trabajadores_interno(self) -> List[Trabajador]:
        return self._trabajadores


# ==============================================================================
# ARCHIVO 21/67: registro_forestal.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\terrenos\registro_forestal.py
# ==============================================================================

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    def __init__(self, id_padron: int, tierra: Tierra, plantacion: Plantacion, propietario: str, avaluo: float):
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_padron(self) -> int:
        return self._id_padron

    def set_id_padron(self, id_padron: int) -> None:
        self._id_padron = id_padron

    def get_tierra(self) -> Tierra:
        return self._tierra

    def get_plantacion(self) -> Plantacion:
        return self._plantacion

    def get_propietario(self) -> str:
        return self._propietario

    def set_propietario(self, propietario: str) -> None:
        self._propietario = propietario

    def get_avaluo(self) -> float:
        return self._avaluo

    def set_avaluo(self, avaluo: float) -> None:
        self._avaluo = avaluo


# ==============================================================================
# ARCHIVO 22/67: tierra.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\entidades\terrenos\tierra.py
# ==============================================================================

class Tierra:
    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = None

    def get_id_padron_catastral(self) -> int:
        return self._id_padron_catastral

    def set_id_padron_catastral(self, id_padron_catastral: int) -> None:
        self._id_padron_catastral = id_padron_catastral

    def get_superficie(self) -> float:
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self._superficie = superficie

    def get_domicilio(self) -> str:
        return self._domicilio

    def set_domicilio(self, domicilio: str) -> None:
        self._domicilio = domicilio

    def get_finca(self):
        return self._finca

    def set_finca(self, finca) -> None:
        self._finca = finca



################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 23/67: __init__.py
# Directorio: excepciones
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/67: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\agua_agotada_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones import mensajes_exception

class AguaAgotadaException(ForestacionException):
    def __init__(self, agua_disponible: float = 0.0, agua_minima: float = 10.0):
        if agua_disponible == 0.0 and agua_minima == 10.0: # Default constructor
            super().__init__(
                mensajes_exception.ERROR_CODE_01,
                mensajes_exception.ERROR_01_AGUA_AGOTADA,
                mensajes_exception.ERROR_01_AGUA_AGOTADA_USER_MESSAGE
            )
        else:
            super().__init__(
                mensajes_exception.ERROR_CODE_01,
                mensajes_exception.ERROR_01_AGUA_AGOTADA,
                mensajes_exception.get_agua_agotada_detallado_message(agua_disponible, agua_minima)
            )
        self._agua_disponible = agua_disponible
        self._agua_minima = agua_minima

    def get_agua_disponible(self) -> float:
        return self._agua_disponible

    def get_agua_minima(self) -> float:
        return self._agua_minima


# ==============================================================================
# ARCHIVO 25/67: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\forestacion_exception.py
# ==============================================================================

class ForestacionException(Exception):
    """Excepción base para todos los errores específicos de la aplicación de forestación.

    Permite encapsular un código de error, un mensaje técnico, un mensaje para el usuario
    y la causa original de la excepción.
    """
    def __init__(self, error_code: str, message: str, user_message: str = None, cause: Exception = None):
        """Inicializa una nueva instancia de ForestacionException.

        Args:
            error_code (str): Código único que identifica el tipo de error.
            message (str): Mensaje técnico detallado de la excepción.
            user_message (str, optional): Mensaje amigable para el usuario. Si no se provee, usa `message`.
            cause (Exception, optional): La excepción original que causó esta excepción.
        """
        super().__init__(message)
        self._error_code = error_code
        self._user_message = user_message if user_message is not None else message
        self._cause = cause

    def get_error_code(self) -> str:
        """Obtiene el código de error de la excepción.

        Returns:
            str: El código de error.
        """
        return self._error_code

    def get_user_message(self) -> str:
        """Obtiene el mensaje amigable para el usuario de la excepción.

        Returns:
            str: El mensaje para el usuario.
        """
        return self._user_message

    def get_full_message(self) -> str:
        """Obtiene el mensaje completo de la excepción, incluyendo el código de error y el mensaje de usuario.

        Returns:
            str: El mensaje completo.
        """
        return f"{self._error_code} - {self._user_message}"

    def __str__(self) -> str:
        """Retorna la representación en cadena de la excepción.

        Returns:
            str: La representación en cadena de la excepción.
        """
        base_str = self.get_full_message()
        if self._cause:
            return f"{base_str} | Causa: {self._cause}"
        return base_str

    @property
    def cause(self) -> Exception:
        """Propiedad para acceder a la excepción original que causó esta excepción.

        Returns:
            Exception: La excepción original.
        """
        return self._cause


# ==============================================================================
# ARCHIVO 26/67: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\mensajes_exception.py
# ==============================================================================

# ============================================
# CÓDIGOS DE ERROR
# ============================================

ERROR_CODE_00 = "ERROR 00"
ERROR_CODE_01 = "ERROR 01"
ERROR_CODE_02 = "ERROR 02"
ERROR_CODE_03 = "ERROR 03"
ERROR_CODE_04 = "ERROR 04"
ERROR_CODE_05 = "ERROR 05"
ERROR_CODE_06 = "ERROR 06"
ERROR_CODE_07 = "ERROR 07"

# ============================================
# ERRORES GENERALES
# ============================================

ERROR_00_NO_IDENTIFICADO = "Se produjo un error no identificado en el sistema"

# ============================================
# ERRORES DE RIEGO Y AGUA
# ============================================

ERROR_01_AGUA_AGOTADA = "Se agotó el agua disponible en la finca"
ERROR_01_AGUA_AGOTADA_USER_MESSAGE = "No hay suficiente agua disponible para continuar el riego. Nivel de agua crítico."

def get_agua_agotada_detallado_message(agua_disponible: float, agua_minima: float) -> str:
    return f"Agua insuficiente para riego. Disponible: {agua_disponible:.2f} L, Mínimo requerido: {agua_minima:.2f} L"

# ============================================
# ERRORES DE SUPERFICIE Y PLANTACIÓN
# ============================================

ERROR_02_SUPERFICIE_INSUFICIENTE_PREFIX = "No se pudo plantar: "
ERROR_02_SUPERFICIE_INSUFICIENTE_SUFFIX = " porque no queda superficie disponible en la finca"

def get_superficie_insuficiente_message(cultivo: str) -> str:
    return ERROR_02_SUPERFICIE_INSUFICIENTE_PREFIX + cultivo + \
           ERROR_02_SUPERFICIE_INSUFICIENTE_SUFFIX

def get_superficie_insuficiente_user_message(cultivo: str) -> str:
    return f"No hay suficiente espacio en la plantación para cultivar {cultivo}"

def get_superficie_insuficiente_detallado_message(cultivo: str, superficie_requerida: float, superficie_disponible: float) -> str:
    return f"No se puede plantar {cultivo}. Requiere: {superficie_requerida:.2f} m², Disponible: {superficie_disponible:.2f} m²"

# ============================================
# ERRORES DE PERSISTENCIA - ESCRITURA
# ============================================

ERROR_03_ARCHIVO_NO_ENCONTRADO_ESCRITURA = "No se encontró la ruta del archivo para escritura"
ERROR_04_IO_ESCRITURA = "Se produjo un error de entrada/salida durante la escritura"

# ============================================
# ERRORES DE PERSISTENCIA - LECTURA
# ============================================

ERROR_05_ARCHIVO_NO_ENCONTRADO_LECTURA = "No se encontró el archivo para lectura"
ERROR_06_IO_LECTURA = "Se produjo un error de entrada/salida durante la lectura"
ERROR_07_CLASS_NOT_FOUND = "Error de conversión de clase durante la deserialización"

def get_archivo_no_encontrado_message(nombre_archivo: str) -> str:
    return f"No se encontró el archivo: {nombre_archivo}"

def get_io_error_message(nombre_archivo: str) -> str:
    return f"Error de entrada/salida al procesar el archivo: {nombre_archivo}"

def get_class_not_found_message(nombre_archivo: str) -> str:
    return f"Error de deserialización. Verifique la versión de las clases en: {nombre_archivo}"

# ============================================
# MENSAJES DE OPERACIONES EXITOSAS
# ============================================

def get_persistencia_exitosa_message(propietario: str) -> str:
    return f"Registro persistido exitosamente: {propietario}"

def get_lectura_exitosa_message(propietario: str) -> str:
    return f"Registro leído exitosamente: {propietario}"


# ==============================================================================
# ARCHIVO 27/67: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\persistencia_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones import mensajes_exception

class PersistenciaException(ForestacionException):
    def __init__(self, error_code: str, message: str, user_message: str = None, cause: Exception = None, tipo_operacion: str = "Desconocida"):
        super().__init__(error_code, message, user_message, cause)
        self._tipo_operacion = tipo_operacion

    def get_tipo_operacion(self) -> str:
        return self._tipo_operacion


# ==============================================================================
# ARCHIVO 28/67: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ==============================================================================

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones import mensajes_exception

class SuperficieInsuficienteException(ForestacionException):
    def __init__(self, tipo_cultivo: str, superficie_requerida: float = 0.0, superficie_disponible: float = 0.0):
        if superficie_requerida == 0.0 and superficie_disponible == 0.0: # Basic constructor
            super().__init__(
                mensajes_exception.ERROR_CODE_02,
                mensajes_exception.get_superficie_insuficiente_message(tipo_cultivo),
                mensajes_exception.get_superficie_insuficiente_user_message(tipo_cultivo)
            )
        else:
            super().__init__(
                mensajes_exception.ERROR_CODE_02,
                mensajes_exception.get_superficie_insuficiente_message(tipo_cultivo),
                mensajes_exception.get_superficie_insuficiente_detallado_message(tipo_cultivo, superficie_requerida, superficie_disponible)
            )
        self._tipo_cultivo = tipo_cultivo
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

    def get_tipo_cultivo(self) -> str:
        return self._tipo_cultivo

    def get_superficie_requerida(self) -> float:
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        return self._superficie_disponible



################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 29/67: __init__.py
# Directorio: patrones
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\factory
################################################################################

# ==============================================================================
# ARCHIVO 30/67: __init__.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\factory\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/67: cultivo_factory.py
# Directorio: patrones\factory
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\factory\cultivo_factory.py
# ==============================================================================

from typing import Dict, Callable
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import PINO_DEFAULT_VARIEDAD, OLIVO_DEFAULT_TIPO_ACEITUNA, LECHUGA_DEFAULT_VARIEDAD, ZANAHORIA_DEFAULT_ES_BABY_CARROT

class CultivoFactory:
    """Fábrica para la creación de objetos Cultivo utilizando el patrón Factory Method.

    Permite la creación de diferentes tipos de cultivos (Pino, Olivo, Lechuga, Zanahoria)
    sin exponer la lógica de instanciación al cliente.
    """
    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        """Crea una instancia de un cultivo basado en la especie proporcionada.

        Args:
            especie (str): El nombre de la especie del cultivo a crear.

        Returns:
            Cultivo: Una instancia del cultivo solicitado.

        Raises:
            ValueError: Si la especie de cultivo no es reconocida.
        """
        factories: Dict[str, Callable[[], Cultivo]] = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie de cultivo desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> Pino:
        """Crea una instancia de Pino con valores por defecto."""
        return Pino(variedad=PINO_DEFAULT_VARIEDAD)

    @staticmethod
    def _crear_olivo() -> Olivo:
        """Crea una instancia de Olivo con valores por defecto."""
        return Olivo(tipo_aceituna=OLIVO_DEFAULT_TIPO_ACEITUNA)

    @staticmethod
    def _crear_lechuga() -> Lechuga:
        """Crea una instancia de Lechuga con valores por defecto."""
        return Lechuga(variedad=LECHUGA_DEFAULT_VARIEDAD)

    @staticmethod
    def _crear_zanahoria() -> Zanahoria:
        """Crea una instancia de Zanahoria con valores por defecto."""
        return Zanahoria(is_baby=ZANAHORIA_DEFAULT_ES_BABY_CARROT)



################################################################################
# DIRECTORIO: patrones\observer
################################################################################

# ==============================================================================
# ARCHIVO 32/67: __init__.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\observer\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 33/67: observable.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\observer\observable.py
# ==============================================================================

from typing import Generic, TypeVar, List
from abc import ABC, abstractmethod
from threading import Lock
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')

class Observable(Generic[T], ABC):
    """Clase base abstracta para objetos observables en el patrón Observer.

    Permite registrar, eliminar y notificar a los observadores sobre cambios de estado.
    """
    def __init__(self):
        """Inicializa una nueva instancia de Observable."""
        
        self._observadores: List[Observer[T]] = []
        self._lock = Lock() # For thread-safe observer management

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Registra un observador para recibir notificaciones.

        Args:
            observador (Observer[T]): El observador a registrar.
        """
        with self._lock:
            if observador not in self._observadores:
                self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Elimina un observador de la lista de suscriptores.

        Args:
            observador (Observer[T]): El observador a eliminar.
        """
        with self._lock:
            if observador in self._observadores:
                self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores registrados sobre un nuevo evento.

        Args:
            evento (T): El evento o dato a notificar.
        """
        # Iterate over a copy to avoid issues if observers modify the list during notification
        observadores_copy = None
        with self._lock:
            observadores_copy = self._observadores[:]

        for observador in observadores_copy:
            observador.actualizar(evento)


# ==============================================================================
# ARCHIVO 34/67: observer.py
# Directorio: patrones\observer
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\observer\observer.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para el patron Observer."""

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        pass


################################################################################
# DIRECTORIO: patrones\observer\eventos
################################################################################

# ==============================================================================
# ARCHIVO 35/67: __init__.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\observer\eventos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/67: evento_plantacion.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\observer\eventos\evento_plantacion.py
# ==============================================================================

from dataclasses import dataclass
from datetime import datetime

@dataclass
class EventoPlantacion:
    """
    Representa un evento que ocurre en una plantación.
    """
    mensaje: str
    timestamp: datetime

# ==============================================================================
# ARCHIVO 37/67: evento_sensor.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\observer\eventos\evento_sensor.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones\singleton
################################################################################

# ==============================================================================
# ARCHIVO 38/67: __init__.py
# Directorio: patrones\singleton
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\singleton\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\strategy
################################################################################

# ==============================================================================
# ARCHIVO 39/67: __init__.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 40/67: absorcion_agua_strategy.py
# Directorio: patrones\strategy
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy\absorcion_agua_strategy.py
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionAguaStrategy(ABC):
    """Interfaz abstracta para las estrategias de cálculo de absorción de agua de cultivos.

    Define el contrato que deben seguir todas las implementaciones de estrategias de absorción.
    """
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """Calcula la cantidad de agua que un cultivo debe absorber.

        Args:
            fecha (date): La fecha actual, utilizada para cálculos estacionales.
            temperatura (float): La temperatura ambiental actual.
            humedad (float): La humedad ambiental actual.
            cultivo (Cultivo): El cultivo para el cual se calcula la absorción.

        Returns:
            int: La cantidad de agua absorbida por el cultivo en litros.
        """
        pass



################################################################################
# DIRECTORIO: patrones\strategy\impl
################################################################################

# ==============================================================================
# ARCHIVO 41/67: __init__.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy\impl\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 42/67: absorcion_constante_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy\impl\absorcion_constante_strategy.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Implementación de la estrategia de absorción de agua constante.

    El cultivo absorbe una cantidad fija de agua, independientemente de factores externos.
    """
    def __init__(self, cantidad_constante: int):
        """Inicializa una nueva instancia de AbsorcionConstanteStrategy.

        Args:
            cantidad_constante (int): La cantidad fija de agua a absorber.
        """
        self._cantidad = cantidad_constante

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """Calcula la absorción de agua, retornando la cantidad constante predefinida.

        Args:
            fecha (date): La fecha actual (no usada en esta estrategia).
            temperatura (float): La temperatura ambiental actual (no usada en esta estrategia).
            humedad (float): La humedad ambiental actual (no usada en esta estrategia).
            cultivo (Cultivo): El cultivo para el cual se calcula la absorción (no usado en esta estrategia).

        Returns:
            int: La cantidad constante de agua a absorber.
        """
        return self._cantidad


# ==============================================================================
# ARCHIVO 43/67: absorcion_seasonal_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\patrones\strategy\impl\absorcion_seasonal_strategy.py
# ==============================================================================

from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import ABSORCION_SEASONAL_VERANO, ABSORCION_SEASONAL_INVIERNO, MES_INICIO_VERANO, MES_FIN_VERANO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """Implementación de la estrategia de absorción de agua estacional.

    La cantidad de agua absorbida por el cultivo varía según la estación del año.
    """
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """Calcula la absorción de agua basándose en la estación (mes).

        Args:
            fecha (date): La fecha actual para determinar el mes.
            temperatura (float): La temperatura ambiental actual (no usada en esta estrategia).
            humedad (float): La humedad ambiental actual (no usada en esta estrategia).
            cultivo (Cultivo): El cultivo para el cual se calcula la absorción (no usado en esta estrategia).

        Returns:
            int: La cantidad de agua absorbida, que varía según si es verano o invierno.
        """
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO



################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 44/67: __init__.py
# Directorio: riego
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\riego\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego\control
################################################################################

# ==============================================================================
# ARCHIVO 45/67: __init__.py
# Directorio: riego\control
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\riego\control\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 46/67: control_riego_task.py
# Directorio: riego\control
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\riego\control\control_riego_task.py
# ==============================================================================

import threading
import time
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUMEDAD_MAX_RIEGO
from python_forestacion.patrones.observer.observable import Observer

class ControlRiegoTask(threading.Thread, Observer[float]):
    """Tarea en segundo plano que controla el sistema de riego de forma automática.

    Actúa como un Observer, reaccionando a las actualizaciones de temperatura y humedad
    para decidir cuándo regar la plantación.
    """
    def __init__(self, temp_task, hum_task, finca: Plantacion, plantacion_service):
        """Inicializa una nueva instancia de ControlRiegoTask.

        Args:
            temp_task: La tarea de lectura de temperatura (Observable).
            hum_task: La tarea de lectura de humedad (Observable).
            finca (Plantacion): La plantación a controlar.
            plantacion_service: El servicio de plantación para realizar el riego.
        """
        threading.Thread.__init__(self)
        Observer.__init__(self)
        self.daemon = True # Set as daemon thread
        self._temp_task = temp_task
        self._hum_task = hum_task
        self._finca = finca
        self._plantacion_service = plantacion_service
        self._stop_event = threading.Event() # Event for graceful shutdown
        self._ultima_temperatura = float('nan')
        self._ultima_humedad = float('nan')

        # Register as observer to sensor tasks
        self._temp_task.agregar_observador(self)
        self._hum_task.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """Actualiza la última temperatura o humedad recibida de un sensor.

        Este método es llamado por los Observables (sensores) cuando hay una nueva lectura.

        Args:
            evento (float): El valor de la temperatura o humedad notificado.
        """
        # This method will be called by the Observable (sensor tasks)
        # We need to determine if the event is temperature or humidity
        # A more robust solution would involve a custom Event object or separate observers
        # For now, we'll assume the last updated value is the one we care about.
        # This is a simplification for the current context.
        # A better approach would be to pass a tuple (sensor_type, value) or use a dedicated event class.
        # For this implementation, we'll check if the event matches the last known value from each sensor.
        if self._temp_task.get_ultima_temperatura() == evento: # Check if it's a temperature update
            self._ultima_temperatura = evento
        elif self._hum_task.get_ultima_humedad() == evento: # Check if it's a humidity update
            self._ultima_humedad = evento

    def run(self):
        """Método principal del hilo que evalúa las condiciones y activa el riego.
        """
        while not self._stop_event.is_set():
            try:
                # Use the last updated values from the sensors
                temp = self._ultima_temperatura
                hum = self._ultima_humedad

                if not (temp == float('nan') or hum == float('nan')):
                    if TEMP_MIN_RIEGO <= temp <= TEMP_MAX_RIEGO and hum < HUMEDAD_MAX_RIEGO:
                        self._plantacion_service.regar(self._finca)

                self._stop_event.wait(2.5)  # Check conditions every 2.5 seconds, allows faster shutdown
            except AguaAgotadaException as e:
                print(e.get_full_message())
                print("Sistema de riego detenido automáticamente por falta de agua.")
                self._stop_event.set()
                break
            except Exception as e:
                print(f"Error inesperado en ControlRiegoTask: {e}")
                self._stop_event.set()
                break

    def detener(self):
        """Detiene la ejecución del hilo de control de riego de forma segura.
        """
        self._stop_event.set()
        # Unregister from observers to clean up
        self._temp_task.eliminar_observador(self)
        self._hum_task.eliminar_observador(self)



################################################################################
# DIRECTORIO: riego\sensores
################################################################################

# ==============================================================================
# ARCHIVO 47/67: __init__.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\riego\sensores\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 48/67: humedad_reader_task.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\riego\sensores\humedad_reader_task.py
# ==============================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor


class HumedadReaderTask(threading.Thread, Observable[EventoSensor]):
    """Tarea en segundo plano para leer la humedad ambiental de forma continua.

    Actúa como un Observable en el patrón Observer, notificando a sus observadores
    cada vez que se lee una nueva humedad.
    """
    def __init__(self):
        """Inicializa una nueva instancia de HumedadReaderTask.
        """
        threading.Thread.__init__(self)
        Observable.__init__(self)
        self.daemon = True # Set as daemon thread
        self._ultima_humedad = float('nan')
        self._stop_event = threading.Event() # Event for graceful shutdown

    def run(self):
        """Método principal del hilo que lee la humedad y notifica a los observadores.
        """
        while not self._stop_event.is_set():
            try:
                self._ultima_humedad = self._leer_sensor()
                print(f"[Humedad] {self._ultima_humedad:.2f} % ")
                self.notificar_observadores(self._ultima_humedad) # Notify observers
                time.sleep(3)  # simula muestreo
            except Exception as e:
                print(f"Error inesperado en HumedadReaderTask: {e}")
                break

    def _leer_sensor(self) -> float:
        """Simula la lectura de un sensor de humedad.

        Returns:
            float: Un valor de humedad aleatorio entre 0 y 100 %.
        """
        return random.uniform(0, 100)  # entre 0% y 100%

    def get_ultima_humedad(self) -> float:
        """Obtiene la última humedad leída por el sensor.

        Returns:
            float: La última humedad leída.
        """
        return self._ultima_humedad

    def detener(self):
        """Detiene la ejecución del hilo de lectura de humedad de forma segura.
        """
        self._stop_event.set()


# ==============================================================================
# ARCHIVO 49/67: temperatura_reader_task.py
# Directorio: riego\sensores
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\riego\sensores\temperatura_reader_task.py
# ==============================================================================

import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor


class TemperaturaReaderTask(threading.Thread, Observable[EventoSensor]):
    """Tarea en segundo plano para leer la temperatura ambiental de forma continua.

    Actúa como un Observable en el patrón Observer, notificando a sus observadores
    cada vez que se lee una nueva temperatura.
    """
    def __init__(self):
        """Inicializa una nueva instancia de TemperaturaReaderTask.
        """
        threading.Thread.__init__(self)
        Observable.__init__(self)
        self.daemon = True # Set as daemon thread
        self._ultima_temperatura = float('nan')
        self._stop_event = threading.Event() # Event for graceful shutdown

    def run(self):
        """Método principal del hilo que lee la temperatura y notifica a los observadores.
        """
        while not self._stop_event.is_set():
            try:
                self._ultima_temperatura = self._leer_sensor()
                print(f"[Temperatura] {self._ultima_temperatura:.2f} °C")
                self.notificar_observadores(self._ultima_temperatura) # Notify observers
                time.sleep(2)  # simula muestreo
            except Exception as e:
                print(f"Error inesperado en TemperaturaReaderTask: {e}")
                break

    def _leer_sensor(self) -> float:
        """Simula la lectura de un sensor de temperatura.

        Returns:
            float: Un valor de temperatura aleatorio entre -25 y 50 °C.
        """
        return random.uniform(-25, 50)  # entre -25 y 50 °C

    def get_ultima_temperatura(self) -> float:
        """Obtiene la última temperatura leída por el sensor.

        Returns:
            float: La última temperatura leída.
        """
        return self._ultima_temperatura

    def detener(self):
        """Detiene la ejecución del hilo de lectura de temperatura de forma segura.
        """
        self._stop_event.set()



################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 50/67: __init__.py
# Directorio: servicios
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 51/67: __init__.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 52/67: arbol_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\arbol_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 53/67: cultivo_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\cultivo_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 54/67: cultivo_service_registry.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ==============================================================================

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



# ==============================================================================
# ARCHIVO 55/67: lechuga_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\lechuga_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 56/67: olivo_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\olivo_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 57/67: pino_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\pino_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 58/67: zanahoria_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\cultivos\zanahoria_service.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: servicios\negocio
################################################################################

# ==============================================================================
# ARCHIVO 59/67: __init__.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\negocio\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 60/67: fincas_service.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\negocio\fincas_service.py
# ==============================================================================

import time
from typing import List, TypeVar, Type

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Forward declaration for PlantacionService to avoid circular imports
# from servicios.terrenos.plantacion_service import PlantacionService

T = TypeVar('T', bound=Cultivo)

class FincasService:
    def __init__(self, plantacion_service, cultivo_service_registry: CultivoServiceRegistry):
        self._fincas: List[RegistroForestal] = []
        self._plantacion_service = plantacion_service
        self._cultivo_service_registry = cultivo_service_registry

    def add_finca(self, finca: RegistroForestal) -> None:
        self._fincas.append(finca)

    def remover_finca(self, finca: RegistroForestal) -> None:
        self._fincas.remove(finca)

    def fumigar(self, id_finca: int, insecticida: str) -> None:
        for finca_registro in self._fincas:
            if finca_registro.get_plantacion().get_id() == id_finca:
                for cultivo in finca_registro.get_plantacion().get_cultivos():
                    print("Se esta fumigando el cultivo:")
                    self._mostrar_datos_cultivo(cultivo)
                    print(f"Con el insecticida: {insecticida}")

    def regar(self) -> None:
        for finca_registro in self._fincas:
            temp_task = TemperaturaReaderTask()
            hum_task = HumedadReaderTask()
            control_task = ControlRiegoTask(
                temp_task, hum_task, finca_registro.get_plantacion(), self._plantacion_service
            )

            temp_task.start()
            hum_task.start()
            control_task.start()

            # Let it run for a while (e.g., 20 seconds as in Java example)
            time.sleep(20)

            # Stop all threads
            temp_task.detener()
            hum_task.detener()
            control_task.detener()

            # Wait for threads to finish (optional, but good practice)
            temp_task.join()
            hum_task.join()
            control_task.join()

    def cosechar_y_empaquetar(self, tipo_cultivo: Type[T]) -> Paquete[T]:
        caja = Paquete[tipo_cultivo]()

        for finca_registro in self._fincas:
            for cultivo in finca_registro.get_plantacion().get_cultivos():
                if isinstance(cultivo, tipo_cultivo):
                    caja.add_item(cultivo)
            # Assuming plantacionService.consumir removes the harvested crops from the plantation
            self._plantacion_service.consumir(finca_registro.get_plantacion(), tipo_cultivo)
            print(f"Se cosecharon los/las {tipo_cultivo.__name__}s de la finca {finca_registro.get_plantacion().get_nombre()}")
        return caja

    def _mostrar_datos_cultivo(self, cultivo: Cultivo) -> None:
        self._cultivo_service_registry.mostrar_datos(cultivo)


# ==============================================================================
# ARCHIVO 61/67: paquete.py
# Directorio: servicios\negocio
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\negocio\paquete.py
# ==============================================================================

from typing import List, Generic, TypeVar
from python_forestacion.entidades.cultivos.cultivo import Cultivo

T = TypeVar('T', bound=Cultivo)

class Paquete(Generic[T]):
    def __init__(self):
        self._id = None  # Java's id was not initialized in constructor, so making it optional
        self._productos: List[T] = []

    def add_item(self, producto: T) -> None:
        self._productos.append(producto)

    def get_items(self) -> List[T]:
        return self._productos

    def mostrar_contenido_caja(self) -> None:
        print("CONTENIDO DE LA CAJA")
        print("____________________")
        for c in self.get_items():
            print(f"Cultivo: {c.__class__.__name__}")



################################################################################
# DIRECTORIO: servicios\personal
################################################################################

# ==============================================================================
# ARCHIVO 62/67: __init__.py
# Directorio: servicios\personal
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 63/67: trabajador_service.py
# Directorio: servicios\personal
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\personal\trabajador_service.py
# ==============================================================================

from datetime import date
from typing import List
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea

class TrabajadorService:
    @staticmethod
    def _obtener_id_tarea(tarea: Tarea) -> int:
        """Obtiene el ID de una tarea para ordenamiento."""
        return tarea.get_id_tarea()

    def trabajar(self, trabajador: Trabajador, fecha: date, herramienta: Herramienta) -> bool:
        if not trabajador.get_apto_medico().esta_apto():
            print(f"El trabajador {trabajador.get_nombre()} no puede trabajar - apto médico inválido")
            return False

        tareas_ordenadas: List[Tarea] = sorted(
            trabajador.get_tareas(), 
            key=TrabajadorService._obtener_id_tarea, 
            reverse=True
        )

        tarea_ejecutada = False
        for tarea in tareas_ordenadas:
            if tarea.get_fecha_programada() == fecha:
                print(f"El trabajador {trabajador.get_nombre()} realizó la tarea {tarea.get_id_tarea()} {tarea.get_descripcion()} con herramienta: {herramienta.get_nombre()}")
                tarea.set_completada(True)
                tarea_ejecutada = True
        return tarea_ejecutada

    def asignar_apto_medico(self, trabajador: Trabajador, apto: bool, fecha_emision: date, observaciones: str) -> None:
        trabajador.asignar_apto_medico(apto, fecha_emision, observaciones)
        print(f"Apto médico actualizado para: {trabajador.get_nombre()}")



################################################################################
# DIRECTORIO: servicios\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 64/67: __init__.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 65/67: plantacion_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\terrenos\plantacion_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 66/67: registro_forestal_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ==============================================================================

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


# ==============================================================================
# ARCHIVO 67/67: tierra_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Users\juanc\Desktop\Diseno_de_sistemas\PythonForestal\python_forestacion\servicios\terrenos\tierra_service.py
# ==============================================================================

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



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 67 
# Generado: 2025-10-21 19:37:21
################################################################################
