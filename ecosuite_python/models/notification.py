from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_protocol import NotificationProtocol
from ..models.notification_type import NotificationType

T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """Refer to the /schemas/notification endpoint for the full JSON Schema definition

    Attributes:
        name (str):
        protocol (NotificationProtocol):
        endpoint (str): By entering a phone number, users opt in to receiving SMS notifications at this endpoint
        notification_type (NotificationType):  Default: NotificationType.ALERT.
    """

    name: str
    protocol: NotificationProtocol
    endpoint: str
    notification_type: NotificationType = NotificationType.ALERT
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        protocol = self.protocol.value

        endpoint = self.endpoint

        notification_type = self.notification_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "protocol": protocol,
                "endpoint": endpoint,
                "notificationType": notification_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        protocol = NotificationProtocol(d.pop("protocol"))

        endpoint = d.pop("endpoint")

        notification_type = NotificationType(d.pop("notificationType"))

        notification = cls(
            name=name,
            protocol=protocol,
            endpoint=endpoint,
            notification_type=notification_type,
        )

        notification.additional_properties = d
        return notification

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
