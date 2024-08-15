from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transactions_transactions import TransactionsTransactions


T = TypeVar("T", bound="Transactions")


@_attrs_define
class Transactions:
    """
    Attributes:
        source (Union[Unset, str]): Name of the source from which the transactions were acquired
        transactions (Union[Unset, TransactionsTransactions]): Map of transactions for each projectId
    """

    source: Union[Unset, str] = UNSET
    transactions: Union[Unset, "TransactionsTransactions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source

        transactions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = self.transactions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if transactions is not UNSET:
            field_dict["transactions"] = transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transactions_transactions import TransactionsTransactions

        d = src_dict.copy()
        source = d.pop("source", UNSET)

        _transactions = d.pop("transactions", UNSET)
        transactions: Union[Unset, TransactionsTransactions]
        if isinstance(_transactions, Unset):
            transactions = UNSET
        else:
            transactions = TransactionsTransactions.from_dict(_transactions)

        transactions = cls(
            source=source,
            transactions=transactions,
        )

        transactions.additional_properties = d
        return transactions

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
