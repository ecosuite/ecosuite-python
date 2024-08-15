from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_predicted_generation_datums_sites_additional_property_systems_additional_property_aggregated_totals import (
        ProjectPredictedGenerationDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals,
    )


T = TypeVar("T", bound="ProjectPredictedGenerationDatumsSitesAdditionalPropertySystemsAdditionalProperty")


@_attrs_define
class ProjectPredictedGenerationDatumsSitesAdditionalPropertySystemsAdditionalProperty:
    """
    Attributes:
        predicted_generation (Union[Unset, float]):
        simple_forecast_generation (Union[Unset, float]):
        irradiance_forecast_generation (Union[Unset, float]):
        ac_energy_forecast_generation (Union[Unset, float]):
        aggregated_totals (Union[Unset,
            ProjectPredictedGenerationDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals]): Keyed by
            datum date
    """

    predicted_generation: Union[Unset, float] = UNSET
    simple_forecast_generation: Union[Unset, float] = UNSET
    irradiance_forecast_generation: Union[Unset, float] = UNSET
    ac_energy_forecast_generation: Union[Unset, float] = UNSET
    aggregated_totals: Union[
        Unset, "ProjectPredictedGenerationDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        predicted_generation = self.predicted_generation

        simple_forecast_generation = self.simple_forecast_generation

        irradiance_forecast_generation = self.irradiance_forecast_generation

        ac_energy_forecast_generation = self.ac_energy_forecast_generation

        aggregated_totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregated_totals, Unset):
            aggregated_totals = self.aggregated_totals.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if predicted_generation is not UNSET:
            field_dict["predictedGeneration"] = predicted_generation
        if simple_forecast_generation is not UNSET:
            field_dict["simpleForecastGeneration"] = simple_forecast_generation
        if irradiance_forecast_generation is not UNSET:
            field_dict["irradianceForecastGeneration"] = irradiance_forecast_generation
        if ac_energy_forecast_generation is not UNSET:
            field_dict["acEnergyForecastGeneration"] = ac_energy_forecast_generation
        if aggregated_totals is not UNSET:
            field_dict["aggregatedTotals"] = aggregated_totals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_predicted_generation_datums_sites_additional_property_systems_additional_property_aggregated_totals import (
            ProjectPredictedGenerationDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals,
        )

        d = src_dict.copy()
        predicted_generation = d.pop("predictedGeneration", UNSET)

        simple_forecast_generation = d.pop("simpleForecastGeneration", UNSET)

        irradiance_forecast_generation = d.pop("irradianceForecastGeneration", UNSET)

        ac_energy_forecast_generation = d.pop("acEnergyForecastGeneration", UNSET)

        _aggregated_totals = d.pop("aggregatedTotals", UNSET)
        aggregated_totals: Union[
            Unset, ProjectPredictedGenerationDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals
        ]
        if isinstance(_aggregated_totals, Unset):
            aggregated_totals = UNSET
        else:
            aggregated_totals = ProjectPredictedGenerationDatumsSitesAdditionalPropertySystemsAdditionalPropertyAggregatedTotals.from_dict(
                _aggregated_totals
            )

        project_predicted_generation_datums_sites_additional_property_systems_additional_property = cls(
            predicted_generation=predicted_generation,
            simple_forecast_generation=simple_forecast_generation,
            irradiance_forecast_generation=irradiance_forecast_generation,
            ac_energy_forecast_generation=ac_energy_forecast_generation,
            aggregated_totals=aggregated_totals,
        )

        project_predicted_generation_datums_sites_additional_property_systems_additional_property.additional_properties = d
        return project_predicted_generation_datums_sites_additional_property_systems_additional_property

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
