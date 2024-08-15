from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lookup_address_business_details_body_indexes import LookupAddressBusinessDetailsBodyIndexes


T = TypeVar("T", bound="LookupAddressBusinessDetailsBody")


@_attrs_define
class LookupAddressBusinessDetailsBody:
    """
    Attributes:
        indexes (Union[Unset, LookupAddressBusinessDetailsBodyIndexes]):
        addresses (Union[Unset, List[List[str]]]):
    """

    indexes: Union[Unset, "LookupAddressBusinessDetailsBodyIndexes"] = UNSET
    addresses: Union[Unset, List[List[str]]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        indexes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.indexes, Unset):
            indexes = self.indexes.to_dict()

        addresses: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data

                addresses.append(addresses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if indexes is not UNSET:
            field_dict["indexes"] = indexes
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lookup_address_business_details_body_indexes import LookupAddressBusinessDetailsBodyIndexes

        d = src_dict.copy()
        _indexes = d.pop("indexes", UNSET)
        indexes: Union[Unset, LookupAddressBusinessDetailsBodyIndexes]
        if isinstance(_indexes, Unset):
            indexes = UNSET
        else:
            indexes = LookupAddressBusinessDetailsBodyIndexes.from_dict(_indexes)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = cast(List[str], addresses_item_data)

            addresses.append(addresses_item)

        lookup_address_business_details_body = cls(
            indexes=indexes,
            addresses=addresses,
        )

        lookup_address_business_details_body.additional_properties = d
        return lookup_address_business_details_body

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
