import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="File")


@_attrs_define
class File:
    """
    Attributes:
        key (Union[Unset, str]):
        type (Union[Unset, str]):
        subtype (Union[Unset, str]):
        path (Union[Unset, str]):
        project (Union[Unset, str]):
        site (Union[Unset, str]):
        system (Union[Unset, str]):
        name (Union[Unset, str]):
        title (Union[Unset, str]):
        suffix (Union[Unset, str]):
        size (Union[Unset, float]):
        updated (Union[Unset, datetime.datetime]):
    """

    key: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    subtype: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    site: Union[Unset, str] = UNSET
    system: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    suffix: Union[Unset, str] = UNSET
    size: Union[Unset, float] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        type = self.type

        subtype = self.subtype

        path = self.path

        project = self.project

        site = self.site

        system = self.system

        name = self.name

        title = self.title

        suffix = self.suffix

        size = self.size

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if type is not UNSET:
            field_dict["type"] = type
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if path is not UNSET:
            field_dict["path"] = path
        if project is not UNSET:
            field_dict["project"] = project
        if site is not UNSET:
            field_dict["site"] = site
        if system is not UNSET:
            field_dict["system"] = system
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if size is not UNSET:
            field_dict["size"] = size
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        type = d.pop("type", UNSET)

        subtype = d.pop("subtype", UNSET)

        path = d.pop("path", UNSET)

        project = d.pop("project", UNSET)

        site = d.pop("site", UNSET)

        system = d.pop("system", UNSET)

        name = d.pop("name", UNSET)

        title = d.pop("title", UNSET)

        suffix = d.pop("suffix", UNSET)

        size = d.pop("size", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        file = cls(
            key=key,
            type=type,
            subtype=subtype,
            path=path,
            project=project,
            site=site,
            system=system,
            name=name,
            title=title,
            suffix=suffix,
            size=size,
            updated=updated,
        )

        file.additional_properties = d
        return file

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
