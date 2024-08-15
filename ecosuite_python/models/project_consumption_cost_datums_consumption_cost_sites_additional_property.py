from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.consumption_cost_datum import ConsumptionCostDatum
    from ..models.project_consumption_cost_datums_consumption_cost_sites_additional_property_systems import (
        ProjectConsumptionCostDatumsConsumptionCostSitesAdditionalPropertySystems,
    )


T = TypeVar("T", bound="ProjectConsumptionCostDatumsConsumptionCostSitesAdditionalProperty")


@_attrs_define
class ProjectConsumptionCostDatumsConsumptionCostSitesAdditionalProperty:
    """
    Attributes:
        total_cost (Union[Unset, float]):
        total_metered_cost (Union[Unset, float]):
        total_demand_charge (Union[Unset, float]):
        total_fixed_cost (Union[Unset, float]):
        aggregated_totals (Union[Unset, List['ConsumptionCostDatum']]):
        systems (Union[Unset, ProjectConsumptionCostDatumsConsumptionCostSitesAdditionalPropertySystems]): Keyed by
            System ID
    """

    total_cost: Union[Unset, float] = UNSET
    total_metered_cost: Union[Unset, float] = UNSET
    total_demand_charge: Union[Unset, float] = UNSET
    total_fixed_cost: Union[Unset, float] = UNSET
    aggregated_totals: Union[Unset, List["ConsumptionCostDatum"]] = UNSET
    systems: Union[Unset, "ProjectConsumptionCostDatumsConsumptionCostSitesAdditionalPropertySystems"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_cost = self.total_cost

        total_metered_cost = self.total_metered_cost

        total_demand_charge = self.total_demand_charge

        total_fixed_cost = self.total_fixed_cost

        aggregated_totals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aggregated_totals, Unset):
            aggregated_totals = []
            for aggregated_totals_item_data in self.aggregated_totals:
                aggregated_totals_item = aggregated_totals_item_data.to_dict()
                aggregated_totals.append(aggregated_totals_item)

        systems: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.systems, Unset):
            systems = self.systems.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if total_metered_cost is not UNSET:
            field_dict["totalMeteredCost"] = total_metered_cost
        if total_demand_charge is not UNSET:
            field_dict["totalDemandCharge"] = total_demand_charge
        if total_fixed_cost is not UNSET:
            field_dict["totalFixedCost"] = total_fixed_cost
        if aggregated_totals is not UNSET:
            field_dict["aggregatedTotals"] = aggregated_totals
        if systems is not UNSET:
            field_dict["systems"] = systems

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.consumption_cost_datum import ConsumptionCostDatum
        from ..models.project_consumption_cost_datums_consumption_cost_sites_additional_property_systems import (
            ProjectConsumptionCostDatumsConsumptionCostSitesAdditionalPropertySystems,
        )

        d = src_dict.copy()
        total_cost = d.pop("totalCost", UNSET)

        total_metered_cost = d.pop("totalMeteredCost", UNSET)

        total_demand_charge = d.pop("totalDemandCharge", UNSET)

        total_fixed_cost = d.pop("totalFixedCost", UNSET)

        aggregated_totals = []
        _aggregated_totals = d.pop("aggregatedTotals", UNSET)
        for aggregated_totals_item_data in _aggregated_totals or []:
            aggregated_totals_item = ConsumptionCostDatum.from_dict(aggregated_totals_item_data)

            aggregated_totals.append(aggregated_totals_item)

        _systems = d.pop("systems", UNSET)
        systems: Union[Unset, ProjectConsumptionCostDatumsConsumptionCostSitesAdditionalPropertySystems]
        if isinstance(_systems, Unset):
            systems = UNSET
        else:
            systems = ProjectConsumptionCostDatumsConsumptionCostSitesAdditionalPropertySystems.from_dict(_systems)

        project_consumption_cost_datums_consumption_cost_sites_additional_property = cls(
            total_cost=total_cost,
            total_metered_cost=total_metered_cost,
            total_demand_charge=total_demand_charge,
            total_fixed_cost=total_fixed_cost,
            aggregated_totals=aggregated_totals,
            systems=systems,
        )

        project_consumption_cost_datums_consumption_cost_sites_additional_property.additional_properties = d
        return project_consumption_cost_datums_consumption_cost_sites_additional_property

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
