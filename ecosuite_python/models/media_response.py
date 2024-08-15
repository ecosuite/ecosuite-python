from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MediaResponse")


@_attrs_define
class MediaResponse:
    """The media that is sent as a response.

    This contains a signed link under the `data` property that the user can then display.

        Attributes:
            created_date_time (str):
            last_updated_date_time (str):
            last_update_author (str):
            tags (List[str]):
            content_type (str):
            content_encoding (str):
            data (str):
            content_length (float):
            tag_i_ds (List[str]):
            code (str):
            name (str):
            description (str):
            id (str):
            key (str):
            author (str):
    """

    created_date_time: str
    last_updated_date_time: str
    last_update_author: str
    tags: List[str]
    content_type: str
    content_encoding: str
    data: str
    content_length: float
    tag_i_ds: List[str]
    code: str
    name: str
    description: str
    id: str
    key: str
    author: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_date_time = self.created_date_time

        last_updated_date_time = self.last_updated_date_time

        last_update_author = self.last_update_author

        tags = self.tags

        content_type = self.content_type

        content_encoding = self.content_encoding

        data = self.data

        content_length = self.content_length

        tag_i_ds = self.tag_i_ds

        code = self.code

        name = self.name

        description = self.description

        id = self.id

        key = self.key

        author = self.author

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdDateTime": created_date_time,
                "lastUpdatedDateTime": last_updated_date_time,
                "lastUpdateAuthor": last_update_author,
                "tags": tags,
                "contentType": content_type,
                "contentEncoding": content_encoding,
                "data": data,
                "contentLength": content_length,
                "tagIDs": tag_i_ds,
                "code": code,
                "name": name,
                "description": description,
                "id": id,
                "key": key,
                "author": author,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_date_time = d.pop("createdDateTime")

        last_updated_date_time = d.pop("lastUpdatedDateTime")

        last_update_author = d.pop("lastUpdateAuthor")

        tags = cast(List[str], d.pop("tags"))

        content_type = d.pop("contentType")

        content_encoding = d.pop("contentEncoding")

        data = d.pop("data")

        content_length = d.pop("contentLength")

        tag_i_ds = cast(List[str], d.pop("tagIDs"))

        code = d.pop("code")

        name = d.pop("name")

        description = d.pop("description")

        id = d.pop("id")

        key = d.pop("key")

        author = d.pop("author")

        media_response = cls(
            created_date_time=created_date_time,
            last_updated_date_time=last_updated_date_time,
            last_update_author=last_update_author,
            tags=tags,
            content_type=content_type,
            content_encoding=content_encoding,
            data=data,
            content_length=content_length,
            tag_i_ds=tag_i_ds,
            code=code,
            name=name,
            description=description,
            id=id,
            key=key,
            author=author,
        )

        media_response.additional_properties = d
        return media_response

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
