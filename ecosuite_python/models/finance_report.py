import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.finance_report_aggregate import FinanceReportAggregate
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finance_report_report import FinanceReportReport


T = TypeVar("T", bound="FinanceReport")


@_attrs_define
class FinanceReport:
    """
    Attributes:
        project_ids (Union[Unset, List[datetime.datetime]]):
        aggregate (Union[Unset, FinanceReportAggregate]):
        report (Union[Unset, FinanceReportReport]):
    """

    project_ids: Union[Unset, List[datetime.datetime]] = UNSET
    aggregate: Union[Unset, FinanceReportAggregate] = UNSET
    report: Union[Unset, "FinanceReportReport"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = []
            for project_ids_item_data in self.project_ids:
                project_ids_item = project_ids_item_data.isoformat()
                project_ids.append(project_ids_item)

        aggregate: Union[Unset, str] = UNSET
        if not isinstance(self.aggregate, Unset):
            aggregate = self.aggregate.value

        report: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report, Unset):
            report = self.report.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_ids is not UNSET:
            field_dict["projectIds"] = project_ids
        if aggregate is not UNSET:
            field_dict["aggregate"] = aggregate
        if report is not UNSET:
            field_dict["report"] = report

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.finance_report_report import FinanceReportReport

        d = src_dict.copy()
        project_ids = []
        _project_ids = d.pop("projectIds", UNSET)
        for project_ids_item_data in _project_ids or []:
            project_ids_item = isoparse(project_ids_item_data)

            project_ids.append(project_ids_item)

        _aggregate = d.pop("aggregate", UNSET)
        aggregate: Union[Unset, FinanceReportAggregate]
        if isinstance(_aggregate, Unset):
            aggregate = UNSET
        else:
            aggregate = FinanceReportAggregate(_aggregate)

        _report = d.pop("report", UNSET)
        report: Union[Unset, FinanceReportReport]
        if isinstance(_report, Unset):
            report = UNSET
        else:
            report = FinanceReportReport.from_dict(_report)

        finance_report = cls(
            project_ids=project_ids,
            aggregate=aggregate,
            report=report,
        )

        finance_report.additional_properties = d
        return finance_report

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
