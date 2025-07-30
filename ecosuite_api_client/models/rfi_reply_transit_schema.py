from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RFIReplyTransitSchema")


@_attrs_define
class RFIReplyTransitSchema:
    """
    Attributes:
        rfi_id (str): The ID of the RFI this is in response to.
        content (str): The reply content.
        media (list[Any]): The linked media.
    """

    rfi_id: str
    content: str
    media: list[Any]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rfi_id = self.rfi_id

        content = self.content

        media = self.media

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rfiID": rfi_id,
                "content": content,
                "media": media,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rfi_id = d.pop("rfiID")

        content = d.pop("content")

        media = cast(list[Any], d.pop("media"))

        rfi_reply_transit_schema = cls(
            rfi_id=rfi_id,
            content=content,
            media=media,
        )

        rfi_reply_transit_schema.additional_properties = d
        return rfi_reply_transit_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
