from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_finance_report_section_categories_item_additional_property_categories_item_additional_property_categories_item import (
        ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAdditionalPropertyCategoriesItem,
    )
    from ..models.project_finance_report_section_categories_item_additional_property_categories_item_additional_property_transactions_item import (
        ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAdditionalPropertyTransactionsItem,
    )


T = TypeVar("T", bound="ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAdditionalProperty")


@_attrs_define
class ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAdditionalProperty:
    """
    Attributes:
        name (Union[Unset, str]):
        totals (Union[Unset, List[float]]):
        transactions (Union[Unset, List['ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAdditi
            onalPropertyTransactionsItem']]):
        categories (Union[Unset, List['ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAddition
            alPropertyCategoriesItem']]):
    """

    name: Union[Unset, str] = UNSET
    totals: Union[Unset, List[float]] = UNSET
    transactions: Union[
        Unset,
        List[
            "ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAdditionalPropertyTransactionsItem"
        ],
    ] = UNSET
    categories: Union[
        Unset,
        List[
            "ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAdditionalPropertyCategoriesItem"
        ],
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        totals: Union[Unset, List[float]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals

        transactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = []
            for transactions_item_data in self.transactions:
                transactions_item = transactions_item_data.to_dict()
                transactions.append(transactions_item)

        categories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if totals is not UNSET:
            field_dict["totals"] = totals
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_finance_report_section_categories_item_additional_property_categories_item_additional_property_categories_item import (
            ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAdditionalPropertyCategoriesItem,
        )
        from ..models.project_finance_report_section_categories_item_additional_property_categories_item_additional_property_transactions_item import (
            ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAdditionalPropertyTransactionsItem,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        totals = cast(List[float], d.pop("totals", UNSET))

        transactions = []
        _transactions = d.pop("transactions", UNSET)
        for transactions_item_data in _transactions or []:
            transactions_item = ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAdditionalPropertyTransactionsItem.from_dict(
                transactions_item_data
            )

            transactions.append(transactions_item)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItemAdditionalPropertyCategoriesItem.from_dict(
                categories_item_data
            )

            categories.append(categories_item)

        project_finance_report_section_categories_item_additional_property_categories_item_additional_property = cls(
            name=name,
            totals=totals,
            transactions=transactions,
            categories=categories,
        )

        project_finance_report_section_categories_item_additional_property_categories_item_additional_property.additional_properties = d
        return project_finance_report_section_categories_item_additional_property_categories_item_additional_property

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