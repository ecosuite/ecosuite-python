from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationSolarNetworkCredentials")


@_attrs_define
class OrganizationSolarNetworkCredentials:
    """
    Attributes:
        host (Union[Unset, str]):
        ssh_host (Union[Unset, str]):
        wss_host (Union[Unset, str]):
        secret (Union[Unset, str]):
        token (Union[Unset, str]):
    """

    host: Union[Unset, str] = UNSET
    ssh_host: Union[Unset, str] = UNSET
    wss_host: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host

        ssh_host = self.ssh_host

        wss_host = self.wss_host

        secret = self.secret

        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if ssh_host is not UNSET:
            field_dict["sshHost"] = ssh_host
        if wss_host is not UNSET:
            field_dict["wssHost"] = wss_host
        if secret is not UNSET:
            field_dict["secret"] = secret
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host", UNSET)

        ssh_host = d.pop("sshHost", UNSET)

        wss_host = d.pop("wssHost", UNSET)

        secret = d.pop("secret", UNSET)

        token = d.pop("token", UNSET)

        organization_solar_network_credentials = cls(
            host=host,
            ssh_host=ssh_host,
            wss_host=wss_host,
            secret=secret,
            token=token,
        )

        organization_solar_network_credentials.additional_properties = d
        return organization_solar_network_credentials

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
