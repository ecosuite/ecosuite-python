from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SolarfluxCredentialsResponse200Environment")


@_attrs_define
class SolarfluxCredentialsResponse200Environment:
    """
    Attributes:
        protocol (Union[Unset, str]):
        host (Union[Unset, str]):
        mqtt_version (Union[Unset, int]):
    """

    protocol: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    mqtt_version: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protocol = self.protocol

        host = self.host

        mqtt_version = self.mqtt_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if host is not UNSET:
            field_dict["host"] = host
        if mqtt_version is not UNSET:
            field_dict["mqttVersion"] = mqtt_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        protocol = d.pop("protocol", UNSET)

        host = d.pop("host", UNSET)

        mqtt_version = d.pop("mqttVersion", UNSET)

        solarflux_credentials_response_200_environment = cls(
            protocol=protocol,
            host=host,
            mqtt_version=mqtt_version,
        )

        solarflux_credentials_response_200_environment.additional_properties = d
        return solarflux_credentials_response_200_environment

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
