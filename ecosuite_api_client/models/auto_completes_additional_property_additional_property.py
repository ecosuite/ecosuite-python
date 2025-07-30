from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoCompletesAdditionalPropertyAdditionalProperty")


@_attrs_define
class AutoCompletesAdditionalPropertyAdditionalProperty:
    """
    Attributes:
        projects (Union[Unset, list[str]]):
    """

    projects: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects: Union[Unset, list[str]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        projects = cast(list[str], d.pop("projects", UNSET))

        auto_completes_additional_property_additional_property = cls(
            projects=projects,
        )

        auto_completes_additional_property_additional_property.additional_properties = d
        return auto_completes_additional_property_additional_property

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
