from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pro_forma_cash_flows_item_payments_item_payment_type import ProFormaCashFlowsItemPaymentsItemPaymentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProFormaCashFlowsItemPaymentsItem")


@_attrs_define
class ProFormaCashFlowsItemPaymentsItem:
    """
    Attributes:
        payment_type (ProFormaCashFlowsItemPaymentsItemPaymentType):
        sub_account (Union[Unset, str]):
    """

    payment_type: ProFormaCashFlowsItemPaymentsItemPaymentType
    sub_account: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_type = self.payment_type.value

        sub_account = self.sub_account

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paymentType": payment_type,
            }
        )
        if sub_account is not UNSET:
            field_dict["subAccount"] = sub_account

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        payment_type = ProFormaCashFlowsItemPaymentsItemPaymentType(d.pop("paymentType"))

        sub_account = d.pop("subAccount", UNSET)

        pro_forma_cash_flows_item_payments_item = cls(
            payment_type=payment_type,
            sub_account=sub_account,
        )

        pro_forma_cash_flows_item_payments_item.additional_properties = d
        return pro_forma_cash_flows_item_payments_item

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
