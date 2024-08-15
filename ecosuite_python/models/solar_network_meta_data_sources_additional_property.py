from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.solar_network_meta_data_sources_additional_property_device_info import (
        SolarNetworkMetaDataSourcesAdditionalPropertyDeviceInfo,
    )


T = TypeVar("T", bound="SolarNetworkMetaDataSourcesAdditionalProperty")


@_attrs_define
class SolarNetworkMetaDataSourcesAdditionalProperty:
    """
    Attributes:
        node_id (Union[Unset, str]):
        device_info (Union[Unset, SolarNetworkMetaDataSourcesAdditionalPropertyDeviceInfo]): Keyed by metadata property,
            eg serialNumber
    """

    node_id: Union[Unset, str] = UNSET
    device_info: Union[Unset, "SolarNetworkMetaDataSourcesAdditionalPropertyDeviceInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id

        device_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.device_info, Unset):
            device_info = self.device_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if device_info is not UNSET:
            field_dict["deviceInfo"] = device_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.solar_network_meta_data_sources_additional_property_device_info import (
            SolarNetworkMetaDataSourcesAdditionalPropertyDeviceInfo,
        )

        d = src_dict.copy()
        node_id = d.pop("nodeId", UNSET)

        _device_info = d.pop("deviceInfo", UNSET)
        device_info: Union[Unset, SolarNetworkMetaDataSourcesAdditionalPropertyDeviceInfo]
        if isinstance(_device_info, Unset):
            device_info = UNSET
        else:
            device_info = SolarNetworkMetaDataSourcesAdditionalPropertyDeviceInfo.from_dict(_device_info)

        solar_network_meta_data_sources_additional_property = cls(
            node_id=node_id,
            device_info=device_info,
        )

        solar_network_meta_data_sources_additional_property.additional_properties = d
        return solar_network_meta_data_sources_additional_property

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
