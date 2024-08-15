import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DRNotification")


@_attrs_define
class DRNotification:
    """Refer to the /schemas/dr-notification endpoint for the full JSON Schema definition

    Attributes:
        event (str):
        date (datetime.datetime):
        user (str):
        protocol (str):
        endpoint (str):
        targets (Union[Unset, List[str]]):
    """

    event: str
    date: datetime.datetime
    user: str
    protocol: str
    endpoint: str
    targets: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event = self.event

        date = self.date.isoformat()

        user = self.user

        protocol = self.protocol

        endpoint = self.endpoint

        targets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = self.targets

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "date": date,
                "user": user,
                "protocol": protocol,
                "endpoint": endpoint,
            }
        )
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event = d.pop("event")

        date = isoparse(d.pop("date"))

        user = d.pop("user")

        protocol = d.pop("protocol")

        endpoint = d.pop("endpoint")

        targets = cast(List[str], d.pop("targets", UNSET))

        dr_notification = cls(
            event=event,
            date=date,
            user=user,
            protocol=protocol,
            endpoint=endpoint,
            targets=targets,
        )

        dr_notification.additional_properties = d
        return dr_notification

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
