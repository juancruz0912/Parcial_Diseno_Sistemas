# Rubrica de Evaluacion Tecnica - Sistema de Gestion Forestal

**Proyecto**: PythonForestal
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
| **Implementacion correcta del patron** | 5 | Clase implementa Singleton con instancia unica | `__new__` con control de instancia unica |
| **Thread-safety** | 5 | Implementacion thread-safe con Lock | Uso de `threading.Lock` con double-checked locking |
| **Acceso consistente** | 3 | Metodo `get_instance()` disponible | Metodo de clase que retorna instancia |
| **Inicializacion perezosa** | 3 | Lazy initialization correcta | Instancia se crea solo cuando se solicita |
| **Uso apropiado en el sistema** | 4 | Singleton usado donde corresponde (Registry) | CultivoServiceRegistry es Singleton |

**Puntaje Seccion 1.1**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Singleton]
```

---

### 1.2 Patron FACTORY METHOD (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Factory encapsula creacion de objetos | Metodo estatico `crear_cultivo(especie)` |
| **Desacoplamiento** | 5 | Cliente no conoce clases concretas | Retorna tipo base `Cultivo`, no tipos concretos |
| **Extensibilidad** | 4 | Facil agregar nuevos tipos | Diccionario de factories, no if/elif cascades |
| **Validacion de entrada** | 3 | Valida parametros y lanza excepciones | Lanza `ValueError` si especie desconocida |
| **Uso apropiado en el sistema** | 3 | Factory usado en servicios (PlantacionService) | `plantar()` usa factory internamente |

**Puntaje Seccion 1.2**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Factory]
```

---

### 1.3 Patron OBSERVER (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Observable y Observer implementados | Clases `Observable[T]` y `Observer[T]` |
| **Generics para tipo-seguridad** | 5 | Uso de TypeVar y Generic[T] | `Observable[float]`, `Observer[float]` |
| **Notificaciones automaticas** | 4 | Observadores notificados al cambiar estado | `notificar_observadores()` llamado en sensores |
| **Desacoplamiento** | 3 | Observable no conoce detalles de Observer | Lista generica de observadores |
| **Uso apropiado en el sistema** | 3 | Sensores como Observable, Control como Observer | TemperaturaReaderTask, ControlRiegoTask |

**Puntaje Seccion 1.3**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Observer]
```

---

### 1.4 Patron STRATEGY (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Interfaz Strategy con implementaciones | `AbsorcionAguaStrategy` (abstracta) |
| **Algoritmos intercambiables** | 5 | Multiples estrategias implementadas | `AbsorcionSeasonalStrategy`, `AbsorcionConstanteStrategy` |
| **Inyeccion de dependencias** | 4 | Estrategia inyectada via constructor | Servicios reciben strategy en `__init__` |
| **Delegacion correcta** | 3 | Servicios delegan calculo a estrategia | `calcular_absorcion()` llamado desde servicio |
| **Uso apropiado en el sistema** | 3 | Estrategias usadas segun tipo de cultivo | Arboles: seasonal, Hortalizas: constante |

**Puntaje Seccion 1.4**: _____ / 20

**Notas del evaluador**:
```
[Espacio para comentarios sobre implementacion de Strategy]
```

---

**PUNTAJE TOTAL SECCION 1**: _____ / 80

---

## Seccion 2: Arquitectura y Diseno (60 puntos)

### 2.1 Separacion de Responsabilidades (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Entidades vs Servicios** | 5 | Entidades solo datos, servicios solo logica | Clases en `entidades/` vs `servicios/` |
| **Service Layer Pattern** | 5 | Capa de servicios bien definida | Servicios contienen toda la logica de negocio |
| **Principio SRP** | 4 | Cada clase una unica responsabilidad | Una clase = un concepto de dominio |
| **Cohesion alta** | 3 | Elementos relacionados agrupados | Modulos tematicos (cultivos, terrenos, personal) |
| **Acoplamiento bajo** | 3 | Dependencias minimizadas | Uso de interfaces, inyeccion de dependencias |

**Puntaje Seccion 2.1**: _____ / 20

---

### 2.2 Jerarquia de Clases (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Herencia apropiada** | 5 | Jerarquia logica de clases | `CultivoService` → `ArbolService` → servicios especificos |
| **Eliminacion de duplicacion** | 4 | Codigo compartido en clases base | `absorver_agua()` en `CultivoService` base |
| **Polimorfismo** | 3 | Subtipos intercambiables | Todos los cultivos son `Cultivo` |
| **Interfaces bien definidas** | 3 | Contratos claros entre clases | Metodos abstractos en clases base |

**Puntaje Seccion 2.2**: _____ / 15

---

### 2.3 Manejo de Excepciones (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Jerarquia de excepciones** | 5 | Excepciones personalizadas heredan de base | `ForestacionException` base |
| **Excepciones especificas** | 4 | Excepciones de dominio implementadas | `SuperficieInsuficienteException`, `AguaAgotadaException`, `PersistenciaException` |
| **Mensajes descriptivos** | 3 | Mensajes claros para usuario y tecnico | Separacion user_message / technical_message |
| **Uso apropiado** | 3 | Excepciones usadas en puntos correctos | Validaciones lanzan excepciones apropiadas |

**Puntaje Seccion 2.3**: _____ / 15

---

### 2.4 Organizacion del Codigo (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Estructura de paquetes** | 3 | Organizacion logica de modulos | Paquetes: entidades, servicios, patrones, riego, excepciones |
| **Modulos tematicos** | 3 | Agrupacion por dominio | cultivos/, terrenos/, personal/ |
| **Archivos `__init__.py`** | 2 | Inicializacion de paquetes | Todos los paquetes con `__init__.py` |
| **Importaciones limpias** | 2 | Sin imports circulares | Uso de TYPE_CHECKING para forward references |

**Puntaje Seccion 2.4**: _____ / 10

---

**PUNTAJE TOTAL SECCION 2**: _____ / 60

---

## Seccion 3: Calidad de Codigo (60 puntos)

### 3.1 PEP 8 Compliance (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Nombres de variables** | 4 | snake_case, descriptivos, sin abreviaciones | `superficie` no `sup`, `altura` no `alt` |
| **Nombres de clases** | 3 | PascalCase consistente | `CultivoFactory`, `PlantacionService` |
| **Nombres de constantes** | 3 | UPPER_SNAKE_CASE en modulo centralizado | Todas en `constantes.py` |
| **Organizacion de imports** | 4 | PEP 8: Standard → Third-party → Local | Secciones comentadas |
| **Longitud de linea** | 2 | Maximo 100-120 caracteres | No lineas excesivamente largas |
| **Espaciado y formato** | 4 | Espaciado consistente segun PEP 8 | 2 lineas entre clases, 1 entre metodos |

**Puntaje Seccion 3.1**: _____ / 20

---

### 3.2 Documentacion (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Docstrings en clases** | 4 | Todas las clases documentadas | Docstring en cada clase publica |
| **Docstrings en metodos** | 4 | Metodos publicos documentados | Google Style: Args, Returns, Raises |
| **Formato Google Style** | 3 | Estilo consistente (NO JavaDoc) | Args: / Returns: / Raises: |
| **Comentarios en codigo complejo** | 2 | Explicacion de logica no obvia | Comentarios donde necesario |
| **README y documentacion externa** | 2 | Documentacion de proyecto completa | README.md, USER_STORIES.md |

**Puntaje Seccion 3.2**: _____ / 15

---

### 3.3 Type Hints (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Type hints en firmas** | 4 | Parametros y retornos tipados | `def metodo(param: str) -> int:` |
| **Uso de TYPE_CHECKING** | 3 | Evita imports circulares | `if TYPE_CHECKING: from ...` |
| **Generics donde apropiado** | 3 | TypeVar y Generic[T] usados | `Observable[T]`, `Paquete[T]` |

**Puntaje Seccion 3.3**: _____ / 10

---

### 3.4 Principios de Codigo Limpio (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **NO magic numbers** | 5 | Constantes centralizadas | CERO valores hardcodeados |
| **NO lambdas** | 4 | Funciones/metodos nombrados | Metodos estaticos en lugar de lambdas |
| **Funciones pequenas** | 3 | Metodos con responsabilidad unica | Funciones < 30 lineas idealmente |
| **Nombres descriptivos** | 3 | Variables y metodos autoexplicativos | `calcular_absorcion()` no `calc()` |

**Puntaje Seccion 3.4**: _____ / 15

---

**PUNTAJE TOTAL SECCION 3**: _____ / 60

---

## Seccion 4: Funcionalidad del Sistema (40 puntos)

### 4.1 Gestion de Cultivos (12 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Multiples tipos de cultivos** | 4 | Al menos 4 tipos implementados | Pino, Olivo, Lechuga, Zanahoria |
| **Plantacion funcional** | 4 | Sistema planta y valida superficie | `plantar()` con validacion |
| **Riego funcional** | 4 | Riego actualiza agua de cultivos | `regar()` consume y distribuye agua |

**Puntaje Seccion 4.1**: _____ / 12

---

### 4.2 Sistema de Riego Automatizado (12 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Sensores operativos** | 4 | Temperatura y humedad en threads | Lecturas cada N segundos |
| **Control automatico** | 4 | Riego basado en condiciones | Evalua temp y humedad |
| **Graceful shutdown** | 4 | Detencion limpia de threads | Uso de Event y timeout |

**Puntaje Seccion 4.2**: _____ / 12

---

### 4.3 Gestion de Personal (8 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Trabajadores y tareas** | 4 | Sistema asigna y ejecuta tareas | `trabajar()` funcional |
| **Apto medico** | 4 | Validacion de certificacion medica | Verifica apto antes de trabajar |

**Puntaje Seccion 4.3**: _____ / 8

---

### 4.4 Persistencia (8 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Guardado funcional** | 4 | Registros persisten en disco | `persistir()` crea archivo .dat |
| **Lectura funcional** | 4 | Registros recuperados correctamente | `leer_registro()` deserializa |

**Puntaje Seccion 4.4**: _____ / 8

---

**PUNTAJE TOTAL SECCION 4**: _____ / 40

---

## Seccion 5: Buenas Practicas Avanzadas (20 puntos)

### 5.1 Threading y Concurrencia (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Threads daemon** | 3 | Threads de fondo como daemon | `daemon=True` |
| **Thread-safety** | 4 | Operaciones thread-safe donde necesario | Lock en Singleton, Event en threads |
| **Manejo de recursos** | 3 | Cierre apropiado de threads | `join()` con timeout |

**Puntaje Seccion 5.1**: _____ / 10

---

### 5.2 Validacion y Robustez (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Validacion de entrada** | 4 | Parametros validados en setters | Superficie > 0, agua >= 0 |
| **Defensive copying** | 3 | Listas inmutables donde apropiado | `get_cultivos()` retorna copia |
| **Manejo de errores** | 3 | Try/except apropiados | Persistencia con manejo de IOError |

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
- Excelente implementacion de patrones de diseno
- Codigo muy limpio y bien documentado
- Arquitectura bien pensada
```

### Areas de Mejora
```
[Espacio para comentarios sobre aspectos a mejorar]

Ejemplo:
- Faltan tests unitarios
- Documentacion de API podria ser mas detallada
- Considerar agregar logging
```

### Recomendaciones
```
[Espacio para recomendaciones especificas]

Ejemplo:
- Agregar tests con pytest
- Implementar patron Command para deshacer operaciones
- Considerar persistencia con base de datos relacional
```

---

## Criterios de Evaluacion Detallados

### Patron SINGLETON - Checklist Detallado

- [ ] Clase tiene atributo `_instance` de clase
- [ ] Metodo `__new__` implementado para controlar instanciacion
- [ ] Thread-safe con `threading.Lock`
- [ ] Double-checked locking correctamente implementado
- [ ] Metodo `get_instance()` disponible
- [ ] Inicializacion perezosa (lazy)
- [ ] Una sola instancia garantizada
- [ ] Usado apropiadamente (Registry, no en todas las clases)

### Patron FACTORY METHOD - Checklist Detallado

- [ ] Metodo factory es estatico
- [ ] Recibe parametro para determinar tipo a crear
- [ ] Retorna tipo base/interfaz, no tipo concreto
- [ ] Cliente NO importa clases concretas
- [ ] Usa diccionario de factories (NO if/elif)
- [ ] Facil agregar nuevos tipos sin modificar factory
- [ ] Validacion de parametros con excepciones
- [ ] Usado en servicios (PlantacionService.plantar)

### Patron OBSERVER - Checklist Detallado

- [ ] Interfaz `Observer[T]` con metodo `actualizar(evento: T)`
- [ ] Clase `Observable[T]` con lista de observadores
- [ ] Metodo `agregar_observador(observador: Observer[T])`
- [ ] Metodo `eliminar_observador(observador: Observer[T])`
- [ ] Metodo `notificar_observadores(evento: T)`
- [ ] Uso de Generics (TypeVar, Generic[T])
- [ ] Sensores heredan de Observable
- [ ] Controlador hereda de Observer
- [ ] Notificaciones automaticas al cambiar estado

### Patron STRATEGY - Checklist Detallado

- [ ] Interfaz `Strategy` abstracta con metodo abstracto
- [ ] Al menos 2 implementaciones concretas
- [ ] Estrategia inyectada via constructor
- [ ] Servicios delegan calculo a estrategia
- [ ] Estrategias intercambiables sin modificar cliente
- [ ] Sin condicionales if/else para seleccionar algoritmo
- [ ] Estrategias usan constantes (no magic numbers)
- [ ] Usado apropiadamente segun tipo de cultivo

### PEP 8 - Checklist Detallado

- [ ] Nombres de variables: snake_case, sin abreviaciones
- [ ] Nombres de clases: PascalCase
- [ ] Nombres de constantes: UPPER_SNAKE_CASE
- [ ] Imports organizados: Standard → Third-party → Local
- [ ] Docstrings en Google Style (NO JavaDoc)
- [ ] Lineas max 100-120 caracteres
- [ ] 2 lineas en blanco entre clases
- [ ] 1 linea en blanco entre metodos
- [ ] Type hints en todas las firmas publicas
- [ ] Uso de TYPE_CHECKING para forward references

### Codigo Limpio - Checklist Detallado

- [ ] CERO magic numbers (todas en constantes.py)
- [ ] CERO lambdas (usar funciones/metodos nombrados)
- [ ] Funciones pequenas (<30 lineas idealmente)
- [ ] Nombres descriptivos (no abreviaciones)
- [ ] Un nivel de abstraccion por funcion
- [ ] Sin codigo duplicado
- [ ] Comentarios solo donde necesario (codigo autoexplicativo)
- [ ] Sin codigo muerto (comentado o sin usar)

---

## Anexo: Mapeo de Historias de Usuario a Criterios

### Epic 1: Terrenos y Plantaciones
- **US-001**: Seccion 4.1 (Gestion de Cultivos)
- **US-002**: Seccion 4.1 (Gestion de Cultivos)
- **US-003**: Seccion 4.4 (Persistencia)

### Epic 2: Gestion de Cultivos
- **US-004 a US-009**: Seccion 4.1 (Gestion de Cultivos), Seccion 1.2 (Factory), Seccion 1.4 (Strategy)

### Epic 3: Riego Automatizado
- **US-010 a US-013**: Seccion 4.2 (Riego Automatizado), Seccion 1.3 (Observer), Seccion 5.1 (Threading)

### Epic 4: Gestion de Personal
- **US-014 a US-017**: Seccion 4.3 (Gestion de Personal)

### Epic 5: Operaciones de Negocio
- **US-018 a US-020**: Seccion 4.1 (Gestion de Cultivos), Seccion 2.1 (Separacion de Responsabilidades)

### Epic 6: Persistencia
- **US-021 a US-023**: Seccion 4.4 (Persistencia), Seccion 2.3 (Manejo de Excepciones)

### Historias Tecnicas
- **US-TECH-001**: Seccion 1.1 (Singleton)
- **US-TECH-002**: Seccion 1.2 (Factory)
- **US-TECH-003**: Seccion 1.3 (Observer)
- **US-TECH-004**: Seccion 1.4 (Strategy)
- **US-TECH-005**: Seccion 2.1 (Arquitectura)

---

## Instrucciones para el Evaluador

### Antes de Evaluar

1. **Leer documentacion**: README.md, USER_STORIES.md, CLAUDE.md
2. **Ejecutar sistema**: `python main.py` debe completar exitosamente
3. **Revisar estructura**: Verificar organizacion de paquetes
4. **Identificar patrones**: Localizar implementaciones de cada patron

### Durante la Evaluacion

1. **Marcar checkboxes**: Usar checklists detallados por patron
2. **Asignar puntajes**: Ser objetivo segun escala de puntuacion
3. **Tomar notas**: Documentar fortalezas y areas de mejora
4. **Buscar evidencias**: Verificar que criterios se cumplan en codigo

### Despues de Evaluar

1. **Calcular totales**: Sumar puntajes por seccion
2. **Determinar calificacion**: Segun tabla de rangos
3. **Escribir comentarios**: Feedback constructivo y especifico
4. **Dar recomendaciones**: Sugerencias concretas de mejora

### Criterios de Objetividad

- **Evidencia en codigo**: Solo puntuar lo que esta implementado
- **No suponer**: Si no se ve, no esta
- **Ser consistente**: Aplicar mismos criterios a todos los proyectos
- **Documentar decisiones**: Justificar puntajes en comentarios

---

**Evaluador**: ________________________________
**Fecha de Evaluacion**: ____________________
**Firma**: ___________________________________

---

**Version de Rubrica**: 1.0.0
**Ultima Actualizacion**: Octubre 2025
**Proyecto de Referencia**: PythonForestal v1.0.0
