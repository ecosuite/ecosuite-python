from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_finance_report_section import ProjectFinanceReportSection


T = TypeVar("T", bound="ProjectFinanceReportReport")


@_attrs_define
class ProjectFinanceReportReport:
    """
    Attributes:
        forecast (Union[Unset, ProjectFinanceReportSection]):
        expected (Union[Unset, ProjectFinanceReportSection]):
        actual (Union[Unset, ProjectFinanceReportSection]):
        latest_best_estimate (Union[Unset, ProjectFinanceReportSection]):
    """

    forecast: Union[Unset, "ProjectFinanceReportSection"] = UNSET
    expected: Union[Unset, "ProjectFinanceReportSection"] = UNSET
    actual: Union[Unset, "ProjectFinanceReportSection"] = UNSET
    latest_best_estimate: Union[Unset, "ProjectFinanceReportSection"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        forecast: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.forecast, Unset):
            forecast = self.forecast.to_dict()

        expected: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.expected, Unset):
            expected = self.expected.to_dict()

        actual: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actual, Unset):
            actual = self.actual.to_dict()

        latest_best_estimate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.latest_best_estimate, Unset):
            latest_best_estimate = self.latest_best_estimate.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if expected is not UNSET:
            field_dict["expected"] = expected
        if actual is not UNSET:
            field_dict["actual"] = actual
        if latest_best_estimate is not UNSET:
            field_dict["latestBestEstimate"] = latest_best_estimate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_finance_report_section import ProjectFinanceReportSection

        d = src_dict.copy()
        _forecast = d.pop("forecast", UNSET)
        forecast: Union[Unset, ProjectFinanceReportSection]
        if isinstance(_forecast, Unset):
            forecast = UNSET
        else:
            forecast = ProjectFinanceReportSection.from_dict(_forecast)

        _expected = d.pop("expected", UNSET)
        expected: Union[Unset, ProjectFinanceReportSection]
        if isinstance(_expected, Unset):
            expected = UNSET
        else:
            expected = ProjectFinanceReportSection.from_dict(_expected)

        _actual = d.pop("actual", UNSET)
        actual: Union[Unset, ProjectFinanceReportSection]
        if isinstance(_actual, Unset):
            actual = UNSET
        else:
            actual = ProjectFinanceReportSection.from_dict(_actual)

        _latest_best_estimate = d.pop("latestBestEstimate", UNSET)
        latest_best_estimate: Union[Unset, ProjectFinanceReportSection]
        if isinstance(_latest_best_estimate, Unset):
            latest_best_estimate = UNSET
        else:
            latest_best_estimate = ProjectFinanceReportSection.from_dict(_latest_best_estimate)

        project_finance_report_report = cls(
            forecast=forecast,
            expected=expected,
            actual=actual,
            latest_best_estimate=latest_best_estimate,
        )

        project_finance_report_report.additional_properties = d
        return project_finance_report_report

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
