from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventLocation")


@_attrs_define
class EventLocation:
    """
    Attributes:
        project (str):
        site (Union[Unset, str]):
        system (Union[Unset, str]):
        node (Union[Unset, str]):
        device (Union[Unset, str]):
    """

    project: str
    site: Union[Unset, str] = UNSET
    system: Union[Unset, str] = UNSET
    node: Union[Unset, str] = UNSET
    device: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project = self.project

        site = self.site

        system = self.system

        node = self.node

        device = self.device

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
            }
        )
        if site is not UNSET:
            field_dict["site"] = site
        if system is not UNSET:
            field_dict["system"] = system
        if node is not UNSET:
            field_dict["node"] = node
        if device is not UNSET:
            field_dict["device"] = device

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project = d.pop("project")

        site = d.pop("site", UNSET)

        system = d.pop("system", UNSET)

        node = d.pop("node", UNSET)

        device = d.pop("device", UNSET)

        event_location = cls(
            project=project,
            site=site,
            system=system,
            node=node,
            device=device,
        )

        event_location.additional_properties = d
        return event_location

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
