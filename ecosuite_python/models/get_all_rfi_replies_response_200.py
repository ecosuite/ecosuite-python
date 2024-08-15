from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rfi_reply_stored import RFIReplyStored


T = TypeVar("T", bound="GetAllRFIRepliesResponse200")


@_attrs_define
class GetAllRFIRepliesResponse200:
    """
    Attributes:
        rfi_replies (Union[Unset, List['RFIReplyStored']]):
    """

    rfi_replies: Union[Unset, List["RFIReplyStored"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rfi_replies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rfi_replies, Unset):
            rfi_replies = []
            for rfi_replies_item_data in self.rfi_replies:
                rfi_replies_item = rfi_replies_item_data.to_dict()
                rfi_replies.append(rfi_replies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rfi_replies is not UNSET:
            field_dict["rfiReplies"] = rfi_replies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rfi_reply_stored import RFIReplyStored

        d = src_dict.copy()
        rfi_replies = []
        _rfi_replies = d.pop("rfiReplies", UNSET)
        for rfi_replies_item_data in _rfi_replies or []:
            rfi_replies_item = RFIReplyStored.from_dict(rfi_replies_item_data)

            rfi_replies.append(rfi_replies_item)

        get_all_rfi_replies_response_200 = cls(
            rfi_replies=rfi_replies,
        )

        get_all_rfi_replies_response_200.additional_properties = d
        return get_all_rfi_replies_response_200

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
