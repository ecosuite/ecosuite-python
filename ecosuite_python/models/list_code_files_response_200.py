from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_response import MediaResponse


T = TypeVar("T", bound="ListCodeFilesResponse200")


@_attrs_define
class ListCodeFilesResponse200:
    """
    Attributes:
        media (Union[Unset, List['MediaResponse']]):
    """

    media: Union[Unset, List["MediaResponse"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        media: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

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
        media = []
        _media = d.pop("media", UNSET)
        for media_item_data in _media or []:
            media_item = MediaResponse.from_dict(media_item_data)

            media.append(media_item)

        list_code_files_response_200 = cls(
            media=media,
        )

        list_code_files_response_200.additional_properties = d
        return list_code_files_response_200

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
