from datetime import date

class AptoMedico:
    def __init__(self, apto: bool, fecha_emision: date, observaciones: str):
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def esta_apto(self) -> bool:
        return self._apto

    def set_apto(self, apto: bool) -> None:
        self._apto = apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def set_fecha_emision(self, fecha_emision: date) -> None:
        self._fecha_emision = fecha_emision

    def get_observaciones(self) -> str:
        return self._observaciones

    def set_observaciones(self, observaciones: str) -> None:
        self._observaciones = observaciones

    def get_resumen(self) -> str:
        return f"Apto: {self._apto} | Fecha: {self._fecha_emision} | Obs: {self._observaciones}"
