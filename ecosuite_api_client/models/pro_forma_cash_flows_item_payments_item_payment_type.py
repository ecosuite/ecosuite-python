from enum import Enum


class ProFormaCashFlowsItemPaymentsItemPaymentType(str, Enum):
    AMORTIZATION = "amortization"
    GENERATION = "generation"
    RECURRING = "recurring"
    SCHEDULED = "scheduled"
    SIZE = "size"
    TARIFF = "tariff"

    def __str__(self) -> str:
        return str(self.value)
