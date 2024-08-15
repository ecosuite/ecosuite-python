from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property import (
        DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalProperty,
    )


T = TypeVar("T", bound="DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystems")


@_attrs_define
class DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystems:
    """Keyed by system code"""

    additional_properties: Dict[
        str, "DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalProperty"
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property import (
            DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalProperty,
        )

        d = src_dict.copy()
        device_sources_response_200_projects_additional_property_sites_additional_property_systems = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        device_sources_response_200_projects_additional_property_sites_additional_property_systems.additional_properties = additional_properties
        return device_sources_response_200_projects_additional_property_sites_additional_property_systems

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> "DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: "DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalProperty",
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
