from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_notification import UserNotification


T = TypeVar("T", bound="CreateUserNotificationResponse200")


@_attrs_define
class CreateUserNotificationResponse200:
    """
    Attributes:
        notification (Union[Unset, UserNotification]): Refer to the /schemas/notification endpoint for the JSON Schema
            definition
    """

    notification: Union[Unset, "UserNotification"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notification, Unset):
            notification = self.notification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notification is not UNSET:
            field_dict["notification"] = notification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_notification import UserNotification

        d = src_dict.copy()
        _notification = d.pop("notification", UNSET)
        notification: Union[Unset, UserNotification]
        if isinstance(_notification, Unset):
            notification = UNSET
        else:
            notification = UserNotification.from_dict(_notification)

        create_user_notification_response_200 = cls(
            notification=notification,
        )

        create_user_notification_response_200.additional_properties = d
        return create_user_notification_response_200

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
