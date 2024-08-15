from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_finance_settings import ProjectFinanceSettings


T = TypeVar("T", bound="GetProjectSettingsResponse200")


@_attrs_define
class GetProjectSettingsResponse200:
    """
    Attributes:
        settings (Union[Unset, ProjectFinanceSettings]): Refer to the /schemas/finance endpoint for the full JSON Schema
            definition
    """

    settings: Union[Unset, "ProjectFinanceSettings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_finance_settings import ProjectFinanceSettings

        d = src_dict.copy()
        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, ProjectFinanceSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ProjectFinanceSettings.from_dict(_settings)

        get_project_settings_response_200 = cls(
            settings=settings,
        )

        get_project_settings_response_200.additional_properties = d
        return get_project_settings_response_200

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
