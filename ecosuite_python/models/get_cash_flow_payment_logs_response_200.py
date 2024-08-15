from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_cash_flow_payment_logs_response_200_cash_flow import GetCashFlowPaymentLogsResponse200CashFlow
    from ..models.payment_logs import PaymentLogs


T = TypeVar("T", bound="GetCashFlowPaymentLogsResponse200")


@_attrs_define
class GetCashFlowPaymentLogsResponse200:
    """
    Attributes:
        cash_flow (Union[Unset, GetCashFlowPaymentLogsResponse200CashFlow]):
        payment_logs (Union[Unset, PaymentLogs]):
    """

    cash_flow: Union[Unset, "GetCashFlowPaymentLogsResponse200CashFlow"] = UNSET
    payment_logs: Union[Unset, "PaymentLogs"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cash_flow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cash_flow, Unset):
            cash_flow = self.cash_flow.to_dict()

        payment_logs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment_logs, Unset):
            payment_logs = self.payment_logs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cash_flow is not UNSET:
            field_dict["cashFlow"] = cash_flow
        if payment_logs is not UNSET:
            field_dict["paymentLogs"] = payment_logs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_cash_flow_payment_logs_response_200_cash_flow import GetCashFlowPaymentLogsResponse200CashFlow
        from ..models.payment_logs import PaymentLogs

        d = src_dict.copy()
        _cash_flow = d.pop("cashFlow", UNSET)
        cash_flow: Union[Unset, GetCashFlowPaymentLogsResponse200CashFlow]
        if isinstance(_cash_flow, Unset):
            cash_flow = UNSET
        else:
            cash_flow = GetCashFlowPaymentLogsResponse200CashFlow.from_dict(_cash_flow)

        _payment_logs = d.pop("paymentLogs", UNSET)
        payment_logs: Union[Unset, PaymentLogs]
        if isinstance(_payment_logs, Unset):
            payment_logs = UNSET
        else:
            payment_logs = PaymentLogs.from_dict(_payment_logs)

        get_cash_flow_payment_logs_response_200 = cls(
            cash_flow=cash_flow,
            payment_logs=payment_logs,
        )

        get_cash_flow_payment_logs_response_200.additional_properties = d
        return get_cash_flow_payment_logs_response_200

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
