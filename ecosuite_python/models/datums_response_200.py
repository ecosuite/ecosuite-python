from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datums_response_200_aggregation import DatumsResponse200Aggregation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datums_response_200_projects import DatumsResponse200Projects
    from ..models.range_ import Range


T = TypeVar("T", bound="DatumsResponse200")


@_attrs_define
class DatumsResponse200:
    """
    Attributes:
        projects (Union[Unset, DatumsResponse200Projects]): Keyed by Project ID, lists the datums for each project
        range_ (Union[Unset, Range]):
        aggregation (Union[Unset, DatumsResponse200Aggregation]):
    """

    projects: Union[Unset, "DatumsResponse200Projects"] = UNSET
    range_: Union[Unset, "Range"] = UNSET
    aggregation: Union[Unset, DatumsResponse200Aggregation] = UNSET
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
        from ..models.datums_response_200_projects import DatumsResponse200Projects
        from ..models.range_ import Range

        d = src_dict.copy()
        _projects = d.pop("projects", UNSET)
        projects: Union[Unset, DatumsResponse200Projects]
        if isinstance(_projects, Unset):
            projects = UNSET
        else:
            projects = DatumsResponse200Projects.from_dict(_projects)

        _range_ = d.pop("range", UNSET)
        range_: Union[Unset, Range]
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)

        _aggregation = d.pop("aggregation", UNSET)
        aggregation: Union[Unset, DatumsResponse200Aggregation]
        if isinstance(_aggregation, Unset):
            aggregation = UNSET
        else:
            aggregation = DatumsResponse200Aggregation(_aggregation)

        datums_response_200 = cls(
            projects=projects,
            range_=range_,
            aggregation=aggregation,
        )

        datums_response_200.additional_properties = d
        return datums_response_200

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