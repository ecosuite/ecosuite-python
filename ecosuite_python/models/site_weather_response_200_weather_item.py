import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_weather_response_200_weather_item_conditions import SiteWeatherResponse200WeatherItemConditions


T = TypeVar("T", bound="SiteWeatherResponse200WeatherItem")


@_attrs_define
class SiteWeatherResponse200WeatherItem:
    """
    Attributes:
        local_date (Union[Unset, datetime.datetime]):
        conditions (Union[Unset, SiteWeatherResponse200WeatherItemConditions]):
    """

    local_date: Union[Unset, datetime.datetime] = UNSET
    conditions: Union[Unset, "SiteWeatherResponse200WeatherItemConditions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        local_date: Union[Unset, str] = UNSET
        if not isinstance(self.local_date, Unset):
            local_date = self.local_date.isoformat()

        conditions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_date is not UNSET:
            field_dict["localDate"] = local_date
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.site_weather_response_200_weather_item_conditions import (
            SiteWeatherResponse200WeatherItemConditions,
        )

        d = src_dict.copy()
        _local_date = d.pop("localDate", UNSET)
        local_date: Union[Unset, datetime.datetime]
        if isinstance(_local_date, Unset):
            local_date = UNSET
        else:
            local_date = isoparse(_local_date)

        _conditions = d.pop("conditions", UNSET)
        conditions: Union[Unset, SiteWeatherResponse200WeatherItemConditions]
        if isinstance(_conditions, Unset):
            conditions = UNSET
        else:
            conditions = SiteWeatherResponse200WeatherItemConditions.from_dict(_conditions)

        site_weather_response_200_weather_item = cls(
            local_date=local_date,
            conditions=conditions,
        )

        site_weather_response_200_weather_item.additional_properties = d
        return site_weather_response_200_weather_item

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
