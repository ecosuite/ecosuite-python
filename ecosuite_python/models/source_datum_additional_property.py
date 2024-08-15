from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceDatumAdditionalProperty")


@_attrs_define
class SourceDatumAdditionalProperty:
    """
    Attributes:
        reading (Union[Unset, float]):
        peak_reading (Union[Unset, float]):
    """

    reading: Union[Unset, float] = UNSET
    peak_reading: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reading = self.reading

        peak_reading = self.peak_reading

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reading is not UNSET:
            field_dict["reading"] = reading
        if peak_reading is not UNSET:
            field_dict["peakReading"] = peak_reading

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reading = d.pop("reading", UNSET)

        peak_reading = d.pop("peakReading", UNSET)

        source_datum_additional_property = cls(
            reading=reading,
            peak_reading=peak_reading,
        )

        source_datum_additional_property.additional_properties = d
        return source_datum_additional_property

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
