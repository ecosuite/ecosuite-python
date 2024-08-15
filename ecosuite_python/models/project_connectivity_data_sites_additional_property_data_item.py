from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectConnectivityDataSitesAdditionalPropertyDataItem")


@_attrs_define
class ProjectConnectivityDataSitesAdditionalPropertyDataItem:
    """
    Attributes:
        date (Union[Unset, str]):
        bytes_ (Union[Unset, int]):
    """

    date: Union[Unset, str] = UNSET
    bytes_: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date = self.date

        bytes_ = self.bytes_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date = d.pop("date", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        project_connectivity_data_sites_additional_property_data_item = cls(
            date=date,
            bytes_=bytes_,
        )

        project_connectivity_data_sites_additional_property_data_item.additional_properties = d
        return project_connectivity_data_sites_additional_property_data_item

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
