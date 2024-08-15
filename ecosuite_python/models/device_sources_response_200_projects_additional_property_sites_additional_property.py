from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_sources_response_200_projects_additional_property_sites_additional_property_systems import (
        DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystems,
    )


T = TypeVar("T", bound="DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalProperty")


@_attrs_define
class DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalProperty:
    """
    Attributes:
        systems (Union[Unset, DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystems]): Keyed
            by system code
    """

    systems: Union[Unset, "DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystems"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        systems: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.systems, Unset):
            systems = self.systems.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if systems is not UNSET:
            field_dict["systems"] = systems

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_sources_response_200_projects_additional_property_sites_additional_property_systems import (
            DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystems,
        )

        d = src_dict.copy()
        _systems = d.pop("systems", UNSET)
        systems: Union[Unset, DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystems]
        if isinstance(_systems, Unset):
            systems = UNSET
        else:
            systems = DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystems.from_dict(
                _systems
            )

        device_sources_response_200_projects_additional_property_sites_additional_property = cls(
            systems=systems,
        )

        device_sources_response_200_projects_additional_property_sites_additional_property.additional_properties = d
        return device_sources_response_200_projects_additional_property_sites_additional_property

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
