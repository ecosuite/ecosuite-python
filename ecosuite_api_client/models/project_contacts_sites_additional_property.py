from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_contact import ProjectContact
    from ..models.project_contacts_sites_additional_property_systems import (
        ProjectContactsSitesAdditionalPropertySystems,
    )
    from ..models.record_contact import RecordContact


T = TypeVar("T", bound="ProjectContactsSitesAdditionalProperty")


@_attrs_define
class ProjectContactsSitesAdditionalProperty:
    """
    Attributes:
        code (Union[Unset, str]):
        contacts (Union[Unset, list['ProjectContact']]):
        record_contacts (Union[Unset, list['RecordContact']]):
        systems (Union[Unset, ProjectContactsSitesAdditionalPropertySystems]): Contacts keyed by System ID
    """

    code: Union[Unset, str] = UNSET
    contacts: Union[Unset, list["ProjectContact"]] = UNSET
    record_contacts: Union[Unset, list["RecordContact"]] = UNSET
    systems: Union[Unset, "ProjectContactsSitesAdditionalPropertySystems"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        contacts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        record_contacts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.record_contacts, Unset):
            record_contacts = []
            for record_contacts_item_data in self.record_contacts:
                record_contacts_item = record_contacts_item_data.to_dict()
                record_contacts.append(record_contacts_item)

        systems: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.systems, Unset):
            systems = self.systems.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if record_contacts is not UNSET:
            field_dict["recordContacts"] = record_contacts
        if systems is not UNSET:
            field_dict["systems"] = systems

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_contact import ProjectContact
        from ..models.project_contacts_sites_additional_property_systems import (
            ProjectContactsSitesAdditionalPropertySystems,
        )
        from ..models.record_contact import RecordContact

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = ProjectContact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        record_contacts = []
        _record_contacts = d.pop("recordContacts", UNSET)
        for record_contacts_item_data in _record_contacts or []:
            record_contacts_item = RecordContact.from_dict(record_contacts_item_data)

            record_contacts.append(record_contacts_item)

        _systems = d.pop("systems", UNSET)
        systems: Union[Unset, ProjectContactsSitesAdditionalPropertySystems]
        if isinstance(_systems, Unset):
            systems = UNSET
        else:
            systems = ProjectContactsSitesAdditionalPropertySystems.from_dict(_systems)

        project_contacts_sites_additional_property = cls(
            code=code,
            contacts=contacts,
            record_contacts=record_contacts,
            systems=systems,
        )

        project_contacts_sites_additional_property.additional_properties = d
        return project_contacts_sites_additional_property

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
