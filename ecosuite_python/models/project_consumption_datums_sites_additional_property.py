from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_consumption_datums_sites_additional_property_aggregated_totals import (
        ProjectConsumptionDatumsSitesAdditionalPropertyAggregatedTotals,
    )
    from ..models.project_consumption_datums_sites_additional_property_systems import (
        ProjectConsumptionDatumsSitesAdditionalPropertySystems,
    )


T = TypeVar("T", bound="ProjectConsumptionDatumsSitesAdditionalProperty")


@_attrs_define
class ProjectConsumptionDatumsSitesAdditionalProperty:
    """
    Attributes:
        aggregated_totals (Union[Unset, ProjectConsumptionDatumsSitesAdditionalPropertyAggregatedTotals]): Keyed by
            datum date
        systems (Union[Unset, ProjectConsumptionDatumsSitesAdditionalPropertySystems]): Keyed by System ID
    """

    aggregated_totals: Union[Unset, "ProjectConsumptionDatumsSitesAdditionalPropertyAggregatedTotals"] = UNSET
    systems: Union[Unset, "ProjectConsumptionDatumsSitesAdditionalPropertySystems"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aggregated_totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregated_totals, Unset):
            aggregated_totals = self.aggregated_totals.to_dict()

        systems: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.systems, Unset):
            systems = self.systems.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregated_totals is not UNSET:
            field_dict["aggregatedTotals"] = aggregated_totals
        if systems is not UNSET:
            field_dict["systems"] = systems

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_consumption_datums_sites_additional_property_aggregated_totals import (
            ProjectConsumptionDatumsSitesAdditionalPropertyAggregatedTotals,
        )
        from ..models.project_consumption_datums_sites_additional_property_systems import (
            ProjectConsumptionDatumsSitesAdditionalPropertySystems,
        )

        d = src_dict.copy()
        _aggregated_totals = d.pop("aggregatedTotals", UNSET)
        aggregated_totals: Union[Unset, ProjectConsumptionDatumsSitesAdditionalPropertyAggregatedTotals]
        if isinstance(_aggregated_totals, Unset):
            aggregated_totals = UNSET
        else:
            aggregated_totals = ProjectConsumptionDatumsSitesAdditionalPropertyAggregatedTotals.from_dict(
                _aggregated_totals
            )

        _systems = d.pop("systems", UNSET)
        systems: Union[Unset, ProjectConsumptionDatumsSitesAdditionalPropertySystems]
        if isinstance(_systems, Unset):
            systems = UNSET
        else:
            systems = ProjectConsumptionDatumsSitesAdditionalPropertySystems.from_dict(_systems)

        project_consumption_datums_sites_additional_property = cls(
            aggregated_totals=aggregated_totals,
            systems=systems,
        )

        project_consumption_datums_sites_additional_property.additional_properties = d
        return project_consumption_datums_sites_additional_property

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
