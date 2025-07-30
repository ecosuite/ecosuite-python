from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LookupAddressBusinessDetailsResponse200")


@_attrs_define
class LookupAddressBusinessDetailsResponse200:
    """
    Attributes:
        places (Union[Unset, list[list[str]]]):
    """

    places: Union[Unset, list[list[str]]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        places: Union[Unset, list[list[str]]] = UNSET
        if not isinstance(self.places, Unset):
            places = []
            for places_item_data in self.places:
                places_item = places_item_data

                places.append(places_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if places is not UNSET:
            field_dict["places"] = places

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        places = []
        _places = d.pop("places", UNSET)
        for places_item_data in _places or []:
            places_item = cast(list[str], places_item_data)

            places.append(places_item)

        lookup_address_business_details_response_200 = cls(
            places=places,
        )

        lookup_address_business_details_response_200.additional_properties = d
        return lookup_address_business_details_response_200

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
