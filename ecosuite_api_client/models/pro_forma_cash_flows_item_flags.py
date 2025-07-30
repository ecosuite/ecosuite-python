from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProFormaCashFlowsItemFlags")


@_attrs_define
class ProFormaCashFlowsItemFlags:
    """
    Attributes:
        backend (Union[Unset, bool]):  Default: False.
        debt (Union[Unset, bool]):  Default: False.
    """

    backend: Union[Unset, bool] = False
    debt: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backend = self.backend

        debt = self.debt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backend is not UNSET:
            field_dict["backend"] = backend
        if debt is not UNSET:
            field_dict["debt"] = debt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backend = d.pop("backend", UNSET)

        debt = d.pop("debt", UNSET)

        pro_forma_cash_flows_item_flags = cls(
            backend=backend,
            debt=debt,
        )

        pro_forma_cash_flows_item_flags.additional_properties = d
        return pro_forma_cash_flows_item_flags

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
