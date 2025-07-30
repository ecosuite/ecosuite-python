from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tariff_flat_demand_charge_includes_flat_demand_rate import TariffFlatDemandChargeIncludesFlatDemandRate
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffFlatDemandCharge")


@_attrs_define
class TariffFlatDemandCharge:
    """
    Attributes:
        enabled (Union[Unset, TariffFlatDemandChargeIncludesFlatDemandRate]):
    """

    enabled: Union[Unset, TariffFlatDemandChargeIncludesFlatDemandRate] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled: Union[Unset, str] = UNSET
        if not isinstance(self.enabled, Unset):
            enabled = self.enabled.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _enabled = d.pop("enabled", UNSET)
        enabled: Union[Unset, TariffFlatDemandChargeIncludesFlatDemandRate]
        if isinstance(_enabled, Unset):
            enabled = UNSET
        else:
            enabled = TariffFlatDemandChargeIncludesFlatDemandRate(_enabled)

        tariff_flat_demand_charge = cls(
            enabled=enabled,
        )

        tariff_flat_demand_charge.additional_properties = d
        return tariff_flat_demand_charge

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
