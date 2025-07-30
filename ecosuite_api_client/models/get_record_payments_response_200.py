from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record import Record
    from ..models.record_payment_details import RecordPaymentDetails


T = TypeVar("T", bound="GetRecordPaymentsResponse200")


@_attrs_define
class GetRecordPaymentsResponse200:
    """
    Attributes:
        record (Union[Unset, Record]): Refer to the /schemas/record endpoint for the full JSON Schema definition
        payment_details (Union[Unset, list['RecordPaymentDetails']]):
    """

    record: Union[Unset, "Record"] = UNSET
    payment_details: Union[Unset, list["RecordPaymentDetails"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

        payment_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.payment_details, Unset):
            payment_details = []
            for payment_details_item_data in self.payment_details:
                payment_details_item = payment_details_item_data.to_dict()
                payment_details.append(payment_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record is not UNSET:
            field_dict["record"] = record
        if payment_details is not UNSET:
            field_dict["paymentDetails"] = payment_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record import Record
        from ..models.record_payment_details import RecordPaymentDetails

        d = dict(src_dict)
        _record = d.pop("record", UNSET)
        record: Union[Unset, Record]
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = Record.from_dict(_record)

        payment_details = []
        _payment_details = d.pop("paymentDetails", UNSET)
        for payment_details_item_data in _payment_details or []:
            payment_details_item = RecordPaymentDetails.from_dict(payment_details_item_data)

            payment_details.append(payment_details_item)

        get_record_payments_response_200 = cls(
            record=record,
            payment_details=payment_details,
        )

        get_record_payments_response_200.additional_properties = d
        return get_record_payments_response_200

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
