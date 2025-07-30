from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_access_controls import UserAccessControls


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """Refer to the /schemas/user endpoint for the full JSON Schema definition

    Attributes:
        email (str):
        first_name (str):
        last_name (str):
        timezone (Union[Unset, str]):
        user_type (Union[Unset, str]):
        access (Union[Unset, UserAccessControls]):
    """

    email: str
    first_name: str
    last_name: str
    timezone: Union[Unset, str] = UNSET
    user_type: Union[Unset, str] = UNSET
    access: Union[Unset, "UserAccessControls"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        timezone = self.timezone

        user_type = self.user_type

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
            }
        )
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if user_type is not UNSET:
            field_dict["userType"] = user_type
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_access_controls import UserAccessControls

        d = dict(src_dict)
        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        timezone = d.pop("timezone", UNSET)

        user_type = d.pop("userType", UNSET)

        _access = d.pop("access", UNSET)
        access: Union[Unset, UserAccessControls]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = UserAccessControls.from_dict(_access)

        user = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            timezone=timezone,
            user_type=user_type,
            access=access,
        )

        user.additional_properties = d
        return user

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
