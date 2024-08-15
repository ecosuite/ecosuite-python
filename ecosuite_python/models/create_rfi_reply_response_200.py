from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rfi_reply_stored import RFIReplyStored


T = TypeVar("T", bound="CreateRFIReplyResponse200")


@_attrs_define
class CreateRFIReplyResponse200:
    """
    Attributes:
        rfi_reply (Union[Unset, RFIReplyStored]):
    """

    rfi_reply: Union[Unset, "RFIReplyStored"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rfi_reply: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rfi_reply, Unset):
            rfi_reply = self.rfi_reply.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rfi_reply is not UNSET:
            field_dict["rfiReply"] = rfi_reply

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rfi_reply_stored import RFIReplyStored

        d = src_dict.copy()
        _rfi_reply = d.pop("rfiReply", UNSET)
        rfi_reply: Union[Unset, RFIReplyStored]
        if isinstance(_rfi_reply, Unset):
            rfi_reply = UNSET
        else:
            rfi_reply = RFIReplyStored.from_dict(_rfi_reply)

        create_rfi_reply_response_200 = cls(
            rfi_reply=rfi_reply,
        )

        create_rfi_reply_response_200.additional_properties = d
        return create_rfi_reply_response_200

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
