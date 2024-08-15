from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_finance_report_section_categories_item import ProjectFinanceReportSectionCategoriesItem


T = TypeVar("T", bound="ProjectFinanceReportSection")


@_attrs_define
class ProjectFinanceReportSection:
    """
    Attributes:
        dates (Union[Unset, List[str]]):
        net_incomes (Union[Unset, List[float]]):
        unlevered_totals (Union[Unset, List[float]]):
        levered_totals (Union[Unset, List[float]]):
        unlevered_irr (Union[Unset, List[float]]):
        levered_irr (Union[Unset, List[float]]):
        retained_earnings (Union[Unset, List[float]]):
        categories (Union[Unset, List['ProjectFinanceReportSectionCategoriesItem']]):
    """

    dates: Union[Unset, List[str]] = UNSET
    net_incomes: Union[Unset, List[float]] = UNSET
    unlevered_totals: Union[Unset, List[float]] = UNSET
    levered_totals: Union[Unset, List[float]] = UNSET
    unlevered_irr: Union[Unset, List[float]] = UNSET
    levered_irr: Union[Unset, List[float]] = UNSET
    retained_earnings: Union[Unset, List[float]] = UNSET
    categories: Union[Unset, List["ProjectFinanceReportSectionCategoriesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dates: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates

        net_incomes: Union[Unset, List[float]] = UNSET
        if not isinstance(self.net_incomes, Unset):
            net_incomes = self.net_incomes

        unlevered_totals: Union[Unset, List[float]] = UNSET
        if not isinstance(self.unlevered_totals, Unset):
            unlevered_totals = self.unlevered_totals

        levered_totals: Union[Unset, List[float]] = UNSET
        if not isinstance(self.levered_totals, Unset):
            levered_totals = self.levered_totals

        unlevered_irr: Union[Unset, List[float]] = UNSET
        if not isinstance(self.unlevered_irr, Unset):
            unlevered_irr = self.unlevered_irr

        levered_irr: Union[Unset, List[float]] = UNSET
        if not isinstance(self.levered_irr, Unset):
            levered_irr = self.levered_irr

        retained_earnings: Union[Unset, List[float]] = UNSET
        if not isinstance(self.retained_earnings, Unset):
            retained_earnings = self.retained_earnings

        categories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dates is not UNSET:
            field_dict["dates"] = dates
        if net_incomes is not UNSET:
            field_dict["netIncomes"] = net_incomes
        if unlevered_totals is not UNSET:
            field_dict["unleveredTotals"] = unlevered_totals
        if levered_totals is not UNSET:
            field_dict["leveredTotals"] = levered_totals
        if unlevered_irr is not UNSET:
            field_dict["unleveredIrr"] = unlevered_irr
        if levered_irr is not UNSET:
            field_dict["leveredIrr"] = levered_irr
        if retained_earnings is not UNSET:
            field_dict["retainedEarnings"] = retained_earnings
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_finance_report_section_categories_item import ProjectFinanceReportSectionCategoriesItem

        d = src_dict.copy()
        dates = cast(List[str], d.pop("dates", UNSET))

        net_incomes = cast(List[float], d.pop("netIncomes", UNSET))

        unlevered_totals = cast(List[float], d.pop("unleveredTotals", UNSET))

        levered_totals = cast(List[float], d.pop("leveredTotals", UNSET))

        unlevered_irr = cast(List[float], d.pop("unleveredIrr", UNSET))

        levered_irr = cast(List[float], d.pop("leveredIrr", UNSET))

        retained_earnings = cast(List[float], d.pop("retainedEarnings", UNSET))

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = ProjectFinanceReportSectionCategoriesItem.from_dict(categories_item_data)

            categories.append(categories_item)

        project_finance_report_section = cls(
            dates=dates,
            net_incomes=net_incomes,
            unlevered_totals=unlevered_totals,
            levered_totals=levered_totals,
            unlevered_irr=unlevered_irr,
            levered_irr=levered_irr,
            retained_earnings=retained_earnings,
            categories=categories,
        )

        project_finance_report_section.additional_properties = d
        return project_finance_report_section

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
