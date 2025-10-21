from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.tierra import Tierra

class TierraService:
    def crear_tierra_con_plantacion(self, id_padron_catastral: int, superficie: float,
                                   domicilio: str, nombre_plantacion: str) -> Tierra:
        tierra = Tierra(id_padron_catastral, superficie, domicilio)

        # Crear plantación asociada automáticamente
        # Hardcoded values for Plantacion as in Java example
        plantacion = Plantacion(1, nombre_plantacion, 100000, tierra)
        tierra.set_finca(plantacion)

        print(f"Tierra creada: {domicilio} con plantación: {nombre_plantacion}")
        return tierra
