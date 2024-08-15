from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_document import RecordDocument


T = TypeVar("T", bound="RecordDocumentsResponse200")


@_attrs_define
class RecordDocumentsResponse200:
    """
    Attributes:
        data (Union[Unset, RecordDocument]):
    """

    data: Union[Unset, "RecordDocument"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_document import RecordDocument

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, RecordDocument]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RecordDocument.from_dict(_data)

        record_documents_response_200 = cls(
            data=data,
        )

        record_documents_response_200.additional_properties = d
        return record_documents_response_200

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