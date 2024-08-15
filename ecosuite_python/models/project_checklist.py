from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_checklist_checklist_type import ProjectChecklistChecklistType

if TYPE_CHECKING:
    from ..models.project_checklist_data import ProjectChecklistData


T = TypeVar("T", bound="ProjectChecklist")


@_attrs_define
class ProjectChecklist:
    """A checklist for a project

    Attributes:
        code (str):
        checklist_type (ProjectChecklistChecklistType):
        data (ProjectChecklistData): The project checklist data
    """

    code: str
    checklist_type: ProjectChecklistChecklistType
    data: "ProjectChecklistData"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        checklist_type = self.checklist_type.value

        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "checklistType": checklist_type,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_checklist_data import ProjectChecklistData

        d = src_dict.copy()
        code = d.pop("code")

        checklist_type = ProjectChecklistChecklistType(d.pop("checklistType"))

        data = ProjectChecklistData.from_dict(d.pop("data"))

        project_checklist = cls(
            code=code,
            checklist_type=checklist_type,
            data=data,
        )

        project_checklist.additional_properties = d
        return project_checklist

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
