from enum import Enum


class SystemSystemStatus(str, Enum):
    CONSTRUCTION = "Construction"
    INTERCONNECTION = "Interconnection"
    NEW_SYSTEM = "New System"
    OPERATIONAL = "Operational"
    PERMITTING = "Permitting"
    PRE_CONSTRUCTION = "Pre-Construction"
    PTO = "PTO"

    def __str__(self) -> str:
        return str(self.value)
