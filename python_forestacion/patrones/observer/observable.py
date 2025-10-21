from typing import Generic, TypeVar, List
from abc import ABC, abstractmethod
from threading import Lock

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para observadores en el patrón Observer.

    Los observadores implementan el método `actualizar` para reaccionar a los eventos
    notificados por un `Observable`.
    """
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Actualiza el estado del observador en respuesta a un evento.

        Args:
            evento (T): El evento o dato notificado por el Observable.
        """
        pass

class Observable(Generic[T], ABC):
    """Clase base abstracta para objetos observables en el patrón Observer.

    Permite registrar, eliminar y notificar a los observadores sobre cambios de estado.
    """
    def __init__(self):
        """Inicializa una nueva instancia de Observable.
        """
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
