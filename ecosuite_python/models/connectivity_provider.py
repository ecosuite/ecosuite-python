from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectivityProvider")


@_attrs_define
class ConnectivityProvider:
    """
    Attributes:
        total (Union[Unset, int]):
        name (Union[Unset, str]):
        project_totals (Union[Unset, Any]):
    """

    total: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    project_totals: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total

        name = self.name

        project_totals = self.project_totals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if name is not UNSET:
            field_dict["name"] = name
        if project_totals is not UNSET:
            field_dict["projectTotals"] = project_totals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total", UNSET)

        name = d.pop("name", UNSET)

        project_totals = d.pop("projectTotals", UNSET)

        connectivity_provider = cls(
            total=total,
            name=name,
            project_totals=project_totals,
        )

        connectivity_provider.additional_properties = d
        return connectivity_provider

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
