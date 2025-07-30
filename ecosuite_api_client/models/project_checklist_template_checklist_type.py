from enum import Enum


class ProjectChecklistTemplateChecklistType(str, Enum):
    ICR = "ICR"
    NTP = "NTP"
    PTO = "PTO"

    def __str__(self) -> str:
        return str(self.value)
