from enum import Enum


class ProjectProjectStatus(str, Enum):
    CONSTRUCTION = "Construction"
    INTERCONNECTION = "Interconnection"
    NEW_PROJECT = "New Project"
    OPERATIONAL = "Operational"
    PERMITTING = "Permitting"
    PRE_CONSTRUCTION = "Pre-Construction"
    PTO = "PTO"

    def __str__(self) -> str:
        return str(self.value)
