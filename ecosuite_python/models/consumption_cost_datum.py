from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsumptionCostDatum")


@_attrs_define
class ConsumptionCostDatum:
    """
    Attributes:
        metered_cost (Union[Unset, float]):
        demand_charge (Union[Unset, float]):
        fixed_cost (Union[Unset, float]):
    """

    metered_cost: Union[Unset, float] = UNSET
    demand_charge: Union[Unset, float] = UNSET
    fixed_cost: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metered_cost = self.metered_cost

        demand_charge = self.demand_charge

        fixed_cost = self.fixed_cost

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metered_cost is not UNSET:
            field_dict["meteredCost"] = metered_cost
        if demand_charge is not UNSET:
            field_dict["demandCharge"] = demand_charge
        if fixed_cost is not UNSET:
            field_dict["fixedCost"] = fixed_cost

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metered_cost = d.pop("meteredCost", UNSET)

        demand_charge = d.pop("demandCharge", UNSET)

        fixed_cost = d.pop("fixedCost", UNSET)

        consumption_cost_datum = cls(
            metered_cost=metered_cost,
            demand_charge=demand_charge,
            fixed_cost=fixed_cost,
        )

        consumption_cost_datum.additional_properties = d
        return consumption_cost_datum

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
