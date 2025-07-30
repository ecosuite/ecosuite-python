from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.record_is_contract import RecordIsContract
from ..models.record_type import RecordType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_contacts_item import RecordContactsItem
    from ..models.record_notes_item import RecordNotesItem


T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """Refer to the /schemas/record endpoint for the full JSON Schema definition

    Attributes:
        name (str):
        is_contract (RecordIsContract):
        record_type (RecordType):
        contacts (Union[Unset, list['RecordContactsItem']]):
        notes (Union[Unset, list['RecordNotesItem']]):
        verified (Union[Unset, bool]):  Default: False.
        hidden_fields (Union[Unset, list[str]]):
    """

    name: str
    is_contract: RecordIsContract
    record_type: RecordType
    contacts: Union[Unset, list["RecordContactsItem"]] = UNSET
    notes: Union[Unset, list["RecordNotesItem"]] = UNSET
    verified: Union[Unset, bool] = False
    hidden_fields: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        is_contract = self.is_contract.value

        record_type = self.record_type.value

        contacts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        notes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        verified = self.verified

        hidden_fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.hidden_fields, Unset):
            hidden_fields = self.hidden_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "isContract": is_contract,
                "recordType": record_type,
            }
        )
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if notes is not UNSET:
            field_dict["notes"] = notes
        if verified is not UNSET:
            field_dict["verified"] = verified
        if hidden_fields is not UNSET:
            field_dict["hiddenFields"] = hidden_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_contacts_item import RecordContactsItem
        from ..models.record_notes_item import RecordNotesItem

        d = dict(src_dict)
        name = d.pop("name")

        is_contract = RecordIsContract(d.pop("isContract"))

        record_type = RecordType(d.pop("recordType"))

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = RecordContactsItem.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = RecordNotesItem.from_dict(notes_item_data)

            notes.append(notes_item)

        verified = d.pop("verified", UNSET)

        hidden_fields = cast(list[str], d.pop("hiddenFields", UNSET))

        record = cls(
            name=name,
            is_contract=is_contract,
            record_type=record_type,
            contacts=contacts,
            notes=notes,
            verified=verified,
            hidden_fields=hidden_fields,
        )

        record.additional_properties = d
        return record

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
