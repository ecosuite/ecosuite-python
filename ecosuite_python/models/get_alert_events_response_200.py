from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_event import AlertEvent
    from ..models.range_ import Range


T = TypeVar("T", bound="GetAlertEventsResponse200")


@_attrs_define
class GetAlertEventsResponse200:
    """
    Attributes:
        events (Union[Unset, AlertEvent]):
        range_ (Union[Unset, Range]):
    """

    events: Union[Unset, "AlertEvent"] = UNSET
    range_: Union[Unset, "Range"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        events: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        range_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_event import AlertEvent
        from ..models.range_ import Range

        d = src_dict.copy()
        _events = d.pop("events", UNSET)
        events: Union[Unset, AlertEvent]
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = AlertEvent.from_dict(_events)

        _range_ = d.pop("range", UNSET)
        range_: Union[Unset, Range]
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)

        get_alert_events_response_200 = cls(
            events=events,
            range_=range_,
        )

        get_alert_events_response_200.additional_properties = d
        return get_alert_events_response_200

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
