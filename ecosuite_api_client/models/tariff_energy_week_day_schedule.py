from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffEnergyWeekDaySchedule")


@_attrs_define
class TariffEnergyWeekDaySchedule:
    """
    Attributes:
        april (Union[Unset, Any]):
        august (Union[Unset, Any]):
        december (Union[Unset, Any]):
        february (Union[Unset, Any]):
        january (Union[Unset, Any]):
        july (Union[Unset, Any]):
        june (Union[Unset, Any]):
        march (Union[Unset, Any]):
        may (Union[Unset, Any]):
        november (Union[Unset, Any]):
        october (Union[Unset, Any]):
        september (Union[Unset, Any]):
    """

    april: Union[Unset, Any] = UNSET
    august: Union[Unset, Any] = UNSET
    december: Union[Unset, Any] = UNSET
    february: Union[Unset, Any] = UNSET
    january: Union[Unset, Any] = UNSET
    july: Union[Unset, Any] = UNSET
    june: Union[Unset, Any] = UNSET
    march: Union[Unset, Any] = UNSET
    may: Union[Unset, Any] = UNSET
    november: Union[Unset, Any] = UNSET
    october: Union[Unset, Any] = UNSET
    september: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        april = self.april

        august = self.august

        december = self.december

        february = self.february

        january = self.january

        july = self.july

        june = self.june

        march = self.march

        may = self.may

        november = self.november

        october = self.october

        september = self.september

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if april is not UNSET:
            field_dict["april"] = april
        if august is not UNSET:
            field_dict["august"] = august
        if december is not UNSET:
            field_dict["december"] = december
        if february is not UNSET:
            field_dict["february"] = february
        if january is not UNSET:
            field_dict["january"] = january
        if july is not UNSET:
            field_dict["july"] = july
        if june is not UNSET:
            field_dict["june"] = june
        if march is not UNSET:
            field_dict["march"] = march
        if may is not UNSET:
            field_dict["may"] = may
        if november is not UNSET:
            field_dict["november"] = november
        if october is not UNSET:
            field_dict["october"] = october
        if september is not UNSET:
            field_dict["september"] = september

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        april = d.pop("april", UNSET)

        august = d.pop("august", UNSET)

        december = d.pop("december", UNSET)

        february = d.pop("february", UNSET)

        january = d.pop("january", UNSET)

        july = d.pop("july", UNSET)

        june = d.pop("june", UNSET)

        march = d.pop("march", UNSET)

        may = d.pop("may", UNSET)

        november = d.pop("november", UNSET)

        october = d.pop("october", UNSET)

        september = d.pop("september", UNSET)

        tariff_energy_week_day_schedule = cls(
            april=april,
            august=august,
            december=december,
            february=february,
            january=january,
            july=july,
            june=june,
            march=march,
            may=may,
            november=november,
            october=october,
            september=september,
        )

        tariff_energy_week_day_schedule.additional_properties = d
        return tariff_energy_week_day_schedule

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
