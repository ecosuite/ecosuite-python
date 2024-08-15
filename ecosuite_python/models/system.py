import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.system_product_type import SystemProductType
from ..models.system_system_status import SystemSystemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="System")


@_attrs_define
class System:
    """Refer to the /schemas/system endpoint for the full JSON Schema definition

    Attributes:
        code (str):
        status (SystemSystemStatus):  Default: SystemSystemStatus.NEW_SYSTEM.
        name (str):
        start_date (datetime.date):
        type (SystemProductType):
        meter_number (Union[Unset, str]):
        contracted_demand (Union[Unset, float]):
        verified (Union[Unset, bool]):  Default: False.
    """

    code: str
    name: str
    start_date: datetime.date
    type: SystemProductType
    status: SystemSystemStatus = SystemSystemStatus.NEW_SYSTEM
    meter_number: Union[Unset, str] = UNSET
    contracted_demand: Union[Unset, float] = UNSET
    verified: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        status = self.status.value

        name = self.name

        start_date = self.start_date.isoformat()

        type = self.type.value

        meter_number = self.meter_number

        contracted_demand = self.contracted_demand

        verified = self.verified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "status": status,
                "name": name,
                "startDate": start_date,
                "type": type,
            }
        )
        if meter_number is not UNSET:
            field_dict["meterNumber"] = meter_number
        if contracted_demand is not UNSET:
            field_dict["contractedDemand"] = contracted_demand
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        status = SystemSystemStatus(d.pop("status"))

        name = d.pop("name")

        start_date = isoparse(d.pop("startDate")).date()

        type = SystemProductType(d.pop("type"))

        meter_number = d.pop("meterNumber", UNSET)

        contracted_demand = d.pop("contractedDemand", UNSET)

        verified = d.pop("verified", UNSET)

        system = cls(
            code=code,
            status=status,
            name=name,
            start_date=start_date,
            type=type,
            meter_number=meter_number,
            contracted_demand=contracted_demand,
            verified=verified,
        )

        system.additional_properties = d
        return system

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
