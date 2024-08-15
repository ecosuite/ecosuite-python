import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.energy_node_status import EnergyNodeStatus
    from ..models.energy_status_sites_additional_property_systems_additional_property_devices_item import (
        EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertyDevicesItem,
    )
    from ..models.energy_status_sites_additional_property_systems_additional_property_sources_item import (
        EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertySourcesItem,
    )


T = TypeVar("T", bound="EnergyStatusSitesAdditionalPropertySystemsAdditionalProperty")


@_attrs_define
class EnergyStatusSitesAdditionalPropertySystemsAdditionalProperty:
    """
    Attributes:
        code (Union[Unset, str]):
        name (Union[Unset, str]):
        dc_size (Union[Unset, int]):
        ac_size (Union[Unset, int]):
        devices (Union[Unset, List['EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertyDevicesItem']]):
        sources (Union[Unset, List['EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertySourcesItem']]):
        nodes_status (Union[Unset, List['EnergyNodeStatus']]):
        status (Union[Unset, str]):
        watts (Union[Unset, float]):
        current (Union[Unset, float]):
        apparent_power (Union[Unset, float]):
        reactive_power (Union[Unset, float]):
        line_voltage (Union[Unset, float]):
        frequency (Union[Unset, float]):
        power_factor (Union[Unset, float]):
        latest_reading_date (Union[Unset, datetime.datetime]):
    """

    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    dc_size: Union[Unset, int] = UNSET
    ac_size: Union[Unset, int] = UNSET
    devices: Union[Unset, List["EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertyDevicesItem"]] = UNSET
    sources: Union[Unset, List["EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertySourcesItem"]] = UNSET
    nodes_status: Union[Unset, List["EnergyNodeStatus"]] = UNSET
    status: Union[Unset, str] = UNSET
    watts: Union[Unset, float] = UNSET
    current: Union[Unset, float] = UNSET
    apparent_power: Union[Unset, float] = UNSET
    reactive_power: Union[Unset, float] = UNSET
    line_voltage: Union[Unset, float] = UNSET
    frequency: Union[Unset, float] = UNSET
    power_factor: Union[Unset, float] = UNSET
    latest_reading_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        name = self.name

        dc_size = self.dc_size

        ac_size = self.ac_size

        devices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        sources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        nodes_status: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nodes_status, Unset):
            nodes_status = []
            for nodes_status_item_data in self.nodes_status:
                nodes_status_item = nodes_status_item_data.to_dict()
                nodes_status.append(nodes_status_item)

        status = self.status

        watts = self.watts

        current = self.current

        apparent_power = self.apparent_power

        reactive_power = self.reactive_power

        line_voltage = self.line_voltage

        frequency = self.frequency

        power_factor = self.power_factor

        latest_reading_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_reading_date, Unset):
            latest_reading_date = self.latest_reading_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if dc_size is not UNSET:
            field_dict["dcSize"] = dc_size
        if ac_size is not UNSET:
            field_dict["acSize"] = ac_size
        if devices is not UNSET:
            field_dict["devices"] = devices
        if sources is not UNSET:
            field_dict["sources"] = sources
        if nodes_status is not UNSET:
            field_dict["nodesStatus"] = nodes_status
        if status is not UNSET:
            field_dict["status"] = status
        if watts is not UNSET:
            field_dict["watts"] = watts
        if current is not UNSET:
            field_dict["current"] = current
        if apparent_power is not UNSET:
            field_dict["apparentPower"] = apparent_power
        if reactive_power is not UNSET:
            field_dict["reactivePower"] = reactive_power
        if line_voltage is not UNSET:
            field_dict["lineVoltage"] = line_voltage
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if power_factor is not UNSET:
            field_dict["powerFactor"] = power_factor
        if latest_reading_date is not UNSET:
            field_dict["latestReadingDate"] = latest_reading_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.energy_node_status import EnergyNodeStatus
        from ..models.energy_status_sites_additional_property_systems_additional_property_devices_item import (
            EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertyDevicesItem,
        )
        from ..models.energy_status_sites_additional_property_systems_additional_property_sources_item import (
            EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertySourcesItem,
        )

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        dc_size = d.pop("dcSize", UNSET)

        ac_size = d.pop("acSize", UNSET)

        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertyDevicesItem.from_dict(
                devices_item_data
            )

            devices.append(devices_item)

        sources = []
        _sources = d.pop("sources", UNSET)
        for sources_item_data in _sources or []:
            sources_item = EnergyStatusSitesAdditionalPropertySystemsAdditionalPropertySourcesItem.from_dict(
                sources_item_data
            )

            sources.append(sources_item)

        nodes_status = []
        _nodes_status = d.pop("nodesStatus", UNSET)
        for nodes_status_item_data in _nodes_status or []:
            nodes_status_item = EnergyNodeStatus.from_dict(nodes_status_item_data)

            nodes_status.append(nodes_status_item)

        status = d.pop("status", UNSET)

        watts = d.pop("watts", UNSET)

        current = d.pop("current", UNSET)

        apparent_power = d.pop("apparentPower", UNSET)

        reactive_power = d.pop("reactivePower", UNSET)

        line_voltage = d.pop("lineVoltage", UNSET)

        frequency = d.pop("frequency", UNSET)

        power_factor = d.pop("powerFactor", UNSET)

        _latest_reading_date = d.pop("latestReadingDate", UNSET)
        latest_reading_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_reading_date, Unset):
            latest_reading_date = UNSET
        else:
            latest_reading_date = isoparse(_latest_reading_date)

        energy_status_sites_additional_property_systems_additional_property = cls(
            code=code,
            name=name,
            dc_size=dc_size,
            ac_size=ac_size,
            devices=devices,
            sources=sources,
            nodes_status=nodes_status,
            status=status,
            watts=watts,
            current=current,
            apparent_power=apparent_power,
            reactive_power=reactive_power,
            line_voltage=line_voltage,
            frequency=frequency,
            power_factor=power_factor,
            latest_reading_date=latest_reading_date,
        )

        energy_status_sites_additional_property_systems_additional_property.additional_properties = d
        return energy_status_sites_additional_property_systems_additional_property

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
