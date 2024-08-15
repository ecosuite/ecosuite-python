from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rfi_reply_stored import RFIReplyStored


T = TypeVar("T", bound="GetAllRFIReplyVersionsResponse200")


@_attrs_define
class GetAllRFIReplyVersionsResponse200:
    """
    Attributes:
        rfi_reply_versions (Union[Unset, List['RFIReplyStored']]):
    """

    rfi_reply_versions: Union[Unset, List["RFIReplyStored"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rfi_reply_versions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rfi_reply_versions, Unset):
            rfi_reply_versions = []
            for rfi_reply_versions_item_data in self.rfi_reply_versions:
                rfi_reply_versions_item = rfi_reply_versions_item_data.to_dict()
                rfi_reply_versions.append(rfi_reply_versions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rfi_reply_versions is not UNSET:
            field_dict["rfiReplyVersions"] = rfi_reply_versions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rfi_reply_stored import RFIReplyStored

        d = src_dict.copy()
        rfi_reply_versions = []
        _rfi_reply_versions = d.pop("rfiReplyVersions", UNSET)
        for rfi_reply_versions_item_data in _rfi_reply_versions or []:
            rfi_reply_versions_item = RFIReplyStored.from_dict(rfi_reply_versions_item_data)

            rfi_reply_versions.append(rfi_reply_versions_item)

        get_all_rfi_reply_versions_response_200 = cls(
            rfi_reply_versions=rfi_reply_versions,
        )

        get_all_rfi_reply_versions_response_200.additional_properties = d
        return get_all_rfi_reply_versions_response_200

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
