# Sistema de Gestion Forestal

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Sistema integral de gestion forestal y agricola que demuestra la implementacion de multiples patrones de diseno de software con enfoque educativo y profesional.

---

## Tabla de Contenidos

- [Contexto del Dominio](#contexto-del-dominio)
- [Caracteristicas Principales](#caracteristicas-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Patrones de Diseno Implementados](#patrones-de-diseno-implementados)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalacion](#instalacion)
- [Uso del Sistema](#uso-del-sistema)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Modulos del Sistema](#modulos-del-sistema)
- [Documentacion Tecnica](#documentacion-tecnica)
- [Testing y Validacion](#testing-y-validacion)
- [Contribucion](#contribucion)
- [Licencia](#licencia)

---

## Contexto del Dominio

### Problema que Resuelve

El sistema **PythonForestal** aborda los desafios de la gestion moderna de fincas forestales y agricolas, un dominio que requiere:

1. **Gestion de Multiples Tipos de Cultivos**
   - Arboles de diferentes especies (Pinos, Olivos) con ciclos de vida largos
   - Hortalizas de ciclo corto (Lechugas, Zanahorias) con requerimientos especificos
   - Cada tipo con caracteristicas y necesidades hidricas particulares

2. **Monitoreo Ambiental en Tiempo Real**
   - Sensores de temperatura y humedad que operan continuamente
   - Sistema de riego automatizado basado en condiciones ambientales
   - Respuesta dinamica a cambios climaticos

3. **Gestion de Recursos Humanos**
   - Control de trabajadores con certificaciones medicas
   - Asignacion y seguimiento de tareas agricolas
   - Herramientas y equipamiento con certificaciones de seguridad

4. **Planificacion Territorial**
   - Optimizacion del uso de superficie disponible
   - Registro catastral de terrenos forestales
   - Control de plantaciones y distribucion espacial

5. **Persistencia y Trazabilidad**
   - Almacenamiento permanente de registros forestales
   - Recuperacion de historicos para auditoria
   - Valuacion de propiedades y avaluos

### Actores del Sistema

- **Propietario de Finca**: Gestiona el registro forestal, supervisa operaciones
- **Trabajador Agricola**: Ejecuta tareas de mantenimiento, plantacion y cosecha
- **Sistema de Riego Automatizado**: Opera de forma autonoma basado en sensores
- **Auditor/Inspector**: Consulta registros persistidos para verificacion

### Flujo de Operaciones Tipico

```
1. REGISTRO --> Se crea un registro forestal con terreno y plantacion
2. PLANTACION --> Se plantan cultivos segun superficie disponible
3. MONITOREO --> Sensores detectan temperatura y humedad continuamente
4. RIEGO AUTOMATICO --> Sistema riega cuando se cumplen condiciones
5. ABSORCION --> Cultivos absorben agua segun estrategias especificas
6. TAREAS --> Trabajadores ejecutan mantenimiento con herramientas
7. COSECHA --> Se recolectan cultivos y empaquetan por tipo
8. PERSISTENCIA --> Datos se guardan para auditoria futura
```

---

## Caracteristicas Principales

### Funcionalidades del Sistema

#### 1. Gestion de Cultivos

- **Creacion dinamica** de 4 tipos de cultivos mediante Factory Pattern
  - **Pino**: Arbol de variedad configurable (Parana, Elliott, etc.)
  - **Olivo**: Arbol con tipo de aceituna (Arbequina, Picual, Manzanilla)
  - **Lechuga**: Hortaliza de invernadero con variedad configurable
  - **Zanahoria**: Hortaliza con opcion de baby carrot

- **Absorcion de agua diferenciada** por tipo
  - Arboles: Absorcion estacional (5L verano, 2L invierno)
  - Hortalizas: Absorcion constante (1-2L independiente de temporada)

- **Crecimiento automatico** para arboles
  - Pino: +0.10m por riego
  - Olivo: +0.01m por riego

#### 2. Sistema de Riego Inteligente

- **Sensores en tiempo real** (patron Observer)
  - Sensor de temperatura: lecturas cada 2 segundos
  - Sensor de humedad: lecturas cada 3 segundos
  - Rangos: -25C a 50C, 0% a 100% humedad

- **Riego automatizado condicional**
  - Se activa cuando:
    - Temperatura entre 8C y 15C, Y
    - Humedad menor a 50%
  - Control cada 2.5 segundos

- **Notificaciones de eventos**
  - Eventos de sensores a observadores suscritos
  - Sistema tipo-seguro con Generics (Observable[float])

#### 3. Gestion de Personal

- **Trabajadores con certificacion medica**
  - Apto medico obligatorio para trabajar
  - Validacion automatica antes de ejecutar tareas
  - Fecha de emision y observaciones medicas

- **Sistema de tareas**
  - Asignacion multiple de tareas por trabajador
  - Ejecucion ordenada por ID (descendente)
  - Estado de tareas (pendiente/completada)
  - Fecha programada para cada tarea

- **Herramientas certificadas**
  - ID unico, nombre y certificacion H&S
  - Asignacion a trabajadores durante tareas

#### 4. Gestion Territorial

- **Tierra**
  - Padron catastral unico
  - Superficie en metros cuadrados
  - Domicilio de ubicacion

- **Plantacion**
  - Nombre identificatorio
  - Control de superficie disponible
  - Lista de cultivos plantados
  - Agua disponible en litros
  - Trabajadores asignados

- **Registro Forestal**
  - Vincula tierra con plantacion
  - Propietario y avaluo fiscal
  - Persistible en disco

#### 5. Operaciones de Negocio

- **Plantacion automatica**
  - Calculo de superficie requerida
  - Validacion de espacio disponible
  - Creacion via Factory Method

- **Riego centralizado**
  - Riega todos los cultivos de una plantacion
  - Verifica agua disponible antes de regar
  - Excepcion si agua insuficiente

- **Cosecha tipada**
  - Cosecha selectiva por tipo de cultivo
  - Empaquetado en cajas genericas tipo-seguras
  - Mostracion de contenido de cajas

- **Fumigacion**
  - Aplicacion de plaguicida a toda la plantacion
  - Registro de tipo de plaguicida aplicado

#### 6. Persistencia de Datos

- **Serializacion con Pickle**
  - Guardado completo de RegistroForestal
  - Directorio configurable (default: `data/`)
  - Nombre de archivo: `{propietario}.dat`

- **Recuperacion de datos**
  - Lectura de registros persistidos
  - Validacion de integridad
  - Manejo de excepciones especificas

---

## Arquitectura del Sistema

### Principios Arquitectonicos

El sistema esta disenado siguiendo principios SOLID:

- **Single Responsibility**: Cada clase tiene una unica razon para cambiar
  - Entidades: Solo contienen datos (DTOs)
  - Servicios: Solo contienen logica de negocio
  - Patrones: Implementaciones aisladas y reutilizables

- **Open/Closed**: Abierto a extension, cerrado a modificacion
  - Nuevos cultivos: Agregar sin modificar factory existente
  - Nuevas estrategias: Implementar interfaz sin cambiar servicios

- **Liskov Substitution**: Subtipos intercambiables
  - Todos los cultivos son Cultivo
  - Todas las estrategias implementan AbsorcionAguaStrategy

- **Interface Segregation**: Interfaces especificas
  - Observer[T]: Generico para cualquier tipo de evento
  - AbsorcionAguaStrategy: Especifico para absorcion

- **Dependency Inversion**: Dependencias de abstracciones
  - Servicios dependen de Strategy (abstraccion), no implementaciones
  - Factory retorna Cultivo (interfaz), no tipos concretos

### Separacion de Capas

```
+----------------------------------+
|        PRESENTACION              |
|  (main.py - Demostracion CLI)    |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE NEGOCIO        |
|  (FincasService, Paquete)        |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE DOMINIO        |
|  (PlantacionService, etc.)       |
+----------------------------------+
                |
                v
+----------------------------------+
|          ENTIDADES               |
|  (Cultivo, Tierra, Trabajador)   |
+----------------------------------+
                |
                v
+----------------------------------+
|      PATRONES / UTILIDADES       |
|  (Factory, Strategy, Observer)   |
+----------------------------------+
```

### Inyeccion de Dependencias

El sistema utiliza inyeccion manual de dependencias:

```python
# Estrategia inyectada en constructor
class PinoService(ArbolService):
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

# Sensores inyectados en controlador
tarea_control = ControlRiegoTask(
    tarea_temp,      # Dependencia inyectada
    tarea_hum,       # Dependencia inyectada
    plantacion,
    plantacion_service
)
```

---

## Patrones de Diseno Implementados

### 1. SINGLETON Pattern

**Ubicacion**: `python_forestacion/servicios/cultivos/cultivo_service_registry.py`

**Problema que resuelve**:
- Garantizar una unica instancia del registro de servicios
- Compartir estado entre todos los servicios del sistema
- Evitar multiples registros inconsistentes

**Implementacion**:
```python
class CultivoServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Thread-safe double-checked locking
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

**Uso en el sistema**:
- Todos los servicios de cultivos comparten el mismo registry
- Elimina cadenas de `isinstance()` mediante dispatch polimorfico
- Acceso: `CultivoServiceRegistry.get_instance()`

**Ventajas**:
- Thread-safe mediante Lock
- Inicializacion perezosa (lazy initialization)
- Punto unico de control

---

### 2. FACTORY METHOD Pattern

**Ubicacion**: `python_forestacion/patrones/factory/cultivo_factory.py`

**Problema que resuelve**:
- Creacion de cultivos sin conocer clases concretas
- Encapsulacion de logica de construccion compleja
- Extensibilidad para nuevos tipos de cultivos

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
```

**Uso en el sistema**:
```python
# PlantacionService usa factory internamente
plantacion_service.plantar(plantacion, "Pino", 5)
# Crea 5 Pinos sin conocer constructor
```

**Ventajas**:
- Codigo cliente independiente de clases concretas
- Facil agregar nuevos cultivos
- Validacion centralizada de especies

---

### 3. OBSERVER Pattern

**Ubicacion**: `python_forestacion/patrones/observer/`

**Problema que resuelve**:
- Notificacion automatica a multiples observadores
- Desacoplamiento entre sensores y consumidores
- Sistema de eventos tipo-seguro

**Implementacion**:
```python
class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento)
```

**Uso en el sistema**:
```python
# Sensor es Observable
class TemperaturaReaderTask(threading.Thread, Observable[float]):
    def run(self):
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            # Notifica a todos los observadores
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)

# ControlRiegoTask es Observer
class ControlRiegoTask(Observer[float]):
    def actualizar(self, evento: float) -> None:
        # Recibe notificacion automaticamente
        self._ultima_temperatura = evento
```

**Ventajas**:
- Tipo-seguro con Generics
- Desacoplamiento total
- Multiples observadores permitidos

---

### 4. STRATEGY Pattern

**Ubicacion**: `python_forestacion/patrones/strategy/`

**Problema que resuelve**:
- Algoritmos de absorcion intercambiables
- Eliminar condicionales tipo if/else
- Permitir cambios en tiempo de ejecucion

**Implementacion**:
```python
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
        return self._cantidad  # Siempre igual
```

**Uso en el sistema**:
```python
# Inyeccion de estrategia en servicio
class PinoService(ArbolService):
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())  # Arboles: seasonal

class ZanahoriaService(CultivoService):
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))  # Hortalizas: constante
```

**Ventajas**:
- Algoritmos intercambiables
- Sin modificar codigo cliente
- Testeable independientemente

---

### 5. REGISTRY Pattern (Bonus)

**Ubicacion**: `python_forestacion/servicios/cultivos/cultivo_service_registry.py`

**Problema que resuelve**:
- Eliminar cascadas de `isinstance()`
- Dispatch polimorfico basado en tipo
- Punto unico de registro de servicios

**Implementacion**:
```python
class CultivoServiceRegistry:
    def __init__(self):
        # Registro de handlers por tipo
        self._absorber_agua_handlers = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

    def absorber_agua(self, cultivo: Cultivo) -> int:
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")

        # Dispatch polimorfico
        return self._absorber_agua_handlers[tipo](cultivo)
```

**Antes (con isinstance)**:
```python
if isinstance(cultivo, Pino):
    return pino_service.absorver_agua(cultivo)
elif isinstance(cultivo, Olivo):
    return olivo_service.absorver_agua(cultivo)
elif isinstance(cultivo, Lechuga):
    return lechuga_service.absorver_agua(cultivo)
# ... 4 mas
```

**Despues (con Registry)**:
```python
return registry.absorber_agua(cultivo)  # Despacho automatico
```

---

## Requisitos del Sistema

### Requisitos de Software

- **Python 3.13** o superior
- **Sistema Operativo**: Windows, Linux, macOS
- **Modulos Estandar**: Solo biblioteca estandar de Python (sin dependencias externas)

### Requisitos de Hardware

- **RAM**: Minimo 512 MB
- **Disco**: 50 MB libres
- **Procesador**: Cualquier procesador moderno (1 GHz+)

---

## Instalacion

### 1. Clonar el Repositorio

```bash
git clone https://github.com/usuario/python-forestal.git
cd python-forestal
```

### 2. Crear Entorno Virtual

#### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Verificar Instalacion

```bash
python --version
# Debe mostrar Python 3.13 o superior
```

### 4. Ejecutar Sistema

```bash
python main.py
```

**Salida esperada**:
```
======================================================================
         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO
======================================================================

----------------------------------------------------------------------
  PATRON SINGLETON: Inicializando servicios
----------------------------------------------------------------------
[OK] Todos los servicios comparten la misma instancia del Registry

1. Creando tierra con plantacion...
...
======================================================================
              EJEMPLO COMPLETADO EXITOSAMENTE
======================================================================
  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)
  [OK] FACTORY     - Creacion de cultivos
  [OK] OBSERVER    - Sistema de sensores y eventos
  [OK] STRATEGY    - Algoritmos de absorcion de agua
======================================================================
```

---

## Uso del Sistema

### Ejemplo Basico

```python
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

# 1. Crear terreno con plantacion
tierra_service = TierraService()
terreno = tierra_service.crear_tierra_con_plantacion(
    id_padron_catastral=1,
    superficie=10000.0,  # m2
    domicilio="Agrelo, Mendoza",
    nombre_plantacion="Finca del Madero"
)

# 2. Obtener plantacion
plantacion = terreno.get_finca()

# 3. Plantar cultivos (usa Factory Method internamente)
plantacion_service = PlantacionService()
plantacion_service.plantar(plantacion, "Pino", 5)
plantacion_service.plantar(plantacion, "Olivo", 3)

# 4. Regar plantacion (usa Strategy Pattern internamente)
plantacion_service.regar(plantacion)

# 5. Cosechar
plantacion_service.cosechar(plantacion)
```

### Sistema de Riego Automatizado

```python
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Crear sensores (Observable)
tarea_temp = TemperaturaReaderTask()
tarea_hum = HumedadReaderTask()

# Crear controlador (Observer)
tarea_control = ControlRiegoTask(
    tarea_temp,
    tarea_hum,
    plantacion,
    plantacion_service
)

# Iniciar threads daemon
tarea_temp.start()
tarea_hum.start()
tarea_control.start()

# Sistema funciona automaticamente
time.sleep(20)  # Dejarlo funcionar 20 segundos

# Detener sistema
tarea_temp.detener()
tarea_hum.detener()
tarea_control.detener()
```

### Persistencia de Datos

```python
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

# Crear registro
registro = RegistroForestal(
    id_padron=1,
    tierra=terreno,
    plantacion=plantacion,
    propietario="Juan Perez",
    avaluo=50309233.55
)

# Persistir
registro_service = RegistroForestalService()
registro_service.persistir(registro)
# Crea archivo: data/Juan Perez.dat

# Recuperar
registro_leido = RegistroForestalService.leer_registro("Juan Perez")
registro_service.mostrar_datos(registro_leido)
```

---

## Estructura del Proyecto

```
PythonForestal/
|
+-- main.py                          # Punto de entrada del sistema
+-- CLAUDE.md                        # Guia para Claude Code
+-- README.md                        # Este archivo
+-- USER_STORIES.md                  # Historias de usuario detalladas
+-- RUBRICA_EVALUACION.md            # Rubrica de evaluacion tecnica
+-- RUBRICA_AUTOMATIZADA.md          # Rubrica para automatizacion n8n
|
+-- .venv/                           # Entorno virtual Python
|
+-- data/                            # Datos persistidos (archivos .dat)
|
+-- python_forestacion/              # Paquete principal
    |
    +-- __init__.py
    +-- constantes.py                # Constantes centralizadas del sistema
    |
    +-- entidades/                   # Objetos de dominio (DTOs)
    |   +-- __init__.py
    |   |
    |   +-- cultivos/                # Cultivos del sistema
    |   |   +-- __init__.py
    |   |   +-- cultivo.py           # Interfaz base
    |   |   +-- arbol.py             # Base para arboles
    |   |   +-- hortaliza.py         # Base para hortalizas
    |   |   +-- pino.py              # Arbol tipo Pino
    |   |   +-- olivo.py             # Arbol tipo Olivo
    |   |   +-- lechuga.py           # Hortaliza tipo Lechuga
    |   |   +-- zanahoria.py         # Hortaliza tipo Zanahoria
    |   |   +-- tipo_aceituna.py     # Enum de tipos de aceituna
    |   |
    |   +-- terrenos/                # Gestion territorial
    |   |   +-- __init__.py
    |   |   +-- tierra.py            # Terreno catastral
    |   |   +-- plantacion.py        # Plantacion agricola
    |   |   +-- registro_forestal.py # Registro completo
    |   |
    |   +-- personal/                # Recursos humanos
    |       +-- __init__.py
    |       +-- trabajador.py        # Trabajador agricola
    |       +-- herramienta.py       # Herramienta de trabajo
    |       +-- tarea.py             # Tarea asignada
    |       +-- apto_medico.py       # Certificacion medica
    |
    +-- servicios/                   # Logica de negocio
    |   +-- __init__.py
    |   |
    |   +-- cultivos/                # Servicios de cultivos
    |   |   +-- __init__.py
    |   |   +-- cultivo_service.py              # Servicio base
    |   |   +-- arbol_service.py                # Servicio base arboles
    |   |   +-- pino_service.py                 # Servicio Pino
    |   |   +-- olivo_service.py                # Servicio Olivo
    |   |   +-- lechuga_service.py              # Servicio Lechuga
    |   |   +-- zanahoria_service.py            # Servicio Zanahoria
    |   |   +-- cultivo_service_registry.py     # Registry + Singleton
    |   |
    |   +-- terrenos/                # Servicios territoriales
    |   |   +-- __init__.py
    |   |   +-- tierra_service.py               # Servicio Tierra
    |   |   +-- plantacion_service.py           # Servicio Plantacion
    |   |   +-- registro_forestal_service.py    # Servicio Registro
    |   |
    |   +-- personal/                # Servicios de personal
    |   |   +-- __init__.py
    |   |   +-- trabajador_service.py           # Servicio Trabajador
    |   |
    |   +-- negocio/                 # Servicios de alto nivel
    |       +-- __init__.py
    |       +-- fincas_service.py               # Operaciones fincas
    |       +-- paquete.py                      # Empaquetado generico
    |
    +-- patrones/                    # Implementaciones de patrones
    |   +-- __init__.py
    |   |
    |   +-- singleton/               # Patron Singleton
    |   |   +-- __init__.py
    |   |
    |   +-- factory/                 # Patron Factory Method
    |   |   +-- __init__.py
    |   |   +-- cultivo_factory.py              # Factory de cultivos
    |   |
    |   +-- observer/                # Patron Observer
    |   |   +-- __init__.py
    |   |   +-- observable.py                   # Clase Observable[T]
    |   |   +-- observer.py                     # Interfaz Observer[T]
    |   |   +-- eventos/
    |   |       +-- __init__.py
    |   |       +-- evento_sensor.py            # Evento de sensores
    |   |       +-- evento_plantacion.py        # Evento de plantacion
    |   |
    |   +-- strategy/                # Patron Strategy
    |       +-- __init__.py
    |       +-- absorcion_agua_strategy.py      # Interfaz Strategy
    |       +-- impl/
    |           +-- __init__.py
    |           +-- absorcion_seasonal_strategy.py      # Seasonal
    |           +-- absorcion_constante_strategy.py     # Constante
    |
    +-- riego/                       # Sistema de riego automatizado
    |   +-- __init__.py
    |   |
    |   +-- sensores/                # Sensores ambientales
    |   |   +-- __init__.py
    |   |   +-- temperatura_reader_task.py      # Sensor temperatura
    |   |   +-- humedad_reader_task.py          # Sensor humedad
    |   |
    |   +-- control/                 # Control de riego
    |       +-- __init__.py
    |       +-- control_riego_task.py           # Controlador
    |
    +-- excepciones/                 # Excepciones personalizadas
        +-- __init__.py
        +-- forestacion_exception.py            # Excepcion base
        +-- superficie_insuficiente_exception.py
        +-- agua_agotada_exception.py
        +-- persistencia_exception.py
        +-- mensajes_exception.py               # Mensajes centralizados
```

---

## Modulos del Sistema

### Modulo: `entidades`

**Responsabilidad**: Objetos de dominio puros (DTOs - Data Transfer Objects)

**Caracteristicas**:
- Solo contienen datos y getters/setters
- NO contienen logica de negocio
- Campos privados con encapsulacion

**Clases principales**:
- `Cultivo`: Interfaz base para todos los cultivos
- `Arbol`: Base para cultivos arboreos (Pino, Olivo)
- `Hortaliza`: Base para cultivos horticolas (Lechuga, Zanahoria)
- `Tierra`: Terreno catastral con superficie
- `Plantacion`: Conjunto de cultivos y trabajadores
- `Trabajador`: Persona con tareas asignadas

---

### Modulo: `servicios`

**Responsabilidad**: Logica de negocio del sistema

**Caracteristicas**:
- Servicios sin estado (stateless)
- Operaciones sobre entidades
- Orquestacion de patrones

**Servicios principales**:
- `PlantacionService`: Plantar, regar, cosechar, fumigar
- `TrabajadorService`: Asignar tareas, verificar apto medico
- `RegistroForestalService`: Persistir y recuperar registros
- `FincasService`: Operaciones de alto nivel en fincas

---

### Modulo: `patrones`

**Responsabilidad**: Implementaciones de patrones de diseno

**Patrones incluidos**:
1. **Singleton**: `CultivoServiceRegistry`
2. **Factory Method**: `CultivoFactory`
3. **Observer**: `Observable[T]` / `Observer[T]`
4. **Strategy**: `AbsorcionAguaStrategy` + implementaciones

---

### Modulo: `riego`

**Responsabilidad**: Sistema de riego automatizado con threads

**Componentes**:
- **Sensores** (Observable):
  - `TemperaturaReaderTask`: Lee temperatura cada 2s
  - `HumedadReaderTask`: Lee humedad cada 3s

- **Control** (Observer):
  - `ControlRiegoTask`: Observa sensores y riega automaticamente

**Modelo de threading**:
- Threads daemon (finalizan con main)
- Graceful shutdown con `threading.Event`
- Timeouts configurables

---

### Modulo: `excepciones`

**Responsabilidad**: Excepciones de dominio especificas

**Jerarquia**:
```
ForestacionException (base)
  +-- SuperficieInsuficienteException
  +-- AguaAgotadaException
  +-- PersistenciaException
```

**Caracteristicas**:
- Mensajes separados: usuario vs tecnico
- Contexto especifico del error
- Causas encadenadas

---

## Documentacion Tecnica

### Convenciones de Codigo

#### PEP 8 Compliance (100%)

- **Nombres de variables**: `snake_case`
- **Nombres de clases**: `PascalCase`
- **Constantes**: `UPPER_SNAKE_CASE` en `constantes.py`
- **Privados**: Prefijo `_nombre`

#### Docstrings (Google Style)

```python
def metodo(self, parametro: str) -> int:
    """
    Descripcion breve del metodo.

    Args:
        parametro: Descripcion del parametro

    Returns:
        Descripcion del valor de retorno

    Raises:
        ValueError: Cuando ocurre validacion
    """
```

#### Type Hints

```python
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from modulo import Clase  # Evita imports circulares

def metodo(self, lista: List[int]) -> Optional[str]:
    pass
```

### Configuracion de Constantes

Todas las constantes en `constantes.py`:

```python
# Agua
AGUA_MINIMA = 10
AGUA_INICIAL_PLANTACION = 500

# Riego
TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50

# Cultivos
SUPERFICIE_PINO = 2.0
AGUA_INICIAL_PINO = 2
ABSORCION_SEASONAL_VERANO = 5
```

**Regla**: NUNCA hardcodear valores magicos en el codigo.

### Manejo de Excepciones

```python
try:
    plantacion_service.plantar(plantacion, "Pino", 100)
except SuperficieInsuficienteException as e:
    print(e.get_user_message())
    print(f"Requerida: {e.get_superficie_requerida()}")
    print(f"Disponible: {e.get_superficie_disponible()}")
except ForestacionException as e:
    print(e.get_full_message())
```

---

## Testing y Validacion

### Ejecucion del Sistema Completo

El archivo `main.py` contiene un test de integracion completo que valida:

1. [x] Patron Singleton - Instancia unica compartida
2. [x] Patron Factory - Creacion de 4 tipos de cultivos
3. [x] Patron Observer - Sensores y notificaciones
4. [x] Patron Strategy - Absorcion diferenciada
5. [x] Plantacion y control de superficie
6. [x] Riego automatizado
7. [x] Gestion de trabajadores con apto medico
8. [x] Cosecha y empaquetado tipado
9. [x] Persistencia y recuperacion
10. [x] Threading y graceful shutdown

### Validacion Manual

```bash
python main.py
```

**Criterios de exito**:
- No errores de importacion
- No excepciones no controladas
- Mensaje final: `EJEMPLO COMPLETADO EXITOSAMENTE`
- Archivo creado: `data/Juan Perez.dat`

### Casos de Prueba

#### Caso 1: Superficie Insuficiente
```python
# Plantacion requiere mas superficie de la disponible
try:
    plantacion_service.plantar(plantacion, "Pino", 10000)
except SuperficieInsuficienteException as e:
    assert e.get_superficie_requerida() > e.get_superficie_disponible()
```

#### Caso 2: Agua Agotada
```python
# Riego sin agua disponible
plantacion.set_agua_disponible(0)
try:
    plantacion_service.regar(plantacion)
except AguaAgotadaException as e:
    assert "agotada" in e.get_user_message().lower()
```

#### Caso 3: Trabajador Sin Apto
```python
# Trabajador sin apto medico no puede trabajar
trabajador = Trabajador(12345678, "Test", [])
resultado = trabajador_service.trabajar(trabajador, date.today(), herramienta)
assert resultado == False
```

---

## Contribucion

### Como Agregar un Nuevo Tipo de Cultivo

#### Paso 1: Definir Constantes

En `constantes.py`:
```python
# Constantes del nuevo cultivo
SUPERFICIE_TOMATE = 0.25
AGUA_INICIAL_TOMATE = 2
```

#### Paso 2: Crear Entidad

En `entidades/cultivos/tomate.py`:
```python
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_TOMATE,
    SUPERFICIE_TOMATE
)

class Tomate(Hortaliza):
    """Entidad Tomate - solo datos."""

    def __init__(self, variedad: str):
        super().__init__(
            agua=AGUA_INICIAL_TOMATE,
            superficie=SUPERFICIE_TOMATE,
            invernadero=True
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        self._variedad = variedad
```

#### Paso 3: Crear Servicio

En `servicios/cultivos/tomate_service.py`:
```python
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

class TomateService(CultivoService):
    """Servicio para Tomate."""

    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))

    def mostrar_datos(self, cultivo: 'Tomate') -> None:
        super().mostrar_datos(cultivo)
        print(f"Variedad: {cultivo.get_variedad()}")
```

#### Paso 4: Registrar en Registry

En `cultivo_service_registry.py`:
```python
from python_forestacion.entidades.cultivos.tomate import Tomate
from python_forestacion.servicios.cultivos.tomate_service import TomateService

class CultivoServiceRegistry:
    def __init__(self):
        self._tomate_service = TomateService()

        self._absorber_agua_handlers[Tomate] = self._absorber_agua_tomate
        self._mostrar_datos_handlers[Tomate] = self._mostrar_datos_tomate

    def _absorber_agua_tomate(self, cultivo):
        return self._tomate_service.absorver_agua(cultivo)

    def _mostrar_datos_tomate(self, cultivo):
        return self._tomate_service.mostrar_datos(cultivo)
```

#### Paso 5: Registrar en Factory

En `cultivo_factory.py`:
```python
@staticmethod
def _crear_tomate() -> Tomate:
    from python_forestacion.entidades.cultivos.tomate import Tomate
    return Tomate(variedad="Cherry")

@staticmethod
def crear_cultivo(especie: str) -> Cultivo:
    factories = {
        # ... existentes
        "Tomate": CultivoFactory._crear_tomate
    }
```

#### Paso 6: Usar el Nuevo Cultivo

```python
plantacion_service.plantar(plantacion, "Tomate", 10)
```

---

## Licencia

Este proyecto es de codigo abierto y esta disponible bajo la licencia MIT.

---

## Contacto y Soporte

- **Documentacion**: Ver `CLAUDE.md` para guia tecnica detallada
- **Historias de Usuario**: Ver `USER_STORIES.md` para casos de uso
- **Rubrica de Evaluacion**: Ver `RUBRICA_EVALUACION.md`

---

## Notas Adicionales

### Compatibilidad con Windows

El sistema fue desarrollado y probado en Windows. Consideraciones:

- **NO usar emojis** en print (problema de encoding)
- **NO usar caracteres Unicode especiales** en consola
- Usar solo ASCII estandar: `[OK]`, `[!]`, `[INFO]`

### Rendimiento

- Sistema optimizado para operaciones locales
- Threads livianos para sensores
- Persistencia con Pickle (rapida pero NO para produccion)

### Limitaciones Conocidas

1. Pickle NO es seguro para datos no confiables
2. Sistema single-process (no distribuido)
3. Sin base de datos relacional
4. Sin interfaz grafica (solo CLI)

**Este es un proyecto EDUCATIVO** enfocado en patrones de diseno, NO en produccion real.

---

**Ultima actualizacion**: Octubre 2025
**Version del sistema**: 1.0.0
**Python requerido**: 3.13+
