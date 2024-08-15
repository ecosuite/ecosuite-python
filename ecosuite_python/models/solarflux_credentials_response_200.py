from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.solarflux_credentials_response_200_credentials import SolarfluxCredentialsResponse200Credentials
    from ..models.solarflux_credentials_response_200_environment import SolarfluxCredentialsResponse200Environment


T = TypeVar("T", bound="SolarfluxCredentialsResponse200")


@_attrs_define
class SolarfluxCredentialsResponse200:
    """
    Attributes:
        credentials (Union[Unset, SolarfluxCredentialsResponse200Credentials]):
        environment (Union[Unset, SolarfluxCredentialsResponse200Environment]):
    """

    credentials: Union[Unset, "SolarfluxCredentialsResponse200Credentials"] = UNSET
    environment: Union[Unset, "SolarfluxCredentialsResponse200Environment"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        environment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if environment is not UNSET:
            field_dict["environment"] = environment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.solarflux_credentials_response_200_credentials import SolarfluxCredentialsResponse200Credentials
        from ..models.solarflux_credentials_response_200_environment import SolarfluxCredentialsResponse200Environment

        d = src_dict.copy()
        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, SolarfluxCredentialsResponse200Credentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = SolarfluxCredentialsResponse200Credentials.from_dict(_credentials)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, SolarfluxCredentialsResponse200Environment]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = SolarfluxCredentialsResponse200Environment.from_dict(_environment)

        solarflux_credentials_response_200 = cls(
            credentials=credentials,
            environment=environment,
        )

        solarflux_credentials_response_200.additional_properties = d
        return solarflux_credentials_response_200

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
