from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_connectivity_data_sites_additional_property_data_item import (
        ProjectConnectivityDataSitesAdditionalPropertyDataItem,
    )


T = TypeVar("T", bound="ProjectConnectivityDataSitesAdditionalProperty")


@_attrs_define
class ProjectConnectivityDataSitesAdditionalProperty:
    """
    Attributes:
        total (Union[Unset, int]):
        data (Union[Unset, List['ProjectConnectivityDataSitesAdditionalPropertyDataItem']]):
    """

    total: Union[Unset, int] = UNSET
    data: Union[Unset, List["ProjectConnectivityDataSitesAdditionalPropertyDataItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total

        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_connectivity_data_sites_additional_property_data_item import (
            ProjectConnectivityDataSitesAdditionalPropertyDataItem,
        )

        d = src_dict.copy()
        total = d.pop("total", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ProjectConnectivityDataSitesAdditionalPropertyDataItem.from_dict(data_item_data)

            data.append(data_item)

        project_connectivity_data_sites_additional_property = cls(
            total=total,
            data=data,
        )

        project_connectivity_data_sites_additional_property.additional_properties = d
        return project_connectivity_data_sites_additional_property

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
