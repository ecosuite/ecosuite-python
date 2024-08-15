from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FinanceReportSectionProjectsItemAdditionalProperty")


@_attrs_define
class FinanceReportSectionProjectsItemAdditionalProperty:
    """
    Attributes:
        totals (Union[Unset, List[float]]): Cash flow totals, grouped by columns > forecast, expected, actual,
            latestBestEstimate, difference
    """

    totals: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        totals: Union[Unset, List[float]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        totals = cast(List[float], d.pop("totals", UNSET))

        finance_report_section_projects_item_additional_property = cls(
            totals=totals,
        )

        finance_report_section_projects_item_additional_property.additional_properties = d
        return finance_report_section_projects_item_additional_property

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
