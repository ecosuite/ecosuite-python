from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property_nodes import (
        DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodes,
    )


T = TypeVar(
    "T", bound="DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalProperty"
)


@_attrs_define
class DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalProperty:
    """
    Attributes:
        nodes (Union[Unset,
            DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodes]): Keyed
            by node ID
    """

    nodes: Union[
        Unset, "DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodes"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nodes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = self.nodes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property_nodes import (
            DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodes,
        )

        d = src_dict.copy()
        _nodes = d.pop("nodes", UNSET)
        nodes: Union[
            Unset,
            DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodes,
        ]
        if isinstance(_nodes, Unset):
            nodes = UNSET
        else:
            nodes = DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodes.from_dict(
                _nodes
            )

        device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property = cls(
            nodes=nodes,
        )

        device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property.additional_properties = d
        return device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property

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
