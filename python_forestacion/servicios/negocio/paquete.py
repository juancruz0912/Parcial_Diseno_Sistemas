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
