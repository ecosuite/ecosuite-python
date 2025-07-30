from enum import Enum


class ProjectRevenueType(str, Enum):
    COMMUNITYSOLAR = "communitySolar"
    FEEDINTARIFF = "feedInTariff"
    PPA = "ppa"

    def __str__(self) -> str:
        return str(self.value)
