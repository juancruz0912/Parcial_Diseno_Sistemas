from typing import List, Type, TypeVar

from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.entidades.terrenos.plantacion import Plantacion

from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException

from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

from python_forestacion.constantes import AGUA_MINIMA

T = TypeVar('T', bound=Cultivo)

class PlantacionService:
    def __init__(self, cultivo_service_registry: CultivoServiceRegistry):
        self._cultivo_service_registry = cultivo_service_registry

    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int) -> bool:
        superficie_ocupada = sum(c.get_superficie() for c in plantacion.get_cultivos_interno())
        sup_disponible = plantacion.get_situada_en().get_superficie() - superficie_ocupada

        for _ in range(cantidad):
            cultivo = self._crear_cultivo(especie)

            if cultivo is None:
                raise ValueError(f"Especie de cultivo no reconocida: {especie}")

            superficie_requerida = cultivo.get_superficie()
            sup_disponible -= superficie_requerida

            if sup_disponible >= 0:
                plantacion.get_cultivos_interno().append(cultivo)
                print(f"Se plantó un/a: {cultivo.__class__.__name__}")
            else:
                raise SuperficieInsuficienteException(
                    cultivo.__class__.__name__,
                    superficie_requerida,
                    sup_disponible + superficie_requerida
                )
        return True

    def _crear_cultivo(self, especie: str) -> Cultivo:
        if especie == "Pino":
            return Pino("cedro")
        elif especie == "Olivo":
            return Olivo(TipoAceituna.NEGRA)
        elif especie == "Lechuga":
            return Lechuga("Mantecosa")
        elif especie == "Zanahoria":
            return Zanahoria(True)
        else:
            return None

    def regar(self, plantacion: Plantacion) -> bool:
        print(f"Regando finca: {plantacion.get_nombre()}")

        for cultivo in plantacion.get_cultivos_interno():
            agua_actual = plantacion.get_agua_disponible()

            if agua_actual > AGUA_MINIMA:
                agua_absorvida = self._absorver_agua_cultivo(cultivo)
                plantacion.set_agua_disponible(agua_actual - agua_absorvida)
            else:
                raise AguaAgotadaException(agua_actual, AGUA_MINIMA)
        return True

    def _absorver_agua_cultivo(self, cultivo: Cultivo) -> int:
        return self._cultivo_service_registry.absorber_agua(cultivo)

    def consumir(self, plantacion: Plantacion, tipo_cultivo: Type[T]) -> bool:
        # Create a new list to hold crops that are not consumed
        cultivos_restantes = []
        consumidos = False
        for cult in plantacion.get_cultivos_interno():
            if not isinstance(cult, tipo_cultivo):
                cultivos_restantes.append(cult)
            else:
                consumidos = True
        plantacion.set_cultivos(cultivos_restantes)
        return consumidos
