from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectIconsItem")


@_attrs_define
class ProjectIconsItem:
    """
    Attributes:
        tooltip (str):
        icon_name (Union[Unset, str]):
        meaning (Union[Unset, str]):
    """

    tooltip: str
    icon_name: Union[Unset, str] = UNSET
    meaning: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tooltip = self.tooltip

        icon_name = self.icon_name

        meaning = self.meaning

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tooltip": tooltip,
            }
        )
        if icon_name is not UNSET:
            field_dict["iconName"] = icon_name
        if meaning is not UNSET:
            field_dict["meaning"] = meaning

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tooltip = d.pop("tooltip")

        icon_name = d.pop("iconName", UNSET)

        meaning = d.pop("meaning", UNSET)

        project_icons_item = cls(
            tooltip=tooltip,
            icon_name=icon_name,
            meaning=meaning,
        )

        project_icons_item.additional_properties = d
        return project_icons_item

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
