from enum import Enum


class GetCashFlowTotalsMode(str, Enum):
    ACTUAL = "actual"
    FORECAST = "forecast"
    LBE = "lbe"

    def __str__(self) -> str:
        return str(self.value)
