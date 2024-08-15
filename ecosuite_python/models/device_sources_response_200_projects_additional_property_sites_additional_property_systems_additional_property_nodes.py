from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property_nodes_additional_property import (
        DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodesAdditionalProperty,
    )


T = TypeVar(
    "T", bound="DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodes"
)


@_attrs_define
class DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodes:
    """Keyed by node ID"""

    additional_properties: Dict[
        str,
        "DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodesAdditionalProperty",
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property_nodes_additional_property import (
            DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodesAdditionalProperty,
        )

        d = src_dict.copy()
        device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property_nodes = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodesAdditionalProperty.from_dict(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property_nodes.additional_properties = additional_properties
        return device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property_nodes

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> "DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodesAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: "DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodesAdditionalProperty",
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties