from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProFormaTaxes")


@_attrs_define
class ProFormaTaxes:
    """
    Attributes:
        property_tax (Union[Unset, float]):
        federal_tax (Union[Unset, float]):
        state_tax (Union[Unset, float]):
        local_tax (Union[Unset, float]):
        itc (Union[Unset, float]):
    """

    property_tax: Union[Unset, float] = UNSET
    federal_tax: Union[Unset, float] = UNSET
    state_tax: Union[Unset, float] = UNSET
    local_tax: Union[Unset, float] = UNSET
    itc: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_tax = self.property_tax

        federal_tax = self.federal_tax

        state_tax = self.state_tax

        local_tax = self.local_tax

        itc = self.itc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_tax is not UNSET:
            field_dict["propertyTax"] = property_tax
        if federal_tax is not UNSET:
            field_dict["federalTax"] = federal_tax
        if state_tax is not UNSET:
            field_dict["stateTax"] = state_tax
        if local_tax is not UNSET:
            field_dict["localTax"] = local_tax
        if itc is not UNSET:
            field_dict["itc"] = itc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        property_tax = d.pop("propertyTax", UNSET)

        federal_tax = d.pop("federalTax", UNSET)

        state_tax = d.pop("stateTax", UNSET)

        local_tax = d.pop("localTax", UNSET)

        itc = d.pop("itc", UNSET)

        pro_forma_taxes = cls(
            property_tax=property_tax,
            federal_tax=federal_tax,
            state_tax=state_tax,
            local_tax=local_tax,
            itc=itc,
        )

        pro_forma_taxes.additional_properties = d
        return pro_forma_taxes

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
