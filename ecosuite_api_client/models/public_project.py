import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_project_sites_item import PublicProjectSitesItem


T = TypeVar("T", bound="PublicProject")


@_attrs_define
class PublicProject:
    """
    Attributes:
        code (Union[Unset, str]):
        name (Union[Unset, str]):
        address (Union[Unset, str]):
        start_date (Union[Unset, datetime.date]):
        dc_size (Union[Unset, float]):
        sites (Union[Unset, list['PublicProjectSitesItem']]):
    """

    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    dc_size: Union[Unset, float] = UNSET
    sites: Union[Unset, list["PublicProjectSitesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        address = self.address

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        dc_size = self.dc_size

        sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if dc_size is not UNSET:
            field_dict["dcSize"] = dc_size
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_project_sites_item import PublicProjectSitesItem

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        dc_size = d.pop("dcSize", UNSET)

        sites = []
        _sites = d.pop("sites", UNSET)
        for sites_item_data in _sites or []:
            sites_item = PublicProjectSitesItem.from_dict(sites_item_data)

            sites.append(sites_item)

        public_project = cls(
            code=code,
            name=name,
            address=address,
            start_date=start_date,
            dc_size=dc_size,
            sites=sites,
        )

        public_project.additional_properties = d
        return public_project

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
