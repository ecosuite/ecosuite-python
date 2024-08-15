from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LookupAddressBusinessDetailsBodyIndexes")


@_attrs_define
class LookupAddressBusinessDetailsBodyIndexes:
    """
    Attributes:
        place (Union[Unset, int]):
        business (Union[Unset, int]):
        phone (Union[Unset, int]):
    """

    place: Union[Unset, int] = UNSET
    business: Union[Unset, int] = UNSET
    phone: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        place = self.place

        business = self.business

        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if place is not UNSET:
            field_dict["place"] = place
        if business is not UNSET:
            field_dict["business"] = business
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        place = d.pop("place", UNSET)

        business = d.pop("business", UNSET)

        phone = d.pop("phone", UNSET)

        lookup_address_business_details_body_indexes = cls(
            place=place,
            business=business,
            phone=phone,
        )

        lookup_address_business_details_body_indexes.additional_properties = d
        return lookup_address_business_details_body_indexes

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
