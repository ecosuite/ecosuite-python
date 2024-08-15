from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transactions_transactions_project_id_item import TransactionsTransactionsProjectIdItem


T = TypeVar("T", bound="TransactionsTransactions")


@_attrs_define
class TransactionsTransactions:
    """Map of transactions for each projectId

    Attributes:
        project_id (Union[Unset, List['TransactionsTransactionsProjectIdItem']]):
    """

    project_id: Union[Unset, List["TransactionsTransactionsProjectIdItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_id: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.project_id, Unset):
            project_id = []
            for project_id_item_data in self.project_id:
                project_id_item = project_id_item_data.to_dict()
                project_id.append(project_id_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transactions_transactions_project_id_item import TransactionsTransactionsProjectIdItem

        d = src_dict.copy()
        project_id = []
        _project_id = d.pop("projectId", UNSET)
        for project_id_item_data in _project_id or []:
            project_id_item = TransactionsTransactionsProjectIdItem.from_dict(project_id_item_data)

            project_id.append(project_id_item)

        transactions_transactions = cls(
            project_id=project_id,
        )

        transactions_transactions.additional_properties = d
        return transactions_transactions

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
