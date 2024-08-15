import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordDocumentDocumentsItem")


@_attrs_define
class RecordDocumentDocumentsItem:
    """
    Attributes:
        file_key (Union[Unset, str]):
        file_name (Union[Unset, str]):
        size (Union[Unset, float]):
        updated (Union[Unset, datetime.datetime]):
        suffix (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    file_key: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    size: Union[Unset, float] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    suffix: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_key = self.file_key

        file_name = self.file_name

        size = self.size

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        suffix = self.suffix

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_key is not UNSET:
            field_dict["fileKey"] = file_key
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if size is not UNSET:
            field_dict["size"] = size
        if updated is not UNSET:
            field_dict["updated"] = updated
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_key = d.pop("fileKey", UNSET)

        file_name = d.pop("fileName", UNSET)

        size = d.pop("size", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        suffix = d.pop("suffix", UNSET)

        title = d.pop("title", UNSET)

        record_document_documents_item = cls(
            file_key=file_key,
            file_name=file_name,
            size=size,
            updated=updated,
            suffix=suffix,
            title=title,
        )

        record_document_documents_item.additional_properties = d
        return record_document_documents_item

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
