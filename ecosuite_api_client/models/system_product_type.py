from enum import Enum


class SystemProductType(str, Enum):
    CONSUMPTION = "consumption"
    GENERATION = "generation"
    STORAGE = "storage"

    def __str__(self) -> str:
        return str(self.value)
