from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceRequestGeneration")


@_attrs_define
class ServiceRequestGeneration:
    """Some information on who to share the new service request with.

    Attributes:
        share_with (Union[Unset, List[str]]): An array of users to share the document with.
    """

    share_with: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        share_with: Union[Unset, List[str]] = UNSET
        if not isinstance(self.share_with, Unset):
            share_with = self.share_with

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if share_with is not UNSET:
            field_dict["shareWith"] = share_with

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        share_with = cast(List[str], d.pop("shareWith", UNSET))

        service_request_generation = cls(
            share_with=share_with,
        )

        service_request_generation.additional_properties = d
        return service_request_generation

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
