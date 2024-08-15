from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.finance_report_section import FinanceReportSection


T = TypeVar("T", bound="FinanceReportReportCategories")


@_attrs_define
class FinanceReportReportCategories:
    """Category breakdown keyed by category name"""

    additional_properties: Dict[str, "FinanceReportSection"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.finance_report_section import FinanceReportSection

        d = src_dict.copy()
        finance_report_report_categories = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FinanceReportSection.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        finance_report_report_categories.additional_properties = additional_properties
        return finance_report_report_categories

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "FinanceReportSection":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "FinanceReportSection") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
