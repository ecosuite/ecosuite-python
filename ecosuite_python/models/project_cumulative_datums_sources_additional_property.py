from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectCumulativeDatumsSourcesAdditionalProperty")


@_attrs_define
class ProjectCumulativeDatumsSourcesAdditionalProperty:
    """
    Attributes:
        day (Union[Unset, str]): The day that the datum is for when aggregating by day
        month (Union[Unset, str]): The month that the datum is for when aggregating by month
        watt_hours (Union[Unset, str]):
        cumulative_watt_hours (Union[Unset, str]):
    """

    day: Union[Unset, str] = UNSET
    month: Union[Unset, str] = UNSET
    watt_hours: Union[Unset, str] = UNSET
    cumulative_watt_hours: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        day = self.day

        month = self.month

        watt_hours = self.watt_hours

        cumulative_watt_hours = self.cumulative_watt_hours

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if month is not UNSET:
            field_dict["month"] = month
        if watt_hours is not UNSET:
            field_dict["wattHours"] = watt_hours
        if cumulative_watt_hours is not UNSET:
            field_dict["cumulativeWattHours"] = cumulative_watt_hours

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        day = d.pop("day", UNSET)

        month = d.pop("month", UNSET)

        watt_hours = d.pop("wattHours", UNSET)

        cumulative_watt_hours = d.pop("cumulativeWattHours", UNSET)

        project_cumulative_datums_sources_additional_property = cls(
            day=day,
            month=month,
            watt_hours=watt_hours,
            cumulative_watt_hours=cumulative_watt_hours,
        )

        project_cumulative_datums_sources_additional_property.additional_properties = d
        return project_cumulative_datums_sources_additional_property

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
