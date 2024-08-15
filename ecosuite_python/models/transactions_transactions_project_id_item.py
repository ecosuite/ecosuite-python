from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionsTransactionsProjectIdItem")


@_attrs_define
class TransactionsTransactionsProjectIdItem:
    """
    Attributes:
        account_type (Union[Unset, str]):
        account_name (Union[Unset, str]):
        debit (Union[Unset, float]):
        credit (Union[Unset, float]):
        transaction_date (Union[Unset, str]):
    """

    account_type: Union[Unset, str] = UNSET
    account_name: Union[Unset, str] = UNSET
    debit: Union[Unset, float] = UNSET
    credit: Union[Unset, float] = UNSET
    transaction_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_type = self.account_type

        account_name = self.account_name

        debit = self.debit

        credit = self.credit

        transaction_date = self.transaction_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if debit is not UNSET:
            field_dict["debit"] = debit
        if credit is not UNSET:
            field_dict["credit"] = credit
        if transaction_date is not UNSET:
            field_dict["transactionDate"] = transaction_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_type = d.pop("accountType", UNSET)

        account_name = d.pop("accountName", UNSET)

        debit = d.pop("debit", UNSET)

        credit = d.pop("credit", UNSET)

        transaction_date = d.pop("transactionDate", UNSET)

        transactions_transactions_project_id_item = cls(
            account_type=account_type,
            account_name=account_name,
            debit=debit,
            credit=credit,
            transaction_date=transaction_date,
        )

        transactions_transactions_project_id_item.additional_properties = d
        return transactions_transactions_project_id_item

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
