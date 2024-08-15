from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_solar_network_credentials import OrganizationSolarNetworkCredentials


T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """Refer to the /schemas/organization endpoint for the full JSON Schema definition

    Attributes:
        name (str):
        id (Union[Unset, str]):
        solar_network_credentials (Union[Unset, OrganizationSolarNetworkCredentials]):
    """

    name: str
    id: Union[Unset, str] = UNSET
    solar_network_credentials: Union[Unset, "OrganizationSolarNetworkCredentials"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        id = self.id

        solar_network_credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.solar_network_credentials, Unset):
            solar_network_credentials = self.solar_network_credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if solar_network_credentials is not UNSET:
            field_dict["solarNetworkCredentials"] = solar_network_credentials

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_solar_network_credentials import OrganizationSolarNetworkCredentials

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        _solar_network_credentials = d.pop("solarNetworkCredentials", UNSET)
        solar_network_credentials: Union[Unset, OrganizationSolarNetworkCredentials]
        if isinstance(_solar_network_credentials, Unset):
            solar_network_credentials = UNSET
        else:
            solar_network_credentials = OrganizationSolarNetworkCredentials.from_dict(_solar_network_credentials)

        organization = cls(
            name=name,
            id=id,
            solar_network_credentials=solar_network_credentials,
        )

        organization.additional_properties = d
        return organization

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
