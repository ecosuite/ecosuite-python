from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_predicted_generation_datums_aggregated_totals import (
        ProjectPredictedGenerationDatumsAggregatedTotals,
    )
    from ..models.project_predicted_generation_datums_sites import ProjectPredictedGenerationDatumsSites


T = TypeVar("T", bound="ProjectPredictedGenerationDatums")


@_attrs_define
class ProjectPredictedGenerationDatums:
    """
    Attributes:
        predicted_generation (Union[Unset, float]):
        simple_forecast_generation (Union[Unset, float]):
        irradiance_forecast_generation (Union[Unset, float]):
        ac_energy_forecast_generation (Union[Unset, float]):
        aggregated_totals (Union[Unset, ProjectPredictedGenerationDatumsAggregatedTotals]): Keyed by datum date
        sites (Union[Unset, ProjectPredictedGenerationDatumsSites]): Keyed by Site ID
    """

    predicted_generation: Union[Unset, float] = UNSET
    simple_forecast_generation: Union[Unset, float] = UNSET
    irradiance_forecast_generation: Union[Unset, float] = UNSET
    ac_energy_forecast_generation: Union[Unset, float] = UNSET
    aggregated_totals: Union[Unset, "ProjectPredictedGenerationDatumsAggregatedTotals"] = UNSET
    sites: Union[Unset, "ProjectPredictedGenerationDatumsSites"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        predicted_generation = self.predicted_generation

        simple_forecast_generation = self.simple_forecast_generation

        irradiance_forecast_generation = self.irradiance_forecast_generation

        ac_energy_forecast_generation = self.ac_energy_forecast_generation

        aggregated_totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregated_totals, Unset):
            aggregated_totals = self.aggregated_totals.to_dict()

        sites: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites.to_dict()

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
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_predicted_generation_datums_aggregated_totals import (
            ProjectPredictedGenerationDatumsAggregatedTotals,
        )
        from ..models.project_predicted_generation_datums_sites import ProjectPredictedGenerationDatumsSites

        d = src_dict.copy()
        predicted_generation = d.pop("predictedGeneration", UNSET)

        simple_forecast_generation = d.pop("simpleForecastGeneration", UNSET)

        irradiance_forecast_generation = d.pop("irradianceForecastGeneration", UNSET)

        ac_energy_forecast_generation = d.pop("acEnergyForecastGeneration", UNSET)

        _aggregated_totals = d.pop("aggregatedTotals", UNSET)
        aggregated_totals: Union[Unset, ProjectPredictedGenerationDatumsAggregatedTotals]
        if isinstance(_aggregated_totals, Unset):
            aggregated_totals = UNSET
        else:
            aggregated_totals = ProjectPredictedGenerationDatumsAggregatedTotals.from_dict(_aggregated_totals)

        _sites = d.pop("sites", UNSET)
        sites: Union[Unset, ProjectPredictedGenerationDatumsSites]
        if isinstance(_sites, Unset):
            sites = UNSET
        else:
            sites = ProjectPredictedGenerationDatumsSites.from_dict(_sites)

        project_predicted_generation_datums = cls(
            predicted_generation=predicted_generation,
            simple_forecast_generation=simple_forecast_generation,
            irradiance_forecast_generation=irradiance_forecast_generation,
            ac_energy_forecast_generation=ac_energy_forecast_generation,
            aggregated_totals=aggregated_totals,
            sites=sites,
        )

        project_predicted_generation_datums.additional_properties = d
        return project_predicted_generation_datums

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
