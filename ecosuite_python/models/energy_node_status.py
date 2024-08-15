import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnergyNodeStatus")


@_attrs_define
class EnergyNodeStatus:
    """
    Attributes:
        node_id (Union[Unset, int]):
        source_id (Union[Unset, str]):
        reading (Union[Unset, float]):
        latest_datum_date (Union[Unset, datetime.datetime]):
        watts (Union[Unset, float]):
        current (Union[Unset, float]):
        apparent_power (Union[Unset, float]):
        reactive_power (Union[Unset, float]):
        voltage (Union[Unset, float]):
        frequency (Union[Unset, float]):
        power_factor (Union[Unset, float]):
        status (Union[Unset, str]):
    """

    node_id: Union[Unset, int] = UNSET
    source_id: Union[Unset, str] = UNSET
    reading: Union[Unset, float] = UNSET
    latest_datum_date: Union[Unset, datetime.datetime] = UNSET
    watts: Union[Unset, float] = UNSET
    current: Union[Unset, float] = UNSET
    apparent_power: Union[Unset, float] = UNSET
    reactive_power: Union[Unset, float] = UNSET
    voltage: Union[Unset, float] = UNSET
    frequency: Union[Unset, float] = UNSET
    power_factor: Union[Unset, float] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id

        source_id = self.source_id

        reading = self.reading

        latest_datum_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_datum_date, Unset):
            latest_datum_date = self.latest_datum_date.isoformat()

        watts = self.watts

        current = self.current

        apparent_power = self.apparent_power

        reactive_power = self.reactive_power

        voltage = self.voltage

        frequency = self.frequency

        power_factor = self.power_factor

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if reading is not UNSET:
            field_dict["reading"] = reading
        if latest_datum_date is not UNSET:
            field_dict["latestDatumDate"] = latest_datum_date
        if watts is not UNSET:
            field_dict["watts"] = watts
        if current is not UNSET:
            field_dict["current"] = current
        if apparent_power is not UNSET:
            field_dict["apparentPower"] = apparent_power
        if reactive_power is not UNSET:
            field_dict["reactivePower"] = reactive_power
        if voltage is not UNSET:
            field_dict["voltage"] = voltage
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if power_factor is not UNSET:
            field_dict["powerFactor"] = power_factor
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_id = d.pop("nodeId", UNSET)

        source_id = d.pop("sourceId", UNSET)

        reading = d.pop("reading", UNSET)

        _latest_datum_date = d.pop("latestDatumDate", UNSET)
        latest_datum_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_datum_date, Unset):
            latest_datum_date = UNSET
        else:
            latest_datum_date = isoparse(_latest_datum_date)

        watts = d.pop("watts", UNSET)

        current = d.pop("current", UNSET)

        apparent_power = d.pop("apparentPower", UNSET)

        reactive_power = d.pop("reactivePower", UNSET)

        voltage = d.pop("voltage", UNSET)

        frequency = d.pop("frequency", UNSET)

        power_factor = d.pop("powerFactor", UNSET)

        status = d.pop("status", UNSET)

        energy_node_status = cls(
            node_id=node_id,
            source_id=source_id,
            reading=reading,
            latest_datum_date=latest_datum_date,
            watts=watts,
            current=current,
            apparent_power=apparent_power,
            reactive_power=reactive_power,
            voltage=voltage,
            frequency=frequency,
            power_factor=power_factor,
            status=status,
        )

        energy_node_status.additional_properties = d
        return energy_node_status

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
