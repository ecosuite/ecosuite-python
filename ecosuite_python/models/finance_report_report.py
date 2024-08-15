from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finance_report_report_categories import FinanceReportReportCategories
    from ..models.finance_report_section import FinanceReportSection


T = TypeVar("T", bound="FinanceReportReport")


@_attrs_define
class FinanceReportReport:
    """
    Attributes:
        dates (Union[Unset, List[str]]):
        unlevered_totals (Union[Unset, FinanceReportSection]):
        cumulative_unlevered_totals (Union[Unset, FinanceReportSection]):
        levered_totals (Union[Unset, FinanceReportSection]):
        net_incomes (Union[Unset, FinanceReportSection]):
        unlevered_irr (Union[Unset, FinanceReportSection]):
        levered_irr (Union[Unset, FinanceReportSection]):
        retained_earnings (Union[Unset, FinanceReportSection]):
        total_value (Union[Unset, FinanceReportSection]):
        categories (Union[Unset, FinanceReportReportCategories]): Category breakdown keyed by category name
    """

    dates: Union[Unset, List[str]] = UNSET
    unlevered_totals: Union[Unset, "FinanceReportSection"] = UNSET
    cumulative_unlevered_totals: Union[Unset, "FinanceReportSection"] = UNSET
    levered_totals: Union[Unset, "FinanceReportSection"] = UNSET
    net_incomes: Union[Unset, "FinanceReportSection"] = UNSET
    unlevered_irr: Union[Unset, "FinanceReportSection"] = UNSET
    levered_irr: Union[Unset, "FinanceReportSection"] = UNSET
    retained_earnings: Union[Unset, "FinanceReportSection"] = UNSET
    total_value: Union[Unset, "FinanceReportSection"] = UNSET
    categories: Union[Unset, "FinanceReportReportCategories"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dates: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates

        unlevered_totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlevered_totals, Unset):
            unlevered_totals = self.unlevered_totals.to_dict()

        cumulative_unlevered_totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cumulative_unlevered_totals, Unset):
            cumulative_unlevered_totals = self.cumulative_unlevered_totals.to_dict()

        levered_totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.levered_totals, Unset):
            levered_totals = self.levered_totals.to_dict()

        net_incomes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.net_incomes, Unset):
            net_incomes = self.net_incomes.to_dict()

        unlevered_irr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlevered_irr, Unset):
            unlevered_irr = self.unlevered_irr.to_dict()

        levered_irr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.levered_irr, Unset):
            levered_irr = self.levered_irr.to_dict()

        retained_earnings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retained_earnings, Unset):
            retained_earnings = self.retained_earnings.to_dict()

        total_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_value, Unset):
            total_value = self.total_value.to_dict()

        categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dates is not UNSET:
            field_dict["dates"] = dates
        if unlevered_totals is not UNSET:
            field_dict["unleveredTotals"] = unlevered_totals
        if cumulative_unlevered_totals is not UNSET:
            field_dict["cumulativeUnleveredTotals"] = cumulative_unlevered_totals
        if levered_totals is not UNSET:
            field_dict["leveredTotals"] = levered_totals
        if net_incomes is not UNSET:
            field_dict["netIncomes"] = net_incomes
        if unlevered_irr is not UNSET:
            field_dict["unleveredIrr"] = unlevered_irr
        if levered_irr is not UNSET:
            field_dict["leveredIrr"] = levered_irr
        if retained_earnings is not UNSET:
            field_dict["retainedEarnings"] = retained_earnings
        if total_value is not UNSET:
            field_dict["totalValue"] = total_value
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.finance_report_report_categories import FinanceReportReportCategories
        from ..models.finance_report_section import FinanceReportSection

        d = src_dict.copy()
        dates = cast(List[str], d.pop("dates", UNSET))

        _unlevered_totals = d.pop("unleveredTotals", UNSET)
        unlevered_totals: Union[Unset, FinanceReportSection]
        if isinstance(_unlevered_totals, Unset):
            unlevered_totals = UNSET
        else:
            unlevered_totals = FinanceReportSection.from_dict(_unlevered_totals)

        _cumulative_unlevered_totals = d.pop("cumulativeUnleveredTotals", UNSET)
        cumulative_unlevered_totals: Union[Unset, FinanceReportSection]
        if isinstance(_cumulative_unlevered_totals, Unset):
            cumulative_unlevered_totals = UNSET
        else:
            cumulative_unlevered_totals = FinanceReportSection.from_dict(_cumulative_unlevered_totals)

        _levered_totals = d.pop("leveredTotals", UNSET)
        levered_totals: Union[Unset, FinanceReportSection]
        if isinstance(_levered_totals, Unset):
            levered_totals = UNSET
        else:
            levered_totals = FinanceReportSection.from_dict(_levered_totals)

        _net_incomes = d.pop("netIncomes", UNSET)
        net_incomes: Union[Unset, FinanceReportSection]
        if isinstance(_net_incomes, Unset):
            net_incomes = UNSET
        else:
            net_incomes = FinanceReportSection.from_dict(_net_incomes)

        _unlevered_irr = d.pop("unleveredIrr", UNSET)
        unlevered_irr: Union[Unset, FinanceReportSection]
        if isinstance(_unlevered_irr, Unset):
            unlevered_irr = UNSET
        else:
            unlevered_irr = FinanceReportSection.from_dict(_unlevered_irr)

        _levered_irr = d.pop("leveredIrr", UNSET)
        levered_irr: Union[Unset, FinanceReportSection]
        if isinstance(_levered_irr, Unset):
            levered_irr = UNSET
        else:
            levered_irr = FinanceReportSection.from_dict(_levered_irr)

        _retained_earnings = d.pop("retainedEarnings", UNSET)
        retained_earnings: Union[Unset, FinanceReportSection]
        if isinstance(_retained_earnings, Unset):
            retained_earnings = UNSET
        else:
            retained_earnings = FinanceReportSection.from_dict(_retained_earnings)

        _total_value = d.pop("totalValue", UNSET)
        total_value: Union[Unset, FinanceReportSection]
        if isinstance(_total_value, Unset):
            total_value = UNSET
        else:
            total_value = FinanceReportSection.from_dict(_total_value)

        _categories = d.pop("categories", UNSET)
        categories: Union[Unset, FinanceReportReportCategories]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = FinanceReportReportCategories.from_dict(_categories)

        finance_report_report = cls(
            dates=dates,
            unlevered_totals=unlevered_totals,
            cumulative_unlevered_totals=cumulative_unlevered_totals,
            levered_totals=levered_totals,
            net_incomes=net_incomes,
            unlevered_irr=unlevered_irr,
            levered_irr=levered_irr,
            retained_earnings=retained_earnings,
            total_value=total_value,
            categories=categories,
        )

        finance_report_report.additional_properties = d
        return finance_report_report

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
