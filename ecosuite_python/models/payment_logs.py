from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_logs_payments import PaymentLogsPayments


T = TypeVar("T", bound="PaymentLogs")


@_attrs_define
class PaymentLogs:
    """
    Attributes:
        payments (Union[Unset, PaymentLogsPayments]):
    """

    payments: Union[Unset, "PaymentLogsPayments"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payments, Unset):
            payments = self.payments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payments is not UNSET:
            field_dict["payments"] = payments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payment_logs_payments import PaymentLogsPayments

        d = src_dict.copy()
        _payments = d.pop("payments", UNSET)
        payments: Union[Unset, PaymentLogsPayments]
        if isinstance(_payments, Unset):
            payments = UNSET
        else:
            payments = PaymentLogsPayments.from_dict(_payments)

        payment_logs = cls(
            payments=payments,
        )

        payment_logs.additional_properties = d
        return payment_logs

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
