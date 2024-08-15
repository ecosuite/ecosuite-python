from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_daylight_response_200_daylight_sites import ProjectDaylightResponse200DaylightSites


T = TypeVar("T", bound="ProjectDaylightResponse200Daylight")


@_attrs_define
class ProjectDaylightResponse200Daylight:
    """
    Attributes:
        sites (Union[Unset, ProjectDaylightResponse200DaylightSites]): Daylight readings keyed by Site code
    """

    sites: Union[Unset, "ProjectDaylightResponse200DaylightSites"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sites: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_daylight_response_200_daylight_sites import ProjectDaylightResponse200DaylightSites

        d = src_dict.copy()
        _sites = d.pop("sites", UNSET)
        sites: Union[Unset, ProjectDaylightResponse200DaylightSites]
        if isinstance(_sites, Unset):
            sites = UNSET
        else:
            sites = ProjectDaylightResponse200DaylightSites.from_dict(_sites)

        project_daylight_response_200_daylight = cls(
            sites=sites,
        )

        project_daylight_response_200_daylight.additional_properties = d
        return project_daylight_response_200_daylight

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
