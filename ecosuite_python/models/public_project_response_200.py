from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_project import PublicProject


T = TypeVar("T", bound="PublicProjectResponse200")


@_attrs_define
class PublicProjectResponse200:
    """
    Attributes:
        project (Union[Unset, PublicProject]):
    """

    project: Union[Unset, "PublicProject"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.public_project import PublicProject

        d = src_dict.copy()
        _project = d.pop("project", UNSET)
        project: Union[Unset, PublicProject]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = PublicProject.from_dict(_project)

        public_project_response_200 = cls(
            project=project,
        )

        public_project_response_200.additional_properties = d
        return public_project_response_200

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