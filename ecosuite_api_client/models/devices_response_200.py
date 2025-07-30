from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.devices_response_200_projects import DevicesResponse200Projects


T = TypeVar("T", bound="DevicesResponse200")


@_attrs_define
class DevicesResponse200:
    """
    Attributes:
        projects (Union[Unset, DevicesResponse200Projects]): Keyed by Project ID, lists the devices for each project
    """

    projects: Union[Unset, "DevicesResponse200Projects"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.devices_response_200_projects import DevicesResponse200Projects

        d = dict(src_dict)
        _projects = d.pop("projects", UNSET)
        projects: Union[Unset, DevicesResponse200Projects]
        if isinstance(_projects, Unset):
            projects = UNSET
        else:
            projects = DevicesResponse200Projects.from_dict(_projects)

        devices_response_200 = cls(
            projects=projects,
        )

        devices_response_200.additional_properties = d
        return devices_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
