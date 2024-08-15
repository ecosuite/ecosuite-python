from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PredictedGenerationDatum")


@_attrs_define
class PredictedGenerationDatum:
    """
    Attributes:
        predicted_generation (Union[Unset, float]):
        simple_forecast_generation (Union[Unset, float]):
        irradiance_forecast_generation (Union[Unset, float]):
        ac_energy_forecast_generation (Union[Unset, float]):
    """

    predicted_generation: Union[Unset, float] = UNSET
    simple_forecast_generation: Union[Unset, float] = UNSET
    irradiance_forecast_generation: Union[Unset, float] = UNSET
    ac_energy_forecast_generation: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        predicted_generation = self.predicted_generation

        simple_forecast_generation = self.simple_forecast_generation

        irradiance_forecast_generation = self.irradiance_forecast_generation

        ac_energy_forecast_generation = self.ac_energy_forecast_generation

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        predicted_generation = d.pop("predictedGeneration", UNSET)

        simple_forecast_generation = d.pop("simpleForecastGeneration", UNSET)

        irradiance_forecast_generation = d.pop("irradianceForecastGeneration", UNSET)

        ac_energy_forecast_generation = d.pop("acEnergyForecastGeneration", UNSET)

        predicted_generation_datum = cls(
            predicted_generation=predicted_generation,
            simple_forecast_generation=simple_forecast_generation,
            irradiance_forecast_generation=irradiance_forecast_generation,
            ac_energy_forecast_generation=ac_energy_forecast_generation,
        )

        predicted_generation_datum.additional_properties = d
        return predicted_generation_datum

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
