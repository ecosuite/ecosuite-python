from enum import Enum


class ProjectInterconnectionWithdrawalReason(str, Enum):
    ENVIRONMENTAL = "environmental"
    INTERCONNECTIONCOSTS = "interconnectionCosts"
    NOTAPPLICABLE = "notApplicable"
    OTHER = "other"
    PERMITTING = "permitting"
    SITECONTROL = "siteControl"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
