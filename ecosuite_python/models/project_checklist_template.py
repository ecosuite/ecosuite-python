from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_checklist_template_checklist_type import ProjectChecklistTemplateChecklistType

if TYPE_CHECKING:
    from ..models.project_checklist_template_schema import ProjectChecklistTemplateSchema


T = TypeVar("T", bound="ProjectChecklistTemplate")


@_attrs_define
class ProjectChecklistTemplate:
    """A checklist template for projects

    Attributes:
        state_regex_source (str): The regex for the project state
        checklist_type (ProjectChecklistTemplateChecklistType):
        schema (ProjectChecklistTemplateSchema): The project checklist template schema
    """

    state_regex_source: str
    checklist_type: ProjectChecklistTemplateChecklistType
    schema: "ProjectChecklistTemplateSchema"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state_regex_source = self.state_regex_source

        checklist_type = self.checklist_type.value

        schema = self.schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stateRegexSource": state_regex_source,
                "checklistType": checklist_type,
                "schema": schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_checklist_template_schema import ProjectChecklistTemplateSchema

        d = src_dict.copy()
        state_regex_source = d.pop("stateRegexSource")

        checklist_type = ProjectChecklistTemplateChecklistType(d.pop("checklistType"))

        schema = ProjectChecklistTemplateSchema.from_dict(d.pop("schema"))

        project_checklist_template = cls(
            state_regex_source=state_regex_source,
            checklist_type=checklist_type,
            schema=schema,
        )

        project_checklist_template.additional_properties = d
        return project_checklist_template

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
