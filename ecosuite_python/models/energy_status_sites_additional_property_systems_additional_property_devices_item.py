from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertyDevicesItem")


@_attrs_define
class EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertyDevicesItem:
    """
    Attributes:
        source_id (Union[Unset, str]):
        dc_size (Union[Unset, int]):
        ac_size (Union[Unset, int]):
    """

    source_id: Union[Unset, str] = UNSET
    dc_size: Union[Unset, int] = UNSET
    ac_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_id = self.source_id

        dc_size = self.dc_size

        ac_size = self.ac_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if dc_size is not UNSET:
            field_dict["dcSize"] = dc_size
        if ac_size is not UNSET:
            field_dict["acSize"] = ac_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_id = d.pop("sourceId", UNSET)

        dc_size = d.pop("dcSize", UNSET)

        ac_size = d.pop("acSize", UNSET)

        energy_status_sites_additional_property_systems_additional_property_devices_item = cls(
            source_id=source_id,
            dc_size=dc_size,
            ac_size=ac_size,
        )

        energy_status_sites_additional_property_systems_additional_property_devices_item.additional_properties = d
        return energy_status_sites_additional_property_systems_additional_property_devices_item

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
