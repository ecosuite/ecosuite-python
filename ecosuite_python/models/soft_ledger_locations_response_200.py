from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.soft_ledger_locations_response_200_locations_item import SoftLedgerLocationsResponse200LocationsItem


T = TypeVar("T", bound="SoftLedgerLocationsResponse200")


@_attrs_define
class SoftLedgerLocationsResponse200:
    """
    Attributes:
        locations (Union[Unset, List['SoftLedgerLocationsResponse200LocationsItem']]):
    """

    locations: Union[Unset, List["SoftLedgerLocationsResponse200LocationsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.soft_ledger_locations_response_200_locations_item import (
            SoftLedgerLocationsResponse200LocationsItem,
        )

        d = src_dict.copy()
        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = SoftLedgerLocationsResponse200LocationsItem.from_dict(locations_item_data)

            locations.append(locations_item)

        soft_ledger_locations_response_200 = cls(
            locations=locations,
        )

        soft_ledger_locations_response_200.additional_properties = d
        return soft_ledger_locations_response_200

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
