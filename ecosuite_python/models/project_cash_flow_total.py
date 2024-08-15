import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_cash_flow_total_actual_data import ProjectCashFlowTotalActualData
    from ..models.project_cash_flow_total_forecast_data import ProjectCashFlowTotalForecastData


T = TypeVar("T", bound="ProjectCashFlowTotal")


@_attrs_define
class ProjectCashFlowTotal:
    """
    Attributes:
        currency (Union[Unset, str]):  Example: USD.
        income (Union[Unset, float]):  Example: 2745241.58.
        expense (Union[Unset, float]):  Example: -810705.05.
        debt (Union[Unset, int]):
        equity (Union[Unset, float]):  Example: -245680.98.
        asset (Union[Unset, float]):  Example: -1422170.83.
        net_income (Union[Unset, float]):  Example: 1934536.53.
        unlevered_total (Union[Unset, float]):  Example: 967460.34.
        levered_total (Union[Unset, float]):  Example: 512365.7.
        retained_earnings (Union[Unset, float]):  Example: 659989.86.
        total_value (Union[Unset, float]):  Example: 1627450.2.
        unlevered_irr (Union[Unset, float]):  Example: 6.7.
        levered_irr (Union[Unset, float]):  Example: 3.57.
        net_sources (Union[Unset, float]):  Example: 43263.57.
        net_uses (Union[Unset, float]):  Example: 5463.57.
        class_b_contributions (Union[Unset, float]):  Example: 5463.57.
        grants (Union[Unset, float]):  Example: 5463.57.
        debt_proceeds (Union[Unset, float]):  Example: 5463.57.
        non_dev_fee_fixed_assets (Union[Unset, float]):  Example: 5463.57.
        dev_fees (Union[Unset, float]):  Example: 5463.57.
        fixed_assets (Union[Unset, float]):  Example: 5463.57.
        actual (Union[Unset, ProjectCashFlowTotalActualData]):
        forecast (Union[Unset, ProjectCashFlowTotalForecastData]):
        timestamp (Union[Unset, datetime.datetime]):  Example: 2023-04-20 04:34:08.198000+00:00.
    """

    currency: Union[Unset, str] = UNSET
    income: Union[Unset, float] = UNSET
    expense: Union[Unset, float] = UNSET
    debt: Union[Unset, int] = UNSET
    equity: Union[Unset, float] = UNSET
    asset: Union[Unset, float] = UNSET
    net_income: Union[Unset, float] = UNSET
    unlevered_total: Union[Unset, float] = UNSET
    levered_total: Union[Unset, float] = UNSET
    retained_earnings: Union[Unset, float] = UNSET
    total_value: Union[Unset, float] = UNSET
    unlevered_irr: Union[Unset, float] = UNSET
    levered_irr: Union[Unset, float] = UNSET
    net_sources: Union[Unset, float] = UNSET
    net_uses: Union[Unset, float] = UNSET
    class_b_contributions: Union[Unset, float] = UNSET
    grants: Union[Unset, float] = UNSET
    debt_proceeds: Union[Unset, float] = UNSET
    non_dev_fee_fixed_assets: Union[Unset, float] = UNSET
    dev_fees: Union[Unset, float] = UNSET
    fixed_assets: Union[Unset, float] = UNSET
    actual: Union[Unset, "ProjectCashFlowTotalActualData"] = UNSET
    forecast: Union[Unset, "ProjectCashFlowTotalForecastData"] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency

        income = self.income

        expense = self.expense

        debt = self.debt

        equity = self.equity

        asset = self.asset

        net_income = self.net_income

        unlevered_total = self.unlevered_total

        levered_total = self.levered_total

        retained_earnings = self.retained_earnings

        total_value = self.total_value

        unlevered_irr = self.unlevered_irr

        levered_irr = self.levered_irr

        net_sources = self.net_sources

        net_uses = self.net_uses

        class_b_contributions = self.class_b_contributions

        grants = self.grants

        debt_proceeds = self.debt_proceeds

        non_dev_fee_fixed_assets = self.non_dev_fee_fixed_assets

        dev_fees = self.dev_fees

        fixed_assets = self.fixed_assets

        actual: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actual, Unset):
            actual = self.actual.to_dict()

        forecast: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.forecast, Unset):
            forecast = self.forecast.to_dict()

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
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
        if retained_earnings is not UNSET:
            field_dict["retainedEarnings"] = retained_earnings
        if total_value is not UNSET:
            field_dict["totalValue"] = total_value
        if unlevered_irr is not UNSET:
            field_dict["unleveredIrr"] = unlevered_irr
        if levered_irr is not UNSET:
            field_dict["leveredIrr"] = levered_irr
        if net_sources is not UNSET:
            field_dict["netSources"] = net_sources
        if net_uses is not UNSET:
            field_dict["netUses"] = net_uses
        if class_b_contributions is not UNSET:
            field_dict["classBContributions"] = class_b_contributions
        if grants is not UNSET:
            field_dict["grants"] = grants
        if debt_proceeds is not UNSET:
            field_dict["debtProceeds"] = debt_proceeds
        if non_dev_fee_fixed_assets is not UNSET:
            field_dict["nonDevFeeFixedAssets"] = non_dev_fee_fixed_assets
        if dev_fees is not UNSET:
            field_dict["devFees"] = dev_fees
        if fixed_assets is not UNSET:
            field_dict["fixedAssets"] = fixed_assets
        if actual is not UNSET:
            field_dict["actual"] = actual
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_cash_flow_total_actual_data import ProjectCashFlowTotalActualData
        from ..models.project_cash_flow_total_forecast_data import ProjectCashFlowTotalForecastData

        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        income = d.pop("income", UNSET)

        expense = d.pop("expense", UNSET)

        debt = d.pop("debt", UNSET)

        equity = d.pop("equity", UNSET)

        asset = d.pop("asset", UNSET)

        net_income = d.pop("netIncome", UNSET)

        unlevered_total = d.pop("unleveredTotal", UNSET)

        levered_total = d.pop("leveredTotal", UNSET)

        retained_earnings = d.pop("retainedEarnings", UNSET)

        total_value = d.pop("totalValue", UNSET)

        unlevered_irr = d.pop("unleveredIrr", UNSET)

        levered_irr = d.pop("leveredIrr", UNSET)

        net_sources = d.pop("netSources", UNSET)

        net_uses = d.pop("netUses", UNSET)

        class_b_contributions = d.pop("classBContributions", UNSET)

        grants = d.pop("grants", UNSET)

        debt_proceeds = d.pop("debtProceeds", UNSET)

        non_dev_fee_fixed_assets = d.pop("nonDevFeeFixedAssets", UNSET)

        dev_fees = d.pop("devFees", UNSET)

        fixed_assets = d.pop("fixedAssets", UNSET)

        _actual = d.pop("actual", UNSET)
        actual: Union[Unset, ProjectCashFlowTotalActualData]
        if isinstance(_actual, Unset):
            actual = UNSET
        else:
            actual = ProjectCashFlowTotalActualData.from_dict(_actual)

        _forecast = d.pop("forecast", UNSET)
        forecast: Union[Unset, ProjectCashFlowTotalForecastData]
        if isinstance(_forecast, Unset):
            forecast = UNSET
        else:
            forecast = ProjectCashFlowTotalForecastData.from_dict(_forecast)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        project_cash_flow_total = cls(
            currency=currency,
            income=income,
            expense=expense,
            debt=debt,
            equity=equity,
            asset=asset,
            net_income=net_income,
            unlevered_total=unlevered_total,
            levered_total=levered_total,
            retained_earnings=retained_earnings,
            total_value=total_value,
            unlevered_irr=unlevered_irr,
            levered_irr=levered_irr,
            net_sources=net_sources,
            net_uses=net_uses,
            class_b_contributions=class_b_contributions,
            grants=grants,
            debt_proceeds=debt_proceeds,
            non_dev_fee_fixed_assets=non_dev_fee_fixed_assets,
            dev_fees=dev_fees,
            fixed_assets=fixed_assets,
            actual=actual,
            forecast=forecast,
            timestamp=timestamp,
        )

        project_cash_flow_total.additional_properties = d
        return project_cash_flow_total

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
