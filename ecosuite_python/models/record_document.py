from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_document_documents_item import RecordDocumentDocumentsItem


T = TypeVar("T", bound="RecordDocument")


@_attrs_define
class RecordDocument:
    """
    Attributes:
        record_id (Union[Unset, str]):
        record_path (Union[Unset, str]):
        record_name (Union[Unset, str]):
        record_type (Union[Unset, str]):
        record_sub_type (Union[Unset, str]):
        documents (Union[Unset, List['RecordDocumentDocumentsItem']]):
    """

    record_id: Union[Unset, str] = UNSET
    record_path: Union[Unset, str] = UNSET
    record_name: Union[Unset, str] = UNSET
    record_type: Union[Unset, str] = UNSET
    record_sub_type: Union[Unset, str] = UNSET
    documents: Union[Unset, List["RecordDocumentDocumentsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        record_id = self.record_id

        record_path = self.record_path

        record_name = self.record_name

        record_type = self.record_type

        record_sub_type = self.record_sub_type

        documents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if record_path is not UNSET:
            field_dict["recordPath"] = record_path
        if record_name is not UNSET:
            field_dict["recordName"] = record_name
        if record_type is not UNSET:
            field_dict["recordType"] = record_type
        if record_sub_type is not UNSET:
            field_dict["recordSubType"] = record_sub_type
        if documents is not UNSET:
            field_dict["documents"] = documents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_document_documents_item import RecordDocumentDocumentsItem

        d = src_dict.copy()
        record_id = d.pop("recordId", UNSET)

        record_path = d.pop("recordPath", UNSET)

        record_name = d.pop("recordName", UNSET)

        record_type = d.pop("recordType", UNSET)

        record_sub_type = d.pop("recordSubType", UNSET)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = RecordDocumentDocumentsItem.from_dict(documents_item_data)

            documents.append(documents_item)

        record_document = cls(
            record_id=record_id,
            record_path=record_path,
            record_name=record_name,
            record_type=record_type,
            record_sub_type=record_sub_type,
            documents=documents,
        )

        record_document.additional_properties = d
        return record_document

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
