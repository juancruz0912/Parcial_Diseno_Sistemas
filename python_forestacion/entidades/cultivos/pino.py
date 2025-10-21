from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO, PINO_INITIAL_ALTURA

class Pino(Arbol):
    """Representa un tipo de cultivo de pino, heredando de Arbol.

    Attributes:
        _variedad (str): La variedad específica del pino.
    """
    def __init__(self, variedad: str):
        """Inicializa una nueva instancia de Pino.

        Args:
            variedad (str): La variedad del pino (e.g., "Parana", "Elliott").
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=PINO_INITIAL_ALTURA
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """Obtiene la variedad del pino.

        Returns:
            str: La variedad del pino.
        """
        return self._variedad
