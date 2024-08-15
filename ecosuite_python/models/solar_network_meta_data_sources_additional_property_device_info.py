from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SolarNetworkMetaDataSourcesAdditionalPropertyDeviceInfo")


@_attrs_define
class SolarNetworkMetaDataSourcesAdditionalPropertyDeviceInfo:
    """Keyed by metadata property, eg serialNumber"""

    additional_properties: Dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        solar_network_meta_data_sources_additional_property_device_info = cls()

        solar_network_meta_data_sources_additional_property_device_info.additional_properties = d
        return solar_network_meta_data_sources_additional_property_device_info

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
