from enum import Enum


class ProjectInterconnectionIEEE1547DisturbanceCategory(str, Enum):
    I = "I"
    II = "II"
    LEGACY = "legacy"

    def __str__(self) -> str:
        return str(self.value)
