from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instantaneous_response_200_projects_item import InstantaneousResponse200ProjectsItem


T = TypeVar("T", bound="InstantaneousResponse200")


@_attrs_define
class InstantaneousResponse200:
    """
    Attributes:
        projects (Union[Unset, List['InstantaneousResponse200ProjectsItem']]):
        generation (Union[Unset, float]):
        timestamp (Union[Unset, float]):
    """

    projects: Union[Unset, List["InstantaneousResponse200ProjectsItem"]] = UNSET
    generation: Union[Unset, float] = UNSET
    timestamp: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        projects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        generation = self.generation

        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projects is not UNSET:
            field_dict["projects"] = projects
        if generation is not UNSET:
            field_dict["generation"] = generation
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.instantaneous_response_200_projects_item import InstantaneousResponse200ProjectsItem

        d = src_dict.copy()
        projects = []
        _projects = d.pop("projects", UNSET)
        for projects_item_data in _projects or []:
            projects_item = InstantaneousResponse200ProjectsItem.from_dict(projects_item_data)

            projects.append(projects_item)

        generation = d.pop("generation", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        instantaneous_response_200 = cls(
            projects=projects,
            generation=generation,
            timestamp=timestamp,
        )

        instantaneous_response_200.additional_properties = d
        return instantaneous_response_200

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
