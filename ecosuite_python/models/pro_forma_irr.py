from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pro_forma_irr_categories import ProFormaIRRCategories


T = TypeVar("T", bound="ProFormaIRR")


@_attrs_define
class ProFormaIRR:
    """
    Attributes:
        irr (Union[Unset, float]):
        income (Union[Unset, float]):
        expenses (Union[Unset, float]):
        net_income (Union[Unset, float]):
        capital_cost (Union[Unset, float]):
        cumulative_cash_flow (Union[Unset, float]):
        categories (Union[Unset, ProFormaIRRCategories]): Category keyed by category name
    """

    irr: Union[Unset, float] = UNSET
    income: Union[Unset, float] = UNSET
    expenses: Union[Unset, float] = UNSET
    net_income: Union[Unset, float] = UNSET
    capital_cost: Union[Unset, float] = UNSET
    cumulative_cash_flow: Union[Unset, float] = UNSET
    categories: Union[Unset, "ProFormaIRRCategories"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        irr = self.irr

        income = self.income

        expenses = self.expenses

        net_income = self.net_income

        capital_cost = self.capital_cost

        cumulative_cash_flow = self.cumulative_cash_flow

        categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if irr is not UNSET:
            field_dict["irr"] = irr
        if income is not UNSET:
            field_dict["income"] = income
        if expenses is not UNSET:
            field_dict["expenses"] = expenses
        if net_income is not UNSET:
            field_dict["netIncome"] = net_income
        if capital_cost is not UNSET:
            field_dict["capitalCost"] = capital_cost
        if cumulative_cash_flow is not UNSET:
            field_dict["cumulativeCashFlow"] = cumulative_cash_flow
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pro_forma_irr_categories import ProFormaIRRCategories

        d = src_dict.copy()
        irr = d.pop("irr", UNSET)

        income = d.pop("income", UNSET)

        expenses = d.pop("expenses", UNSET)

        net_income = d.pop("netIncome", UNSET)

        capital_cost = d.pop("capitalCost", UNSET)

        cumulative_cash_flow = d.pop("cumulativeCashFlow", UNSET)

        _categories = d.pop("categories", UNSET)
        categories: Union[Unset, ProFormaIRRCategories]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = ProFormaIRRCategories.from_dict(_categories)

        pro_forma_irr = cls(
            irr=irr,
            income=income,
            expenses=expenses,
            net_income=net_income,
            capital_cost=capital_cost,
            cumulative_cash_flow=cumulative_cash_flow,
            categories=categories,
        )

        pro_forma_irr.additional_properties = d
        return pro_forma_irr

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
