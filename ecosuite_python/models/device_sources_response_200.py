from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_sources_response_200_projects import DeviceSourcesResponse200Projects


T = TypeVar("T", bound="DeviceSourcesResponse200")


@_attrs_define
class DeviceSourcesResponse200:
    """
    Attributes:
        projects (Union[Unset, DeviceSourcesResponse200Projects]): Keyed by project code
    """

    projects: Union[Unset, "DeviceSourcesResponse200Projects"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        projects: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_sources_response_200_projects import DeviceSourcesResponse200Projects

        d = src_dict.copy()
        _projects = d.pop("projects", UNSET)
        projects: Union[Unset, DeviceSourcesResponse200Projects]
        if isinstance(_projects, Unset):
            projects = UNSET
        else:
            projects = DeviceSourcesResponse200Projects.from_dict(_projects)

        device_sources_response_200 = cls(
            projects=projects,
        )

        device_sources_response_200.additional_properties = d
        return device_sources_response_200

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
