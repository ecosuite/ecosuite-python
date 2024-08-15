from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.device_sources_response_200_projects_additional_property import (
        DeviceSourcesResponse200ProjectsAdditionalProperty,
    )


T = TypeVar("T", bound="DeviceSourcesResponse200Projects")


@_attrs_define
class DeviceSourcesResponse200Projects:
    """Keyed by project code"""

    additional_properties: Dict[str, "DeviceSourcesResponse200ProjectsAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_sources_response_200_projects_additional_property import (
            DeviceSourcesResponse200ProjectsAdditionalProperty,
        )

        d = src_dict.copy()
        device_sources_response_200_projects = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DeviceSourcesResponse200ProjectsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        device_sources_response_200_projects.additional_properties = additional_properties
        return device_sources_response_200_projects

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "DeviceSourcesResponse200ProjectsAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "DeviceSourcesResponse200ProjectsAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
