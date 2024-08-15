from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expected_generation_datums_response_200_aggregation import ExpectedGenerationDatumsResponse200Aggregation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_expected_generation_datums import ProjectExpectedGenerationDatums
    from ..models.range_ import Range


T = TypeVar("T", bound="ExpectedGenerationDatumsResponse200")


@_attrs_define
class ExpectedGenerationDatumsResponse200:
    """
    Attributes:
        projects (Union[Unset, ProjectExpectedGenerationDatums]):
        range_ (Union[Unset, Range]):
        aggregation (Union[Unset, ExpectedGenerationDatumsResponse200Aggregation]):
    """

    projects: Union[Unset, "ProjectExpectedGenerationDatums"] = UNSET
    range_: Union[Unset, "Range"] = UNSET
    aggregation: Union[Unset, ExpectedGenerationDatumsResponse200Aggregation] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        projects: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects.to_dict()

        range_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        aggregation: Union[Unset, str] = UNSET
        if not isinstance(self.aggregation, Unset):
            aggregation = self.aggregation.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projects is not UNSET:
            field_dict["projects"] = projects
        if range_ is not UNSET:
            field_dict["range"] = range_
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_expected_generation_datums import ProjectExpectedGenerationDatums
        from ..models.range_ import Range

        d = src_dict.copy()
        _projects = d.pop("projects", UNSET)
        projects: Union[Unset, ProjectExpectedGenerationDatums]
        if isinstance(_projects, Unset):
            projects = UNSET
        else:
            projects = ProjectExpectedGenerationDatums.from_dict(_projects)

        _range_ = d.pop("range", UNSET)
        range_: Union[Unset, Range]
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)

        _aggregation = d.pop("aggregation", UNSET)
        aggregation: Union[Unset, ExpectedGenerationDatumsResponse200Aggregation]
        if isinstance(_aggregation, Unset):
            aggregation = UNSET
        else:
            aggregation = ExpectedGenerationDatumsResponse200Aggregation(_aggregation)

        expected_generation_datums_response_200 = cls(
            projects=projects,
            range_=range_,
            aggregation=aggregation,
        )

        expected_generation_datums_response_200.additional_properties = d
        return expected_generation_datums_response_200

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
