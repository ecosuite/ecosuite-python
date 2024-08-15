from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record_payment_details_cash_flows_item import RecordPaymentDetailsCashFlowsItem
    from ..models.record_payment_details_historic_performance import RecordPaymentDetailsHistoricPerformance


T = TypeVar("T", bound="RecordPaymentDetails")


@_attrs_define
class RecordPaymentDetails:
    """
    Attributes:
        cash_flows (Union[Unset, List['RecordPaymentDetailsCashFlowsItem']]):
        historic_performance (Union[Unset, RecordPaymentDetailsHistoricPerformance]):
    """

    cash_flows: Union[Unset, List["RecordPaymentDetailsCashFlowsItem"]] = UNSET
    historic_performance: Union[Unset, "RecordPaymentDetailsHistoricPerformance"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cash_flows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cash_flows, Unset):
            cash_flows = []
            for cash_flows_item_data in self.cash_flows:
                cash_flows_item = cash_flows_item_data.to_dict()
                cash_flows.append(cash_flows_item)

        historic_performance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.historic_performance, Unset):
            historic_performance = self.historic_performance.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cash_flows is not UNSET:
            field_dict["cashFlows"] = cash_flows
        if historic_performance is not UNSET:
            field_dict["historicPerformance"] = historic_performance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record_payment_details_cash_flows_item import RecordPaymentDetailsCashFlowsItem
        from ..models.record_payment_details_historic_performance import RecordPaymentDetailsHistoricPerformance

        d = src_dict.copy()
        cash_flows = []
        _cash_flows = d.pop("cashFlows", UNSET)
        for cash_flows_item_data in _cash_flows or []:
            cash_flows_item = RecordPaymentDetailsCashFlowsItem.from_dict(cash_flows_item_data)

            cash_flows.append(cash_flows_item)

        _historic_performance = d.pop("historicPerformance", UNSET)
        historic_performance: Union[Unset, RecordPaymentDetailsHistoricPerformance]
        if isinstance(_historic_performance, Unset):
            historic_performance = UNSET
        else:
            historic_performance = RecordPaymentDetailsHistoricPerformance.from_dict(_historic_performance)

        record_payment_details = cls(
            cash_flows=cash_flows,
            historic_performance=historic_performance,
        )

        record_payment_details.additional_properties = d
        return record_payment_details

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
