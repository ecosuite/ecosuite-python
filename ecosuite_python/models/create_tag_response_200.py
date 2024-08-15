from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_tag_response import MediaTagResponse


T = TypeVar("T", bound="CreateTagResponse200")


@_attrs_define
class CreateTagResponse200:
    """
    Attributes:
        tag (Union[Unset, MediaTagResponse]): The media tag as it is stored in DynamoDB.
    """

    tag: Union[Unset, "MediaTagResponse"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_tag_response import MediaTagResponse

        d = src_dict.copy()
        _tag = d.pop("tag", UNSET)
        tag: Union[Unset, MediaTagResponse]
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = MediaTagResponse.from_dict(_tag)

        create_tag_response_200 = cls(
            tag=tag,
        )

        create_tag_response_200.additional_properties = d
        return create_tag_response_200

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
