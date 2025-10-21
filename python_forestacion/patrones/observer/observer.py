from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class Observer(Generic[T], ABC):
    """Interfaz para el patron Observer."""

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        pass