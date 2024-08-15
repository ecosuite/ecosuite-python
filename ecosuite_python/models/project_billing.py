from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectBilling")


@_attrs_define
class ProjectBilling:
    """
    Attributes:
        record_id (Union[Unset, str]):
        path (Union[Unset, str]):
        name (Union[Unset, str]):
        frequency (Union[Unset, str]):
        payment_terms (Union[Unset, int]):
        payment_due (Union[Unset, bool]):
    """

    record_id: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    frequency: Union[Unset, str] = UNSET
    payment_terms: Union[Unset, int] = UNSET
    payment_due: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        record_id = self.record_id

        path = self.path

        name = self.name

        frequency = self.frequency

        payment_terms = self.payment_terms

        payment_due = self.payment_due

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if path is not UNSET:
            field_dict["path"] = path
        if name is not UNSET:
            field_dict["name"] = name
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if payment_terms is not UNSET:
            field_dict["paymentTerms"] = payment_terms
        if payment_due is not UNSET:
            field_dict["paymentDue"] = payment_due

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        record_id = d.pop("recordId", UNSET)

        path = d.pop("path", UNSET)

        name = d.pop("name", UNSET)

        frequency = d.pop("frequency", UNSET)

        payment_terms = d.pop("paymentTerms", UNSET)

        payment_due = d.pop("paymentDue", UNSET)

        project_billing = cls(
            record_id=record_id,
            path=path,
            name=name,
            frequency=frequency,
            payment_terms=payment_terms,
            payment_due=payment_due,
        )

        project_billing.additional_properties = d
        return project_billing

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
