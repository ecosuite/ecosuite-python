import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentLogsPayments")


@_attrs_define
class PaymentLogsPayments:
    """
    Attributes:
        advised_amount (Union[Unset, float]):
        reading (Union[Unset, float]):
        advised_reading (Union[Unset, float]):
        expected_amount (Union[Unset, float]):
        start (Union[Unset, datetime.date]):
        end (Union[Unset, datetime.date]):
    """

    advised_amount: Union[Unset, float] = UNSET
    reading: Union[Unset, float] = UNSET
    advised_reading: Union[Unset, float] = UNSET
    expected_amount: Union[Unset, float] = UNSET
    start: Union[Unset, datetime.date] = UNSET
    end: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        advised_amount = self.advised_amount

        reading = self.reading

        advised_reading = self.advised_reading

        expected_amount = self.expected_amount

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: Union[Unset, str] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advised_amount is not UNSET:
            field_dict["advisedAmount"] = advised_amount
        if reading is not UNSET:
            field_dict["reading"] = reading
        if advised_reading is not UNSET:
            field_dict["advisedReading"] = advised_reading
        if expected_amount is not UNSET:
            field_dict["expectedAmount"] = expected_amount
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        advised_amount = d.pop("advisedAmount", UNSET)

        reading = d.pop("reading", UNSET)

        advised_reading = d.pop("advisedReading", UNSET)

        expected_amount = d.pop("expectedAmount", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.date]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start).date()

        _end = d.pop("end", UNSET)
        end: Union[Unset, datetime.date]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end).date()

        payment_logs_payments = cls(
            advised_amount=advised_amount,
            reading=reading,
            advised_reading=advised_reading,
            expected_amount=expected_amount,
            start=start,
            end=end,
        )

        payment_logs_payments.additional_properties = d
        return payment_logs_payments

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
