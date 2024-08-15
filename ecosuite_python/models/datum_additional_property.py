from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatumAdditionalProperty")


@_attrs_define
class DatumAdditionalProperty:
    """
    Attributes:
        generation (Union[Unset, float]):
        generation_reading (Union[Unset, float]):
        normalised_generation (Union[Unset, float]):
        consumption (Union[Unset, float]):
        consumption_reading (Union[Unset, float]):
        export (Union[Unset, float]):
        export_reading (Union[Unset, float]):
        storage (Union[Unset, float]):
        storage_reading (Union[Unset, float]):
        forecast_48_consumption (Union[Unset, float]):
        forecast_12_consumption (Union[Unset, float]):
        forecast_24_consumption (Union[Unset, float]):
        forecast_consumption (Union[Unset, float]):
    """

    generation: Union[Unset, float] = UNSET
    generation_reading: Union[Unset, float] = UNSET
    normalised_generation: Union[Unset, float] = UNSET
    consumption: Union[Unset, float] = UNSET
    consumption_reading: Union[Unset, float] = UNSET
    export: Union[Unset, float] = UNSET
    export_reading: Union[Unset, float] = UNSET
    storage: Union[Unset, float] = UNSET
    storage_reading: Union[Unset, float] = UNSET
    forecast_48_consumption: Union[Unset, float] = UNSET
    forecast_12_consumption: Union[Unset, float] = UNSET
    forecast_24_consumption: Union[Unset, float] = UNSET
    forecast_consumption: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        generation = self.generation

        generation_reading = self.generation_reading

        normalised_generation = self.normalised_generation

        consumption = self.consumption

        consumption_reading = self.consumption_reading

        export = self.export

        export_reading = self.export_reading

        storage = self.storage

        storage_reading = self.storage_reading

        forecast_48_consumption = self.forecast_48_consumption

        forecast_12_consumption = self.forecast_12_consumption

        forecast_24_consumption = self.forecast_24_consumption

        forecast_consumption = self.forecast_consumption

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if generation is not UNSET:
            field_dict["generation"] = generation
        if generation_reading is not UNSET:
            field_dict["generationReading"] = generation_reading
        if normalised_generation is not UNSET:
            field_dict["normalisedGeneration"] = normalised_generation
        if consumption is not UNSET:
            field_dict["consumption"] = consumption
        if consumption_reading is not UNSET:
            field_dict["consumptionReading"] = consumption_reading
        if export is not UNSET:
            field_dict["export"] = export
        if export_reading is not UNSET:
            field_dict["exportReading"] = export_reading
        if storage is not UNSET:
            field_dict["storage"] = storage
        if storage_reading is not UNSET:
            field_dict["storageReading"] = storage_reading
        if forecast_48_consumption is not UNSET:
            field_dict["forecast48Consumption"] = forecast_48_consumption
        if forecast_12_consumption is not UNSET:
            field_dict["forecast12Consumption"] = forecast_12_consumption
        if forecast_24_consumption is not UNSET:
            field_dict["forecast24Consumption"] = forecast_24_consumption
        if forecast_consumption is not UNSET:
            field_dict["forecastConsumption"] = forecast_consumption

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        generation = d.pop("generation", UNSET)

        generation_reading = d.pop("generationReading", UNSET)

        normalised_generation = d.pop("normalisedGeneration", UNSET)

        consumption = d.pop("consumption", UNSET)

        consumption_reading = d.pop("consumptionReading", UNSET)

        export = d.pop("export", UNSET)

        export_reading = d.pop("exportReading", UNSET)

        storage = d.pop("storage", UNSET)

        storage_reading = d.pop("storageReading", UNSET)

        forecast_48_consumption = d.pop("forecast48Consumption", UNSET)

        forecast_12_consumption = d.pop("forecast12Consumption", UNSET)

        forecast_24_consumption = d.pop("forecast24Consumption", UNSET)

        forecast_consumption = d.pop("forecastConsumption", UNSET)

        datum_additional_property = cls(
            generation=generation,
            generation_reading=generation_reading,
            normalised_generation=normalised_generation,
            consumption=consumption,
            consumption_reading=consumption_reading,
            export=export,
            export_reading=export_reading,
            storage=storage,
            storage_reading=storage_reading,
            forecast_48_consumption=forecast_48_consumption,
            forecast_12_consumption=forecast_12_consumption,
            forecast_24_consumption=forecast_24_consumption,
            forecast_consumption=forecast_consumption,
        )

        datum_additional_property.additional_properties = d
        return datum_additional_property

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
