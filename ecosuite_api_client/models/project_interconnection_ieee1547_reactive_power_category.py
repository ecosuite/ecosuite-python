from enum import Enum


class ProjectInterconnectionIEEE1547ReactivePowerCategory(str, Enum):
    A = "A"
    B = "B"
    LEGACY = "legacy"

    def __str__(self) -> str:
        return str(self.value)
