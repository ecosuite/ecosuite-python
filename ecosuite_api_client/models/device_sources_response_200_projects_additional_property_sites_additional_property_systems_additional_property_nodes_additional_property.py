from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodesAdditionalProperty",
)


@_attrs_define
class DeviceSourcesResponse200ProjectsAdditionalPropertySitesAdditionalPropertySystemsAdditionalPropertyNodesAdditionalProperty:
    """The device details

    Attributes:
        id (Union[Unset, str]):
        devices (Union[Unset, list[str]]):
    """

    id: Union[Unset, str] = UNSET
    devices: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        devices: Union[Unset, list[str]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        devices = cast(list[str], d.pop("devices", UNSET))

        device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property_nodes_additional_property = cls(
            id=id,
            devices=devices,
        )

        device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property_nodes_additional_property.additional_properties = d
        return device_sources_response_200_projects_additional_property_sites_additional_property_systems_additional_property_nodes_additional_property

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
