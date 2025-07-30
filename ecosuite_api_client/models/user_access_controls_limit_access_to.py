from enum import Enum


class UserAccessControlsLimitAccessTo(str, Enum):
    NO = "no"
    PORTFOLIOS = "portfolios"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
