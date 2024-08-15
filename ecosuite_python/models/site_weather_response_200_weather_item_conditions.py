from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteWeatherResponse200WeatherItemConditions")


@_attrs_define
class SiteWeatherResponse200WeatherItemConditions:
    """
    Attributes:
        sky (Union[Unset, str]):
        icon (Union[Unset, str]):
    """

    sky: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sky = self.sky

        icon = self.icon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sky is not UNSET:
            field_dict["sky"] = sky
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sky = d.pop("sky", UNSET)

        icon = d.pop("icon", UNSET)

        site_weather_response_200_weather_item_conditions = cls(
            sky=sky,
            icon=icon,
        )

        site_weather_response_200_weather_item_conditions.additional_properties = d
        return site_weather_response_200_weather_item_conditions

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
