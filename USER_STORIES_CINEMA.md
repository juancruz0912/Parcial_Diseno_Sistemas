# Historias de Usuario - Sistema de Venta de Entradas de Cine

**Proyecto**: CineApp
**Version**: 1.0.0
**Fecha**: Octubre 2025
**Metodologia**: User Story Mapping

---

## Indice

1. [Epic 1: Gestion de Peliculas y Funciones](#epic-1-gestion-de-peliculas-y-funciones)
2. [Epic 2: Compra de Entradas](#epic-2-compra-de-entradas)
3. [Epic 3: Registro y Notificaciones a Clientes](#epic-3-registro-y-notificaciones-a-clientes)
4. [Epic 4: Estrategias de Precios](#epic-4-estrategias-de-precios)
5. [Historias Tecnicas (Patrones de Diseno)](#historias-tecnicas-patrones-de-diseno)

---

## Epic 1: Gestion de Peliculas y Funciones

### US-001: Agregar nueva pelicula a la cartelera

**Como** administrador del cine
**Quiero** agregar nuevas peliculas a la cartelera con su informacion relevante (titulo, sinopsis, genero, duracion)
**Para** que los clientes puedan ver las peliculas disponibles y el sistema pueda notificarles.

#### Criterios de Aceptacion

- [x] El sistema debe permitir registrar una pelicula con titulo, sinopsis, genero y duracion en minutos.
- [x] La pelicula debe ser anadida a una lista centralizada en el `CineManager` (Singleton).
- [x] Al agregar una pelicula nueva, se debe disparar un evento para notificar a los clientes suscritos a novedades generales (Observer).

#### Detalles Tecnicos

**Clase**: `Pelicula` (`cinema_app/entidades/pelicula.py`)
**Singleton**: `CineManager` (`cinema_app/patrones/singleton/cine_manager.py`)

**Explicacion del Proceso**:
El administrador interactua con el sistema para dar de alta una nueva pelicula. Esta operacion es centralizada por el `CineManager`, que es la unica fuente de verdad para la cartelera. Una vez que la pelicula es anadida exitosamente, el `CineManager` (actuando como `Observable`) emite una notificacion. Los `Cliente`s (actuando como `Observer`s) reciben esta notificacion y pueden reaccionar a ella, por ejemplo, mostrando un mensaje al usuario.

**Codigo de ejemplo**:
```python
from cinema_app.patrones.singleton.cine_manager import CineManager
from cinema_app.entidades.pelicula import Pelicula

# 1. Obtener instancia unica del gestor
cine_manager = CineManager.get_instance()

# 2. Crear la entidad Pelicula
nueva_pelicula = Pelicula(
    titulo="Inception",
    sinopsis="Un ladron que roba secretos corporativos a traves del uso de la tecnologia de compartir suenos.",
    genero="Ciencia Ficcion",
    duracion=148
)

# 3. El manager centraliza la operacion y notifica a los observadores internamente
cine_manager.agregar_pelicula(nueva_pelicula)
```

**Trazabilidad**: `main.py` (simulado) lineas 20-30

---

### US-002: Programar funcion para una pelicula

**Como** administrador del cine
**Quiero** programar funciones para las peliculas en diferentes salas y horarios
**Para** que los clientes puedan elegir cuando ver una pelicula y comprar sus entradas.

#### Criterios de Aceptacion

- [x] Se debe poder asociar una `Pelicula` existente a una `Sala` y un `datetime` de inicio.
- [x] Cada `Sala` tiene un nombre/numero y una capacidad finita de asientos (ej. 100).
- [x] Cada `Funcion` debe autogenerar un mapa de asientos (ej. un diccionario de 'A1' a 'J10') inicializados como `disponible`.
- [x] Al programar una nueva funcion, se debe notificar a los clientes interesados (patron Observer).

#### Detalles Tecnicos

**Clases**: `Funcion` (`cinema_app/entidades/funcion.py`), `Sala` (`cinema_app/entidades/sala.py`)
**Singleton**: `CineManager`

**Explicacion del Proceso**:
El `CineManager` orquesta la creacion de una `Funcion`. Primero, localiza la `Pelicula` y la `Sala` en sus registros internos. Luego, instancia un objeto `Funcion`, que en su constructor genera la matriz de asientos disponibles. Finalmente, el `CineManager` agrega esta funcion a su lista y notifica a los observadores sobre el nuevo evento, pasando detalles como el nombre de la pelicula y el horario.

**Codigo de ejemplo**:
```python
from datetime import datetime

# El manager busca la pelicula y la sala por sus IDs o nombres
pelicula = cine_manager.buscar_pelicula("Inception")
sala = cine_manager.get_sala("Sala IMAX")

# Programar la funcion para una fecha y hora especificas
fecha_hora = datetime(2025, 11, 1, 22, 0) # 1 de Noviembre a las 22:00
cine_manager.programar_funcion(pelicula, sala, fecha_hora)
```

**Notificacion (Observer) dentro de `CineManager`**:
```python
# Dentro de cine_manager.programar_funcion()
def programar_funcion(self, pelicula, sala, fecha_hora):
    # ... logica para crear la funcion ...
    self._funciones.append(nueva_funcion)
    
    # Notificar a los observadores
    evento = {
        'tipo': 'NUEVA_FUNCION',
        'pelicula': pelicula.titulo,
        'sala': sala.nombre,
        'fecha': fecha_hora.strftime("%d/%m/%Y a las %H:%M")
    }
    self.notificar_observadores(evento)
```

**Trazabilidad**: `main.py` (simulado) lineas 35-45

---

## Epic 2: Compra de Entradas

### US-003: Generar compra de entrada con Factory Method

**Como** cliente
**Quiero** generar la compra de una entrada para una funcion y asiento especifico
**Para** asegurar mi lugar en el cine.

#### Criterios de Aceptacion

- [x] El sistema debe crear un objeto `Entrada` usando un `EntradaFactory` para encapsular la logica de creacion.
- [x] El Factory debe poder crear diferentes tipos de entrada: `EntradaEstandar`, `Entrada3D`, `EntradaVIP`.
- [x] La entrada generada debe contener la pelicula, funcion, asiento y un precio base.
- [x] El asiento seleccionado debe marcarse como `ocupado` en el mapa de asientos de la `Funcion`.
- [x] Si el asiento ya esta ocupado, la operacion debe fallar con un error claro.

#### Detalles Tecnicos

**Factory**: `EntradaFactory` (`cinema_app/patrones/factory/entrada_factory.py`)
**Productos**: `EntradaEstandar`, `Entrada3D`, `EntradaVIP` (subclases de `Entrada` en `cinema_app/entidades/entrada.py`)
**Servicio**: `CineManager.vender_entrada()`

**Explicacion del Proceso**:
1.  El cliente elige una funcion y un asiento disponible.
2.  La peticion llega al `CineManager`, que valida si el asiento sigue libre en la `Funcion` seleccionada.
3.  Si esta libre, el `CineManager` invoca al `EntradaFactory.crear_entrada()`, pasandole el tipo de entrada requerido (ej. '3D', 'VIP'). El tipo podria depender de la `Sala`.
4.  El Factory instancia la subclase correcta de `Entrada` (ej. `Entrada3D`) y le asigna un precio base.
5.  El `CineManager` recibe la entrada creada, marca el asiento como `ocupado` y la devuelve al cliente.

**Codigo de ejemplo**:
```python
# El cliente selecciona funcion y asiento
funcion_elegida = cine_manager.get_funciones_por_pelicula("Inception")[0]
asiento_elegido = "F8"

# El manager gestiona la venta, determinando el tipo de entrada y la estrategia de precio
tipo_entrada = funcion_elegida.sala.tipo_proyeccion # ej. "3D"
estrategia_precio = EstrategiaPrecioNormal() # Estrategia por defecto

entrada_comprada = cine_manager.vender_entrada(
    funcion=funcion_elegida, 
    asiento=asiento_elegido, 
    tipo_entrada=tipo_entrada,
    estrategia_precio=estrategia_precio
)

if entrada_comprada:
    print(f"Entrada comprada con exito para el asiento {asiento_elegido}!")
    print(f"Tipo: {type(entrada_comprada).__name__}")
    print(f"Precio final: ${entrada_comprada.get_precio_final():.2f}")
```

**Trazabilidad**: `main.py` (simulado) lineas 70-85

---

## Epic 3: Registro y Notificaciones a Clientes

### US-004: Suscribirse a notificaciones (Observer)

**Como** cliente registrado
**Quiero** suscribirme para recibir notificaciones sobre novedades del cine
**Para** mantenerme informado de estrenos y nuevas funciones.

#### Criterios de Aceptacion

- [x] El cliente debe poder agregarse como `Observer` al `CineManager` (`Observable`).
- [x] El `CineManager` debe mantener una lista de observadores suscritos de forma segura.
- [x] El cliente debe implementar la interfaz `Observer` con un metodo `actualizar(evento)` que define como reacciona a la notificacion.

#### Detalles Tecnicos

**Patron**: Observer
**Observable**: `CineManager` (contiene el estado y notifica los cambios)
**Observer**: `Cliente` (quiere ser notificado de los cambios)

**Explicacion del Proceso**:
El patron Observer desacopla al emisor de los receptores. El `CineManager` no necesita saber que hacen los clientes con las notificaciones. Su unica responsabilidad es mantener una lista de suscriptores y notificarles cuando ocurre un evento relevante (ej. `agregar_pelicula`). El `Cliente`, al implementar la interfaz `Observer`, se compromete a tener un metodo `actualizar`, permitiendo que el `CineManager` lo invoque polimorficamente sin conocer su implementacion interna.

**Codigo de ejemplo**:
```python
# Crear clientes
cliente_ana = Cliente(nombre="Ana Gomez", email="ana.gomez@example.com")
cliente_luis = Cliente(nombre="Luis Diaz", email="luis.diaz@example.com")

# Ana quiere recibir notificaciones de todo
cine_manager.suscribir_observador(cliente_ana)

# Luis tambien se suscribe
cine_manager.suscribir_observador(cliente_luis)

# ... mas tarde, el admin agrega una pelicula, y ambos reciben la notificacion ...

# En algun momento, Luis decide desuscribirse para no recibir mas notificaciones
cine_manager.desuscribir_observador(cliente_luis)
```

**Implementacion detallada en Cliente**:
```python
# En cinema_app/entidades/cliente.py
from cinema_app.patrones.observer.observer import Observer

class Cliente(Observer):
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def actualizar(self, evento: dict) -> None:
        # Logica de reaccion a la notificacion
        # Podria enviar un email, una notificacion push, o simplemente imprimir
        print(f"--- Notificacion para {self.nombre} ({self.email}) ---")
        if evento['tipo'] == "NUEVA_PELICULA":
            print(f"> ¡Nuevo Estreno! Ya puedes ver '{evento['titulo']}'.")
        elif evento['tipo'] == "NUEVA_FUNCION":
            print(f"> ¡Nueva funcion disponible para '{evento['pelicula']}' en la sala {evento['sala']}!\n  Fecha: {evento['fecha']}")
        print("-----------------------------------------------------")
```

**Trazabilidad**: `main.py` (simulado) lineas 50-55

---

## Epic 4: Estrategias de Precios

### US-005: Aplicar estrategia de precio a la entrada (Strategy)

**Como** administrador del cine
**Quiero** definir diferentes estrategias para calcular el precio final de las entradas
**Para** poder ofrecer descuentos (dia de semana, estudiante) y precios especiales (salas premium).

#### Criterios de Aceptacion

- [x] El sistema debe permitir definir algoritmos de calculo de precios que implementen una interfaz comun `EstrategiaPrecio`.
- [x] Ejemplos: `EstrategiaPrecioNormal`, `EstrategiaDescuentoSemanal`, `EstrategiaPrecioEstudiante`.
- [x] El objeto `Entrada` (Contexto) debe tener una referencia a un objeto de estrategia de precio.
- [x] El `CineManager` inyecta la estrategia adecuada en la `Entrada` en el momento de la venta.
- [x] El precio final se calcula delegando la operacion a la estrategia asignada, desacoplando la `Entrada` de la logica de precios.

#### Detalles Tecnicos

**Patron**: Strategy
**Contexto**: `Entrada` (el objeto cuyo comportamiento cambia)
**Interfaz**: `EstrategiaPrecio` (`cinema_app/patrones/strategy/estrategia_precio.py`)
**Implementaciones**: `EstrategiaPrecioNormal`, `EstrategiaDescuentoSemanal` (`cinema_app/patrones/strategy/impl/`)

**Explicacion del Proceso**:
El patron Strategy permite definir una familia de algoritmos, encapsular cada uno de ellos y hacerlos intercambiables. En este caso, la `Entrada` no sabe como se calcula un descuento; solo sabe que tiene un objeto `EstrategiaPrecio` que puede hacerlo. Al momento de la venta, el `CineManager` puede decidir que estrategia aplicar (ej. si es martes, aplica `EstrategiaDescuentoSemanal`). Esta estrategia se `inyecta` en el objeto `Entrada`. Cuando se llama a `entrada.get_precio_final()`, este metodo simplemente invoca al metodo `calcular()` de la estrategia que tenga asignada.

**Codigo de ejemplo**:
```python
from cinema_app.patrones.strategy.impl.estrategia_descuento_semanal import EstrategiaDescuentoSemanal
from cinema_app.patrones.strategy.impl.estrategia_precio_normal import EstrategiaPrecioNormal
from datetime import date

# ... se crea la entrada con un precio base a traves del factory ...
# entrada = factory.crear_entrada('3D', ...)

# El CineManager decide que estrategia aplicar
hoy = date.today()
if hoy.weekday() < 4: # Lunes a Jueves (0-3)
    print("Aplicando descuento de dia de semana!")
    estrategia = EstrategiaDescuentoSemanal(descuento_porcentual=25)
else: # Fin de semana
    print("Aplicando precio normal de fin de semana.")
    estrategia = EstrategiaPrecioNormal()

# Se inyecta la estrategia en la entrada
entrada_comprada.set_estrategia_precio(estrategia)

# Se calcula el precio final delegando a la estrategia
precio_final = entrada_comprada.get_precio_final()

print(f"Precio base: ${entrada_comprada.get_precio_base():.2f}")
print(f"Precio final con estrategia '{type(estrategia).__name__}': ${precio_final:.2f}")
```

**Trazabilidad**: `main.py` (simulado) lineas 90-105

---

## Historias Tecnicas (Patrones de Diseno)

### US-TECH-001: Implementar Singleton para CineManager

**Como** arquitecto de software
**Quiero** garantizar una unica instancia del `CineManager` en toda la aplicacion
**Para** tener un punto de acceso global y consistente que gestione un estado compartido (cartelera, funciones, clientes), evitando conflictos y duplicidad de datos.

#### Criterios de Aceptacion

- [x] Implementar el patron Singleton de forma `thread-safe` para prevenir condiciones de carrera en entornos multihilo.
- [x] Utilizar `double-checked locking` con un `threading.Lock` para una inicializacion perezosa (lazy) y eficiente.
- [x] El constructor `__new__` debe controlar la creacion o lanzar un error si se intenta instanciar directamente.

#### Detalles Tecnicos

**Clase**: `CineManager` (`cinema_app/patrones/singleton/cine_manager.py`)
**Patron**: Singleton

**Justificacion de Diseno**:
El `CineManager` actua como el corazon del sistema, manteniendo listas de peliculas, funciones y clientes que deben ser consistentes en toda la aplicacion. Si multiples instancias existieran, una parte del sistema podria agregar una pelicula y otra parte no la veria, llevando a un estado inconsistente. El Singleton asegura que todos los componentes del sistema operen sobre la misma informacion. La implementacion `thread-safe` es crucial si, por ejemplo, un hilo de administrador agrega una pelicula mientras multiples hilos de clientes consultan la cartelera.

**Implementacion**:
```python
from threading import Lock

class CineManager: # Tambien heredaria de Observable
    _instance = None
    _lock = Lock()

    def __new__(cls):
        # Prevenir instanciacion directa: 'CineManager()' lanzara error
        raise RuntimeError("No se puede instanciar directamente. Use get_instance().")

    @classmethod
    def get_instance(cls):
        if cls._instance is None: # Primera verificacion (sin bloqueo)
            with cls._lock: # Bloqueo adquirido solo si la instancia es nula
                if cls._instance is None: # Segunda verificacion (dentro del bloqueo)
                    print("Creando la unica instancia de CineManager...")
                    cls._instance = super().__new__(cls)
                    # Inicializar estado interno una sola vez
                    cls._instance._inicializar_listas()
        return cls._instance

    def _inicializar_listas(self):
        self._peliculas = []
        self._funciones = []
        self._clientes = []
        self._observadores = []
```

### US-TECH-002: Implementar Observer para Notificaciones

**Como** arquitecto de software
**Quiero** implementar el patron Observer para el sistema de notificaciones
**Para** desacoplar completamente el `CineManager` (el sujeto que publica eventos) de los `Cliente`s (los observadores que reaccionan a ellos), permitiendo un sistema extensible.

#### Criterios de Aceptacion

- [x] Crear una interfaz abstracta `Observer` con un metodo `actualizar(evento)`.
- [x] Crear una clase base o mixin `Observable` con metodos `suscribir_observador`, `desuscribir_observador` y `notificar_observadores`.
- [x] `CineManager` debe actuar como `Observable` (heredando o componiendo).
- [x] `Cliente` debe implementar la interfaz `Observer`.

#### Detalles Tecnicos

**Interfaces**: `Observable`, `Observer` (`cinema_app/patrones/observer/`)

**Justificacion de Diseno**:
Sin este patron, cada vez que el `CineManager` realiza una accion que requiere notificacion (ej. `agregar_pelicula`), tendria que contener logica especifica para notificar: `si es notificacion por email, hacer X; si es por SMS, hacer Y`. Esto crea un acoplamiento fuerte. Con Observer, el `CineManager` solo necesita iterar sobre su lista de observadores y llamar a `observador.actualizar(evento)`. No sabe ni le importa lo que cada observador hace. Manana podriamos anadir un `SistemaDeEstadisticasObserver` que actualiza un dashboard, sin tocar una sola linea del `CineManager`.

**Implementacion (Observable)**:
```python
# cinema_app/patrones/observer/observable.py
from .observer import Observer

class Observable:
    def __init__(self):
        self._observadores: list[Observer] = []

    def suscribir_observador(self, observador: Observer):
        if observador not in self._observadores:
            self._observadores.append(observador)

    def desuscribir_observador(self, observador: Observer):
        self._observadores.remove(observador)

    def notificar_observadores(self, evento: dict):
        # Notifica a una copia de la lista para evitar problemas si un observador
        # se desuscribe durante la notificacion.
        for observador in self._observadores[:]:
            observador.actualizar(evento)
```

### US-TECH-003: Implementar Factory Method para Entradas

**Como** arquitecto de software
**Quiero** centralizar la creacion de objetos `Entrada` usando el patron Factory Method
**Para** encapsular la logica de instanciacion, desacoplar el codigo cliente de las clases concretas y facilitar la adicion de nuevos tipos de entrada en el futuro.

#### Criterios de Aceptacion

- [x] Crear una clase `EntradaFactory` con un metodo estatico `crear_entrada(tipo, ...)`.
- [x] El factory debe soportar la creacion de `EntradaEstandar`, `Entrada3D`, `EntradaVIP`.
- [x] Usar un diccionario para mapear los tipos (string) a los constructores de las clases, evitando `if/elif` y facilitando la extension.
- [x] Lanzar un `ValueError` claro si el tipo de entrada es desconocido.

#### Detalles Tecnicos

**Clase**: `EntradaFactory` (`cinema_app/patrones/factory/entrada_factory.py`)
**Patron**: Factory Method

**Justificacion de Diseno**:
El `CineManager`, al vender una entrada, no deberia preocuparse por los detalles de como se construye una `EntradaVIP` vs una `Entrada3D`. Su responsabilidad es gestionar la venta, no la construccion de objetos. El Factory Method extrae esta logica. Si en el futuro se crea una `Entrada4DX` con atributos y precio base diferentes, solo necesitamos modificar el `EntradaFactory` para anadir la nueva logica. El `CineManager` y el resto del flujo de venta permanecen intactos, cumpliendo con el Principio Abierto/Cerrado.

**Implementacion**:
```python
from cinema_app.entidades.entrada import Entrada, EntradaEstandar, Entrada3D, EntradaVIP

class EntradaFactory:
    # Mapeo de string a clase constructora. Facil de extender.
    _constructores = {
        "ESTANDAR": EntradaEstandar,
        "3D": Entrada3D,
        "VIP": EntradaVIP
    }

    @staticmethod
    def crear_entrada(tipo: str, funcion, asiento) -> Entrada:
        tipo_upper = tipo.upper()
        if tipo_upper not in EntradaFactory._constructores:
            raise ValueError(f"Tipo de entrada desconocido: {tipo}")
        
        # La logica de precios base podria venir de un archivo de configuracion
        precios_base = {"ESTANDAR": 10.0, "3D": 12.5, "VIP": 18.0}
        precio_base = precios_base.get(tipo_upper, 10.0)

        constructor = EntradaFactory._constructores[tipo_upper]
        print(f"Factory: Creando instancia de {constructor.__name__}...")
        return constructor(funcion, asiento, precio_base)
```

### US-TECH-004: Implementar Strategy para Calculo de Precios

**Como** arquitecto de software
**Quiero** implementar algoritmos de calculo de precios intercambiables usando el patron Strategy
**Para** permitir que la politica de precios evolucione independientemente de los objetos `Entrada`, haciendo el sistema flexible y abierto a extensiones.

#### Criterios de Aceptacion

- [x] Crear una interfaz `EstrategiaPrecio` con un metodo `calcular(precio_base)`.
- [x] Implementar al menos dos estrategias concretas: `EstrategiaPrecioNormal` (que no hace nada) y `EstrategiaDescuentoSemanal`.
- [x] La clase `Entrada` (Contexto) debe tener un atributo para almacenar la estrategia y un metodo para inyectarla (`set_estrategia_precio`).
- [x] El metodo `get_precio_final()` en `Entrada` debe delegar el calculo a la estrategia, si existe.

#### Detalles Tecnicos

**Interfaz**: `EstrategiaPrecio` (`cinema_app/patrones/strategy/estrategia_precio.py`)
**Patron**: Strategy

**Justificacion de Diseno**:
Las politicas de precios son una de las partes mas volatiles de un sistema de ventas. Hardcodear `if dia == 'martes': precio *= 0.5` dentro de la clase `Entrada` la haria rigida y dificil de mantener. El patron Strategy extrae estos algoritmos en clases separadas. Esto nos permite anadir nuevas estrategias (ej. `Estrategia2x1`, `EstrategiaCombo`) sin modificar `Entrada`. Ademas, permite cambiar la estrategia de un objeto en tiempo de ejecucion, ofreciendo una flexibilidad enorme.

**Implementacion (Interfaz y Estrategia Concreta)**:
```python
# cinema_app/patrones/strategy/estrategia_precio.py
from abc import ABC, abstractmethod

class EstrategiaPrecio(ABC):
    @abstractmethod
    def calcular(self, precio_base: float) -> float:
        pass

# cinema_app/patrones/strategy/impl/estrategia_descuento_semanal.py
class EstrategiaDescuentoSemanal(EstrategiaPrecio):
    def __init__(self, descuento_porcentual: float):
        self._descuento = descuento_porcentual

    def calcular(self, precio_base: float) -> float:
        descuento = precio_base * (self._descuento / 100)
        print(f"Strategy: Aplicando descuento de ${descuento:.2f}")
        return precio_base - descuento
```

**Uso en la clase Entrada (Contexto)**:
```python
# cinema_app/entidades/entrada.py
class Entrada:
    def __init__(self, funcion, asiento, precio_base):
        self._funcion = funcion
        self._asiento = asiento
        self._precio_base = precio_base
        self._estrategia_precio: EstrategiaPrecio = None # Inicia sin estrategia

    def set_estrategia_precio(self, estrategia: EstrategiaPrecio):
        self._estrategia_precio = estrategia

    def get_precio_final(self) -> float:
        if not self._estrategia_precio:
            return self._precio_base
        # Delegacion del calculo al objeto estrategia
        return self._estrategia_precio.calcular(self._precio_base)
```

---

## Resumen de Cobertura Funcional

| Epic | Historias | Completadas | Cobertura |
|------|-----------|-------------|-----------|
| Epic 1: Gestion de Peliculas y Funciones | 2 | 2 | 100% |
| Epic 2: Compra de Entradas | 1 | 1 | 100% |
| Epic 3: Registro y Notificaciones | 1 | 1 | 100% |
| Epic 4: Estrategias de Precios | 1 | 1 | 100% |
| Historias Tecnicas (Patrones) | 4 | 4 | 100% |
| **TOTAL** | **9** | **9** | **100%** |

### Patrones de Diseno Cubiertos

- [x] SINGLETON - CineManager
- [x] FACTORY METHOD - EntradaFactory
- [x] OBSERVER - Notificaciones a Clientes
- [x] STRATEGY - Calculo de Precios

---

**Ultima actualizacion**: Octubre 2025
**Estado**: COMPLETO
**Cobertura funcional**: 100%
