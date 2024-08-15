from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSolarNodeLoginUrlResponse200")


@_attrs_define
class GetSolarNodeLoginUrlResponse200:
    """
    Attributes:
        solar_node_login_url (Union[Unset, str]):
    """

    solar_node_login_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        solar_node_login_url = self.solar_node_login_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if solar_node_login_url is not UNSET:
            field_dict["solarNodeLoginUrl"] = solar_node_login_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        solar_node_login_url = d.pop("solarNodeLoginUrl", UNSET)

        get_solar_node_login_url_response_200 = cls(
            solar_node_login_url=solar_node_login_url,
        )

        get_solar_node_login_url_response_200.additional_properties = d
        return get_solar_node_login_url_response_200

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
