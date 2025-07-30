from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portfolio_reports import PortfolioReports


T = TypeVar("T", bound="Portfolio")


@_attrs_define
class Portfolio:
    """Refer to the /schemas/portfolio endpoint for the full JSON Schema definition

    Attributes:
        name (str):
        projects (list[str]):
        reports (Union[Unset, PortfolioReports]):
    """

    name: str
    projects: list[str]
    reports: Union[Unset, "PortfolioReports"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        projects = self.projects

        reports: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reports, Unset):
            reports = self.reports.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "projects": projects,
            }
        )
        if reports is not UNSET:
            field_dict["reports"] = reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portfolio_reports import PortfolioReports

        d = dict(src_dict)
        name = d.pop("name")

        projects = cast(list[str], d.pop("projects"))

        _reports = d.pop("reports", UNSET)
        reports: Union[Unset, PortfolioReports]
        if isinstance(_reports, Unset):
            reports = UNSET
        else:
            reports = PortfolioReports.from_dict(_reports)

        portfolio = cls(
            name=name,
            projects=projects,
            reports=reports,
        )

        portfolio.additional_properties = d
        return portfolio

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
