from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_finance_report_section_categories_item_additional_property_categories_item import (
        ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItem,
    )


T = TypeVar("T", bound="ProjectFinanceReportSectionCategoriesItemAdditionalProperty")


@_attrs_define
class ProjectFinanceReportSectionCategoriesItemAdditionalProperty:
    """
    Attributes:
        name (Union[Unset, str]):
        totals (Union[Unset, list[float]]):
        categories (Union[Unset, list['ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItem']]):
    """

    name: Union[Unset, str] = UNSET
    totals: Union[Unset, list[float]] = UNSET
    categories: Union[Unset, list["ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        totals: Union[Unset, list[float]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals

        categories: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if totals is not UNSET:
            field_dict["totals"] = totals
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_finance_report_section_categories_item_additional_property_categories_item import (
            ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItem,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        totals = cast(list[float], d.pop("totals", UNSET))

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = ProjectFinanceReportSectionCategoriesItemAdditionalPropertyCategoriesItem.from_dict(
                categories_item_data
            )

            categories.append(categories_item)

        project_finance_report_section_categories_item_additional_property = cls(
            name=name,
            totals=totals,
            categories=categories,
        )

        project_finance_report_section_categories_item_additional_property.additional_properties = d
        return project_finance_report_section_categories_item_additional_property

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
