import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordPaymentDetailsCashFlowsItem")


@_attrs_define
class RecordPaymentDetailsCashFlowsItem:
    """
    Attributes:
        date (Union[Unset, datetime.date]):
        monthly_total (Union[Unset, float]):
    """

    date: Union[Unset, datetime.date] = UNSET
    monthly_total: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        monthly_total = self.monthly_total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if monthly_total is not UNSET:
            field_dict["monthlyTotal"] = monthly_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        monthly_total = d.pop("monthlyTotal", UNSET)

        record_payment_details_cash_flows_item = cls(
            date=date,
            monthly_total=monthly_total,
        )

        record_payment_details_cash_flows_item.additional_properties = d
        return record_payment_details_cash_flows_item

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
