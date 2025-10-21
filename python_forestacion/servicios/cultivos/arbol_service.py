from python_forestacion.entidades.cultivos.arbol import Arbol

class ArbolService:
    def crecer(self, arbol: Arbol, incremento: float) -> bool:
        if 0 < incremento < 1:
            arbol.set_altura(arbol.get_altura() + incremento)
            self._consumir_agua_por_crecimiento(arbol)
            return True
        return False

    def _consumir_agua_por_crecimiento(self, arbol: Arbol) -> None:
        if arbol.get_agua() > 0:
            arbol.set_agua(arbol.get_agua() - 1)
