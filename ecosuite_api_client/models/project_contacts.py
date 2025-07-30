from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_contacts_sites import ProjectContactsSites
    from ..models.record_contact import RecordContact


T = TypeVar("T", bound="ProjectContacts")


@_attrs_define
class ProjectContacts:
    """
    Attributes:
        code (Union[Unset, str]):
        record_contacts (Union[Unset, list['RecordContact']]):
        sites (Union[Unset, ProjectContactsSites]): Contacts keyed by Site ID
    """

    code: Union[Unset, str] = UNSET
    record_contacts: Union[Unset, list["RecordContact"]] = UNSET
    sites: Union[Unset, "ProjectContactsSites"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        record_contacts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.record_contacts, Unset):
            record_contacts = []
            for record_contacts_item_data in self.record_contacts:
                record_contacts_item = record_contacts_item_data.to_dict()
                record_contacts.append(record_contacts_item)

        sites: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if record_contacts is not UNSET:
            field_dict["recordContacts"] = record_contacts
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_contacts_sites import ProjectContactsSites
        from ..models.record_contact import RecordContact

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        record_contacts = []
        _record_contacts = d.pop("recordContacts", UNSET)
        for record_contacts_item_data in _record_contacts or []:
            record_contacts_item = RecordContact.from_dict(record_contacts_item_data)

            record_contacts.append(record_contacts_item)

        _sites = d.pop("sites", UNSET)
        sites: Union[Unset, ProjectContactsSites]
        if isinstance(_sites, Unset):
            sites = UNSET
        else:
            sites = ProjectContactsSites.from_dict(_sites)

        project_contacts = cls(
            code=code,
            record_contacts=record_contacts,
            sites=sites,
        )

        project_contacts.additional_properties = d
        return project_contacts

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
