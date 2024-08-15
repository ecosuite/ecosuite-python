import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dr_event_priority import DREventPriority
from ..types import UNSET, Unset

T = TypeVar("T", bound="DREvent")


@_attrs_define
class DREvent:
    """Refer to the /schemas/dr-event endpoint for the full JSON Schema definition

    Attributes:
        priority (DREventPriority):
        name (str):
        start_date (datetime.datetime):
        notification_date (datetime.datetime):
        end_date (datetime.datetime):
        goal (str):
        participants (List[str]):
        notification_sent (Union[Unset, bool]):
    """

    priority: DREventPriority
    name: str
    start_date: datetime.datetime
    notification_date: datetime.datetime
    end_date: datetime.datetime
    goal: str
    participants: List[str]
    notification_sent: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        priority = self.priority.value

        name = self.name

        start_date = self.start_date.isoformat()

        notification_date = self.notification_date.isoformat()

        end_date = self.end_date.isoformat()

        goal = self.goal

        participants = self.participants

        notification_sent = self.notification_sent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "priority": priority,
                "name": name,
                "startDate": start_date,
                "notificationDate": notification_date,
                "endDate": end_date,
                "goal": goal,
                "participants": participants,
            }
        )
        if notification_sent is not UNSET:
            field_dict["notificationSent"] = notification_sent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        priority = DREventPriority(d.pop("priority"))

        name = d.pop("name")

        start_date = isoparse(d.pop("startDate"))

        notification_date = isoparse(d.pop("notificationDate"))

        end_date = isoparse(d.pop("endDate"))

        goal = d.pop("goal")

        participants = cast(List[str], d.pop("participants"))

        notification_sent = d.pop("notificationSent", UNSET)

        dr_event = cls(
            priority=priority,
            name=name,
            start_date=start_date,
            notification_date=notification_date,
            end_date=end_date,
            goal=goal,
            participants=participants,
            notification_sent=notification_sent,
        )

        dr_event.additional_properties = d
        return dr_event

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
