from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_group import UserGroup


T = TypeVar("T", bound="GroupsResponse200")


@_attrs_define
class GroupsResponse200:
    """
    Attributes:
        groups (Union[Unset, UserGroup]):
    """

    groups: Union[Unset, "UserGroup"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        groups: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_group import UserGroup

        d = src_dict.copy()
        _groups = d.pop("groups", UNSET)
        groups: Union[Unset, UserGroup]
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = UserGroup.from_dict(_groups)

        groups_response_200 = cls(
            groups=groups,
        )

        groups_response_200.additional_properties = d
        return groups_response_200

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
