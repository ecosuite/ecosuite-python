from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile import Profile


T = TypeVar("T", bound="GetProfileResponse200")


@_attrs_define
class GetProfileResponse200:
    """
    Attributes:
        profile (Union[Unset, Profile]): Refer to the /schemas/profile endpoint for the full JSON Schema definition
    """

    profile: Union[Unset, "Profile"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile is not UNSET:
            field_dict["profile"] = profile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.profile import Profile

        d = src_dict.copy()
        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, Profile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = Profile.from_dict(_profile)

        get_profile_response_200 = cls(
            profile=profile,
        )

        get_profile_response_200.additional_properties = d
        return get_profile_response_200

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
