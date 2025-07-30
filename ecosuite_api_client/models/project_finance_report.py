import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_finance_report_report import ProjectFinanceReportReport


T = TypeVar("T", bound="ProjectFinanceReport")


@_attrs_define
class ProjectFinanceReport:
    """
    Attributes:
        timestamp (Union[Unset, datetime.datetime]):
        report (Union[Unset, ProjectFinanceReportReport]):
    """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    report: Union[Unset, "ProjectFinanceReportReport"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        report: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.report, Unset):
            report = self.report.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if report is not UNSET:
            field_dict["report"] = report

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_finance_report_report import ProjectFinanceReportReport

        d = dict(src_dict)
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        _report = d.pop("report", UNSET)
        report: Union[Unset, ProjectFinanceReportReport]
        if isinstance(_report, Unset):
            report = UNSET
        else:
            report = ProjectFinanceReportReport.from_dict(_report)

        project_finance_report = cls(
            timestamp=timestamp,
            report=report,
        )

        project_finance_report.additional_properties = d
        return project_finance_report

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
