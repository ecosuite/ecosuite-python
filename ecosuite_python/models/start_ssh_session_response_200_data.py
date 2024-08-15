from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartSshSessionResponse200Data")


@_attrs_define
class StartSshSessionResponse200Data:
    """
    Attributes:
        authorization (Union[Unset, str]):
        authorization_date (Union[Unset, float]):
        username (Union[Unset, str]):
        password (Union[Unset, str]):
    """

    authorization: Union[Unset, str] = UNSET
    authorization_date: Union[Unset, float] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorization = self.authorization

        authorization_date = self.authorization_date

        username = self.username

        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization is not UNSET:
            field_dict["authorization"] = authorization
        if authorization_date is not UNSET:
            field_dict["authorization-date"] = authorization_date
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authorization = d.pop("authorization", UNSET)

        authorization_date = d.pop("authorization-date", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        start_ssh_session_response_200_data = cls(
            authorization=authorization,
            authorization_date=authorization_date,
            username=username,
            password=password,
        )

        start_ssh_session_response_200_data.additional_properties = d
        return start_ssh_session_response_200_data

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
