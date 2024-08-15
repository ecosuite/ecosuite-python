from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Participant")


@_attrs_define
class Participant:
    """Refer to the /schemas/participant endpoint for the full JSON Schema definition

    Attributes:
        code (str):
        contact_user (str):
        phone_contact (str):
    """

    code: str
    contact_user: str
    phone_contact: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        contact_user = self.contact_user

        phone_contact = self.phone_contact

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "contactUser": contact_user,
                "phoneContact": phone_contact,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        contact_user = d.pop("contactUser")

        phone_contact = d.pop("phoneContact")

        participant = cls(
            code=code,
            contact_user=contact_user,
            phone_contact=phone_contact,
        )

        participant.additional_properties = d
        return participant

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
