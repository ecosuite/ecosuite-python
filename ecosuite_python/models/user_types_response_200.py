from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_type import UserType


T = TypeVar("T", bound="UserTypesResponse200")


@_attrs_define
class UserTypesResponse200:
    """
    Attributes:
        user_types (Union[Unset, UserType]): Refer to the /schemas/user-type endpoint for the full JSON Schema
            definition
    """

    user_types: Union[Unset, "UserType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_types: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_types, Unset):
            user_types = self.user_types.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_types is not UNSET:
            field_dict["userTypes"] = user_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_type import UserType

        d = src_dict.copy()
        _user_types = d.pop("userTypes", UNSET)
        user_types: Union[Unset, UserType]
        if isinstance(_user_types, Unset):
            user_types = UNSET
        else:
            user_types = UserType.from_dict(_user_types)

        user_types_response_200 = cls(
            user_types=user_types,
        )

        user_types_response_200.additional_properties = d
        return user_types_response_200

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
