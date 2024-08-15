from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_response import MediaResponse


T = TypeVar("T", bound="GetFileResponse200")


@_attrs_define
class GetFileResponse200:
    """
    Attributes:
        media (Union[Unset, MediaResponse]): The media that is sent as a response.

            This contains a signed link under the `data` property that the user can then display.
    """

    media: Union[Unset, "MediaResponse"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        media: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if media is not UNSET:
            field_dict["media"] = media

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_response import MediaResponse

        d = src_dict.copy()
        _media = d.pop("media", UNSET)
        media: Union[Unset, MediaResponse]
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = MediaResponse.from_dict(_media)

        get_file_response_200 = cls(
            media=media,
        )

        get_file_response_200.additional_properties = d
        return get_file_response_200

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
