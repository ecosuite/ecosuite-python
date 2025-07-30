from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instruction_body_params import InstructionBodyParams


T = TypeVar("T", bound="InstructionBody")


@_attrs_define
class InstructionBody:
    """
    Attributes:
        path (Union[Unset, str]):
        params (Union[Unset, InstructionBodyParams]):
    """

    path: Union[Unset, str] = UNSET
    params: Union[Unset, "InstructionBodyParams"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instruction_body_params import InstructionBodyParams

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, InstructionBodyParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = InstructionBodyParams.from_dict(_params)

        instruction_body = cls(
            path=path,
            params=params,
        )

        instruction_body.additional_properties = d
        return instruction_body

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
