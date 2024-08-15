from enum import Enum


class NotificationType(str, Enum):
    ALERT = "alert"
    DEMANDRESPONSE = "demandresponse"
    MEDIA = "media"
    PROJECT = "project"
    REPORT = "report"
    UPCOMING = "upcoming"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
