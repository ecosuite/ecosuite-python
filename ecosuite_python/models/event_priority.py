from enum import IntEnum


class EventPriority(IntEnum):
    VALUE_1 = 1
    VALUE_5 = 5
    VALUE_10 = 10

    def __str__(self) -> str:
        return str(self.value)
