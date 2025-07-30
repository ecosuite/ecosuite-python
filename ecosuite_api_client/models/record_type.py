from enum import Enum


class RecordType(str, Enum):
    COMPLIANCE = "compliance"
    ENERGY = "energy"
    FINANCIAL = "financial"

    def __str__(self) -> str:
        return str(self.value)
