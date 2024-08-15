from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_type_subtypes import DocumentTypeSubtypes


T = TypeVar("T", bound="DocumentType")


@_attrs_define
class DocumentType:
    """
    Attributes:
        name (Union[Unset, str]):
        subtypes (Union[Unset, DocumentTypeSubtypes]): Map of document sub types keyed by sub type ID
    """

    name: Union[Unset, str] = UNSET
    subtypes: Union[Unset, "DocumentTypeSubtypes"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        subtypes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subtypes, Unset):
            subtypes = self.subtypes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if subtypes is not UNSET:
            field_dict["subtypes"] = subtypes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_type_subtypes import DocumentTypeSubtypes

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _subtypes = d.pop("subtypes", UNSET)
        subtypes: Union[Unset, DocumentTypeSubtypes]
        if isinstance(_subtypes, Unset):
            subtypes = UNSET
        else:
            subtypes = DocumentTypeSubtypes.from_dict(_subtypes)

        document_type = cls(
            name=name,
            subtypes=subtypes,
        )

        document_type.additional_properties = d
        return document_type

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
