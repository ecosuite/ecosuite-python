from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MediaTransitUpload")


@_attrs_define
class MediaTransitUpload:
    """The information that is provided to upload some media.

    Attributes:
        content_type (str):
        content_encoding (str):
        name (str):
        description (str):
        tags (List[str]):
    """

    content_type: str
    content_encoding: str
    name: str
    description: str
    tags: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_type = self.content_type

        content_encoding = self.content_encoding

        name = self.name

        description = self.description

        tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentType": content_type,
                "contentEncoding": content_encoding,
                "name": name,
                "description": description,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_type = d.pop("contentType")

        content_encoding = d.pop("contentEncoding")

        name = d.pop("name")

        description = d.pop("description")

        tags = cast(List[str], d.pop("tags"))

        media_transit_upload = cls(
            content_type=content_type,
            content_encoding=content_encoding,
            name=name,
            description=description,
            tags=tags,
        )

        media_transit_upload.additional_properties = d
        return media_transit_upload

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
