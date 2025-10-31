# Rubrica de Evaluacion Tecnica - Sistema de Venta de Entradas de Cine

**Proyecto**: CineApp
**Version**: 1.0.0
**Fecha**: Octubre 2025
**Tipo de Evaluacion**: Tecnica Academica / Profesional

---

## Instrucciones de Uso

Esta rubrica esta disenada para evaluar proyectos de software que implementen patrones de diseno en Python. Se utiliza para:

1. **Evaluacion academica**: Proyectos de estudiantes en cursos de Ingenieria de Software
2. **Evaluacion tecnica**: Entrevistas tecnicas para desarrolladores
3. **Code review**: Revision de calidad de codigo en proyectos profesionales
4. **Autoevaluacion**: Chequeo de cumplimiento de buenas practicas

### Escala de Puntuacion

- **Excelente (4 puntos)**: Cumple completamente con criterio, implementacion superior
- **Bueno (3 puntos)**: Cumple con criterio, implementacion correcta con minimos detalles
- **Suficiente (2 puntos)**: Cumple parcialmente, implementacion funcional con deficiencias
- **Insuficiente (1 punto)**: No cumple o cumplimiento minimo, implementacion deficiente
- **No Implementado (0 puntos)**: Criterio no implementado

### Puntaje Total

- **Puntaje Maximo**: 260 puntos
- **Puntaje de Aprobacion**: 182 puntos (70%)
- **Puntaje de Excelencia**: 234 puntos (90%)

---

## Seccion 1: Patrones de Diseno (80 puntos)

### 1.1 Patron SINGLETON (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Clase implementa Singleton con instancia unica | `__new__` con control de instancia unica o metodo `get_instance()` |
| **Thread-safety** | 5 | Implementacion thread-safe con Lock | Uso de `threading.Lock` con double-checked locking |
| **Acceso consistente** | 3 | Metodo `get_instance()` disponible | Metodo de clase que retorna instancia |
| **Inicializacion perezosa** | 3 | Lazy initialization correcta | Instancia se crea solo cuando se solicita |
| **Uso apropiado en el sistema** | 4 | Singleton usado donde corresponde (CineManager) | CineManager es Singleton para gestor central |

**Puntaje Seccion 1.1**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Singleton]
Verificar:
- Prevencion de instanciacion directa
- Prevencion de clonacion (__copy__, __deepcopy__)
- Estado consistente compartido (peliculas, funciones, clientes)
```

---

### 1.2 Patron FACTORY METHOD (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Factory encapsula creacion de objetos | Metodo estatico `crear_entrada(tipo, ...)` |
| **Desacoplamiento** | 5 | Cliente no conoce clases concretas | Retorna tipo base `Entrada`, no tipos concretos |
| **Extensibilidad** | 4 | Facil agregar nuevos tipos | Diccionario de factories o metodos dedicados |
| **Validacion de entrada** | 3 | Valida parametros y lanza excepciones | Lanza `ValueError` si tipo desconocido |
| **Uso apropiado en el sistema** | 3 | Factory usado en venta de entradas | `CineManager.vender_entrada()` usa factory |

**Puntaje Seccion 1.2**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Factory]
Verificar:
- Al menos 3 tipos de entrada (Estandar, 3D, VIP, IMAX)
- Jerarquia: Entrada (base) -> subclases concretas
- NO if/elif cascades (usar diccionario)
- Precios base centralizados en Factory
```

---

### 1.3 Patron OBSERVER (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Observable y Observer implementados | Clases `Observable` y `Observer` (interfaz) |
| **Desacoplamiento** | 5 | Observable no conoce detalles de Observer | Lista generica de observadores |
| **Notificaciones automaticas** | 4 | Observadores notificados al cambiar estado | `notificar_observadores()` en eventos clave |
| **Suscripcion/Desuscripcion** | 3 | Metodos para gestionar observadores | `suscribir_observador()`, `desuscribir_observador()` |
| **Uso apropiado en el sistema** | 3 | CineManager como Observable, Cliente como Observer | Notificaciones de peliculas, funciones, cancelaciones |

**Puntaje Seccion 1.3**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Observer]
Verificar:
- Thread-safety en lista de observadores
- Copia defensiva al notificar (evitar modificaciones concurrentes)
- Eventos: NUEVA_PELICULA, NUEVA_FUNCION, FUNCION_CANCELADA
- Cliente implementa metodo actualizar(evento)
```

---

### 1.4 Patron STRATEGY (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Interfaz Strategy con implementaciones | `EstrategiaPrecio` (abstracta) |
| **Algoritmos intercambiables** | 5 | Multiples estrategias implementadas | Al menos 3: Normal, Descuento, Estudiante, Combo |
| **Inyeccion de dependencias** | 4 | Estrategia inyectada en Entrada | `entrada.set_estrategia_precio(estrategia)` |
| **Delegacion correcta** | 3 | Entrada delega calculo a estrategia | `get_precio_final()` llama `estrategia.calcular()` |
| **Uso apropiado en el sistema** | 3 | Estrategias usadas segun contexto | Dia semana, estudiante, combo, sala premium |

**Puntaje Seccion 1.4**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Strategy]
Verificar:
- Interfaz: calcular(precio_base) -> precio_final
- Cambio dinamico en tiempo de ejecucion
- Estrategias NO modifican Entrada
- Opcion BONUS: EstrategiaPrecioCompuesta (combina multiples)
```

---

**PUNTAJE TOTAL SECCION 1**: _____ / 80

---

## Seccion 2: Arquitectura y Diseno (60 puntos)

### 2.1 Separacion de Responsabilidades (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Entidades vs Servicios** | 5 | Entidades solo datos, servicios solo logica | Clases en `entidades/` vs `patrones/singleton/` |
| **CineManager como Facade** | 5 | Gestor centraliza operaciones | CineManager orquesta peliculas, funciones, ventas |
| **Principio SRP** | 4 | Cada clase una unica responsabilidad | Pelicula, Funcion, Sala, Entrada son conceptos separados |
| **Cohesion alta** | 3 | Elementos relacionados agrupados | Modulos tematicos (entradas, estrategias, excepciones) |
| **Acoplamiento bajo** | 3 | Dependencias minimizadas | Uso de interfaces (Observer, Strategy) |

**Puntaje Seccion 2.1**: _____ / 20

---

### 2.2 Jerarquia de Clases (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Herencia apropiada** | 5 | Jerarquia logica de clases | `Entrada` → `EntradaEstandar`, `Entrada3D`, `EntradaVIP` |
| **Eliminacion de duplicacion** | 4 | Codigo compartido en clases base | `get_precio_final()`, `get_codigo()` en `Entrada` base |
| **Polimorfismo** | 3 | Subtipos intercambiables | Todas las entradas son `Entrada` |
| **Interfaces bien definidas** | 3 | Contratos claros entre clases | Metodos abstractos en `EstrategiaPrecio`, `Observer` |

**Puntaje Seccion 2.2**: _____ / 15

---

### 2.3 Manejo de Excepciones (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Jerarquia de excepciones** | 5 | Excepciones personalizadas heredan de base | `CinemaException` base (opcional pero recomendado) |
| **Excepciones especificas** | 4 | Excepciones de dominio implementadas | `AsientoOcupadoException`, `PeliculaDuplicadaException`, `SalaOcupadaException`, etc. |
| **Mensajes descriptivos** | 3 | Mensajes claros para usuario | Incluyen contexto (asiento, pelicula, fecha) |
| **Uso apropiado** | 3 | Excepciones usadas en puntos correctos | Validaciones lanzan excepciones apropiadas |

**Puntaje Seccion 2.3**: _____ / 15

---

### 2.4 Organizacion del Codigo (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Estructura de paquetes** | 3 | Organizacion logica de modulos | Paquetes: entidades, patrones, excepciones |
| **Modulos tematicos** | 3 | Agrupacion por dominio | patrones/singleton/, patrones/factory/, patrones/observer/, patrones/strategy/ |
| **Archivos `__init__.py`** | 2 | Inicializacion de paquetes | Todos los paquetes con `__init__.py` |
| **Importaciones limpias** | 2 | Sin imports circulares | Uso de TYPE_CHECKING si necesario |

**Puntaje Seccion 2.4**: _____ / 10

---

**PUNTAJE TOTAL SECCION 2**: _____ / 60

---

## Seccion 3: Calidad de Codigo (60 puntos)

### 3.1 PEP 8 Compliance (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Nombres de variables** | 4 | snake_case, descriptivos, sin abreviaciones | `precio_base` no `pb`, `fecha_hora` no `fh` |
| **Nombres de clases** | 3 | PascalCase consistente | `EntradaFactory`, `CineManager`, `EstrategiaPrecio` |
| **Nombres de constantes** | 3 | UPPER_SNAKE_CASE | `PRECIO_BASE_ESTANDAR`, `DESCUENTO_LUNES_JUEVES` |
| **Organizacion de imports** | 4 | PEP 8: Standard → Third-party → Local | Secciones separadas y ordenadas |
| **Longitud de linea** | 2 | Maximo 100-120 caracteres | No lineas excesivamente largas |
| **Espaciado y formato** | 4 | Espaciado consistente segun PEP 8 | 2 lineas entre clases, 1 entre metodos |

**Puntaje Seccion 3.1**: _____ / 20

---

### 3.2 Documentacion (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Docstrings en clases** | 4 | Todas las clases documentadas | Docstring en cada clase publica |
| **Docstrings en metodos** | 4 | Metodos publicos documentados | Google Style: Args, Returns, Raises |
| **Formato consistente** | 3 | Estilo Google o NumPy (NO JavaDoc) | Args: / Returns: / Raises: |
| **Comentarios en codigo complejo** | 2 | Explicacion de logica no obvia | Comentarios donde necesario (thread-safety, reservas) |
| **README y documentacion externa** | 2 | Documentacion de proyecto completa | README.md, USER_STORIES.md |

**Puntaje Seccion 3.2**: _____ / 15

---

### 3.3 Type Hints (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Type hints en firmas** | 4 | Parametros y retornos tipados | `def metodo(param: str) -> int:` |
| **Uso de TYPE_CHECKING** | 3 | Evita imports circulares si necesario | `if TYPE_CHECKING: from ...` |
| **Tipos complejos** | 3 | List, Dict, Optional usados correctamente | `list[Pelicula]`, `dict[str, Funcion]`, `Optional[Cliente]` |

**Puntaje Seccion 3.3**: _____ / 10

---

### 3.4 Principios de Codigo Limpio (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **NO magic numbers** | 5 | Constantes con nombre descriptivo | CERO valores hardcodeados |
| **NO lambdas innecesarias** | 4 | Funciones/metodos nombrados | Metodos dedicados en Factory (CRITICO) |
| **Funciones pequenas** | 3 | Metodos con responsabilidad unica | Funciones < 30 lineas idealmente |
| **Nombres descriptivos** | 3 | Variables y metodos autoexplicativos | `calcular_precio_final()` no `calc()` |

**Puntaje Seccion 3.4**: _____ / 15

---

**PUNTAJE TOTAL SECCION 3**: _____ / 60

---

## Seccion 4: Funcionalidad del Sistema (40 puntos)

### 4.1 Gestion de Peliculas y Funciones (12 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Registro de peliculas** | 4 | Sistema agrega peliculas con validaciones | Titulo unico, duracion > 0 |
| **Programacion de funciones** | 4 | Funciones con sala, fecha, generacion de asientos | Mapa de asientos auto-generado |
| **Consulta de cartelera** | 4 | Listado y busqueda funcional | Por titulo, genero, fecha |

**Puntaje Seccion 4.1**: _____ / 12

---

### 4.2 Compra de Entradas (12 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Seleccion de asientos** | 4 | Verificacion de disponibilidad | `verificar_asiento_disponible()` |
| **Creacion via Factory** | 4 | Uso de EntradaFactory | Cliente NO instancia directamente |
| **Aplicacion de estrategias** | 4 | Precio calculado con Strategy | `set_estrategia_precio()`, `get_precio_final()` |

**Puntaje Seccion 4.2**: _____ / 12

---

### 4.3 Sistema de Notificaciones (8 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Suscripcion de clientes** | 4 | Clientes se suscriben a eventos | `suscribir_observador()` funcional |
| **Notificaciones automaticas** | 4 | Eventos notificados correctamente | Al agregar pelicula, programar funcion, cancelar |

**Puntaje Seccion 4.3**: _____ / 8

---

### 4.4 Funcionalidades Adicionales (8 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Gestion de salas** | 4 | Salas con tipos y capacidades | Estandar, 3D, IMAX, VIP |
| **Validaciones robustas** | 4 | Multiples validaciones implementadas | Fechas, capacidades, duplicados |

**Puntaje Seccion 4.4**: _____ / 8

---

**PUNTAJE TOTAL SECCION 4**: _____ / 40

---

## Seccion 5: Buenas Practicas Avanzadas (20 puntos)

### 5.1 Thread-Safety y Concurrencia (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Thread-safety en Singleton** | 4 | Double-checked locking | Lock en `get_instance()` |
| **Thread-safety en reservas** | 3 | Operaciones atomicas en asientos | Lock en `reservar_asiento_temporal()`, `confirmar_reserva()` |
| **Manejo de concurrencia** | 3 | Multiples usuarios simultaneos | Previene doble reserva del mismo asiento |

**Puntaje Seccion 5.1**: _____ / 10

---

### 5.2 Validacion y Robustez (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Validacion de entrada** | 4 | Parametros validados apropiadamente | Duracion > 0, fechas futuras, emails validos |
| **Defensive copying** | 3 | Listas inmutables donde apropiado | `get_funciones()` retorna copia |
| **Manejo de errores** | 3 | Try/except apropiados | Validaciones con excepciones especificas |

**Puntaje Seccion 5.2**: _____ / 10

---

**PUNTAJE TOTAL SECCION 5**: _____ / 20

---

## Resumen de Evaluacion

### Desglose por Seccion

| Seccion | Puntaje Obtenido | Puntaje Maximo | Porcentaje |
|---------|------------------|----------------|------------|
| 1. Patrones de Diseno | _____ | 80 | _____% |
| 2. Arquitectura y Diseno | _____ | 60 | _____% |
| 3. Calidad de Codigo | _____ | 60 | _____% |
| 4. Funcionalidad del Sistema | _____ | 40 | _____% |
| 5. Buenas Practicas Avanzadas | _____ | 20 | _____% |
| **TOTAL** | **_____** | **260** | **_____%** |

### Calificacion Final

| Rango de Puntaje | Calificacion | Descripcion |
|------------------|--------------|-------------|
| 234 - 260 (90%+) | **Excelente** | Implementacion profesional de alta calidad |
| 208 - 233 (80-89%) | **Muy Bueno** | Implementacion solida con practicas avanzadas |
| 182 - 207 (70-79%) | **Bueno** | Implementacion correcta que cumple requisitos |
| 156 - 181 (60-69%) | **Suficiente** | Implementacion funcional con deficiencias |
| 0 - 155 (<60%) | **Insuficiente** | Requiere mejoras significativas |

**CALIFICACION FINAL**: ________________

---

## Comentarios Generales del Evaluador

### Fortalezas Identificadas
```
[Espacio para comentarios sobre aspectos destacados del proyecto]

Ejemplo:
- Excelente implementacion de Observer con desacoplamiento total
- Strategy pattern muy bien aplicado con multiples estrategias
- Singleton thread-safe correctamente implementado
- Factory Method facilita extension con nuevos tipos de entrada
```

### Areas de Mejora
```
[Espacio para comentarios sobre aspectos a mejorar]

Ejemplo:
- Faltan tests unitarios para validaciones criticas
- CineManager podria estar sobrecargado (considerar dividir responsabilidades)
- Documentacion de API podria incluir ejemplos de uso
- Considerar agregar logging para debugging
- Falta manejo de transacciones en compras (rollback si falla pago)
```

### Recomendaciones
```
[Espacio para recomendaciones especificas]

Ejemplo:
- Agregar tests con pytest (test_singleton, test_factory, test_observer, test_strategy)
- Implementar persistencia con base de datos (SQLite o PostgreSQL)
- Agregar patron Command para deshacer cancelaciones
- Considerar patron Memento para historial de cambios
- Implementar API REST con FastAPI para exponer funcionalidades
- Agregar autenticacion JWT para clientes
```

---

## Criterios de Evaluacion Detallados

### Patron SINGLETON - Checklist Detallado

- [ ] Clase tiene atributo `_instance` de clase
- [ ] Metodo `__new__` lanza RuntimeError o metodo `get_instance()` disponible
- [ ] Thread-safe con `threading.Lock`
- [ ] Double-checked locking correctamente implementado
- [ ] Inicializacion perezosa (lazy)
- [ ] Una sola instancia garantizada
- [ ] Prevencion de clonacion (`__copy__`, `__deepcopy__`)
- [ ] Usado apropiadamente (CineManager, NO en todas las clases)
- [ ] Estado consistente compartido (peliculas, funciones, clientes, salas)

### Patron FACTORY METHOD - Checklist Detallado

- [ ] Metodo factory es estatico
- [ ] Recibe parametro `tipo` para determinar entrada a crear
- [ ] Retorna tipo base `Entrada`, no tipo concreto
- [ ] Cliente NO importa clases concretas (EntradaEstandar, Entrada3D, etc.)
- [ ] Usa diccionario de constructores o metodos dedicados
- [ ] **CRITICO**: NO usa lambdas (debe usar metodos estaticos `_crear_estandar`, `_crear_3d`, etc.)
- [ ] Facil agregar nuevos tipos sin modificar logica existente
- [ ] Validacion de parametros con excepciones (`ValueError`)
- [ ] Precios base centralizados en Factory (no hardcodeados)
- [ ] Usado en `CineManager.vender_entrada()`
- [ ] Al menos 3-4 tipos: Estandar, 3D, VIP, IMAX

### Patron OBSERVER - Checklist Detallado

- [ ] Interfaz `Observer` con metodo `actualizar(evento: dict)`
- [ ] Clase `Observable` con lista de observadores
- [ ] Metodo `suscribir_observador(observador: Observer)`
- [ ] Metodo `desuscribir_observador(observador: Observer)`
- [ ] Metodo `notificar_observadores(evento: dict)`
- [ ] Thread-safety en lista de observadores (Lock o copia defensiva)
- [ ] CineManager hereda de Observable
- [ ] Cliente implementa interfaz Observer
- [ ] Notificaciones automaticas al cambiar estado
- [ ] Eventos tienen estructura dict con 'tipo' y datos relevantes
- [ ] Al menos 3 tipos de eventos: NUEVA_PELICULA, NUEVA_FUNCION, FUNCION_CANCELADA
- [ ] Cliente procesa eventos segun tipo
- [ ] Observable no conoce implementacion de Observer (desacoplamiento)

### Patron STRATEGY - Checklist Detallado

- [ ] Interfaz `EstrategiaPrecio` abstracta con metodo `calcular(precio_base)`
- [ ] Al menos 3 implementaciones concretas
- [ ] Estrategias implementadas:
  - [ ] EstrategiaPrecioNormal (retorna precio sin cambios)
  - [ ] EstrategiaDescuentoSemanal (descuento % en dias especificos)
  - [ ] EstrategiaPrecioEstudiante (descuento para estudiantes)
  - [ ] BONUS: EstrategiaPrecioCombo (descuento por cantidad)
  - [ ] BONUS: EstrategiaPrecioSalaPremium (recargo IMAX/VIP)
  - [ ] BONUS: EstrategiaPrecioCompuesta (combina multiples)
- [ ] Estrategia inyectada via `set_estrategia_precio(estrategia)`
- [ ] Entrada delega calculo a estrategia en `get_precio_final()`
- [ ] Estrategias intercambiables sin modificar Entrada
- [ ] Sin condicionales if/else en Entrada para seleccionar algoritmo
- [ ] Estrategias NO modifican estado de Entrada
- [ ] Cambio dinamico en tiempo de ejecucion posible
- [ ] Metodo `get_descripcion()` en estrategias (opcional pero recomendado)

### PEP 8 - Checklist Detallado

- [ ] Nombres de variables: snake_case, sin abreviaciones
- [ ] Nombres de clases: PascalCase consistente
- [ ] Nombres de constantes: UPPER_SNAKE_CASE
- [ ] Imports organizados: Standard → Third-party → Local
- [ ] Docstrings en Google Style (NO JavaDoc)
- [ ] Lineas max 100-120 caracteres
- [ ] 2 lineas en blanco entre clases de nivel superior
- [ ] 1 linea en blanco entre metodos
- [ ] Type hints en todas las firmas publicas
- [ ] Uso de TYPE_CHECKING para forward references si necesario
- [ ] Espaciado correcto alrededor de operadores
- [ ] Sin trailing whitespace

### Codigo Limpio - Checklist Detallado

- [ ] CERO magic numbers (todas las constantes con nombre)
- [ ] **CRITICO**: CERO lambdas en Factory (usar metodos estaticos)
- [ ] Funciones pequenas (<30 lineas idealmente, <50 maximo)
- [ ] Nombres descriptivos (no abreviaciones ni nombres de 1 letra excepto indices)
- [ ] Un nivel de abstraccion por funcion
- [ ] Sin codigo duplicado (DRY)
- [ ] Comentarios solo donde necesario (codigo autoexplicativo)
- [ ] Sin codigo muerto (comentado o sin usar)
- [ ] Sin print() para debugging (usar logging o remover)
- [ ] Validaciones claras y explicitas

### Excepciones - Checklist Detallado

- [ ] Al menos 5 excepciones personalizadas:
  - [ ] AsientoOcupadoException
  - [ ] PeliculaDuplicadaException
  - [ ] SalaOcupadaException
  - [ ] AsientoNoDisponibleException
  - [ ] FuncionConEntradasException
  - [ ] CancelacionDenegadaException
  - [ ] ReservaExpiradaException
  - [ ] EmailDuplicadoException (si se implementa)
- [ ] Excepciones heredan de clase base comun (opcional)
- [ ] Mensajes incluyen contexto (asiento, pelicula, fecha)
- [ ] Excepciones lanzadas en puntos apropiados
- [ ] Try/except usado donde se espera error (IO, conversiones)

---

## Anexo: Mapeo de Historias de Usuario a Criterios

### Epic 1: Gestion de Peliculas y Funciones
- **US-001**: Seccion 4.1, Seccion 1.3 (Observer - notificacion)
- **US-002**: Seccion 4.1 (Consulta cartelera)
- **US-003**: Seccion 4.1, Seccion 2.3 (Validaciones)
- **US-004**: Seccion 4.1 (Consulta funciones)
- **US-005**: Seccion 4.1, Seccion 1.3 (Observer - cancelacion)

### Epic 2: Compra de Entradas
- **US-006**: Seccion 4.2 (Seleccion asientos)
- **US-007**: Seccion 4.2, Seccion 1.2 (Factory Method)
- **US-008**: Seccion 4.2, Seccion 1.4 (Strategy)
- **US-009**: Seccion 4.2, Seccion 1.4 (Strategy combo)
- **US-010**: Seccion 4.2, Seccion 2.3 (Excepciones)

### Epic 3: Registro y Notificaciones a Clientes
- **US-011**: Seccion 4.3, Seccion 2.3 (Validaciones)
- **US-012**: Seccion 4.3, Seccion 1.3 (Observer)
- **US-013**: Seccion 4.3, Seccion 1.3 (Observer especifico)
- **US-014**: Seccion 4.3 (Historial)

### Epic 4: Estrategias de Precios
- **US-015**: Seccion 1.4 (Strategy Normal)
- **US-016**: Seccion 1.4 (Strategy Descuento Semanal)
- **US-017**: Seccion 1
