from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertySourcesAdditionalProperty",
)


@_attrs_define
class ProjectPredictedConsumptionDatumsSitesAdditionalPropertySystemsAdditionalPropertySourcesAdditionalProperty:
    """
    Attributes:
        predicted_consumption (Union[Unset, float]):
        historic_consumption (Union[Unset, float]):
        target_consumption (Union[Unset, float]):
    """

    predicted_consumption: Union[Unset, float] = UNSET
    historic_consumption: Union[Unset, float] = UNSET
    target_consumption: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        predicted_consumption = self.predicted_consumption

        historic_consumption = self.historic_consumption

        target_consumption = self.target_consumption

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if predicted_consumption is not UNSET:
            field_dict["predictedConsumption"] = predicted_consumption
        if historic_consumption is not UNSET:
            field_dict["historicConsumption"] = historic_consumption
        if target_consumption is not UNSET:
            field_dict["targetConsumption"] = target_consumption

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        predicted_consumption = d.pop("predictedConsumption", UNSET)

        historic_consumption = d.pop("historicConsumption", UNSET)

        target_consumption = d.pop("targetConsumption", UNSET)

        project_predicted_consumption_datums_sites_additional_property_systems_additional_property_sources_additional_property = cls(
            predicted_consumption=predicted_consumption,
            historic_consumption=historic_consumption,
            target_consumption=target_consumption,
        )

        project_predicted_consumption_datums_sites_additional_property_systems_additional_property_sources_additional_property.additional_properties = d
        return project_predicted_consumption_datums_sites_additional_property_systems_additional_property_sources_additional_property

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
