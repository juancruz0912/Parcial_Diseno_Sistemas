from python_forestacion.entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    _cant_arboles = 0

    def __init__(self, agua: int, superficie: float, altura: float):
        super().__init__(agua, superficie)
        Arbol._cant_arboles += 1
        self._id = Arbol._cant_arboles
        self._altura = altura

    def get_id(self) -> int:
        return self._id

    def get_altura(self) -> float:
        return self._altura

    def set_altura(self, altura: float) -> None:
        self._altura = altura

    @staticmethod
    def get_cant_arboles() -> int:
        return Arbol._cant_arboles
