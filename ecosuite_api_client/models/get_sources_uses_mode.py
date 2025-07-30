from enum import Enum


class GetSourcesUsesMode(str, Enum):
    LIFETIME = "lifetime"
    TODATE = "toDate"

    def __str__(self) -> str:
        return str(self.value)
