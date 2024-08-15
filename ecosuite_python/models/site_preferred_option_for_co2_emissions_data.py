from enum import Enum


class SitePreferredOptionForCO2EmissionsData(str, Enum):
    GRIDEMISSIONS = "gridemissions"
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
