from enum import Enum


class EventType(str, Enum):
    DATA = "data"
    ENERGY = "energy"
    FINANCE = "finance"
    OTHER = "other"
    SOLARNETWORK = "solarnetwork"

    def __str__(self) -> str:
        return str(self.value)
