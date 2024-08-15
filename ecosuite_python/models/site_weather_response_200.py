from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.site_weather_response_200_aggregation import SiteWeatherResponse200Aggregation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_ import Range
    from ..models.site_weather_response_200_weather_item import SiteWeatherResponse200WeatherItem


T = TypeVar("T", bound="SiteWeatherResponse200")


@_attrs_define
class SiteWeatherResponse200:
    """
    Attributes:
        weather (Union[Unset, List['SiteWeatherResponse200WeatherItem']]):
        range_ (Union[Unset, Range]):
        aggregation (Union[Unset, SiteWeatherResponse200Aggregation]):
    """

    weather: Union[Unset, List["SiteWeatherResponse200WeatherItem"]] = UNSET
    range_: Union[Unset, "Range"] = UNSET
    aggregation: Union[Unset, SiteWeatherResponse200Aggregation] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        weather: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.weather, Unset):
            weather = []
            for weather_item_data in self.weather:
                weather_item = weather_item_data.to_dict()
                weather.append(weather_item)

        range_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        aggregation: Union[Unset, str] = UNSET
        if not isinstance(self.aggregation, Unset):
            aggregation = self.aggregation.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weather is not UNSET:
            field_dict["weather"] = weather
        if range_ is not UNSET:
            field_dict["range"] = range_
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.range_ import Range
        from ..models.site_weather_response_200_weather_item import SiteWeatherResponse200WeatherItem

        d = src_dict.copy()
        weather = []
        _weather = d.pop("weather", UNSET)
        for weather_item_data in _weather or []:
            weather_item = SiteWeatherResponse200WeatherItem.from_dict(weather_item_data)

            weather.append(weather_item)

        _range_ = d.pop("range", UNSET)
        range_: Union[Unset, Range]
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)

        _aggregation = d.pop("aggregation", UNSET)
        aggregation: Union[Unset, SiteWeatherResponse200Aggregation]
        if isinstance(_aggregation, Unset):
            aggregation = UNSET
        else:
            aggregation = SiteWeatherResponse200Aggregation(_aggregation)

        site_weather_response_200 = cls(
            weather=weather,
            range_=range_,
            aggregation=aggregation,
        )

        site_weather_response_200.additional_properties = d
        return site_weather_response_200

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