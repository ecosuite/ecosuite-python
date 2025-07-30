from enum import Enum


class ProjectFinanceSettingsAccountingProvider(str, Enum):
    SOFTLEDGER = "softledger"

    def __str__(self) -> str:
        return str(self.value)
