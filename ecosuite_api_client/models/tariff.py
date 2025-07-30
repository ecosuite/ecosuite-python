import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tariff_fixed_charge_units import TariffFixedChargeUnits
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tariff_energy_week_day_schedule import TariffEnergyWeekDaySchedule
    from ..models.tariff_energy_week_end_schedule import TariffEnergyWeekEndSchedule
    from ..models.tariff_flat_demand_charge import TariffFlatDemandCharge
    from ..models.tariff_tier import TariffTier


T = TypeVar("T", bound="Tariff")


@_attrs_define
class Tariff:
    """
    Attributes:
        end (datetime.date):
        rates (list[list['TariffTier']]):
        start (datetime.date):
        energy_week_day_schedule (Union[Unset, TariffEnergyWeekDaySchedule]):
        energy_week_end_schedule (Union[Unset, TariffEnergyWeekEndSchedule]):
        fixed_charge_first_meter (Union[Unset, float]):
        fixed_charge_units (Union[Unset, TariffFixedChargeUnits]):
        flat_demand (Union[Unset, TariffFlatDemandCharge]):
    """

    end: datetime.date
    rates: list[list["TariffTier"]]
    start: datetime.date
    energy_week_day_schedule: Union[Unset, "TariffEnergyWeekDaySchedule"] = UNSET
    energy_week_end_schedule: Union[Unset, "TariffEnergyWeekEndSchedule"] = UNSET
    fixed_charge_first_meter: Union[Unset, float] = UNSET
    fixed_charge_units: Union[Unset, TariffFixedChargeUnits] = UNSET
    flat_demand: Union[Unset, "TariffFlatDemandCharge"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end.isoformat()

        rates = []
        for rates_item_data in self.rates:
            rates_item = []
            for rates_item_item_data in rates_item_data:
                rates_item_item = rates_item_item_data.to_dict()
                rates_item.append(rates_item_item)

            rates.append(rates_item)

        start = self.start.isoformat()

        energy_week_day_schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.energy_week_day_schedule, Unset):
            energy_week_day_schedule = self.energy_week_day_schedule.to_dict()

        energy_week_end_schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.energy_week_end_schedule, Unset):
            energy_week_end_schedule = self.energy_week_end_schedule.to_dict()

        fixed_charge_first_meter = self.fixed_charge_first_meter

        fixed_charge_units: Union[Unset, str] = UNSET
        if not isinstance(self.fixed_charge_units, Unset):
            fixed_charge_units = self.fixed_charge_units.value

        flat_demand: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.flat_demand, Unset):
            flat_demand = self.flat_demand.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end": end,
                "rates": rates,
                "start": start,
            }
        )
        if energy_week_day_schedule is not UNSET:
            field_dict["energyWeekDaySchedule"] = energy_week_day_schedule
        if energy_week_end_schedule is not UNSET:
            field_dict["energyWeekEndSchedule"] = energy_week_end_schedule
        if fixed_charge_first_meter is not UNSET:
            field_dict["fixedChargeFirstMeter"] = fixed_charge_first_meter
        if fixed_charge_units is not UNSET:
            field_dict["fixedChargeUnits"] = fixed_charge_units
        if flat_demand is not UNSET:
            field_dict["flatDemand"] = flat_demand

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tariff_energy_week_day_schedule import TariffEnergyWeekDaySchedule
        from ..models.tariff_energy_week_end_schedule import TariffEnergyWeekEndSchedule
        from ..models.tariff_flat_demand_charge import TariffFlatDemandCharge
        from ..models.tariff_tier import TariffTier

        d = dict(src_dict)
        end = isoparse(d.pop("end")).date()

        rates = []
        _rates = d.pop("rates")
        for rates_item_data in _rates:
            rates_item = []
            _rates_item = rates_item_data
            for rates_item_item_data in _rates_item:
                rates_item_item = TariffTier.from_dict(rates_item_item_data)

                rates_item.append(rates_item_item)

            rates.append(rates_item)

        start = isoparse(d.pop("start")).date()

        _energy_week_day_schedule = d.pop("energyWeekDaySchedule", UNSET)
        energy_week_day_schedule: Union[Unset, TariffEnergyWeekDaySchedule]
        if isinstance(_energy_week_day_schedule, Unset):
            energy_week_day_schedule = UNSET
        else:
            energy_week_day_schedule = TariffEnergyWeekDaySchedule.from_dict(_energy_week_day_schedule)

        _energy_week_end_schedule = d.pop("energyWeekEndSchedule", UNSET)
        energy_week_end_schedule: Union[Unset, TariffEnergyWeekEndSchedule]
        if isinstance(_energy_week_end_schedule, Unset):
            energy_week_end_schedule = UNSET
        else:
            energy_week_end_schedule = TariffEnergyWeekEndSchedule.from_dict(_energy_week_end_schedule)

        fixed_charge_first_meter = d.pop("fixedChargeFirstMeter", UNSET)

        _fixed_charge_units = d.pop("fixedChargeUnits", UNSET)
        fixed_charge_units: Union[Unset, TariffFixedChargeUnits]
        if isinstance(_fixed_charge_units, Unset):
            fixed_charge_units = UNSET
        else:
            fixed_charge_units = TariffFixedChargeUnits(_fixed_charge_units)

        _flat_demand = d.pop("flatDemand", UNSET)
        flat_demand: Union[Unset, TariffFlatDemandCharge]
        if isinstance(_flat_demand, Unset):
            flat_demand = UNSET
        else:
            flat_demand = TariffFlatDemandCharge.from_dict(_flat_demand)

        tariff = cls(
            end=end,
            rates=rates,
            start=start,
            energy_week_day_schedule=energy_week_day_schedule,
            energy_week_end_schedule=energy_week_end_schedule,
            fixed_charge_first_meter=fixed_charge_first_meter,
            fixed_charge_units=fixed_charge_units,
            flat_demand=flat_demand,
        )

        tariff.additional_properties = d
        return tariff

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
