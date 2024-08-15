from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectCashFlowTotalActualData")


@_attrs_define
class ProjectCashFlowTotalActualData:
    """
    Attributes:
        income (Union[Unset, float]):  Example: 1911166.83.
        expense (Union[Unset, float]):  Example: -687157.79.
        debt (Union[Unset, int]):
        equity (Union[Unset, float]):  Example: -245680.98.
        asset (Union[Unset, float]):  Example: -1422170.83.
        net_income (Union[Unset, float]):  Example: 1224009.04.
        unlevered_total (Union[Unset, float]):  Example: 256932.85.
        levered_total (Union[Unset, float]):  Example: -198161.79.
    """

    income: Union[Unset, float] = UNSET
    expense: Union[Unset, float] = UNSET
    debt: Union[Unset, int] = UNSET
    equity: Union[Unset, float] = UNSET
    asset: Union[Unset, float] = UNSET
    net_income: Union[Unset, float] = UNSET
    unlevered_total: Union[Unset, float] = UNSET
    levered_total: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        income = self.income

        expense = self.expense

        debt = self.debt

        equity = self.equity

        asset = self.asset

        net_income = self.net_income

        unlevered_total = self.unlevered_total

        levered_total = self.levered_total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if income is not UNSET:
            field_dict["income"] = income
        if expense is not UNSET:
            field_dict["expense"] = expense
        if debt is not UNSET:
            field_dict["debt"] = debt
        if equity is not UNSET:
            field_dict["equity"] = equity
        if asset is not UNSET:
            field_dict["asset"] = asset
        if net_income is not UNSET:
            field_dict["netIncome"] = net_income
        if unlevered_total is not UNSET:
            field_dict["unleveredTotal"] = unlevered_total
        if levered_total is not UNSET:
            field_dict["leveredTotal"] = levered_total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        income = d.pop("income", UNSET)

        expense = d.pop("expense", UNSET)

        debt = d.pop("debt", UNSET)

        equity = d.pop("equity", UNSET)

        asset = d.pop("asset", UNSET)

        net_income = d.pop("netIncome", UNSET)

        unlevered_total = d.pop("unleveredTotal", UNSET)

        levered_total = d.pop("leveredTotal", UNSET)

        project_cash_flow_total_actual_data = cls(
            income=income,
            expense=expense,
            debt=debt,
            equity=equity,
            asset=asset,
            net_income=net_income,
            unlevered_total=unlevered_total,
            levered_total=levered_total,
        )

        project_cash_flow_total_actual_data.additional_properties = d
        return project_cash_flow_total_actual_data

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
