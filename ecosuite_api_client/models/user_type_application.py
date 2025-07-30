from enum import Enum


class UserTypeApplication(str, Enum):
    AMS = "ams"
    ECONODE = "econode"

    def __str__(self) -> str:
        return str(self.value)
