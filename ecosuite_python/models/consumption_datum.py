from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsumptionDatum")


@_attrs_define
class ConsumptionDatum:
    """
    Attributes:
        consumption (Union[Unset, float]):
        consumption_reading (Union[Unset, float]):
        consumption_max (Union[Unset, float]):
        consumption_min (Union[Unset, float]):
        power_factor (Union[Unset, float]):
        power_factor_max (Union[Unset, float]):
        power_factor_min (Union[Unset, float]):
    """

    consumption: Union[Unset, float] = UNSET
    consumption_reading: Union[Unset, float] = UNSET
    consumption_max: Union[Unset, float] = UNSET
    consumption_min: Union[Unset, float] = UNSET
    power_factor: Union[Unset, float] = UNSET
    power_factor_max: Union[Unset, float] = UNSET
    power_factor_min: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        consumption = self.consumption

        consumption_reading = self.consumption_reading

        consumption_max = self.consumption_max

        consumption_min = self.consumption_min

        power_factor = self.power_factor

        power_factor_max = self.power_factor_max

        power_factor_min = self.power_factor_min

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consumption is not UNSET:
            field_dict["consumption"] = consumption
        if consumption_reading is not UNSET:
            field_dict["consumptionReading"] = consumption_reading
        if consumption_max is not UNSET:
            field_dict["consumptionMax"] = consumption_max
        if consumption_min is not UNSET:
            field_dict["consumptionMin"] = consumption_min
        if power_factor is not UNSET:
            field_dict["powerFactor"] = power_factor
        if power_factor_max is not UNSET:
            field_dict["powerFactorMax"] = power_factor_max
        if power_factor_min is not UNSET:
            field_dict["powerFactorMin"] = power_factor_min

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        consumption = d.pop("consumption", UNSET)

        consumption_reading = d.pop("consumptionReading", UNSET)

        consumption_max = d.pop("consumptionMax", UNSET)

        consumption_min = d.pop("consumptionMin", UNSET)

        power_factor = d.pop("powerFactor", UNSET)

        power_factor_max = d.pop("powerFactorMax", UNSET)

        power_factor_min = d.pop("powerFactorMin", UNSET)

        consumption_datum = cls(
            consumption=consumption,
            consumption_reading=consumption_reading,
            consumption_max=consumption_max,
            consumption_min=consumption_min,
            power_factor=power_factor,
            power_factor_max=power_factor_max,
            power_factor_min=power_factor_min,
        )

        consumption_datum.additional_properties = d
        return consumption_datum

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
