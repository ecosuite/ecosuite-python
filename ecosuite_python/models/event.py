import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.event_priority import EventPriority
from ..models.event_type import EventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_location import EventLocation
    from ..models.event_note import EventNote


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """Refer to the /schemas/event endpoint for the full JSON Schema definition

    Attributes:
        type (EventType):
        cause (str):
        start_date (datetime.datetime):
        description (str):
        priority (Union[Unset, EventPriority]):  Default: EventPriority.VALUE_1.
        due_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        location (Union[Unset, EventLocation]):
        notes (Union[Unset, List['EventNote']]):
    """

    type: EventType
    cause: str
    start_date: datetime.datetime
    description: str
    priority: Union[Unset, EventPriority] = EventPriority.VALUE_1
    due_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, "EventLocation"] = UNSET
    notes: Union[Unset, List["EventNote"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        cause = self.cause

        start_date = self.start_date.isoformat()

        description = self.description

        priority: Union[Unset, int] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        notes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "cause": cause,
                "startDate": start_date,
                "description": description,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if location is not UNSET:
            field_dict["location"] = location
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_location import EventLocation
        from ..models.event_note import EventNote

        d = src_dict.copy()
        type = EventType(d.pop("type"))

        cause = d.pop("cause")

        start_date = isoparse(d.pop("startDate"))

        description = d.pop("description")

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, EventPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = EventPriority(_priority)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _location = d.pop("location", UNSET)
        location: Union[Unset, EventLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = EventLocation.from_dict(_location)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = EventNote.from_dict(notes_item_data)

            notes.append(notes_item)

        event = cls(
            type=type,
            cause=cause,
            start_date=start_date,
            description=description,
            priority=priority,
            due_date=due_date,
            end_date=end_date,
            location=location,
            notes=notes,
        )

        event.additional_properties = d
        return event

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
