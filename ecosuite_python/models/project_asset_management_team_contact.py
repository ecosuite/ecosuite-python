from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAssetManagementTeamContact")


@_attrs_define
class ProjectAssetManagementTeamContact:
    """
    Attributes:
        name (Union[Unset, str]):  Default: 'DevCo'.
        email (Union[Unset, str]):  Default: 'assetmanagement@ecogyenergy.com'.
        phone (Union[Unset, str]):  Default: '718-395-3620'.
    """

    name: Union[Unset, str] = "DevCo"
    email: Union[Unset, str] = "assetmanagement@ecogyenergy.com"
    phone: Union[Unset, str] = "718-395-3620"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        email = self.email

        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        project_asset_management_team_contact = cls(
            name=name,
            email=email,
            phone=phone,
        )

        project_asset_management_team_contact.additional_properties = d
        return project_asset_management_team_contact

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
