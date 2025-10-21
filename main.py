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
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService
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

        # Crear servicios de cultivos individuales
        pino_service = PinoService()
        olivo_service = OlivoService()
        lechuga_service = LechugaService()
        zanahoria_service = ZanahoriaService()

        # Crear el Registry Pattern
        cultivo_service_registry = CultivoServiceRegistry(
            pino_service, olivo_service, lechuga_service, zanahoria_service)

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

        # ============================================
        # 10. DETENER SISTEMA DE RIEGO
        # ============================================
        print("\n10. Deteniendo sistema de riego...")
        time.sleep(20) # Allow irrigation to run for a bit
        tarea_temp.detener()
        tarea_hum.detener()
        tarea_control.detener()

        # Wait for threads to finish
        tarea_temp.join()
        tarea_hum.join()
        tarea_control.join()

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
