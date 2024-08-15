from enum import Enum


class GetFinanceReportMode(str, Enum):
    ACTUAL = "actual"
    NORMALISED = "normalised"

    def __str__(self) -> str:
        return str(self.value)
