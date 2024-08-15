import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Range")


@_attrs_define
class Range:
    """
    Attributes:
        local_start_date (Union[Unset, datetime.datetime]):
        local_end_date (Union[Unset, datetime.datetime]):
    """

    local_start_date: Union[Unset, datetime.datetime] = UNSET
    local_end_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        local_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.local_start_date, Unset):
            local_start_date = self.local_start_date.isoformat()

        local_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.local_end_date, Unset):
            local_end_date = self.local_end_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_start_date is not UNSET:
            field_dict["localStartDate"] = local_start_date
        if local_end_date is not UNSET:
            field_dict["localEndDate"] = local_end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _local_start_date = d.pop("localStartDate", UNSET)
        local_start_date: Union[Unset, datetime.datetime]
        if isinstance(_local_start_date, Unset):
            local_start_date = UNSET
        else:
            local_start_date = isoparse(_local_start_date)

        _local_end_date = d.pop("localEndDate", UNSET)
        local_end_date: Union[Unset, datetime.datetime]
        if isinstance(_local_end_date, Unset):
            local_end_date = UNSET
        else:
            local_end_date = isoparse(_local_end_date)

        range_ = cls(
            local_start_date=local_start_date,
            local_end_date=local_end_date,
        )

        range_.additional_properties = d
        return range_

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
