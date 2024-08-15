from enum import Enum


class ProjectPredictedGenerationDatumsAggregation(str, Enum):
    DAY = "day"
    HOUR = "hour"
    MONTH = "month"
    VALUE_4 = "15minute"
    VALUE_5 = "5minute"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
