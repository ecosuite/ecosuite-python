import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_project_sites_item_systems_item import PublicProjectSitesItemSystemsItem


T = TypeVar("T", bound="PublicProjectSitesItem")


@_attrs_define
class PublicProjectSitesItem:
    """
    Attributes:
        name (Union[Unset, str]):
        address (Union[Unset, str]):
        production_start_date (Union[Unset, datetime.date]):
        dc_size (Union[Unset, float]):
        systems (Union[Unset, List['PublicProjectSitesItemSystemsItem']]):
    """

    name: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    production_start_date: Union[Unset, datetime.date] = UNSET
    dc_size: Union[Unset, float] = UNSET
    systems: Union[Unset, List["PublicProjectSitesItemSystemsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        address = self.address

        production_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.production_start_date, Unset):
            production_start_date = self.production_start_date.isoformat()

        dc_size = self.dc_size

        systems: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.systems, Unset):
            systems = []
            for systems_item_data in self.systems:
                systems_item = systems_item_data.to_dict()
                systems.append(systems_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if production_start_date is not UNSET:
            field_dict["productionStartDate"] = production_start_date
        if dc_size is not UNSET:
            field_dict["dcSize"] = dc_size
        if systems is not UNSET:
            field_dict["systems"] = systems

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.public_project_sites_item_systems_item import PublicProjectSitesItemSystemsItem

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        _production_start_date = d.pop("productionStartDate", UNSET)
        production_start_date: Union[Unset, datetime.date]
        if isinstance(_production_start_date, Unset):
            production_start_date = UNSET
        else:
            production_start_date = isoparse(_production_start_date).date()

        dc_size = d.pop("dcSize", UNSET)

        systems = []
        _systems = d.pop("systems", UNSET)
        for systems_item_data in _systems or []:
            systems_item = PublicProjectSitesItemSystemsItem.from_dict(systems_item_data)

            systems.append(systems_item)

        public_project_sites_item = cls(
            name=name,
            address=address,
            production_start_date=production_start_date,
            dc_size=dc_size,
            systems=systems,
        )

        public_project_sites_item.additional_properties = d
        return public_project_sites_item

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
