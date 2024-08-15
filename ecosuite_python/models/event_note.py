import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventNote")


@_attrs_define
class EventNote:
    """
    Attributes:
        note (str):
        note_date (Union[Unset, datetime.datetime]):
    """

    note: str
    note_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        note = self.note

        note_date: Union[Unset, str] = UNSET
        if not isinstance(self.note_date, Unset):
            note_date = self.note_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "note": note,
            }
        )
        if note_date is not UNSET:
            field_dict["noteDate"] = note_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        note = d.pop("note")

        _note_date = d.pop("noteDate", UNSET)
        note_date: Union[Unset, datetime.datetime]
        if isinstance(_note_date, Unset):
            note_date = UNSET
        else:
            note_date = isoparse(_note_date)

        event_note = cls(
            note=note,
            note_date=note_date,
        )

        event_note.additional_properties = d
        return event_note

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
