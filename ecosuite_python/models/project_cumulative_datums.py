from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_cumulative_datums_sources import ProjectCumulativeDatumsSources
    from ..models.range_ import Range


T = TypeVar("T", bound="ProjectCumulativeDatums")


@_attrs_define
class ProjectCumulativeDatums:
    """
    Attributes:
        range_ (Union[Unset, Range]):
        year (Union[Unset, str]): The year that the datums are for when cumulating by year
        month (Union[Unset, str]): The month that the datums are for when cumulating by month
        sources (Union[Unset, ProjectCumulativeDatumsSources]): Map of datums keyed by source ID
    """

    range_: Union[Unset, "Range"] = UNSET
    year: Union[Unset, str] = UNSET
    month: Union[Unset, str] = UNSET
    sources: Union[Unset, "ProjectCumulativeDatumsSources"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        range_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        year = self.year

        month = self.month

        sources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if range_ is not UNSET:
            field_dict["range"] = range_
        if year is not UNSET:
            field_dict["year"] = year
        if month is not UNSET:
            field_dict["month"] = month
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_cumulative_datums_sources import ProjectCumulativeDatumsSources
        from ..models.range_ import Range

        d = src_dict.copy()
        _range_ = d.pop("range", UNSET)
        range_: Union[Unset, Range]
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)

        year = d.pop("year", UNSET)

        month = d.pop("month", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: Union[Unset, ProjectCumulativeDatumsSources]
        if isinstance(_sources, Unset):
            sources = UNSET
        else:
            sources = ProjectCumulativeDatumsSources.from_dict(_sources)

        project_cumulative_datums = cls(
            range_=range_,
            year=year,
            month=month,
            sources=sources,
        )

        project_cumulative_datums.additional_properties = d
        return project_cumulative_datums

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
