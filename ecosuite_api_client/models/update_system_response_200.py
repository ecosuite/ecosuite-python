from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system import System


T = TypeVar("T", bound="UpdateSystemResponse200")


@_attrs_define
class UpdateSystemResponse200:
    """
    Attributes:
        system (Union[Unset, System]): Refer to the /schemas/system endpoint for the full JSON Schema definition
    """

    system: Union[Unset, "System"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.system, Unset):
            system = self.system.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if system is not UNSET:
            field_dict["system"] = system

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system import System

        d = dict(src_dict)
        _system = d.pop("system", UNSET)
        system: Union[Unset, System]
        if isinstance(_system, Unset):
            system = UNSET
        else:
            system = System.from_dict(_system)

        update_system_response_200 = cls(
            system=system,
        )

        update_system_response_200.additional_properties = d
        return update_system_response_200

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
