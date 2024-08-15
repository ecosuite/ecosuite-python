from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_cumulative_datums_response_200_aggregation import ProjectCumulativeDatumsResponse200Aggregation
from ..models.project_cumulative_datums_response_200_cumulation import ProjectCumulativeDatumsResponse200Cumulation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_cumulative_datums import ProjectCumulativeDatums


T = TypeVar("T", bound="ProjectCumulativeDatumsResponse200")


@_attrs_define
class ProjectCumulativeDatumsResponse200:
    """
    Attributes:
        cumulation_date (Union[Unset, str]):
        cumulation (Union[Unset, ProjectCumulativeDatumsResponse200Cumulation]):
        aggregation (Union[Unset, ProjectCumulativeDatumsResponse200Aggregation]):
        source_ids (Union[Unset, List[str]]):
        project (Union[Unset, str]):
        datums (Union[Unset, ProjectCumulativeDatums]):
    """

    cumulation_date: Union[Unset, str] = UNSET
    cumulation: Union[Unset, ProjectCumulativeDatumsResponse200Cumulation] = UNSET
    aggregation: Union[Unset, ProjectCumulativeDatumsResponse200Aggregation] = UNSET
    source_ids: Union[Unset, List[str]] = UNSET
    project: Union[Unset, str] = UNSET
    datums: Union[Unset, "ProjectCumulativeDatums"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cumulation_date = self.cumulation_date

        cumulation: Union[Unset, str] = UNSET
        if not isinstance(self.cumulation, Unset):
            cumulation = self.cumulation.value

        aggregation: Union[Unset, str] = UNSET
        if not isinstance(self.aggregation, Unset):
            aggregation = self.aggregation.value

        source_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.source_ids, Unset):
            source_ids = self.source_ids

        project = self.project

        datums: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.datums, Unset):
            datums = self.datums.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cumulation_date is not UNSET:
            field_dict["cumulationDate"] = cumulation_date
        if cumulation is not UNSET:
            field_dict["cumulation"] = cumulation
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if source_ids is not UNSET:
            field_dict["sourceIds"] = source_ids
        if project is not UNSET:
            field_dict["project"] = project
        if datums is not UNSET:
            field_dict["datums"] = datums

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_cumulative_datums import ProjectCumulativeDatums

        d = src_dict.copy()
        cumulation_date = d.pop("cumulationDate", UNSET)

        _cumulation = d.pop("cumulation", UNSET)
        cumulation: Union[Unset, ProjectCumulativeDatumsResponse200Cumulation]
        if isinstance(_cumulation, Unset):
            cumulation = UNSET
        else:
            cumulation = ProjectCumulativeDatumsResponse200Cumulation(_cumulation)

        _aggregation = d.pop("aggregation", UNSET)
        aggregation: Union[Unset, ProjectCumulativeDatumsResponse200Aggregation]
        if isinstance(_aggregation, Unset):
            aggregation = UNSET
        else:
            aggregation = ProjectCumulativeDatumsResponse200Aggregation(_aggregation)

        source_ids = cast(List[str], d.pop("sourceIds", UNSET))

        project = d.pop("project", UNSET)

        _datums = d.pop("datums", UNSET)
        datums: Union[Unset, ProjectCumulativeDatums]
        if isinstance(_datums, Unset):
            datums = UNSET
        else:
            datums = ProjectCumulativeDatums.from_dict(_datums)

        project_cumulative_datums_response_200 = cls(
            cumulation_date=cumulation_date,
            cumulation=cumulation,
            aggregation=aggregation,
            source_ids=source_ids,
            project=project,
            datums=datums,
        )

        project_cumulative_datums_response_200.additional_properties = d
        return project_cumulative_datums_response_200

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
