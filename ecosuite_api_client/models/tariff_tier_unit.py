from enum import Enum


class TariffTierUnit(str, Enum):
    KWH = "kWh"

    def __str__(self) -> str:
        return str(self.value)
