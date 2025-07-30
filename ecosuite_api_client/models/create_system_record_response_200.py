from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record import Record


T = TypeVar("T", bound="CreateSystemRecordResponse200")


@_attrs_define
class CreateSystemRecordResponse200:
    """
    Attributes:
        record (Union[Unset, Record]): Refer to the /schemas/record endpoint for the full JSON Schema definition
    """

    record: Union[Unset, "Record"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record is not UNSET:
            field_dict["record"] = record

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record import Record

        d = dict(src_dict)
        _record = d.pop("record", UNSET)
        record: Union[Unset, Record]
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = Record.from_dict(_record)

        create_system_record_response_200 = cls(
            record=record,
        )

        create_system_record_response_200.additional_properties = d
        return create_system_record_response_200

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
