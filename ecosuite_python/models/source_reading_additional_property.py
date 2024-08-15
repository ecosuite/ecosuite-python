from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceReadingAdditionalProperty")


@_attrs_define
class SourceReadingAdditionalProperty:
    """
    Attributes:
        reading (Union[Unset, float]):
        start (Union[Unset, float]):
        end (Union[Unset, float]):
    """

    reading: Union[Unset, float] = UNSET
    start: Union[Unset, float] = UNSET
    end: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reading = self.reading

        start = self.start

        end = self.end

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reading is not UNSET:
            field_dict["reading"] = reading
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reading = d.pop("reading", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        source_reading_additional_property = cls(
            reading=reading,
            start=start,
            end=end,
        )

        source_reading_additional_property.additional_properties = d
        return source_reading_additional_property

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
