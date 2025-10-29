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
5. [Epic 5: Gestion de Salas y Asientos](#epic-5-gestion-de-salas-y-asientos)
6. [Historias Tecnicas (Patrones de Diseno)](#historias-tecnicas-patrones-de-diseno)

---

## Epic 1: Gestion de Peliculas y Funciones

### US-001: Registrar Nueva Pelicula en Cartelera

**Como** administrador del cine
**Quiero** registrar una nueva pelicula con toda su informacion
**Para** tener disponibles las peliculas en el sistema y notificar a clientes interesados

#### Criterios de Aceptacion

- [x] El sistema debe permitir crear una pelicula con:
  - Titulo unico (cadena de texto no vacia)
  - Sinopsis descriptiva (cadena de texto)
  - Genero (Accion, Drama, Comedia, Ciencia Ficcion, Terror, etc.)
  - Duracion en minutos (numero entero positivo)
  - Clasificacion por edad (ATP, +13, +16, +18)
  - Director y reparto principal (opcional)
- [x] La duracion debe ser mayor a 0, si no lanzar `ValueError`
- [x] El titulo no puede estar duplicado en el sistema
- [x] Al agregar una pelicula, el sistema debe notificar automaticamente a todos los clientes suscritos
- [x] La pelicula debe almacenarse en el gestor central (Singleton)

#### Detalles Tecnicos

**Clase**: `Pelicula` (`cinema_app/entidades/pelicula.py`)
**Singleton**: `CineManager` (`cinema_app/patrones/singleton/cine_manager.py`)
**Patron**: Observer (notificacion automatica)

**Codigo de ejemplo**:
```python
from cinema_app.patrones.singleton.cine_manager import CineManager
from cinema_app.entidades.pelicula import Pelicula

# Obtener instancia unica del gestor
cine_manager = CineManager.get_instance()

# Crear pelicula
pelicula = Pelicula(
    titulo="Inception",
    sinopsis="Un ladron que roba secretos corporativos a traves del uso de la tecnologia de compartir suenos.",
    genero="Ciencia Ficcion",
    duracion=148,
    clasificacion="+13",
    director="Christopher Nolan"
)

# Agregar al sistema (notifica automaticamente)
cine_manager.agregar_pelicula(pelicula)
```

**Validaciones**:
```python
# Duracion valida
pelicula = Pelicula("Matrix", "...", "Ciencia Ficcion", 136, "+13")  # OK

# Duracion invalida
pelicula = Pelicula("Matrix", "...", "Ciencia Ficcion", 0, "+13")  # ValueError
pelicula = Pelicula("Matrix", "...", "Ciencia Ficcion", -10, "+13")  # ValueError

# Titulo duplicado
cine_manager.agregar_pelicula(pelicula1)
cine_manager.agregar_pelicula(pelicula1)  # PeliculaDuplicadaException
```

**Notificacion Observer**:
```python
# Dentro de CineManager.agregar_pelicula()
evento = {
    'tipo': 'NUEVA_PELICULA',
    'titulo': pelicula.titulo,
    'genero': pelicula.genero,
    'clasificacion': pelicula.clasificacion
}
self.notificar_observadores(evento)
```

**Trazabilidad**: `main.py` lineas 20-35

---

### US-002: Consultar Cartelera Completa

**Como** cliente
**Quiero** ver todas las peliculas disponibles en cartelera
**Para** decidir cual quiero ver

#### Criterios de Aceptacion

- [x] El sistema debe mostrar todas las peliculas registradas
- [x] Debe mostrar: titulo, genero, duracion, clasificacion, sinopsis
- [x] Debe poder filtrarse por genero
- [x] Debe poder ordenarse por titulo o duracion
- [x] Si no hay peliculas, mostrar mensaje apropiado

#### Detalles Tecnicos

**Servicio**: `CineManager.listar_peliculas()`
**Servicio**: `CineManager.buscar_peliculas_por_genero()`

**Codigo de ejemplo**:
```python
# Listar todas las peliculas
peliculas = cine_manager.listar_peliculas()
for pelicula in peliculas:
    print(f"{pelicula.titulo} - {pelicula.genero} ({pelicula.duracion} min)")

# Filtrar por genero
peliculas_accion = cine_manager.buscar_peliculas_por_genero("Accion")

# Buscar por titulo
pelicula = cine_manager.buscar_pelicula("Inception")
if pelicula:
    print(pelicula.mostrar_informacion())
```

**Salida esperada**:
```
=== CARTELERA DE PELICULAS ===
1. Inception - Ciencia Ficcion (148 min) [+13]
   Director: Christopher Nolan
   Sinopsis: Un ladron que roba secretos...

2. Avengers: Endgame - Accion (181 min) [+13]
   Director: Russo Brothers
   Sinopsis: Los heroes restantes...
```

**Trazabilidad**: `main.py` lineas 40-50

---

### US-003: Programar Funcion para Pelicula

**Como** administrador del cine
**Quiero** programar funciones para las peliculas en diferentes salas y horarios
**Para** que los clientes puedan elegir cuando y donde ver la pelicula

#### Criterios de Aceptacion

- [x] Una funcion debe tener:
  - Pelicula asociada (referencia valida)
  - Sala asignada (referencia valida)
  - Fecha y hora de inicio (datetime futuro)
  - Precio base inicial
  - Mapa de asientos generado automaticamente
- [x] No pueden haber dos funciones en la misma sala a la misma hora
- [x] La funcion debe generarse con todos los asientos disponibles
- [x] Al programar una funcion, notificar a clientes suscritos a esa pelicula
- [x] Debe validar que la sala tenga capacidad suficiente

#### Detalles Tecnicos

**Clase**: `Funcion` (`cinema_app/entidades/funcion.py`)
**Servicio**: `CineManager.programar_funcion()`
**Patron**: Observer (notificacion automatica)

**Codigo de ejemplo**:
```python
from datetime import datetime

# Buscar pelicula y sala
pelicula = cine_manager.buscar_pelicula("Inception")
sala = cine_manager.get_sala("Sala IMAX 1")

# Programar funcion
fecha_hora = datetime(2025, 11, 15, 20, 30)  # 15 Nov 2025 a las 20:30

funcion = cine_manager.programar_funcion(
    pelicula=pelicula,
    sala=sala,
    fecha_hora=fecha_hora,
    precio_base=10.0
)

print(f"Funcion programada ID: {funcion.id}")
print(f"Asientos disponibles: {funcion.get_cantidad_asientos_disponibles()}")
```

**Validaciones**:
```python
# Fecha pasada
fecha_pasada = datetime(2020, 1, 1, 10, 0)
cine_manager.programar_funcion(pelicula, sala, fecha_pasada)  # ValueError

# Sala ocupada
funcion1 = cine_manager.programar_funcion(pelicula1, sala1, fecha1)
funcion2 = cine_manager.programar_funcion(pelicula2, sala1, fecha1)  # SalaOcupadaException
```

**Generacion de asientos**:
```python
# Dentro de Funcion.__init__()
def _generar_mapa_asientos(self):
    self._asientos = {}
    filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for fila in filas:
        for numero in range(1, self._sala.get_asientos_por_fila() + 1):
            codigo_asiento = f"{fila}{numero}"
            self._asientos[codigo_asiento] = {
                'ocupado': False,
                'tipo': 'estandar'
            }
```

**Notificacion Observer**:
```python
# Notificar a clientes suscritos a esta pelicula
evento = {
    'tipo': 'NUEVA_FUNCION',
    'pelicula': pelicula.titulo,
    'sala': sala.nombre,
    'fecha': fecha_hora.strftime("%d/%m/%Y %H:%M"),
    'asientos_disponibles': funcion.get_cantidad_asientos_disponibles()
}
self.notificar_observadores(evento)
```

**Trazabilidad**: `main.py` lineas 55-70

---

### US-004: Consultar Funciones Disponibles

**Como** cliente
**Quiero** ver todas las funciones disponibles para una pelicula
**Para** elegir el horario y sala que me convenga

#### Criterios de Aceptacion

- [x] El sistema debe mostrar todas las funciones de una pelicula
- [x] Debe mostrar: sala, fecha, hora, asientos disponibles, precio base
- [x] Debe poder filtrarse por fecha
- [x] Debe poder filtrarse por sala
- [x] Solo debe mostrar funciones futuras (no pasadas)
- [x] Debe indicar si la funcion esta agotada

#### Detalles Tecnicos

**Servicio**: `CineManager.get_funciones_por_pelicula()`
**Servicio**: `CineManager.get_funciones_por_fecha()`

**Codigo de ejemplo**:
```python
# Obtener funciones de una pelicula
pelicula = cine_manager.buscar_pelicula("Inception")
funciones = cine_manager.get_funciones_por_pelicula(pelicula)

for funcion in funciones:
    disponibles = funcion.get_cantidad_asientos_disponibles()
    total = funcion.get_capacidad_total()
    estado = "AGOTADA" if disponibles == 0 else f"{disponibles}/{total} disponibles"
    
    print(f"Funcion ID: {funcion.id}")
    print(f"Sala: {funcion.sala.nombre}")
    print(f"Fecha: {funcion.fecha_hora.strftime('%d/%m/%Y %H:%M')}")
    print(f"Asientos: {estado}")
    print(f"Precio base: ${funcion.precio_base:.2f}")
    print("---")
```

**Salida esperada**:
```
=== FUNCIONES PARA "INCEPTION" ===

Funcion ID: 1
Sala: Sala IMAX 1
Fecha: 15/11/2025 20:30
Tipo: 3D
Asientos: 95/100 disponibles
Precio base: $12.50
---

Funcion ID: 2
Sala: Sala Premium 2
Fecha: 15/11/2025 22:45
Tipo: VIP
Asientos: AGOTADA
Precio base: $18.00
---
```

**Filtros disponibles**:
```python
# Filtrar por fecha
from datetime import date
funciones_hoy = cine_manager.get_funciones_por_fecha(date.today())

# Filtrar por sala y pelicula
funciones_imax = cine_manager.get_funciones_por_sala_y_pelicula(sala_imax, pelicula)
```

**Trazabilidad**: `main.py` lineas 75-90

---

### US-005: Cancelar Funcion Programada

**Como** administrador del cine
**Quiero** cancelar una funcion programada
**Para** liberar la sala por mantenimiento o falta de demanda

#### Criterios de Aceptacion

- [x] Solo se pueden cancelar funciones sin entradas vendidas
- [x] Si hay entradas vendidas, lanzar `FuncionConEntradasException`
- [x] Al cancelar, notificar a clientes suscritos
- [x] La funcion cancelada debe marcarse como inactiva (no eliminarse)
- [x] Debe registrar motivo de cancelacion

#### Detalles Tecnicos

**Servicio**: `CineManager.cancelar_funcion()`

**Codigo de ejemplo**:
```python
# Cancelar funcion sin entradas vendidas
try:
    cine_manager.cancelar_funcion(
        funcion_id=5,
        motivo="Mantenimiento de sala"
    )
    print("Funcion cancelada exitosamente")
except FuncionConEntradasException as e:
    print(f"Error: {e.message}")
    print(f"Entradas vendidas: {e.cantidad_entradas}")
```

**Notificacion**:
```python
# Notificar cancelacion
evento = {
    'tipo': 'FUNCION_CANCELADA',
    'pelicula': funcion.pelicula.titulo,
    'fecha': funcion.fecha_hora.strftime("%d/%m/%Y %H:%M"),
    'motivo': motivo
}
self.notificar_observadores(evento)
```

**Trazabilidad**: `main.py` lineas 240-250

---

## Epic 2: Compra de Entradas

### US-006: Seleccionar Asientos Disponibles

**Como** cliente
**Quiero** ver los asientos disponibles de una funcion
**Para** elegir donde quiero sentarme

#### Criterios de Aceptacion

- [x] El sistema debe mostrar un mapa visual de asientos
- [x] Debe indicar: disponible, ocupado, no disponible
- [x] Debe mostrar tipos especiales (VIP, discapacitados)
- [x] Debe actualizar en tiempo real la disponibilidad
- [x] Debe permitir seleccionar multiples asientos

#### Detalles Tecnicos

**Servicio**: `Funcion.mostrar_mapa_asientos()`
**Servicio**: `Funcion.verificar_asiento_disponible()`

**Codigo de ejemplo**:
```python
# Mostrar mapa de asientos
funcion.mostrar_mapa_asientos()

# Verificar disponibilidad
asiento = "F8"
if funcion.verificar_asiento_disponible(asiento):
    print(f"Asiento {asiento} disponible")
else:
    print(f"Asiento {asiento} ocupado")

# Seleccionar multiples asientos
asientos_seleccionados = ["F8", "F9", "F10"]
todos_disponibles = all(
    funcion.verificar_asiento_disponible(a) 
    for a in asientos_seleccionados
)
```

**Salida esperada**:
```
=== MAPA DE ASIENTOS - SALA IMAX 1 ===
      PANTALLA
      ========

   1  2  3  4  5  6  7  8  9  10
A [O][O][D][D][D][D][D][O][O][O]
B [D][D][D][D][D][D][D][D][D][D]
C [D][D][D][D][D][D][D][D][D][D]
D [V][V][D][D][D][D][D][D][V][V]
E [V][V][D][D][D][D][D][D][V][V]
F [D][D][D][D][D][D][D][O][D][D]

[D] = Disponible
[O] = Ocupado
[V] = VIP
```

**Trazabilidad**: `main.py` lineas 95-110

---

### US-007: Generar Compra de Entrada con Factory Method

**Como** cliente
**Quiero** generar la compra de una entrada para una funcion y asiento especifico
**Para** asegurar mi lugar en el cine

#### Criterios de Aceptacion

- [x] El sistema debe crear un objeto `Entrada` usando `EntradaFactory`
- [x] El Factory debe soportar tipos: Estandar, 3D, VIP, IMAX
- [x] La entrada debe contener: pelicula, funcion, asiento, precio base, cliente
- [x] El asiento debe marcarse como ocupado inmediatamente
- [x] Si el asiento esta ocupado, lanzar `AsientoOcupadoException`
- [x] Debe generar un codigo unico de entrada
- [x] NO se debe instanciar `Entrada` directamente

#### Detalles Tecnicos

**Factory**: `EntradaFactory` (`cinema_app/patrones/factory/entrada_factory.py`)
**Productos**: `EntradaEstandar`, `Entrada3D`, `EntradaVIP`, `EntradaIMAX`
**Patron**: Factory Method

**Codigo de ejemplo**:
```python
from cinema_app.patrones.factory.entrada_factory import EntradaFactory

# Seleccionar funcion y asiento
funcion = cine_manager.get_funcion(id=1)
asiento = "F8"
cliente = cliente_juan  # Asumiendo que ya existe

# Determinar tipo segun sala
tipo_entrada = funcion.sala.get_tipo_proyeccion()  # "3D", "VIP", "IMAX"

# Crear entrada usando Factory (NO instanciacion directa)
try:
    entrada = EntradaFactory.crear_entrada(
        tipo=tipo_entrada,
        funcion=funcion,
        asiento=asiento,
        cliente=cliente
    )
    
    print(f"Entrada creada: {entrada.get_codigo()}")
    print(f"Tipo: {type(entrada).__name__}")
    print(f"Precio base: ${entrada.get_precio_base():.2f}")
    
except AsientoOcupadoException as e:
    print(f"Error: El asiento {e.asiento} ya esta ocupado")
```

**Factory interno**:
```python
# Dentro de EntradaFactory
@staticmethod
def crear_entrada(tipo: str, funcion, asiento, cliente):
    # Diccionario de constructores (NO if/elif)
    constructores = {
        "ESTANDAR": EntradaFactory._crear_estandar,
        "3D": EntradaFactory._crear_3d,
        "VIP": EntradaFactory._crear_vip,
        "IMAX": EntradaFactory._crear_imax
    }
    
    tipo_upper = tipo.upper()
    if tipo_upper not in constructores:
        raise ValueError(f"Tipo de entrada desconocido: {tipo}")
    
    # Validar asiento disponible
    if not funcion.verificar_asiento_disponible(asiento):
        raise AsientoOcupadoException(asiento)
    
    # Crear entrada con metodo dedicado
    return constructores[tipo_upper](funcion, asiento, cliente)

@staticmethod
def _crear_3d(funcion, asiento, cliente):
    precio_base = 12.50
    return Entrada3D(funcion, asiento, cliente, precio_base)
```

**Constantes de precios base**:
```python
PRECIO_BASE_ESTANDAR = 10.0
PRECIO_BASE_3D = 12.5
PRECIO_BASE_VIP = 18.0
PRECIO_BASE_IMAX = 15.0
```

**Trazabilidad**: `main.py` lineas 115-135

---

### US-008: Confirmar Compra de Entrada

**Como** cliente
**Quiero** confirmar la compra de mi entrada
**Para** completar la transaccion y recibir mi codigo de entrada

#### Criterios de Aceptacion

- [x] Debe aplicar la estrategia de precio correspondiente
- [x] Debe marcar el asiento como ocupado permanentemente
- [x] Debe generar codigo unico QR/barcode
- [x] Debe registrar la venta en el sistema
- [x] Debe enviar confirmacion al cliente (email/notificacion)
- [x] Si falla el pago, liberar el asiento

#### Detalles Tecnicos

**Servicio**: `CineManager.confirmar_compra()`
**Patron**: Strategy (aplicacion de precio)

**Codigo de ejemplo**:
```python
from cinema_app.patrones.strategy.impl.estrategia_descuento_semanal import EstrategiaDescuentoSemanal

# Crear entrada
entrada = EntradaFactory.crear_entrada("3D", funcion, "F8", cliente)

# Aplicar estrategia de precio
estrategia = EstrategiaDescuentoSemanal(descuento_porcentual=25)
entrada.set_estrategia_precio(estrategia)

# Confirmar compra
try:
    resultado = cine_manager.confirmar_compra(entrada)
    
    print("=== COMPRA CONFIRMADA ===")
    print(f"Codigo: {resultado.codigo}")
    print(f"Pelicula: {entrada.funcion.pelicula.titulo}")
    print(f"Fecha: {entrada.funcion.fecha_hora.strftime('%d/%m/%Y %H:%M')}")
    print(f"Asiento: {entrada.asiento}")
    print(f"Precio base: ${entrada.get_precio_base():.2f}")
    print(f"Precio final: ${entrada.get_precio_final():.2f}")
    print(f"Ahorro: ${entrada.get_precio_base() - entrada.get_precio_final():.2f}")
    
except CompraFallidaException as e:
    print(f"Error en la compra: {e.message}")
    # Asiento liberado automaticamente
```

**Salida esperada**:
```
=== COMPRA CONFIRMADA ===
Codigo: QR-2025-001-F8
Pelicula: Inception
Fecha: 15/11/2025 20:30
Sala: IMAX 1
Asiento: F8
Tipo: Entrada3D
Precio base: $12.50
Descuento: $3.13 (25%)
Precio final: $9.37

Confirmacion enviada a: juan.perez@email.com
```

**Trazabilidad**: `main.py` lineas 140-160

---

### US-009: Comprar Multiples Entradas (Combo)

**Como** cliente
**Quiero** comprar multiples entradas de una vez
**Para** ir al cine con amigos o familia

#### Criterios de Aceptacion

- [x] Debe permitir seleccionar multiples asientos contiguos
- [x] Debe aplicar estrategia de precio combo si aplica
- [x] Todos los asientos deben estar disponibles
- [x] Si un asiento esta ocupado, no se vende ninguno
- [x] Debe generar una entrada por cada asiento
- [x] Todas las entradas deben tener el mismo codigo de compra

#### Detalles Tecnicos

**Servicio**: `CineManager.comprar_combo()`
**Patron**: Strategy (estrategia combo)

**Codigo de ejemplo**:
```python
from cinema_app.patrones.strategy.impl.estrategia_precio_combo import EstrategiaPrecioCombo

# Seleccionar multiples asientos
asientos = ["F8", "F9", "F10", "F11"]

# Verificar todos disponibles
if not funcion.verificar_asientos_disponibles(asientos):
    print("Error: Algunos asientos no estan disponibles")
    return

# Crear combo
estrategia_combo = EstrategiaPrecioCombo(
    cantidad_entradas=len(asientos),
    descuento_combo=15  # 15% descuento por combo
)

# Comprar combo
resultado = cine_manager.comprar_combo(
    funcion=funcion,
    asientos=asientos,
    cliente=cliente,
    estrategia=estrategia_combo
)

print(f"Combo comprado: {len(resultado.entradas)} entradas")
print(f"Codigo de compra: {resultado.codigo_compra}")
print(f"Total sin descuento: ${resultado.precio_base_total:.2f}")
print(f"Total con descuento: ${resultado.precio_final_total:.2f}")
print(f"Ahorro total: ${resultado.ahorro_total:.2f}")
```

**Trazabilidad**: `main.py` lineas 165-185

---

### US-010: Cancelar Entrada Comprada

**Como** cliente
**Quiero** cancelar una entrada que compre
**Para** recuperar mi dinero si no puedo asistir

#### Criterios de Aceptacion

- [x] Solo se puede cancelar con minimo 2 horas de anticipacion
- [x] Debe liberar el asiento para otros clientes
- [x] Debe procesarse reembolso (segun politica)
- [x] Debe invalidar el codigo de entrada
- [x] Debe notificar al cliente la cancelacion
- [x] Si es parte de un combo, cancelar todo el combo

#### Detalles Tecnicos

**Servicio**: `CineManager.cancelar_entrada()`

**Codigo de ejemplo**:
```python
from datetime import datetime, timedelta

# Intentar cancelar entrada
codigo_entrada = "QR-2025-001-F8"

try:
    reembolso = cine_manager.cancelar_entrada(
        codigo=codigo_entrada,
        cliente=cliente
    )
    
    print("=== CANCELACION EXITOSA ===")
    print(f"Entrada: {codigo_entrada}")
    print(f"Reembolso: ${reembolso.monto:.2f}")
    print(f"Metodo: {reembolso.metodo}")
    print(f"Tiempo estimado: {reembolso.dias_habiles} dias habiles")
    
except CancelacionDenegadaException as e:
    print(f"Error: {e.message}")
    print(f"Razon: {e.razon}")
```

**Validaciones**:
```python
# Verificar tiempo minimo
tiempo_restante = funcion.fecha_hora - datetime.now()
if tiempo_restante < timedelta(hours=2):
    raise CancelacionDenegadaException(
        "Debe cancelar con minimo 2 horas de anticipacion"
    )
```

**Trazabilidad**: `main.py` lineas 255-270

---

## Epic 3: Registro y Notificaciones a Clientes

### US-011: Registrar Cliente en el Sistema

**Como** visitante
**Quiero** registrarme como cliente del cine
**Para** poder comprar entradas y recibir notificaciones

#### Criterios de Aceptacion

- [x] Un cliente debe tener:
  - Nombre completo
  - Email unico (validado)
  - Telefono (opcional)
  - Fecha de nacimiento (para validar edad en peliculas)
  - Preferencias de notificacion (email, SMS, push)
- [x] El email no puede estar duplicado
- [x] El email debe tener formato valido
- [x] Al registrarse, enviar email de bienvenida
- [x] El cliente debe implementar interfaz `Observer`

#### Detalles Tecnicos

**Clase**: `Cliente` (`cinema_app/entidades/cliente.py`)
**Servicio**: `CineManager.registrar_cliente()`
**Patron**: Observer (el cliente es un observador)

**Codigo de ejemplo**:
```python
from cinema_app.entidades.cliente import Cliente
from datetime import date

# Crear cliente
cliente = Cliente(
    nombre="Juan Perez",
    email="juan.perez@email.com",
    telefono="+5491112345678",
    fecha_nacimiento=date(1990, 5, 15),
    preferencias_notificacion={
        'email': True,
        'sms': False,
        'push': True
    }
)

# Registrar en el sistema
cine_manager.registrar_cliente(cliente)

# Cliente automaticamente suscrito a notificaciones generales
print(f"Cliente registrado: {cliente.nombre}")
print(f"ID: {cliente.id}")
```

**Validaciones**:
```python
# Email valido
if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
    raise EmailInvalidoException(email)

# Email duplicado
if cine_manager.existe_cliente_por_email(email):
    raise EmailDuplicadoException(email)

# Calcular edad
edad = calcular_edad(fecha_nacimiento)
if edad < 13:
    raise EdadMinimaException("Debes tener al menos 13 años")
```

**Trazabilidad**: `main.py` lineas 15-30

---

### US-012: Suscribirse a Notificaciones Generales (Observer)

**Como** cliente registrado
**Quiero** suscribirme para recibir notificaciones sobre novedades del cine
**Para** estar informado de estrenos y promociones

#### Criterios de Aceptacion

- [x] El cliente debe poder suscribirse/desuscribirse en cualquier momento
- [x] Debe recibir notificaciones de: nuevas peliculas, nuevas funciones, promociones
- [x] Las notificaciones deben respetar sus preferencias (email/SMS/push)
- [x] Debe implementar el metodo `actualizar(evento)` de la interfaz `Observer`
- [x] El `CineManager` actua como `Observable` y gestiona la lista de suscriptores

#### Detalles Tecnicos

**Patron**: Observer
**Observable**: `CineManager`
**Observer**: `Cliente`

**Codigo de ejemplo**:
```python
# Cliente se suscribe
cine_manager.suscribir_observador(cliente_juan)
cine_manager.suscribir_observador(cliente_maria)

# Mas tarde, Juan se desuscribe
cine_manager.desuscribir_observador(cliente_juan)

# Solo Maria recibira futuras notificaciones
```

**Implementacion en Cliente**:
```python
from cinema_app.patrones.observer.observer import Observer

class Cliente(Observer):
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self._historial_notificaciones = []

    def actualizar(self, evento: dict) -> None:
        """Recibe notificaciones del CineManager"""
        self._historial_notificaciones.append(evento)
        
        # Procesar segun tipo de evento
        if evento['tipo'] == "NUEVA_PELICULA":
            self._notificar_nueva_pelicula(evento)
        elif evento['tipo'] == "NUEVA_FUNCION":
            self._notificar_nueva_funcion(evento)
        elif evento['tipo'] == "PROMOCION":
            self._notificar_promocion(evento)
    
    def _notificar_nueva_pelicula(self, evento):
        mensaje = f"""
        --- Notificacion para {self.nombre} ---
        ¡NUEVO ESTRENO!
        
        Pelicula: {evento['titulo']}
        Genero: {evento['genero']}
        Clasificacion: {evento['clasificacion']}
        
        ¡Ya puedes ver los horarios disponibles!
        --------------------------------------
        """
        self._enviar_notificacion(mensaje)
    
    def _enviar_notificacion(self, mensaje):
        # Segun preferencias del cliente
        if self.preferencias['email']:
            print(f"Email enviado a: {self.email}")
        if self.preferencias['sms']:
            print(f"SMS enviado a: {self.telefono}")
        print(mensaje)
```

**Implementacion en CineManager (Observable)**:
```python
from cinema_app.patrones.observer.observable import Observable

class CineManager(Observable):
    def __init__(self):
        super().__init__()  # Inicializa lista de observadores
        self._peliculas = []
        self._funciones = []
        self._clientes = []
    
    def agregar_pelicula(self, pelicula):
        self._peliculas.append(pelicula)
        
        # Notificar a todos los observadores
        evento = {
            'tipo': 'NUEVA_PELICULA',
            'titulo': pelicula.titulo,
            'genero': pelicula.genero,
            'clasificacion': pelicula.clasificacion,
            'duracion': pelicula.duracion
        }
        self.notificar_observadores(evento)
```

**Trazabilidad**: `main.py` lineas 190-210

---

### US-013: Suscribirse a Pelicula Especifica

**Como** cliente
**Quiero** suscribirme a notificaciones de una pelicula especifica
**Para** ser notificado cuando se agreguen nuevas funciones solo de esa pelicula

#### Criterios de Aceptacion

- [x] El cliente debe poder suscribirse a peliculas individuales
- [x] Solo recibe notificaciones de funciones de esas peliculas
- [x] Puede estar suscrito a multiples peliculas simultaneamente
- [x] Puede desuscribirse de una pelicula en particular
- [x] Si la pelicula sale de cartelera, desuscribirse automaticamente

#### Detalles Tecnicos

**Servicio**: `CineManager.suscribir_a_pelicula()`
**Patron**: Observer (variante con filtros)

**Codigo de ejemplo**:
```python
# Suscribirse a peliculas especificas
pelicula_inception = cine_manager.buscar_pelicula("Inception")
pelicula_avatar = cine_manager.buscar_pelicula("Avatar 3")

cine_manager.suscribir_a_pelicula(cliente_juan, pelicula_inception)
cine_manager.suscribir_a_pelicula(cliente_juan, pelicula_avatar)

# Cuando se programa una funcion de Inception, Juan recibe notificacion
# Cuando se programa una funcion de otra pelicula, Juan NO recibe notificacion

# Desuscribirse de una pelicula
cine_manager.desuscribir_de_pelicula(cliente_juan, pelicula_inception)
```

**Implementacion interna**:
```python
class CineManager:
    def __init__(self):
        # Diccionario: pelicula -> lista de observadores
        self._suscripciones_peliculas = {}
    
    def suscribir_a_pelicula(self, cliente, pelicula):
        if pelicula not in self._suscripciones_peliculas:
            self._suscripciones_peliculas[pelicula] = []
        
        if cliente not in self._suscripciones_peliculas[pelicula]:
            self._suscripciones_peliculas[pelicula].append(cliente)
    
    def programar_funcion(self, pelicula, sala, fecha_hora):
        # ... crear funcion ...
        
        # Notificar solo a clientes suscritos a esta pelicula
        if pelicula in self._suscripciones_peliculas:
            evento = {
                'tipo': 'NUEVA_FUNCION',
                'pelicula': pelicula.titulo,
                'sala': sala.nombre,
                'fecha': fecha_hora.strftime("%d/%m/%Y %H:%M")
            }
            
            for cliente in self._suscripciones_peliculas[pelicula]:
                cliente.actualizar(evento)
```

**Trazabilidad**: `main.py` lineas 215-230

---

### US-014: Ver Historial de Notificaciones

**Como** cliente
**Quiero** ver mi historial de notificaciones recibidas
**Para** revisar promociones o funciones que me perdí

#### Criterios de Aceptacion

- [x] Debe almacenar todas las notificaciones recibidas
- [x] Debe mostrar: fecha, tipo, mensaje
- [x] Debe poder filtrarse por tipo de notificacion
- [x] Debe poder filtrarse por rango de fechas
- [x] Debe poder marcarse como leido/no leido

#### Detalles Tecnicos

**Servicio**: `Cliente.get_historial_notificaciones()`

**Codigo de ejemplo**:
```python
# Ver todas las notificaciones
notificaciones = cliente.get_historial_notificaciones()
for notif in notificaciones:
    print(f"[{notif.fecha}] {notif.tipo}: {notif.mensaje}")

# Filtrar por tipo
notif_peliculas = cliente.get_historial_notificaciones(tipo="NUEVA_PELICULA")

# Filtrar por fecha
from datetime import date, timedelta
ultimos_7_dias = cliente.get_historial_notificaciones(
    fecha_desde=date.today() - timedelta(days=7)
)

# Ver solo no leidas
no_leidas = cliente.get_notificaciones_no_leidas()
print(f"Tienes {len(no_leidas)} notificaciones sin leer")
```

**Trazabilidad**: `main.py` lineas 235-245

---

## Epic 4: Estrategias de Precios

### US-015: Aplicar Precio Normal (Strategy)

**Como** sistema de ventas
**Quiero** aplicar el precio base normal a una entrada
**Para** calcular el precio cuando no hay descuentos ni promociones

#### Criterios de Aceptacion

- [x] Debe implementar interfaz `EstrategiaPrecio`
- [x] El metodo `calcular()` retorna el precio base sin modificaciones
- [x] Debe usarse como estrategia por defecto
- [x] El objeto `Entrada` debe recibir esta estrategia via inyeccion

#### Detalles Tecnicos

**Clase**: `EstrategiaPrecioNormal` (`cinema_app/patrones/strategy/impl/estrategia_precio_normal.py`)
**Patron**: Strategy

**Codigo de ejemplo**:
```python
from cinema_app.patrones.strategy.impl.estrategia_precio_normal import EstrategiaPrecioNormal

# Crear entrada con precio normal
entrada = EntradaFactory.crear_entrada("3D", funcion, "F8", cliente)

# Aplicar estrategia normal (por defecto)
estrategia = EstrategiaPrecioNormal()
entrada.set_estrategia_precio(estrategia)

precio_final = entrada.get_precio_final()
# precio_final == entrada.get_precio_base() (sin cambios)

print(f"Precio base: ${entrada.get_precio_base():.2f}")
print(f"Precio final: ${precio_final:.2f}")
```

**Implementacion**:
```python
from cinema_app.patrones.strategy.estrategia_precio import EstrategiaPrecio

class EstrategiaPrecioNormal(EstrategiaPrecio):
    def calcular(self, precio_base: float) -> float:
        """Retorna el precio base sin modificaciones"""
        return precio_base
    
    def get_descripcion(self) -> str:
        return "Precio normal sin descuentos"
```

**Trazabilidad**: `main.py` lineas 280-290

---

### US-016: Aplicar Descuento por Dia de Semana (Strategy)

**Como** administrador del cine
**Quiero** ofrecer descuentos en dias de semana
**Para** incentivar ventas en dias de baja demanda

#### Criterios de Aceptacion

- [x] Debe aplicar descuento porcentual en dias laborables (Lunes-Jueves)
- [x] El porcentaje de descuento debe ser configurable
- [x] No aplica en fines de semana y feriados
- [x] Debe mostrar el ahorro obtenido
- [x] Debe implementar interfaz `EstrategiaPrecio`

#### Detalles Tecnicos

**Clase**: `EstrategiaDescuentoSemanal` (`cinema_app/patrones/strategy/impl/estrategia_descuento_semanal.py`)
**Patron**: Strategy

**Codigo de ejemplo**:
```python
from cinema_app.patrones.strategy.impl.estrategia_descuento_semanal import EstrategiaDescuentoSemanal
from datetime import date

# Verificar si hoy aplica descuento
hoy = date.today()
dia_semana = hoy.weekday()  # 0=Lunes, 6=Domingo

if dia_semana < 4:  # Lunes a Jueves
    estrategia = EstrategiaDescuentoSemanal(descuento_porcentual=25)
    entrada.set_estrategia_precio(estrategia)
    
    precio_base = entrada.get_precio_base()
    precio_final = entrada.get_precio_final()
    ahorro = precio_base - precio_final
    
    print(f"¡Descuento del dia! Ahorras ${ahorro:.2f}")
else:
    print("Descuento no disponible en fin de semana")
```

**Implementacion**:
```python
class EstrategiaDescuentoSemanal(EstrategiaPrecio):
    def __init__(self, descuento_porcentual: float):
        if not 0 <= descuento_porcentual <= 100:
            raise ValueError("Descuento debe estar entre 0 y 100")
        self._descuento = descuento_porcentual
    
    def calcular(self, precio_base: float) -> float:
        descuento_monto = precio_base * (self._descuento / 100)
        precio_final = precio_base - descuento_monto
        
        print(f"Strategy: Aplicando descuento semanal de {self._descuento}%")
        print(f"Strategy: Descuento: ${descuento_monto:.2f}")
        
        return precio_final
    
    def get_descripcion(self) -> str:
        return f"Descuento de dia de semana: {self._descuento}%"
```

**Constantes**:
```python
DESCUENTO_LUNES_JUEVES = 25  # 25% de descuento
DIAS_CON_DESCUENTO = [0, 1, 2, 3]  # Lunes a Jueves
```

**Trazabilidad**: `main.py` lineas 295-310

---

### US-017: Aplicar Precio Estudiante (Strategy)

**Como** estudiante
**Quiero** obtener descuento presentando mi credencial
**Para** pagar menos por las entradas

#### Criterios de Aceptacion

- [x] Debe aplicar descuento fijo o porcentual para estudiantes
- [x] El cliente debe tener atributo `es_estudiante` validado
- [x] Requiere presentacion de credencial vigente
- [x] No se combina con otros descuentos (o toma el mejor)
- [x] Debe implementar interfaz `EstrategiaPrecio`

#### Detalles Tecnicos

**Clase**: `EstrategiaPrecioEstudiante` (`cinema_app/patrones/strategy/impl/estrategia_precio_estudiante.py`)
**Patron**: Strategy

**Codigo de ejemplo**:
```python
from cinema_app.patrones.strategy.impl.estrategia_precio_estudiante import EstrategiaPrecioEstudiante

# Verificar si cliente es estudiante
if cliente.es_estudiante and cliente.credencial_vigente():
    estrategia = EstrategiaPrecioEstudiante(
        descuento_porcentual=30,
        requiere_credencial=True
    )
    entrada.set_estrategia_precio(estrategia)
    
    print(f"Precio estudiante: ${entrada.get_precio_final():.2f}")
else:
    print("Credencial de estudiante no valida o vencida")
```

**Implementacion**:
```python
class EstrategiaPrecioEstudiante(EstrategiaPrecio):
    def __init__(self, descuento_porcentual: float, requiere_credencial: bool = True):
        self._descuento = descuento_porcentual
        self._requiere_credencial = requiere_credencial
    
    def calcular(self, precio_base: float) -> float:
        descuento_monto = precio_base * (self._descuento / 100)
        precio_final = precio_base - descuento_monto
        
        print(f"Strategy: Precio estudiante - {self._descuento}% descuento")
        return precio_final
    
    def validar_credencial(self, cliente) -> bool:
        if not self._requiere_credencial:
            return True
        
        return (cliente.es_estudiante and 
                cliente.credencial and 
                not cliente.credencial.esta_vencida())
    
    def get_descripcion(self) -> str:
        return f"Precio estudiante: {self._descuento}% descuento"
```

**Validacion de credencial**:
```python
class Cliente:
    def credencial_vigente(self) -> bool:
        if not self.credencial:
            return False
        
        from datetime import date
        return self.credencial.fecha_vencimiento > date.today()
```

**Trazabilidad**: `main.py` lineas 315-330

---

### US-018: Aplicar Precio Combo/Grupal (Strategy)

**Como** cliente que compra multiples entradas
**Quiero** obtener descuento por compra grupal
**Para** ahorrar cuando voy con amigos o familia

#### Criterios de Aceptacion

- [x] Debe aplicar descuento progresivo segun cantidad de entradas
- [x] Ejemplo: 2 entradas 10%, 3 entradas 15%, 4+ entradas 20%
- [x] El descuento se aplica sobre el total, no individual
- [x] Todas las entradas deben ser para la misma funcion
- [x] Debe implementar interfaz `EstrategiaPrecio`

#### Detalles Tecnicos

**Clase**: `EstrategiaPrecioCombo` (`cinema_app/patrones/strategy/impl/estrategia_precio_combo.py`)
**Patron**: Strategy

**Codigo de ejemplo**:
```python
from cinema_app.patrones.strategy.impl.estrategia_precio_combo import EstrategiaPrecioCombo

# Comprar 4 entradas juntas
cantidad_entradas = 4
estrategia = EstrategiaPrecioCombo(cantidad_entradas)

# Calcular descuento
precio_individual = 12.50
precio_total_base = precio_individual * cantidad_entradas
precio_total_final = estrategia.calcular(precio_total_base)

print(f"Precio individual: ${precio_individual:.2f}")
print(f"Cantidad: {cantidad_entradas}")
print(f"Total sin descuento: ${precio_total_base:.2f}")
print(f"Total con descuento combo: ${precio_total_final:.2f}")
print(f"Ahorro total: ${precio_total_base - precio_total_final:.2f}")
```

**Implementacion**:
```python
class EstrategiaPrecioCombo(EstrategiaPrecio):
    # Tabla de descuentos por cantidad
    DESCUENTOS = {
        2: 10,  # 2 entradas: 10%
        3: 15,  # 3 entradas: 15%
        4: 20,  # 4+ entradas: 20%
    }
    
    def __init__(self, cantidad_entradas: int):
        if cantidad_entradas < 2:
            raise ValueError("Combo requiere minimo 2 entradas")
        self._cantidad = cantidad_entradas
    
    def calcular(self, precio_base_total: float) -> float:
        descuento_porcentual = self._obtener_descuento()
        descuento_monto = precio_base_total * (descuento_porcentual / 100)
        precio_final = precio_base_total - descuento_monto
        
        print(f"Strategy: Combo de {self._cantidad} entradas")
        print(f"Strategy: Descuento: {descuento_porcentual}% (${descuento_monto:.2f})")
        
        return precio_final
    
    def _obtener_descuento(self) -> int:
        """Obtiene el descuento segun cantidad de entradas"""
        if self._cantidad >= 4:
            return self.DESCUENTOS[4]
        elif self._cantidad in self.DESCUENTOS:
            return self.DESCUENTOS[self._cantidad]
        return 0
    
    def get_descripcion(self) -> str:
        descuento = self._obtener_descuento()
        return f"Combo {self._cantidad} entradas: {descuento}% descuento"
```

**Trazabilidad**: `main.py` lineas 335-355

---

### US-019: Aplicar Precio Especial Sala Premium (Strategy)

**Como** administrador del cine
**Quiero** cobrar precio premium en salas especiales (IMAX, VIP, 4DX)
**Para** reflejar el costo y calidad superior de estas salas

#### Criterios de Aceptacion

- [x] Debe aplicar recargo porcentual segun tipo de sala
- [x] Ejemplo: IMAX +25%, VIP +50%, 4DX +40%
- [x] El recargo se suma al precio base
- [x] Puede combinarse con descuentos (descuento aplica sobre precio con recargo)
- [x] Debe implementar interfaz `EstrategiaPrecio`

#### Detalles Tecnicos

**Clase**: `EstrategiaPrecioSalaPremium` (`cinema_app/patrones/strategy/impl/estrategia_precio_sala_premium.py`)
**Patron**: Strategy

**Codigo de ejemplo**:
```python
from cinema_app.patrones.strategy.impl.estrategia_precio_sala_premium import EstrategiaPrecioSalaPremium

# Entrada para sala IMAX
tipo_sala = funcion.sala.get_tipo()  # "IMAX", "VIP", "4DX"

estrategia = EstrategiaPrecioSalaPremium(tipo_sala)
entrada.set_estrategia_precio(estrategia)

precio_base = entrada.get_precio_base()
precio_final = entrada.get_precio_final()

print(f"Precio base: ${precio_base:.2f}")
print(f"Tipo sala: {tipo_sala}")
print(f"Precio final: ${precio_final:.2f}")
```

**Implementacion**:
```python
class EstrategiaPrecioSalaPremium(EstrategiaPrecio):
    # Recargos por tipo de sala
    RECARGOS = {
        "IMAX": 25,    # +25%
        "VIP": 50,     # +50%
        "4DX": 40,     # +40%
        "PREMIUM": 30  # +30%
    }
    
    def __init__(self, tipo_sala: str):
        if tipo_sala not in self.RECARGOS:
            raise ValueError(f"Tipo de sala desconocido: {tipo_sala}")
        self._tipo_sala = tipo_sala
    
    def calcular(self, precio_base: float) -> float:
        recargo_porcentual = self.RECARGOS[self._tipo_sala]
        recargo_monto = precio_base * (recargo_porcentual / 100)
        precio_final = precio_base + recargo_monto
        
        print(f"Strategy: Sala {self._tipo_sala}")
        print(f"Strategy: Recargo: +{recargo_porcentual}% (${recargo_monto:.2f})")
        
        return precio_final
    
    def get_descripcion(self) -> str:
        recargo = self.RECARGOS[self._tipo_sala]
        return f"Sala {self._tipo_sala}: +{recargo}% sobre precio base"
```

**Trazabilidad**: `main.py` lineas 360-375

---

### US-020: Combinar Multiples Estrategias de Precio

**Como** sistema de ventas
**Quiero** poder combinar multiples estrategias de precio
**Para** aplicar descuentos y recargos simultaneamente

#### Criterios de Aceptacion

- [x] Debe permitir encadenar estrategias
- [x] El orden de aplicacion debe ser configurable
- [x] Orden sugerido: Recargos primero, luego descuentos
- [x] Debe calcular precio paso a paso
- [x] Debe mostrar desglose de cada ajuste

#### Detalles Tecnicos

**Clase**: `EstrategiaPrecioCompuesta` (`cinema_app/patrones/strategy/impl/estrategia_precio_compuesta.py`)
**Patron**: Strategy (Composite)

**Codigo de ejemplo**:
```python
from cinema_app.patrones.strategy.impl.estrategia_precio_compuesta import EstrategiaPrecioCompuesta

# Crear estrategias individuales
estrategia_sala = EstrategiaPrecioSalaPremium("IMAX")  # +25%
estrategia_dia = EstrategiaDescuentoSemanal(20)  # -20%

# Combinar estrategias
estrategia_compuesta = EstrategiaPrecioCompuesta([
    estrategia_sala,    # Se aplica primero
    estrategia_dia      # Se aplica sobre el resultado anterior
])

entrada.set_estrategia_precio(estrategia_compuesta)

# Calculo paso a paso:
# 1. Precio base: $10.00
# 2. + Recargo IMAX 25%: $12.50
# 3. - Descuento dia 20%: $10.00
precio_final = entrada.get_precio_final()

# Ver desglose
desglose = estrategia_compuesta.get_desglose()
for paso in desglose:
    print(f"{paso['descripcion']}: ${paso['precio']:.2f}")
```

**Implementacion**:
```python
class EstrategiaPrecioCompuesta(EstrategiaPrecio):
    def __init__(self, estrategias: list[EstrategiaPrecio]):
        if not estrategias:
            raise ValueError("Debe proporcionar al menos una estrategia")
        self._estrategias = estrategias
        self._desglose = []
    
    def calcular(self, precio_base: float) -> float:
        self._desglose = []
        precio_actual = precio_base
        
        self._desglose.append({
            'descripcion': 'Precio base',
            'precio': precio_base
        })
        
        # Aplicar cada estrategia secuencialmente
        for estrategia in self._estrategias:
            precio_anterior = precio_actual
            precio_actual = estrategia.calcular(precio_actual)
            
            self._desglose.append({
                'descripcion': estrategia.get_descripcion(),
                'precio': precio_actual,
                'ajuste': precio_actual - precio_anterior
            })
        
        return precio_actual
    
    def get_desglose(self) -> list:
        return self._desglose.copy()
    
    def get_descripcion(self) -> str:
        descripciones = [e.get_descripcion() for e in self._estrategias]
        return " + ".join(descripciones)
```

**Salida desglose**:
```
=== DESGLOSE DE PRECIO ===
Precio base: $10.00
+ Sala IMAX: +25%: $12.50 (+$2.50)
- Descuento dia: 20%: $10.00 (-$2.50)
-------------------------
PRECIO FINAL: $10.00
```

**Trazabilidad**: `main.py` lineas 380-405

---

## Epic 5: Gestion de Salas y Asientos

### US-021: Crear Sala con Configuracion Especifica

**Como** administrador del cine
**Quiero** crear salas con diferentes configuraciones
**Para** adaptarme a distintos tipos de proyecciones y capacidades

#### Criterios de Aceptacion

- [x] Una sala debe tener:
  - Nombre/numero unico
  - Capacidad total (cantidad de asientos)
  - Tipo de proyeccion (Estandar, 3D, IMAX, VIP, 4DX)
  - Distribucion de filas y columnas
  - Asientos especiales (discapacitados, VIP)
- [x] La capacidad debe coincidir con filas × columnas
- [x] Debe validar que el nombre no este duplicado
- [x] Debe generarse automaticamente el mapa de asientos

#### Detalles Tecnicos

**Clase**: `Sala` (`cinema_app/entidades/sala.py`)
**Servicio**: `CineManager.crear_sala()`

**Codigo de ejemplo**:
```python
from cinema_app.entidades.sala import Sala

# Crear sala estandar
sala_1 = Sala(
    nombre="Sala 1",
    filas=10,
    asientos_por_fila=10,
    tipo_proyeccion="ESTANDAR"
)

# Crear sala IMAX
sala_imax = Sala(
    nombre="Sala IMAX 1",
    filas=12,
    asientos_por_fila=15,
    tipo_proyeccion="IMAX",
    asientos_vip=['D1', 'D2', 'D14', 'D15', 'E1', 'E2', 'E14', 'E15']
)

# Registrar en el sistema
cine_manager.agregar_sala(sala_1)
cine_manager.agregar_sala(sala_imax)

print(f"Sala creada: {sala_1.nombre}")
print(f"Capacidad: {sala_1.get_capacidad()}")
print(f"Tipo: {sala_1.tipo_proyeccion}")
```

**Validaciones**:
```python
# Capacidad coherente
capacidad_calculada = filas * asientos_por_fila
if capacidad != capacidad_calculada:
    raise ValueError(f"Capacidad incorrecta: {capacidad} != {capacidad_calculada}")

# Nombre duplicado
if cine_manager.existe_sala(nombre):
    raise SalaDuplicadaException(nombre)
```

**Trazabilidad**: `main.py` lineas 410-425

---

### US-022: Marcar Asientos Especiales (VIP, Discapacitados)

**Como** administrador del cine
**Quiero** designar asientos especiales en cada sala
**Para** ofrecer opciones premium y accesibilidad

#### Criterios de Aceptacion

- [x] Debe poder marcar asientos como VIP (precio diferenciado)
- [x] Debe poder marcar asientos para discapacitados (accesibilidad)
- [x] Los asientos especiales deben mostrarse diferenciados en el mapa
- [x] Debe validar que los codigos de asiento existan
- [x] Los asientos especiales no pueden superponerse

#### Detalles Tecnicos

**Servicio**: `Sala.marcar_asientos_especiales()`

**Codigo de ejemplo**:
```python
# Marcar asientos VIP (generalmente filas centrales)
sala.marcar_asientos_vip([
    'D8', 'D9', 'D10',
    'E8', 'E9', 'E10',
    'F8', 'F9', 'F10'
])

# Marcar asientos para discapacitados (primera fila, pasillos)
sala.marcar_asientos_discapacitados([
    'A1', 'A10',
    'B1', 'B10'
])

# Ver configuracion
print(sala.get_configuracion_asientos())
```

**Visualizacion**:
```
=== CONFIGURACION SALA IMAX 1 ===
      PANTALLA
      ========

   1  2  3  4  5  6  7  8  9  10
A [♿][E][E][E][E][E][E][E][E][♿]
B [♿][E][E][E][E][E][E][E][E][♿]
C [E][E][E][E][E][E][E][E][E][E]
D [E][E][E][E][E][V][V][V][E][E]
E [E][E][E][E][E][V][V][V][E][E]
F [E][E][E][E][E][V][V][V][E][E]

[E] = Estandar
[V] = VIP (+30%)
[♿] = Discapacitados (accesible)
```

**Trazabilidad**: `main.py` lineas 430-445

---

### US-023: Validar Disponibilidad de Asientos en Tiempo Real

**Como** sistema de ventas
**Quiero** validar disponibilidad de asientos en tiempo real
**Para** evitar ventas duplicadas del mismo asiento

#### Criterios de Aceptacion

- [x] Debe verificar disponibilidad antes de cada venta
- [x] Debe bloquear asiento temporalmente durante compra (5 minutos)
- [x] Si el tiempo expira, liberar asiento automaticamente
- [x] Debe manejar concurrencia (multiples usuarios viendo misma funcion)
- [x] Thread-safe en modificacion de estado de asientos

#### Detalles Tecnicos

**Servicio**: `Funcion.reservar_asiento_temporal()`
**Servicio**: `Funcion.confirmar_reserva()`
**Servicio**: `Funcion.liberar_reserva_temporal()`

**Codigo de ejemplo**:
```python
from datetime import datetime, timedelta
import threading

# Intentar reservar asiento
asiento = "F8"
cliente_id = cliente.id

try:
    # Reserva temporal (5 minutos)
    token_reserva = funcion.reservar_asiento_temporal(
        asiento=asiento,
        cliente_id=cliente_id,
        duracion_minutos=5
    )
    
    print(f"Asiento {asiento} reservado por 5 minutos")
    print(f"Token: {token_reserva}")
    
    # Cliente completa compra...
    # ...
    
    # Confirmar reserva (marca como ocupado permanentemente)
    funcion.confirmar_reserva(token_reserva)
    print("Reserva confirmada - asiento ocupado")
    
except AsientoNoDisponibleException as e:
    print(f"Asiento {asiento} no disponible")
    print(f"Reservado por cliente: {e.cliente_id}")
    print(f"Expira en: {e.tiempo_restante} segundos")
```

**Implementacion con thread-safety**:
```python
from threading import Lock

class Funcion:
    def __init__(self, pelicula, sala, fecha_hora):
        self._lock = Lock()  # Thread-safe
        self._asientos = {}
        self._reservas_temporales = {}
    
    def reservar_asiento_temporal(self, asiento, cliente_id, duracion_minutos):
        with self._lock:  # Bloqueo para thread-safety
            # Verificar disponibilidad
            if not self._verificar_disponible(asiento):
                raise AsientoNoDisponibleException(asiento)
            
            # Crear reserva temporal
            token = self._generar_token_reserva()
            expiracion = datetime.now() + timedelta(minutes=duracion_minutos)
            
            self._reservas_temporales[token] = {
                'asiento': asiento,
                'cliente_id': cliente_id,
                'expiracion': expiracion
            }
            
            # Marcar asiento como reservado temporalmente
            self._asientos[asiento]['estado'] = 'RESERVADO_TEMPORAL'
            self._asientos[asiento]['token'] = token
            
            # Iniciar timer para liberar automaticamente
            self._iniciar_timer_liberacion(token, duracion_minutos * 60)
            
            return token
    
    def confirmar_reserva(self, token):
        with self._lock:
            if token not in self._reservas_temporales:
                raise ReservaInvalidaException(token)
            
            reserva = self._reservas_temporales[token]
            
            # Verificar no expirada
            if datetime.now() > reserva['expiracion']:
                raise ReservaExpiradaException(token)
            
            # Marcar asiento como ocupado permanentemente
            asiento = reserva['asiento']
            self._asientos[asiento]['estado'] = 'OCUPADO'
            self._asientos[asiento]['cliente_id'] = reserva['cliente_id']
            
            # Eliminar reserva temporal
            del self._reservas_temporales[token]
    
    def _iniciar_timer_liberacion(self, token, segundos):
        def liberar():
            with self._lock:
                if token in self._reservas_temporales:
                    reserva = self._reservas_temporales[token]
                    asiento = reserva['asiento']
                    
                    # Liberar asiento si sigue en estado temporal
                    if self._asientos[asiento]['estado'] == 'RESERVADO_TEMPORAL':
                        self._asientos[asiento]['estado'] = 'DISPONIBLE'
                        del self._reservas_temporales[token]
                        print(f"Reserva temporal de {asiento} expirada y liberada")
        
        timer = threading.Timer(segundos, liberar)
        timer.daemon = True
        timer.start()
```

**Trazabilidad**: `main.py` lineas 450-475

---

## Historias Tecnicas (Patrones de Diseno)

### US-TECH-001: Implementar Singleton para CineManager

**Como** arquitecto de software
**Quiero** garantizar una unica instancia del `CineManager` en toda la aplicacion
**Para** tener un punto de acceso global y estado consistente de cartelera, funciones y clientes

#### Criterios de Aceptacion

- [x] Implementar patron Singleton thread-safe
- [x] Usar double-checked locking con `threading.Lock`
- [x] Inicializacion perezosa (lazy initialization)
- [x] Metodo `get_instance()` para acceso
- [x] Constructor `__new__` debe prevenir instanciacion directa
- [x] NO permitir multiples instancias bajo ninguna circunstancia

#### Detalles Tecnicos

**Clase**: `CineManager` (`cinema_app/patrones/singleton/cine_manager.py`)
**Patron**: Singleton

**Justificacion**:
El `CineManager` es el corazon del sistema. Administra:
- Lista de peliculas en cartelera
- Funciones programadas
- Clientes registrados
- Observadores suscritos
- Salas disponibles

Si existieran multiples instancias, cada una tendria su propia vista del estado, causando inconsistencias. Por ejemplo, un hilo podria agregar una pelicula que otro hilo no veria. El Singleton garantiza que todos los componentes del sistema operan sobre los mismos datos.

**Implementacion**:
```python
from threading import Lock

class CineManager:
    _instance = None
    _lock = Lock()
    _inicializado = False

    def __new__(cls):
        # Prevenir instanciacion directa
        raise RuntimeError(
            "No se puede instanciar CineManager directamente. "
            "Use CineManager.get_instance()"
        )

    @classmethod
    def get_instance(cls):
        # Primera verificacion (sin bloqueo) - optimizacion
        if cls._instance is None:
            # Adquirir bloqueo solo si la instancia es None
            with cls._lock:
                # Segunda verificacion (dentro del bloqueo)
                if cls._instance is None:
                    print("Creando la unica instancia de CineManager...")
                    # Crear instancia saltando __new__
                    cls._instance = object.__new__(cls)
                    
                    # Inicializar UNA SOLA VEZ
                    if not cls._inicializado:
                        cls._instance._inicializar()
                        cls._inicializado = True
        
        return cls._instance

    def _inicializar(self):
        """Inicializa el estado interno una sola vez"""
        print("Inicializando estado de CineManager...")
        
        # Listas principales
        self._peliculas = []
        self._funciones = []
        self._clientes = []
        self._salas = []
        
        # Observer pattern
        self._observadores = []
        self._suscripciones_peliculas = {}
        
        # Contadores para IDs unicos
        self._contador_funcion = 0
        self._contador_entrada = 0
        
        print("CineManager inicializado correctamente")

    # Prevenir clonacion
    def __copy__(self):
        raise RuntimeError("No se puede clonar CineManager (Singleton)")
    
    def __deepcopy__(self, memo):
        raise RuntimeError("No se puede clonar CineManager (Singleton)")
```

**Uso correcto**:
```python
# CORRECTO: Usar get_instance()
cine_manager = CineManager.get_instance()

# INCORRECTO: Instanciacion directa (lanzara RuntimeError)
# cine_manager = CineManager()  # ❌ ERROR

# Verificar que es singleton
manager1 = CineManager.get_instance()
manager2 = CineManager.get_instance()

assert manager1 is manager2  # ✓ Misma instancia
```

**Thread-safety demostrado**:
```python
import threading

def crear_manager():
    manager = CineManager.get_instance()
    print(f"Thread {threading.current_thread().name}: {id(manager)}")

# Crear 10 threads que intentan obtener instancia simultaneamente
threads = []
for i in range(10):
    t = threading.Thread(target=crear_manager, name=f"Thread-{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Resultado: Todos los threads obtienen la MISMA instancia (mismo ID)
```

**Trazabilidad**: `cine_manager.py` lineas 1-85

---

### US-TECH-002: Implementar Observer para Notificaciones

**Como** arquitecto de software
**Quiero** implementar el patron Observer para el sistema de notificaciones
**Para** desacoplar el `CineManager` (sujeto) de los `Cliente`s (observadores)

#### Criterios de Aceptacion

- [x] Crear interfaz abstracta `Observer` con metodo `actualizar(evento)`
- [x] Crear clase base `Observable` con metodos:
  - `suscribir_observador(observador)`
  - `desuscribir_observador(observador)`
  - `notificar_observadores(evento)`
- [x] `CineManager` debe heredar de `Observable`
- [x] `Cliente` debe implementar interfaz `Observer`
- [x] Thread-safe en lista de observadores

#### Detalles Tecnicos

**Interfaces**: `Observable`, `Observer` (`cinema_app/patrones/observer/`)
**Patron**: Observer

**Justificacion**:
Sin Observer, cada vez que el `CineManager` agregara una pelicula, tendria que:
```python
# ❌ MAL: Acoplamiento fuerte
def agregar_pelicula(self, pelicula):
    self._peliculas.append(pelicula)
    
    # Logica especifica de notificacion hardcodeada
    for cliente in self._clientes:
        if cliente.preferencias['email']:
            enviar_email(cliente.email, pelicula)
        if cliente.preferencias['sms']:
            enviar_sms(cliente.telefono, pelicula)
    # Si queremos agregar notificaciones push, hay que modificar AQUI
```

Con Observer:
```python
# ✓ BIEN: Desacoplamiento
def agregar_pelicula(self, pelicula):
    self._peliculas.append(pelicula)
    
    # El manager no sabe QUE hacen los observadores
    evento = {'tipo': 'NUEVA_PELICULA', 'titulo': pelicula.titulo}
    self.notificar_observadores(evento)
    # Agregar notificaciones push: crear nuevo Observer, sin tocar esto
```

**Implementacion (Interfaces)**:
```python
# cinema_app/patrones/observer/observer.py
from abc import ABC, abstractmethod

class Observer(ABC):
    """Interfaz que deben implementar todos los observadores"""
    
    @abstractmethod
    def actualizar(self, evento: dict) -> None:
        """
        Metodo llamado cuando el observable notifica un cambio
        
        Args:
            evento: Diccionario con informacion del evento
                   Debe contener al menos 'tipo' como clave
        """
        pass
```

```python
# cinema_app/patrones/observer/observable.py
from .observer import Observer
from threading import Lock

class Observable:
    """Clase base para sujetos observables"""
    
    def __init__(self):
        self._observadores: list[Observer] = []
        self._lock = Lock()  # Thread-safe
    
    def suscribir_observador(self, observador: Observer) -> None:
        """Agrega un observador a la lista de suscritos"""
        with self._lock:
            if observador not in self._observadores:
                self._observadores.append(observador)
                print(f"Observador suscrito: {type(observador).__name__}")
    
    def desuscribir_observador(self, observador: Observer) -> None:
        """Remueve un observador de la lista de suscritos"""
        with self._lock:
            if observador in self._observadores:
                self._observadores.remove(observador)
                print(f"Observador desuscrito: {type(observador).__name__}")
    
    def notificar_observadores(self, evento: dict) -> None:
        """
        Notifica a todos los observadores de un evento
        
        Args:
            evento: Diccionario con informacion del evento
        """
        # Trabajar con copia para evitar problemas si un observador
        # se desuscribe durante la notificacion
        with self._lock:
            observadores_copia = self._observadores.copy()
        
        print(f"Notificando a {len(observadores_copia)} observador(es)...")
        
        for observador in observadores_copia:
            try:
                observador.actualizar(evento)
            except Exception as e:
                # No dejar que un observador defectuoso rompa todo
                print(f"Error al notificar observador {type(observador).__name__}: {e}")
```

**Implementacion (CineManager como Observable)**:
```python
class CineManager(Observable):
    def _inicializar(self):
        super().__init__()  # Inicializa lista de observadores
        self._peliculas = []
        # ... resto de inicializacion
    
    def agregar_pelicula(self, pelicula: Pelicula) -> None:
        """Agrega pelicula y notifica a observadores"""
        
        # Validar duplicados
        if self._existe_pelicula(pelicula.titulo):
            raise PeliculaDuplicadaException(pelicula.titulo)
        
        # Agregar a lista
        self._peliculas.append(pelicula)
        print(f"Pelicula '{pelicula.titulo}' agregada a la cartelera")
        
        # Notificar automaticamente
        evento = {
            'tipo': 'NUEVA_PELICULA',
            'titulo': pelicula.titulo,
            'genero': pelicula.genero,
            'clasificacion': pelicula.clasificacion,
            'duracion': pelicula.duracion
        }
        self.notificar_observadores(evento)
```

**Implementacion (Cliente como Observer)**:
```python
from cinema_app.patrones.observer.observer import Observer

class Cliente(Observer):
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self._historial_notificaciones = []
    
    def actualizar(self, evento: dict) -> None:
        """Implementacion del metodo Observer"""
        
        # Registrar en historial
        from datetime import datetime
        evento_con_fecha = evento.copy()
        evento_con_fecha['fecha'] = datetime.now()
        self._historial_notificaciones.append(evento_con_fecha)
        
        # Procesar segun tipo
        tipo = evento.get('tipo', 'DESCONOCIDO')
        
        if tipo == 'NUEVA_PELICULA':
            self._procesar_nueva_pelicula(evento)
        elif tipo == 'NUEVA_FUNCION':
            self._procesar_nueva_funcion(evento)
        elif tipo == 'PROMOCION':
            self._procesar_promocion(evento)
        elif tipo == 'FUNCION_CANCELADA':
            self._procesar_cancelacion(evento)
    
    def _procesar_nueva_pelicula(self, evento):
        print(f"\n{'='*50}")
        print(f"NOTIFICACION PARA: {self.nombre}")
        print(f"{'='*50}")
        print("🎬 ¡NUEVO ESTRENO!")
        print(f"Pelicula: {evento['titulo']}")
        print(f"Genero: {evento['genero']}")
        print(f"Clasificacion: {evento['clasificacion']}")
        print("¡Ya puedes ver los horarios disponibles!")
        print(f"{'='*50}\n")
        
        # Aqui podria enviar email real
        # self._enviar_email(evento)
    
    def _procesar_nueva_funcion(self, evento):
        print(f"\n{'='*50}")
        print(f"NOTIFICACION PARA: {self.nombre}")
        print(f"{'='*50}")
        print("🎞️  ¡NUEVA FUNCION DISPONIBLE!")
        print(f"Pelicula: {evento['pelicula']}")
        print(f"Sala: {evento['sala']}")
        print(f"Fecha: {evento['fecha']}")
        print(f"Asientos disponibles: {evento.get('asientos_disponibles', 'N/A')}")
        print(f"{'='*50}\n")
```

**Ejemplo de uso completo**:
```python
# 1. Crear manager (Singleton + Observable)
manager = CineManager.get_instance()

# 2. Crear clientes (Observers)
cliente_juan = Cliente("Juan Perez", "juan@email.com")
cliente_maria = Cliente("Maria Lopez", "maria@email.com")

# 3. Suscribir clientes
manager.suscribir_observador(cliente_juan)
manager.suscribir_observador(cliente_maria)

# 4. Agregar pelicula (dispara notificacion)
pelicula = Pelicula("Inception", "...", "Ciencia Ficcion", 148, "+13")
manager.agregar_pelicula(pelicula)

# Salida:
# Notificando a 2 observador(es)...
# ==================================================
# NOTIFICACION PARA: Juan Perez
# ==================================================
# 🎬 ¡NUEVO ESTRENO!
# Pelicula: Inception
# ...
# ==================================================
# NOTIFICACION PARA: Maria Lopez
# ==================================================
# 🎬 ¡NUEVO ESTRENO!
# Pelicula: Inception
# ...

# 5. Juan se desuscribe
manager.desuscribir_observador(cliente_juan)

# 6. Programar funcion (solo Maria recibe notificacion)
funcion = manager.programar_funcion(pelicula, sala, fecha)
```

**Trazabilidad**: `observable.py` lineas 1-60, `observer.py` lineas 1-20, `cliente.py` lineas 45-120

---

### US-TECH-003: Implementar Factory Method para Entradas

**Como** arquitecto de software
**Quiero** centralizar la creacion de objetos `Entrada` usando Factory Method
**Para** desacoplar el codigo cliente de las clases concretas y facilitar extension

#### Criterios de Aceptacion

- [x] Crear clase `EntradaFactory` con metodo estatico `crear_entrada()`
- [x] Soportar tipos: EntradaEstandar, Entrada3D, EntradaVIP, EntradaIMAX
- [x] Usar diccionario para mapear tipos a constructores (NO if/elif)
- [x] Cada tipo debe tener metodo factory dedicado (NO lambdas)
- [x] Lanzar `ValueError` claro si tipo desconocido
- [x] Retornar tipo base `Entrada` (no tipos concretos)