from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicProjectSitesItemSystemsItem")


@_attrs_define
class PublicProjectSitesItemSystemsItem:
    """
    Attributes:
        name (Union[Unset, str]):
        dc_size (Union[Unset, float]):
        type (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    dc_size: Union[Unset, float] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        dc_size = self.dc_size

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if dc_size is not UNSET:
            field_dict["dcSize"] = dc_size
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        dc_size = d.pop("dcSize", UNSET)

        type = d.pop("type", UNSET)

        public_project_sites_item_systems_item = cls(
            name=name,
            dc_size=dc_size,
            type=type,
        )

        public_project_sites_item_systems_item.additional_properties = d
        return public_project_sites_item_systems_item

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
