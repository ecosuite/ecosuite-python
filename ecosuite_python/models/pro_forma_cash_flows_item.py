from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pro_forma_cash_flows_item_flags import ProFormaCashFlowsItemFlags
    from ..models.pro_forma_cash_flows_item_payments_item import ProFormaCashFlowsItemPaymentsItem


T = TypeVar("T", bound="ProFormaCashFlowsItem")


@_attrs_define
class ProFormaCashFlowsItem:
    """
    Attributes:
        id (str): The ID used to uniquely identify this cashflow on this Pro Forma. Extreme caution should be taken
            before editing as the ID is used to link payment logs and documents to the cash flow, and changing an already
            used ID will break those links
        name (str):
        category (str):
        account (str):
        payments (List['ProFormaCashFlowsItemPaymentsItem']):
        record_id (Union[Unset, str]):
        flags (Union[Unset, ProFormaCashFlowsItemFlags]):
    """

    id: str
    name: str
    category: str
    account: str
    payments: List["ProFormaCashFlowsItemPaymentsItem"]
    record_id: Union[Unset, str] = UNSET
    flags: Union[Unset, "ProFormaCashFlowsItemFlags"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        category = self.category

        account = self.account

        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        record_id = self.record_id

        flags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "category": category,
                "account": account,
                "payments": payments,
            }
        )
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pro_forma_cash_flows_item_flags import ProFormaCashFlowsItemFlags
        from ..models.pro_forma_cash_flows_item_payments_item import ProFormaCashFlowsItemPaymentsItem

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        category = d.pop("category")

        account = d.pop("account")

        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = ProFormaCashFlowsItemPaymentsItem.from_dict(payments_item_data)

            payments.append(payments_item)

        record_id = d.pop("recordId", UNSET)

        _flags = d.pop("flags", UNSET)
        flags: Union[Unset, ProFormaCashFlowsItemFlags]
        if isinstance(_flags, Unset):
            flags = UNSET
        else:
            flags = ProFormaCashFlowsItemFlags.from_dict(_flags)

        pro_forma_cash_flows_item = cls(
            id=id,
            name=name,
            category=category,
            account=account,
            payments=payments,
            record_id=record_id,
            flags=flags,
        )

        pro_forma_cash_flows_item.additional_properties = d
        return pro_forma_cash_flows_item

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
