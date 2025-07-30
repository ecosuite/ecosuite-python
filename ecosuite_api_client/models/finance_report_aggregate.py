from enum import Enum


class FinanceReportAggregate(str, Enum):
    MONTH = "month"
    QUARTER = "quarter"
    TOTAL = "total"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
