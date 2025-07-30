from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_connectivity_data_sites import ProjectConnectivityDataSites


T = TypeVar("T", bound="ProjectConnectivityData")


@_attrs_define
class ProjectConnectivityData:
    """
    Attributes:
        sites (Union[Unset, ProjectConnectivityDataSites]): Keyed by Site ID, list the connectivity data for each Site
    """

    sites: Union[Unset, "ProjectConnectivityDataSites"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sites: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_connectivity_data_sites import ProjectConnectivityDataSites

        d = dict(src_dict)
        _sites = d.pop("sites", UNSET)
        sites: Union[Unset, ProjectConnectivityDataSites]
        if isinstance(_sites, Unset):
            sites = UNSET
        else:
            sites = ProjectConnectivityDataSites.from_dict(_sites)

        project_connectivity_data = cls(
            sites=sites,
        )

        project_connectivity_data.additional_properties = d
        return project_connectivity_data

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
