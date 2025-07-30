from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordContact")


@_attrs_define
class RecordContact:
    """
    Attributes:
        name (Union[Unset, str]):
        type_ (Union[Unset, str]):
        notes (Union[Unset, str]):
        record_id (Union[Unset, str]):
        record_name (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    record_id: Union[Unset, str] = UNSET
    record_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        notes = self.notes

        record_id = self.record_id

        record_name = self.record_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if notes is not UNSET:
            field_dict["notes"] = notes
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if record_name is not UNSET:
            field_dict["recordName"] = record_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        notes = d.pop("notes", UNSET)

        record_id = d.pop("recordId", UNSET)

        record_name = d.pop("recordName", UNSET)

        record_contact = cls(
            name=name,
            type_=type_,
            notes=notes,
            record_id=record_id,
            record_name=record_name,
        )

        record_contact.additional_properties = d
        return record_contact

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
