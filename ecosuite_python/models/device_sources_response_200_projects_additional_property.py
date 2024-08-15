from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_sources_response_200_projects_additional_property_sites import (
        DeviceSourcesResponse200ProjectsAdditionalPropertySites,
    )


T = TypeVar("T", bound="DeviceSourcesResponse200ProjectsAdditionalProperty")


@_attrs_define
class DeviceSourcesResponse200ProjectsAdditionalProperty:
    """
    Attributes:
        sites (Union[Unset, DeviceSourcesResponse200ProjectsAdditionalPropertySites]): Keyed by site code
    """

    sites: Union[Unset, "DeviceSourcesResponse200ProjectsAdditionalPropertySites"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sites: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_sources_response_200_projects_additional_property_sites import (
            DeviceSourcesResponse200ProjectsAdditionalPropertySites,
        )

        d = src_dict.copy()
        _sites = d.pop("sites", UNSET)
        sites: Union[Unset, DeviceSourcesResponse200ProjectsAdditionalPropertySites]
        if isinstance(_sites, Unset):
            sites = UNSET
        else:
            sites = DeviceSourcesResponse200ProjectsAdditionalPropertySites.from_dict(_sites)

        device_sources_response_200_projects_additional_property = cls(
            sites=sites,
        )

        device_sources_response_200_projects_additional_property.additional_properties = d
        return device_sources_response_200_projects_additional_property

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
