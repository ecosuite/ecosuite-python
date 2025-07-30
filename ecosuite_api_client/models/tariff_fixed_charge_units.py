from enum import Enum


class TariffFixedChargeUnits(str, Enum):
    VALUE_0 = "$/day"
    VALUE_1 = "$/month"
    VALUE_2 = "$/year"

    def __str__(self) -> str:
        return str(self.value)
