from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.media_tag_response_s3_additional_property import MediaTagResponseS3AdditionalProperty


T = TypeVar("T", bound="MediaTagResponseS3")


@_attrs_define
class MediaTagResponseS3:
    """The S3 information that is stored."""

    additional_properties: Dict[str, "MediaTagResponseS3AdditionalProperty"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_tag_response_s3_additional_property import MediaTagResponseS3AdditionalProperty

        d = src_dict.copy()
        media_tag_response_s3 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = MediaTagResponseS3AdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        media_tag_response_s3.additional_properties = additional_properties
        return media_tag_response_s3

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "MediaTagResponseS3AdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "MediaTagResponseS3AdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
