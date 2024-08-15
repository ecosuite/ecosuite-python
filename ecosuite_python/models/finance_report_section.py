from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finance_report_section_projects_item import FinanceReportSectionProjectsItem


T = TypeVar("T", bound="FinanceReportSection")


@_attrs_define
class FinanceReportSection:
    """
    Attributes:
        totals (Union[Unset, List[float]]): Cash flow totals, grouped by columns > forecast, expected, actual,
            latestBestEstimate, difference
        projects (Union[Unset, List['FinanceReportSectionProjectsItem']]):
    """

    totals: Union[Unset, List[float]] = UNSET
    projects: Union[Unset, List["FinanceReportSectionProjectsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        totals: Union[Unset, List[float]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals

        projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if totals is not UNSET:
            field_dict["totals"] = totals
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.finance_report_section_projects_item import FinanceReportSectionProjectsItem

        d = src_dict.copy()
        totals = cast(List[float], d.pop("totals", UNSET))

        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = FinanceReportSectionProjectsItem.from_dict(projects_item_data)

            projects.append(projects_item)

        finance_report_section = cls(
            totals=totals,
            projects=projects,
        )

        finance_report_section.additional_properties = d
        return finance_report_section

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
