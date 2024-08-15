from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RFIReplyTransitSchema")


@_attrs_define
class RFIReplyTransitSchema:
    """
    Attributes:
        rfi_id (str): The ID of the RFI this is in response to.
        content (str): The reply content.
        media (List[Any]): The linked media.
    """

    rfi_id: str
    content: str
    media: List[Any]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rfi_id = self.rfi_id

        content = self.content

        media = self.media

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rfi_id = d.pop("rfiID")

        content = d.pop("content")

        media = cast(List[Any], d.pop("media"))

        rfi_reply_transit_schema = cls(
            rfi_id=rfi_id,
            content=content,
            media=media,
        )

        rfi_reply_transit_schema.additional_properties = d
        return rfi_reply_transit_schema

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
