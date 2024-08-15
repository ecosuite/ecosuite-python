import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SolarNetworkDatum")


@_attrs_define
class SolarNetworkDatum:
    """A SolarNetwork datum is keyed by date, node and source and contains additional reading data

    Attributes:
        created (Union[Unset, datetime.datetime]):
        node_id (Union[Unset, int]):
        source_id (Union[Unset, str]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    node_id: Union[Unset, int] = UNSET
    source_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, float] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        node_id = self.node_id

        source_id = self.source_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        node_id = d.pop("nodeId", UNSET)

        source_id = d.pop("sourceId", UNSET)

        solar_network_datum = cls(
            created=created,
            node_id=node_id,
            source_id=source_id,
        )

        solar_network_datum.additional_properties = d
        return solar_network_datum

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> float:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: float) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
