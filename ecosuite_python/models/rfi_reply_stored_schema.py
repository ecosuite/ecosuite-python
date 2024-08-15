import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="RFIReplyStoredSchema")


@_attrs_define
class RFIReplyStoredSchema:
    """
    Attributes:
        id (str): The RFI reply ID.
        author (str): Who authored the RFI reply.
        created_date_time (datetime.date): When the RFI reply was created.
        last_updated_date_time (datetime.date): When the RFI reply was last updated
        last_updated_by (str): Who authored the last update.
        version (str): The RFI reply version.
        rfi_id (str): The ID of the RFI this is in response to.
        content (str): The reply content.
        media (List[Any]): The linked media.
    """

    id: str
    author: str
    created_date_time: datetime.date
    last_updated_date_time: datetime.date
    last_updated_by: str
    version: str
    rfi_id: str
    content: str
    media: List[Any]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        author = self.author

        created_date_time = self.created_date_time.isoformat()

        last_updated_date_time = self.last_updated_date_time.isoformat()

        last_updated_by = self.last_updated_by

        version = self.version

        rfi_id = self.rfi_id

        content = self.content

        media = self.media

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "author": author,
                "createdDateTime": created_date_time,
                "lastUpdatedDateTime": last_updated_date_time,
                "lastUpdatedBy": last_updated_by,
                "version": version,
                "rfiID": rfi_id,
                "content": content,
                "media": media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        author = d.pop("author")

        created_date_time = isoparse(d.pop("createdDateTime")).date()

        last_updated_date_time = isoparse(d.pop("lastUpdatedDateTime")).date()

        last_updated_by = d.pop("lastUpdatedBy")

        version = d.pop("version")

        rfi_id = d.pop("rfiID")

        content = d.pop("content")

        media = cast(List[Any], d.pop("media"))

        rfi_reply_stored_schema = cls(
            id=id,
            author=author,
            created_date_time=created_date_time,
            last_updated_date_time=last_updated_date_time,
            last_updated_by=last_updated_by,
            version=version,
            rfi_id=rfi_id,
            content=content,
            media=media,
        )

        rfi_reply_stored_schema.additional_properties = d
        return rfi_reply_stored_schema

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
