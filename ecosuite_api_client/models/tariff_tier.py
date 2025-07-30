from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tariff_tier_unit import TariffTierUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="TariffTier")


@_attrs_define
class TariffTier:
    """
    Attributes:
        rate (float):
        unit (TariffTierUnit):  Default: TariffTierUnit.KWH.
        max_ (Union[Unset, float]):
    """

    rate: float
    unit: TariffTierUnit = TariffTierUnit.KWH
    max_: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        unit = self.unit.value

        max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rate": rate,
                "unit": unit,
            }
        )
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate")

        unit = TariffTierUnit(d.pop("unit"))

        max_ = d.pop("max", UNSET)

        tariff_tier = cls(
            rate=rate,
            unit=unit,
            max_=max_,
        )

        tariff_tier.additional_properties = d
        return tariff_tier

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
