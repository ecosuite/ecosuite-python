from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.auto_completes_additional_property import AutoCompletesAdditionalProperty


T = TypeVar("T", bound="AutoCompletes")


@_attrs_define
class AutoCompletes:
    """Keyed by property name"""

    additional_properties: dict[str, "AutoCompletesAdditionalProperty"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_completes_additional_property import AutoCompletesAdditionalProperty

        d = dict(src_dict)
        auto_completes = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AutoCompletesAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        auto_completes.additional_properties = additional_properties
        return auto_completes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "AutoCompletesAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "AutoCompletesAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
