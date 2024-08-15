from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_predicted_consumption_datums_sites_additional_property_systems_additional_property_aggregated_totals import (
        ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals,
    )
    from ..models.project_predicted_consumption_datums_sites_additional_property_systems_additional_property_sources import (
        ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertySources,
    )


T = TypeVar("T", bound="ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalProperty")


@_attrs_define
class ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalProperty:
    """
    Attributes:
        predicted_consumption (Union[Unset, float]):
        historic_consumption (Union[Unset, float]):
        target_consumption (Union[Unset, float]):
        sources (Union[Unset,
            ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertySources]): Keyed by source ID
        aggregated_totals (Union[Unset,
            ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals]): Keyed by
            datum date
    """

    predicted_consumption: Union[Unset, float] = UNSET
    historic_consumption: Union[Unset, float] = UNSET
    target_consumption: Union[Unset, float] = UNSET
    sources: Union[
        Unset, "ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertySources"
    ] = UNSET
    aggregated_totals: Union[
        Unset, "ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        predicted_consumption = self.predicted_consumption

        historic_consumption = self.historic_consumption

        target_consumption = self.target_consumption

        sources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources.to_dict()

        aggregated_totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregated_totals, Unset):
            aggregated_totals = self.aggregated_totals.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if predicted_consumption is not UNSET:
            field_dict["predictedConsumption"] = predicted_consumption
        if historic_consumption is not UNSET:
            field_dict["historicConsumption"] = historic_consumption
        if target_consumption is not UNSET:
            field_dict["targetConsumption"] = target_consumption
        if sources is not UNSET:
            field_dict["sources"] = sources
        if aggregated_totals is not UNSET:
            field_dict["aggregatedTotals"] = aggregated_totals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_predicted_consumption_datums_sites_additional_property_systems_additional_property_aggregated_totals import (
            ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals,
        )
        from ..models.project_predicted_consumption_datums_sites_additional_property_systems_additional_property_sources import (
            ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertySources,
        )

        d = src_dict.copy()
        predicted_consumption = d.pop("predictedConsumption", UNSET)

        historic_consumption = d.pop("historicConsumption", UNSET)

        target_consumption = d.pop("targetConsumption", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: Union[Unset, ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertySources]
        if isinstance(_sources, Unset):
            sources = UNSET
        else:
            sources = (
                ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertySources.from_dict(
                    _sources
                )
            )

        _aggregated_totals = d.pop("aggregatedTotals", UNSET)
        aggregated_totals: Union[
            Unset, ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals
        ]
        if isinstance(_aggregated_totals, Unset):
            aggregated_totals = UNSET
        else:
            aggregated_totals = ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals.from_dict(
                _aggregated_totals
            )

        project_predicted_consumption_datums_sites_additional_property_systems_additional_property = cls(
            predicted_consumption=predicted_consumption,
            historic_consumption=historic_consumption,
            target_consumption=target_consumption,
            sources=sources,
            aggregated_totals=aggregated_totals,
        )

        project_predicted_consumption_datums_sites_additional_property_systems_additional_property.additional_properties = d
        return project_predicted_consumption_datums_sites_additional_property_systems_additional_property

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
