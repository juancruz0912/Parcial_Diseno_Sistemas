# Historias de Usuario - Sistema de Gestion Forestal

**Proyecto**: PythonForestal
**Version**: 1.0.0
**Fecha**: Octubre 2025
**Metodologia**: User Story Mapping

---

## Indice

1. [Epic 1: Gestion de Terrenos y Plantaciones](#epic-1-gestion-de-terrenos-y-plantaciones)
2. [Epic 2: Gestion de Cultivos](#epic-2-gestion-de-cultivos)
3. [Epic 3: Sistema de Riego Automatizado](#epic-3-sistema-de-riego-automatizado)
4. [Epic 4: Gestion de Personal](#epic-4-gestion-de-personal)
5. [Epic 5: Operaciones de Negocio](#epic-5-operaciones-de-negocio)
6. [Epic 6: Persistencia y Auditoria](#epic-6-persistencia-y-auditoria)
7. [Historias Tecnicas (Patrones de Diseno)](#historias-tecnicas-patrones-de-diseno)

---

## Epic 1: Gestion de Terrenos y Plantaciones

### US-001: Registrar Terreno Forestal

**Como** propietario de finca forestal
**Quiero** registrar un terreno con su padron catastral y superficie
**Para** tener un control oficial de mis propiedades

#### Criterios de Aceptacion

- [x] El sistema debe permitir crear un terreno con:
  - Padron catastral unico (numero entero positivo)
  - Superficie en metros cuadrados (numero positivo)
  - Domicilio de ubicacion (cadena de texto)
- [x] La superficie debe ser mayor a 0, si no lanzar `ValueError`
- [x] El terreno debe poder modificarse posteriormente
- [x] El sistema debe validar que los datos sean consistentes

#### Detalles Tecnicos

**Clase**: `Tierra` (`python_forestacion/entidades/terrenos/tierra.py`)
**Servicio**: `TierraService` (`python_forestacion/servicios/terrenos/tierra_service.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.servicios.terrenos.tierra_service import TierraService

tierra_service = TierraService()
terreno = tierra_service.crear_tierra_con_plantacion(
    id_padron_catastral=1,
    superficie=10000.0,
    domicilio="Agrelo, Mendoza",
    nombre_plantacion="Finca del Madero"
)
```

**Validaciones**:
```python
# Superficie valida
terreno.set_superficie(15000.0)  # OK

# Superficie invalida
terreno.set_superficie(-100.0)  # ValueError: superficie debe ser mayor a cero
terreno.set_superficie(0)  # ValueError: superficie debe ser mayor a cero
```

**Trazabilidad**: `main.py` lineas 111-116

---

### US-002: Crear Plantacion en Terreno

**Como** administrador de finca
**Quiero** crear una plantacion asociada a un terreno
**Para** organizar los cultivos en parcelas identificables

#### Criterios de Aceptacion

- [x] Una plantacion debe tener:
  - Nombre identificatorio unico
  - Superficie maxima (heredada del terreno)
  - Agua disponible inicial (500L por defecto)
  - Lista de cultivos (vacia al inicio)
  - Lista de trabajadores (vacia al inicio)
- [x] La plantacion debe estar asociada a un terreno valido
- [x] El agua disponible no puede ser negativa
- [x] El sistema debe controlar la superficie ocupada vs disponible

#### Detalles Tecnicos

**Clase**: `Plantacion` (`python_forestacion/entidades/terrenos/plantacion.py`)
**Servicio**: `PlantacionService` (`python_forestacion/servicios/terrenos/plantacion_service.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.entidades.terrenos.plantacion import Plantacion

plantacion = Plantacion(
    nombre="Finca del Madero",
    superficie=10000.0,
    agua=500
)

# Obtener desde terreno
plantacion = terreno.get_finca()
```

**Validaciones**:
```python
# Agua valida
plantacion.set_agua_disponible(1000)  # OK

# Agua invalida
plantacion.set_agua_disponible(-50)  # ValueError: agua no puede ser negativa
```

**Trazabilidad**: `main.py` linea 117, `tierra_service.py` lineas 21-54

---

### US-003: Crear Registro Forestal Completo

**Como** auditor catastral
**Quiero** crear un registro forestal que vincule terreno, plantacion, propietario y avaluo
**Para** tener documentacion oficial completa

#### Criterios de Aceptacion

- [x] Un registro forestal debe contener:
  - ID de padron (numero unico)
  - Referencia a Tierra
  - Referencia a Plantacion
  - Nombre del propietario
  - Avaluo fiscal (numero decimal positivo)
- [x] Todos los campos son obligatorios
- [x] El registro debe poder persistirse y recuperarse
- [x] El registro debe poder mostrarse en consola con formato

#### Detalles Tecnicos

**Clase**: `RegistroForestal` (`python_forestacion/entidades/terrenos/registro_forestal.py`)
**Servicio**: `RegistroForestalService` (`python_forestacion/servicios/terrenos/registro_forestal_service.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

registro = RegistroForestal(
    id_padron=1,
    tierra=terreno,
    plantacion=plantacion,
    propietario="Juan Perez",
    avaluo=50309233.55
)
```

**Salida de mostracion**:
```
REGISTRO FORESTAL
=================
Padron:      1
Propietario: Juan Perez
Avaluo:      50309233.55
Domicilio:   Agrelo, Mendoza
Superficie: 10000.0
Cantidad de cultivos plantados: 20
```

**Trazabilidad**: `main.py` lineas 123-129

---

## Epic 2: Gestion de Cultivos

### US-004: Plantar Pinos en Plantacion

**Como** tecnico forestal
**Quiero** plantar pinos de una variedad especifica
**Para** iniciar una forestacion de arboles maderables

#### Criterios de Aceptacion

- [x] Debe poder plantar multiples pinos simultaneamente
- [x] Cada pino debe tener:
  - Variedad (Parana, Elliott, Taeda, etc.)
  - Superficie: 2.0 m² por arbol
  - Agua inicial: 2L
  - Altura inicial: 1.0m
- [x] El sistema debe verificar superficie disponible
- [x] Si no hay superficie, lanzar `SuperficieInsuficienteException`
- [x] Los pinos deben crearse via Factory Method (no instanciacion directa)

#### Detalles Tecnicos

**Clase**: `Pino` (`python_forestacion/entidades/cultivos/pino.py`)
**Servicio**: `PinoService` (`python_forestacion/servicios/cultivos/pino_service.py`)
**Factory**: `CultivoFactory` (`python_forestacion/patrones/factory/cultivo_factory.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

plantacion_service = PlantacionService()

# Plantar 5 pinos (usa Factory Method internamente)
plantacion_service.plantar(plantacion, "Pino", 5)

# Superficie requerida: 5 * 2.0 = 10 m²
# Superficie ocupada aumenta automaticamente
```

**Constantes utilizadas**:
```python
SUPERFICIE_PINO = 2.0  # m²
AGUA_INICIAL_PINO = 2  # litros
ALTURA_INICIAL_ARBOL = 1.0  # metros
```

**Trazabilidad**: `main.py` linea 141

---

### US-005: Plantar Olivos con Tipo de Aceituna

**Como** productor olivicola
**Quiero** plantar olivos especificando el tipo de aceituna
**Para** cultivar variedades especificas de aceitunas

#### Criterios de Aceptacion

- [x] Debe poder plantar multiples olivos simultaneamente
- [x] Cada olivo debe tener:
  - Tipo de aceituna (Arbequina, Picual, Manzanilla)
  - Superficie: 3.0 m² por arbol
  - Agua inicial: 5L
  - Altura inicial: 0.5m (mas bajo que pino)
- [x] El sistema debe verificar superficie disponible
- [x] Los olivos deben crearse via Factory Method

#### Detalles Tecnicos

**Clase**: `Olivo` (`python_forestacion/entidades/cultivos/olivo.py`)
**Enum**: `TipoAceituna` (`python_forestacion/entidades/cultivos/tipo_aceituna.py`)
**Servicio**: `OlivoService` (`python_forestacion/servicios/cultivos/olivo_service.py`)

**Codigo de ejemplo**:
```python
# Plantar 5 olivos (tipo de aceituna se asigna por defecto)
plantacion_service.plantar(plantacion, "Olivo", 5)

# Superficie requerida: 5 * 3.0 = 15 m²
```

**Tipos de aceituna disponibles**:
```python
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

TipoAceituna.ARBEQUINA
TipoAceituna.PICUAL
TipoAceituna.MANZANILLA
```

**Constantes utilizadas**:
```python
SUPERFICIE_OLIVO = 3.0  # m²
AGUA_INICIAL_OLIVO = 5  # litros
```

**Trazabilidad**: `main.py` linea 142

---

### US-006: Plantar Lechugas en Invernadero

**Como** productor horticola
**Quiero** plantar lechugas en invernadero
**Para** producir hortalizas de hoja verde

#### Criterios de Aceptacion

- [x] Debe poder plantar multiples lechugas simultaneamente
- [x] Cada lechuga debe tener:
  - Variedad (Crespa, Mantecosa, Morada, etc.)
  - Superficie: 0.10 m² por planta
  - Agua inicial: 1L
  - Invernadero: True (siempre en invernadero)
- [x] Las lechugas ocupan menos superficie que arboles
- [x] El sistema debe verificar superficie disponible

#### Detalles Tecnicos

**Clase**: `Lechuga` (`python_forestacion/entidades/cultivos/lechuga.py`)
**Servicio**: `LechugaService` (`python_forestacion/servicios/cultivos/lechuga_service.py`)

**Codigo de ejemplo**:
```python
# Plantar 5 lechugas
plantacion_service.plantar(plantacion, "Lechuga", 5)

# Superficie requerida: 5 * 0.10 = 0.5 m²
```

**Constantes utilizadas**:
```python
SUPERFICIE_LECHUGA = 0.10  # m²
AGUA_INICIAL_LECHUGA = 1  # litros
```

**Trazabilidad**: `main.py` linea 143

---

### US-007: Plantar Zanahorias (Baby Carrot y Regular)

**Como** productor horticola
**Quiero** plantar zanahorias normales o baby carrots
**Para** diversificar mi produccion horticola

#### Criterios de Aceptacion

- [x] Debe poder plantar multiples zanahorias simultaneamente
- [x] Cada zanahoria debe tener:
  - Tipo: Baby carrot (True) o regular (False)
  - Superficie: 0.15 m² por planta
  - Agua inicial: 0L (comienza sin agua)
  - Invernadero: False (cultivo a campo abierto)
- [x] Las zanahorias no requieren invernadero
- [x] El sistema debe verificar superficie disponible

#### Detalles Tecnicos

**Clase**: `Zanahoria` (`python_forestacion/entidades/cultivos/zanahoria.py`)
**Servicio**: `ZanahoriaService` (`python_forestacion/servicios/cultivos/zanahoria_service.py`)

**Codigo de ejemplo**:
```python
# Plantar 5 zanahorias
plantacion_service.plantar(plantacion, "Zanahoria", 5)

# Superficie requerida: 5 * 0.15 = 0.75 m²
```

**Constantes utilizadas**:
```python
SUPERFICIE_ZANAHORIA = 0.15  # m²
AGUA_INICIAL_ZANAHORIA = 0  # litros (sin agua inicial)
```

**Verificar tipo**:
```python
zanahoria = cultivos[0]
if zanahoria.is_baby_carrot():
    print("Es baby carrot")
else:
    print("Es zanahoria regular")
```

**Trazabilidad**: `main.py` linea 144

---

### US-008: Regar Todos los Cultivos de una Plantacion

**Como** sistema automatizado de riego
**Quiero** regar todos los cultivos de una plantacion
**Para** mantener el nivel hidrico necesario

#### Criterios de Aceptacion

- [x] El riego debe:
  - Consumir agua de la plantacion (10L por riego)
  - Distribuir agua a todos los cultivos
  - Cada cultivo absorbe segun su estrategia
  - Arboles (Pino, Olivo): Absorcion estacional (5L verano, 2L invierno)
  - Hortalizas (Lechuga, Zanahoria): Absorcion constante (1-2L)
- [x] Si no hay suficiente agua, lanzar `AguaAgotadaException`
- [x] Los arboles deben crecer en altura al recibir agua
- [x] El sistema debe usar el patron Strategy para absorcion

#### Detalles Tecnicos

**Servicio**: `PlantacionService.regar()`
**Estrategias**:
- `AbsorcionSeasonalStrategy` (arboles)
- `AbsorcionConstanteStrategy` (hortalizas)

**Codigo de ejemplo**:
```python
# Regar plantacion
plantacion_service.regar(plantacion)

# Proceso:
# 1. Verifica agua disponible >= 10L
# 2. Consume 10L de la plantacion
# 3. Cada cultivo absorbe segun su estrategia
# 4. Arboles crecen en altura
```

**Absorcion por tipo**:
```python
# Pino y Olivo (estacional)
# - Verano (marzo-agosto): 5L
# - Invierno (sept-feb): 2L

# Lechuga (constante)
# - Siempre: 1L

# Zanahoria (constante)
# - Siempre: 2L
```

**Crecimiento**:
```python
# Pino: +0.10m por riego
# Olivo: +0.01m por riego
```

**Trazabilidad**: `plantacion_service.py` lineas 82-129

---

### US-009: Mostrar Datos de Cultivos por Tipo

**Como** administrador de finca
**Quiero** ver los datos de cada cultivo de forma especifica
**Para** conocer el estado actual de mis plantaciones

#### Criterios de Aceptacion

- [x] El sistema debe mostrar datos especificos por tipo:
  - **Pino**: Cultivo, Superficie, Agua, ID, Altura, Variedad
  - **Olivo**: Cultivo, Superficie, Agua, ID, Altura, Tipo de aceituna
  - **Lechuga**: Cultivo, Superficie, Agua, Variedad, Invernadero
  - **Zanahoria**: Cultivo, Superficie, Agua, Es baby carrot
- [x] Usar el patron Registry para dispatch polimorfico
- [x] NO usar cascadas de isinstance()

#### Detalles Tecnicos

**Registry**: `CultivoServiceRegistry.mostrar_datos()`

**Codigo de ejemplo**:
```python
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

registry = CultivoServiceRegistry.get_instance()

for cultivo in plantacion.get_cultivos():
    registry.mostrar_datos(cultivo)
    # Despacho automatico al servicio correcto
```

**Salida ejemplo (Pino)**:
```
Cultivo: Pino
Superficie: 2.0 m²
Agua almacenada: 7 L
ID: 1
Altura: 1.2 m
Variedad: Parana
```

**Trazabilidad**: `cultivo_service_registry.py` lineas 78-89

---

## Epic 3: Sistema de Riego Automatizado

### US-010: Monitorear Temperatura en Tiempo Real

**Como** sistema de riego automatizado
**Quiero** leer la temperatura ambiental cada 2 segundos
**Para** tomar decisiones de riego basadas en condiciones reales

#### Criterios de Aceptacion

- [x] El sensor debe:
  - Ejecutarse en un thread daemon separado
  - Leer temperatura cada 2 segundos (configurable)
  - Generar lecturas aleatorias entre -25C y 50C
  - Notificar a observadores cada vez que lee
  - Soportar detencion graceful con timeout
- [x] Implementar patron Observer (Observable)
- [x] Usar Generics para tipo-seguridad: `Observable[float]`

#### Detalles Tecnicos

**Clase**: `TemperaturaReaderTask` (`python_forestacion/riego/sensores/temperatura_reader_task.py`)
**Patron**: Observer (Observable[float])

**Codigo de ejemplo**:
```python
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask

# Crear sensor (thread daemon)
tarea_temp = TemperaturaReaderTask()

# Iniciar lectura continua
tarea_temp.start()

# Detener cuando sea necesario
tarea_temp.detener()
tarea_temp.join(timeout=2.0)
```

**Constantes**:
```python
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
SENSOR_TEMP_MIN = -25  # °C
SENSOR_TEMP_MAX = 50  # °C
```

**Eventos generados**:
```python
# Cada lectura notifica valor float a observadores
temperatura: float = 22.5
self.notificar_observadores(temperatura)
```

**Trazabilidad**: `main.py` lineas 158-166

---

### US-011: Monitorear Humedad en Tiempo Real

**Como** sistema de riego automatizado
**Quiero** leer la humedad ambiental cada 3 segundos
**Para** complementar datos de temperatura en decisiones de riego

#### Criterios de Aceptacion

- [x] El sensor debe:
  - Ejecutarse en un thread daemon separado
  - Leer humedad cada 3 segundos (configurable)
  - Generar lecturas aleatorias entre 0% y 100%
  - Notificar a observadores cada vez que lee
  - Soportar detencion graceful con timeout
- [x] Implementar patron Observer (Observable)
- [x] Usar Generics para tipo-seguridad: `Observable[float]`

#### Detalles Tecnicos

**Clase**: `HumedadReaderTask` (`python_forestacion/riego/sensores/humedad_reader_task.py`)
**Patron**: Observer (Observable[float])

**Codigo de ejemplo**:
```python
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask

# Crear sensor (thread daemon)
tarea_hum = HumedadReaderTask()

# Iniciar lectura continua
tarea_hum.start()

# Detener cuando sea necesario
tarea_hum.detener()
tarea_hum.join(timeout=2.0)
```

**Constantes**:
```python
INTERVALO_SENSOR_HUMEDAD = 3.0  # segundos
SENSOR_HUMEDAD_MIN = 0  # %
SENSOR_HUMEDAD_MAX = 100  # %
```

**Trazabilidad**: `main.py` lineas 158-166

---

### US-012: Control Automatico de Riego Basado en Sensores

**Como** sistema de riego automatizado
**Quiero** regar automaticamente cuando se cumplan condiciones ambientales
**Para** optimizar el uso de agua segun necesidades reales

#### Criterios de Aceptacion

- [x] El controlador debe:
  - Ejecutarse en un thread daemon separado
  - Evaluar condiciones cada 2.5 segundos
  - Observar sensores de temperatura y humedad
  - Regar cuando:
    - Temperatura entre 8C y 15C, Y
    - Humedad menor a 50%
  - NO regar si condiciones no se cumplen
  - Manejar excepcion si no hay agua disponible
- [x] Implementar patron Observer (Observer[float])
- [x] Recibir sensores via inyeccion de dependencias

#### Detalles Tecnicos

**Clase**: `ControlRiegoTask` (`python_forestacion/riego/control/control_riego_task.py`)
**Patron**: Observer (observa sensores)

**Codigo de ejemplo**:
```python
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Inyectar dependencias
tarea_control = ControlRiegoTask(
    sensor_temperatura=tarea_temp,
    sensor_humedad=tarea_hum,
    plantacion=plantacion,
    plantacion_service=plantacion_service
)

# Iniciar control automatico
tarea_control.start()

# Detener cuando sea necesario
tarea_control.detener()
tarea_control.join(timeout=2.0)
```

**Logica de decision**:
```python
if (TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO) and (humedad < HUMEDAD_MAX_RIEGO):
    # REGAR
    plantacion_service.regar(plantacion)
else:
    # NO REGAR
    pass
```

**Constantes de riego**:
```python
TEMP_MIN_RIEGO = 8  # °C
TEMP_MAX_RIEGO = 15  # °C
HUMEDAD_MAX_RIEGO = 50  # %
INTERVALO_CONTROL_RIEGO = 2.5  # segundos
```

**Trazabilidad**: `main.py` lineas 160-166, `control_riego_task.py` lineas 67-91

---

### US-013: Detener Sistema de Riego de Forma Segura

**Como** administrador del sistema
**Quiero** detener el sistema de riego de forma controlada
**Para** evitar corrupcion de datos o procesos incompletos

#### Criterios de Aceptacion

- [x] El sistema debe:
  - Detener todos los threads con `threading.Event`
  - Esperar finalizacion con timeout configurable (2s)
  - NO forzar terminacion abrupta
  - Permitir que threads completen operacion actual
- [x] Threads deben ser daemon (finalizan con main)
- [x] Usar timeout de `constantes.py`

#### Detalles Tecnicos

**Codigo de ejemplo**:
```python
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT

# Detener sensores y control
tarea_temp.detener()
tarea_hum.detener()
tarea_control.detener()

# Esperar finalizacion con timeout
tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)  # 2s
tarea_hum.join(timeout=THREAD_JOIN_TIMEOUT)
tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)

# Si timeout expira, threads daemon finalizan automaticamente
```

**Constantes**:
```python
THREAD_JOIN_TIMEOUT = 2.0  # segundos
```

**Trazabilidad**: `main.py` lineas 256-263

---

## Epic 4: Gestion de Personal

### US-014: Registrar Trabajador con Tareas Asignadas

**Como** jefe de personal
**Quiero** registrar trabajadores con sus tareas asignadas
**Para** organizar el trabajo agricola

#### Criterios de Aceptacion

- [x] Un trabajador debe tener:
  - DNI unico (numero entero)
  - Nombre completo
  - Lista de tareas asignadas (puede estar vacia)
  - Apto medico (inicialmente sin apto)
- [x] Las tareas deben tener:
  - ID unico
  - Fecha programada
  - Descripcion de la tarea
  - Estado (pendiente/completada)
- [x] Un trabajador puede tener multiples tareas
- [x] Lista de trabajadores es inmutable (defensive copy)

#### Detalles Tecnicos

**Clases**:
- `Trabajador` (`python_forestacion/entidades/personal/trabajador.py`)
- `Tarea` (`python_forestacion/entidades/personal/tarea.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from datetime import date

# Crear tareas
tareas = [
    Tarea(1, date.today(), "Desmalezar"),
    Tarea(2, date.today(), "Abonar"),
    Tarea(3, date.today(), "Marcar surcos")
]

# Crear trabajador
trabajador = Trabajador(
    dni=43888734,
    nombre="Juan Perez",
    tareas=tareas
)
```

**Trazabilidad**: `main.py` lineas 176-185

---

### US-015: Asignar Apto Medico a Trabajador

**Como** medico laboral
**Quiero** asignar un apto medico a un trabajador
**Para** certificar que esta apto para trabajar

#### Criterios de Aceptacion

- [x] Un apto medico debe tener:
  - Estado de aptitud (True/False)
  - Fecha de emision
  - Observaciones medicas (opcional)
- [x] El sistema debe verificar apto antes de trabajar
- [x] Si no tiene apto valido, no puede ejecutar tareas
- [x] El servicio debe permitir asignar/actualizar apto

#### Detalles Tecnicos

**Clase**: `AptoMedico` (`python_forestacion/entidades/personal/apto_medico.py`)
**Servicio**: `TrabajadorService.asignar_apto_medico()`

**Codigo de ejemplo**:
```python
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from datetime import date

trabajador_service = TrabajadorService()

# Asignar apto medico
trabajador_service.asignar_apto_medico(
    trabajador=trabajador,
    apto=True,
    fecha_emision=date.today(),
    observaciones="Estado de salud: excelente"
)

# Verificar apto
if trabajador.get_apto_medico().esta_apto():
    print("Trabajador apto para trabajar")
else:
    print("Trabajador NO apto")
```

**Trazabilidad**: `main.py` lineas 191-196

---

### US-016: Ejecutar Tareas Asignadas a Trabajador

**Como** trabajador agricola
**Quiero** ejecutar las tareas que me fueron asignadas
**Para** completar mi jornada laboral

#### Criterios de Aceptacion

- [x] El trabajador debe:
  - Tener apto medico valido
  - Ejecutar solo tareas de la fecha especificada
  - Usar una herramienta asignada
  - Marcar tareas como completadas
- [x] Las tareas deben ejecutarse en orden ID descendente
- [x] Si no tiene apto medico, retornar False (no ejecuta)
- [x] Si tiene apto medico, retornar True (ejecuta)

#### Detalles Tecnicos

**Servicio**: `TrabajadorService.trabajar()`
**Clase**: `Herramienta` (`python_forestacion/entidades/personal/herramienta.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.entidades.personal.herramienta import Herramienta

# Crear herramienta
herramienta = Herramienta(
    id_herramienta=1,
    nombre="Pala",
    certificado_hys=True
)

# Ejecutar tareas
resultado = trabajador_service.trabajar(
    trabajador=trabajador,
    fecha=date.today(),
    util=herramienta
)

if resultado:
    print("Tareas ejecutadas exitosamente")
else:
    print("No puede trabajar - sin apto medico")
```

**Salida esperada**:
```
El trabajador Juan Perez realizo la tarea 3 Marcar surcos con herramienta: Pala
El trabajador Juan Perez realizo la tarea 2 Abonar con herramienta: Pala
El trabajador Juan Perez realizo la tarea 1 Desmalezar con herramienta: Pala
```

**Ordenamiento**:
```python
# Tareas se ordenan por ID descendente (3, 2, 1)
# Usa metodo estatico _obtener_id_tarea() en lugar de lambda
```

**Trazabilidad**: `main.py` lineas 199-204, `trabajador_service.py` lineas 34-72

---

### US-017: Asignar Trabajadores a Plantacion

**Como** jefe de personal
**Quiero** asignar trabajadores a una plantacion especifica
**Para** organizar el personal por finca

#### Criterios de Aceptacion

- [x] Una plantacion debe poder tener multiples trabajadores
- [x] La lista de trabajadores debe ser inmutable (defensive copy)
- [x] Debe poder obtener lista de trabajadores
- [x] Debe poder reemplazar lista completa de trabajadores

#### Detalles Tecnicos

**Clase**: `Plantacion.set_trabajadores()`

**Codigo de ejemplo**:
```python
trabajadores = [
    Trabajador(43888734, "Juan Perez", tareas.copy()),
    Trabajador(40222333, "Maria Lopez", tareas.copy())
]

# Asignar trabajadores a plantacion
plantacion.set_trabajadores(trabajadores)

# Obtener trabajadores (copia inmutable)
lista_trabajadores = plantacion.get_trabajadores()
```

**Trazabilidad**: `main.py` linea 187

---

## Epic 5: Operaciones de Negocio

### US-018: Gestionar Multiples Fincas

**Como** propietario de multiples fincas
**Quiero** gestionar varias fincas desde un servicio centralizado
**Para** tener control unificado de todas mis propiedades

#### Criterios de Aceptacion

- [x] El servicio debe permitir:
  - Agregar fincas (RegistroForestal)
  - Buscar finca por ID de padron
  - Fumigar una finca especifica
  - Cosechar y empaquetar por tipo de cultivo
- [x] Debe manejar multiples fincas simultaneamente
- [x] Debe usar diccionario interno para almacenar fincas

#### Detalles Tecnicos

**Servicio**: `FincasService` (`python_forestacion/servicios/negocio/fincas_service.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.servicios.negocio.fincas_service import FincasService

fincas_service = FincasService()

# Agregar finca
fincas_service.add_finca(registro)

# Buscar finca por padron
finca = fincas_service.buscar_finca(1)
```

**Trazabilidad**: `main.py` linea 225

---

### US-019: Fumigar Plantacion Completa

**Como** tecnico agricola
**Quiero** fumigar toda una plantacion con un plaguicida especifico
**Para** controlar plagas y enfermedades

#### Criterios de Aceptacion

- [x] Debe permitir especificar:
  - ID de padron de la finca a fumigar
  - Tipo de plaguicida a aplicar
- [x] Debe fumigar todos los cultivos de la plantacion
- [x] Debe mostrar mensaje de confirmacion
- [x] Si finca no existe, manejar error apropiadamente

#### Detalles Tecnicos

**Servicio**: `FincasService.fumigar()`

**Codigo de ejemplo**:
```python
# Fumigar finca ID 1 con insecticida
fincas_service.fumigar(
    id_padron=1,
    plaguicida="insecto organico"
)
```

**Salida esperada**:
```
Fumigando plantacion con: insecto organico
```

**Trazabilidad**: `main.py` linea 228

---

### US-020: Cosechar y Empaquetar Cultivos por Tipo

**Como** encargado de cosecha
**Quiero** cosechar todos los cultivos de un tipo especifico y empaquetarlos
**Para** preparar productos para venta

#### Criterios de Aceptacion

- [x] Debe permitir cosechar por tipo de cultivo (Class type)
- [x] Debe:
  - Buscar todos los cultivos del tipo especificado
  - Removerlos de todas las plantaciones
  - Empaquetarlos en un Paquete generico tipo-seguro
  - Mostrar cantidad cosechada
- [x] Usar Generics para tipo-seguridad: `Paquete[T]`
- [x] Permitir mostrar contenido de la caja

#### Detalles Tecnicos

**Servicio**: `FincasService.cosechar_yempaquetar()`
**Clase**: `Paquete[T]` (`python_forestacion/servicios/negocio/paquete.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.pino import Pino

# Cosechar todas las lechugas
caja_lechugas = fincas_service.cosechar_yempaquetar(Lechuga)
caja_lechugas.mostrar_contenido_caja()

# Cosechar todos los pinos
caja_pinos = fincas_service.cosechar_yempaquetar(Pino)
caja_pinos.mostrar_contenido_caja()
```

**Salida esperada**:
```
COSECHANDO 5 unidades de <class 'python_forestacion.entidades.cultivos.lechuga.Lechuga'>

Contenido de la caja:
  Tipo: Lechuga
  Cantidad: 5
  ID Paquete: 1

COSECHANDO 5 unidades de <class 'python_forestacion.entidades.cultivos.pino.Pino'>

Contenido de la caja:
  Tipo: Pino
  Cantidad: 5
  ID Paquete: 2
```

**Tipo-seguridad**:
```python
# Paquete es generico tipo-seguro
caja_lechugas: Paquete[Lechuga] = ...
caja_pinos: Paquete[Pino] = ...
```

**Trazabilidad**: `main.py` lineas 232-236

---

## Epic 6: Persistencia y Auditoria

### US-021: Persistir Registro Forestal en Disco

**Como** administrador del sistema
**Quiero** guardar registros forestales en disco
**Para** mantener datos permanentes entre ejecuciones

#### Criterios de Aceptacion

- [x] El sistema debe:
  - Serializar RegistroForestal completo con Pickle
  - Guardar en directorio `data/`
  - Nombre de archivo: `{propietario}.dat`
  - Crear directorio si no existe
  - Mostrar mensaje de confirmacion
- [x] Si ocurre error, lanzar `PersistenciaException`
- [x] Cerrar recursos apropiadamente en bloque finally

#### Detalles Tecnicos

**Servicio**: `RegistroForestalService.persistir()`

**Codigo de ejemplo**:
```python
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService

registro_service = RegistroForestalService()

# Persistir registro
registro_service.persistir(registro)
# Crea: data/Juan Perez.dat
```

**Salida esperada**:
```
Registro de Juan Perez persistido exitosamente en data/Juan Perez.dat
```

**Constantes**:
```python
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"
```

**Manejo de errores**:
```python
try:
    registro_service.persistir(registro)
except PersistenciaException as e:
    print(e.get_user_message())
    print(f"Archivo: {e.get_nombre_archivo()}")
    print(f"Operacion: {e.get_tipo_operacion().value}")
```

**Trazabilidad**: `main.py` linea 242, `registro_forestal_service.py` lineas 62-112

---

### US-022: Recuperar Registro Forestal desde Disco

**Como** auditor
**Quiero** recuperar registros forestales guardados previamente
**Para** consultar historicos y realizar auditorias

#### Criterios de Aceptacion

- [x] El sistema debe:
  - Deserializar archivo `.dat` con Pickle
  - Buscar en directorio `data/`
  - Validar que propietario no sea nulo/vacio
  - Retornar RegistroForestal completo
  - Mostrar mensaje de confirmacion
- [x] Si archivo no existe, lanzar `PersistenciaException`
- [x] Si archivo corrupto, lanzar `PersistenciaException`
- [x] Cerrar recursos apropiadamente en bloque finally

#### Detalles Tecnicos

**Servicio**: `RegistroForestalService.leer_registro()` (metodo estatico)

**Codigo de ejemplo**:
```python
# Leer registro persistido
registro_leido = RegistroForestalService.leer_registro("Juan Perez")

# Mostrar datos recuperados
registro_service.mostrar_datos(registro_leido)
```

**Salida esperada**:
```
Registro de Juan Perez recuperado exitosamente desde data/Juan Perez.dat

REGISTRO FORESTAL
=================
Padron:      1
Propietario: Juan Perez
Avaluo:      50309233.55
...
```

**Validaciones**:
```python
# Propietario vacio
try:
    RegistroForestalService.leer_registro("")
except ValueError as e:
    print("El nombre del propietario no puede ser nulo o vacio")

# Archivo no existe
try:
    RegistroForestalService.leer_registro("NoExiste")
except PersistenciaException as e:
    print(f"Archivo no encontrado: {e.get_nombre_archivo()}")
```

**Trazabilidad**: `main.py` lineas 246-247, `registro_forestal_service.py` lineas 114-171

---

### US-023: Mostrar Datos Completos de Registro Forestal

**Como** auditor
**Quiero** ver todos los datos de un registro forestal en formato legible
**Para** analizar la informacion completa de una finca

#### Criterios de Aceptacion

- [x] El sistema debe mostrar:
  - Encabezado "REGISTRO FORESTAL"
  - Padron catastral
  - Propietario
  - Avaluo fiscal
  - Domicilio del terreno
  - Superficie del terreno
  - Cantidad de cultivos plantados
  - Listado detallado de cada cultivo
- [x] Cada cultivo debe mostrarse con datos especificos de su tipo
- [x] Usar Registry para dispatch polimorfico

#### Detalles Tecnicos

**Servicio**: `RegistroForestalService.mostrar_datos()`

**Codigo de ejemplo**:
```python
# Mostrar registro completo
registro_service.mostrar_datos(registro)
```

**Salida esperada**:
```
REGISTRO FORESTAL
=================
Padron:      1
Propietario: Juan Perez
Avaluo:      50309233.55
Domicilio:   Agrelo, Mendoza
Superficie: 10000.0
Cantidad de cultivos plantados: 20
Listado de Cultivos plantados
____________________________

Cultivo: Pino
Superficie: 2.0 m²
Agua almacenada: 7 L
ID: 1
Altura: 1.2 m
Variedad: Parana

Cultivo: Olivo
Superficie: 3.0 m²
Agua almacenada: 9 L
ID: 2
Altura: 0.52 m
Tipo de aceituna: Arbequina

...
```

**Trazabilidad**: `main.py` linea 247, `registro_forestal_service.py` lineas 28-60

---

## Historias Tecnicas (Patrones de Diseno)

### US-TECH-001: Implementar Singleton para CultivoServiceRegistry

**Como** arquitecto de software
**Quiero** garantizar una unica instancia del registro de servicios
**Para** compartir estado consistente entre todos los servicios

#### Criterios de Aceptacion

- [x] Implementar patron Singleton thread-safe
- [x] Usar double-checked locking con Lock
- [x] Inicializacion perezosa (lazy initialization)
- [x] Metodo `get_instance()` para acceso
- [x] Constructor `__new__` para controlar instanciacion
- [x] NO permitir multiples instancias

#### Detalles Tecnicos

**Clase**: `CultivoServiceRegistry`
**Patron**: Singleton

**Implementacion**:
```python
from threading import Lock

class CultivoServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked
                    cls._instance = super().__new__(cls)
                    # Inicializar servicios una sola vez
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance
```

**Uso**:
```python
# Opcion 1: Instanciacion directa
registry = CultivoServiceRegistry()

# Opcion 2: Metodo get_instance()
registry = CultivoServiceRegistry.get_instance()

# Ambas retornan la MISMA instancia
assert registry is CultivoServiceRegistry.get_instance()
```

**Trazabilidad**: `cultivo_service_registry.py` lineas 20-46

---

### US-TECH-002: Implementar Factory Method para Creacion de Cultivos

**Como** arquitecto de software
**Quiero** centralizar creacion de cultivos mediante Factory Method
**Para** desacoplar cliente de clases concretas

#### Criterios de Aceptacion

- [x] Crear clase `CultivoFactory` con metodo estatico
- [x] Soportar creacion de: Pino, Olivo, Lechuga, Zanahoria
- [x] Usar diccionario de factories (no if/elif cascades)
- [x] Lanzar `ValueError` si especie desconocida
- [x] Retornar tipo base `Cultivo` (no tipos concretos)
- [x] NO usar lambdas - usar metodos estaticos dedicados

#### Detalles Tecnicos

**Clase**: `CultivoFactory`
**Patron**: Factory Method

**Implementacion**:
```python
class CultivoFactory:
    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> Pino:
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Parana")

    # ... otros metodos _crear_*
```

**Uso**:
```python
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory

# Cliente NO conoce clases concretas
cultivo = CultivoFactory.crear_cultivo("Pino")
# Retorna Cultivo (interfaz), no Pino (concreto)
```

**Trazabilidad**: `cultivo_factory.py` lineas 8-67

---

### US-TECH-003: Implementar Observer Pattern para Sensores

**Como** arquitecto de software
**Quiero** implementar patron Observer con Generics
**Para** notificar cambios de sensores de forma tipo-segura

#### Criterios de Aceptacion

- [x] Crear clase `Observable[T]` generica
- [x] Crear interfaz `Observer[T]` generica
- [x] Soportar multiples observadores
- [x] Metodos: `agregar_observador()`, `eliminar_observador()`, `notificar_observadores()`
- [x] Sensores heredan de `Observable[float]`
- [x] Controlador hereda de `Observer[float]`
- [x] Thread-safe en notificaciones

#### Detalles Tecnicos

**Clases**: `Observable[T]`, `Observer[T]`
**Patron**: Observer

**Implementacion**:
```python
from typing import Generic, TypeVar, List
from abc import ABC, abstractmethod

T = TypeVar('T')

class Observer(Generic[T], ABC):
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        pass

class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento)
```

**Uso**:
```python
# Sensor es Observable[float]
class TemperaturaReaderTask(threading.Thread, Observable[float]):
    def run(self):
        while not self._detenido.is_set():
            temp = self._leer_temperatura()
            self.notificar_observadores(temp)  # Notifica float

# Controlador es Observer[float]
class ControlRiegoTask(Observer[float]):
    def actualizar(self, evento: float) -> None:
        self._ultima_temperatura = evento  # Recibe float
```

**Trazabilidad**: `observable.py`, `observer.py`

---

### US-TECH-004: Implementar Strategy Pattern para Absorcion de Agua

**Como** arquitecto de software
**Quiero** implementar algoritmos intercambiables de absorcion
**Para** permitir diferentes estrategias segun tipo de cultivo

#### Criterios de Aceptacion

- [x] Crear interfaz `AbsorcionAguaStrategy` abstracta
- [x] Implementar `AbsorcionSeasonalStrategy` (arboles)
- [x] Implementar `AbsorcionConstanteStrategy` (hortalizas)
- [x] Inyectar estrategia en constructor de servicios
- [x] Servicios delegan calculo a estrategia
- [x] Estrategias usan constantes de `constantes.py`

#### Detalles Tecnicos

**Interfaz**: `AbsorcionAguaStrategy`
**Implementaciones**: `AbsorcionSeasonalStrategy`, `AbsorcionConstanteStrategy`
**Patron**: Strategy

**Implementacion**:
```python
# Interfaz
class AbsorcionAguaStrategy(ABC):
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        pass

# Estrategia 1: Seasonal
class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo):
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO  # 5L
        else:
            return ABSORCION_SEASONAL_INVIERNO  # 2L

# Estrategia 2: Constante
class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo):
        return self._cantidad
```

**Inyeccion**:
```python
class PinoService(ArbolService):
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())  # Inyeccion

class ZanahoriaService(CultivoService):
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))  # Inyeccion
```

**Delegacion**:
```python
class CultivoService(ABC):
    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        # Delegar a estrategia
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida
```

**Trazabilidad**: `absorcion_seasonal_strategy.py`, `absorcion_constante_strategy.py`, `cultivo_service.py` lineas 35-59

---

### US-TECH-005: Implementar Registry Pattern para Dispatch Polimorfico

**Como** arquitecto de software
**Quiero** eliminar cascadas de isinstance()
**Para** mejorar mantenibilidad y extensibilidad

#### Criterios de Aceptacion

- [x] Crear diccionarios de handlers por tipo
- [x] Registrar handler para cada tipo de cultivo
- [x] Metodo `absorber_agua()` usa dispatch automatico
- [x] Metodo `mostrar_datos()` usa dispatch automatico
- [x] Lanzar error si tipo no registrado
- [x] NO usar lambdas - usar metodos de instancia dedicados

#### Detalles Tecnicos

**Clase**: `CultivoServiceRegistry`
**Patron**: Registry

**Implementacion**:
```python
class CultivoServiceRegistry:
    def __init__(self):
        # Diccionarios de handlers
        self._absorber_agua_handlers = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

        self._mostrar_datos_handlers = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

    def absorber_agua(self, cultivo: Cultivo) -> int:
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo)

    # Handlers dedicados (NO lambdas)
    def _absorber_agua_pino(self, cultivo):
        return self._pino_service.absorver_agua(cultivo)
```

**Ventajas**:
- Sin `isinstance()` cascades
- Facil agregar nuevos tipos
- Mejor rendimiento (O(1) lookup)
- Mas testeable

**Trazabilidad**: `cultivo_service_registry.py` lineas 48-89

---

## Resumen de Cobertura Funcional

### Totales por Epic

| Epic | Historias | Completadas | Cobertura |
|------|-----------|-------------|-----------|
| Epic 1: Terrenos y Plantaciones | 3 | 3 | 100% |
| Epic 2: Gestion de Cultivos | 6 | 6 | 100% |
| Epic 3: Riego Automatizado | 4 | 4 | 100% |
| Epic 4: Gestion de Personal | 4 | 4 | 100% |
| Epic 5: Operaciones de Negocio | 3 | 3 | 100% |
| Epic 6: Persistencia y Auditoria | 3 | 3 | 100% |
| Historias Tecnicas (Patrones) | 5 | 5 | 100% |
| **TOTAL** | **28** | **28** | **100%** |

### Patrones de Diseno Cubiertos

- [x] SINGLETON - CultivoServiceRegistry
- [x] FACTORY METHOD - CultivoFactory
- [x] OBSERVER - Sensores y eventos
- [x] STRATEGY - Absorcion de agua
- [x] REGISTRY - Dispatch polimorfico (bonus)

### Funcionalidades Completas

- [x] Gestion de 4 tipos de cultivos
- [x] Sistema de riego automatizado con 3 threads
- [x] Gestion de trabajadores con apto medico
- [x] Persistencia con Pickle
- [x] Operaciones de negocio de alto nivel
- [x] Manejo de excepciones especificas
- [x] PEP 8 compliance 100%
- [x] Type hints con TYPE_CHECKING
- [x] Constantes centralizadas
- [x] Codigo limpio sin lambdas

---

**Ultima actualizacion**: Octubre 2025
**Estado**: COMPLETO
**Cobertura funcional**: 100%
