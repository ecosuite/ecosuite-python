from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteContactsItem")


@_attrs_define
class SiteContactsItem:
    """
    Attributes:
        name (str):
        type (str):
        email (Union[Unset, str]):
        phone (Union[Unset, str]):
        voip (Union[Unset, str]):
        notes (Union[Unset, str]):
    """

    name: str
    type: str
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    voip: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type = self.type

        email = self.email

        phone = self.phone

        voip = self.voip

        notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if voip is not UNSET:
            field_dict["voip"] = voip
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = d.pop("type")

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        voip = d.pop("voip", UNSET)

        notes = d.pop("notes", UNSET)

        site_contacts_item = cls(
            name=name,
            type=type,
            email=email,
            phone=phone,
            voip=voip,
            notes=notes,
        )

        site_contacts_item.additional_properties = d
        return site_contacts_item

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
