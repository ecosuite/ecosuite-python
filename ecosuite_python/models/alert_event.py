import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertEvent")


@_attrs_define
class AlertEvent:
    """
    Attributes:
        user_notification_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        message (Union[Unset, str]):
        timestamp (Union[Unset, float]):
        local_timestamp (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
    """

    user_notification_id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    timestamp: Union[Unset, float] = UNSET
    local_timestamp: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_notification_id = self.user_notification_id

        user_id = self.user_id

        message = self.message

        timestamp = self.timestamp

        local_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.local_timestamp, Unset):
            local_timestamp = self.local_timestamp.isoformat()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_notification_id is not UNSET:
            field_dict["userNotificationId"] = user_notification_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if message is not UNSET:
            field_dict["message"] = message
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if local_timestamp is not UNSET:
            field_dict["localTimestamp"] = local_timestamp
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_notification_id = d.pop("userNotificationId", UNSET)

        user_id = d.pop("userId", UNSET)

        message = d.pop("message", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        _local_timestamp = d.pop("localTimestamp", UNSET)
        local_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_local_timestamp, Unset):
            local_timestamp = UNSET
        else:
            local_timestamp = isoparse(_local_timestamp)

        id = d.pop("id", UNSET)

        alert_event = cls(
            user_notification_id=user_notification_id,
            user_id=user_id,
            message=message,
            timestamp=timestamp,
            local_timestamp=local_timestamp,
            id=id,
        )

        alert_event.additional_properties = d
        return alert_event

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
