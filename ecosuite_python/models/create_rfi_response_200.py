from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rfi_stored import RFIStored


T = TypeVar("T", bound="CreateRFIResponse200")


@_attrs_define
class CreateRFIResponse200:
    """
    Attributes:
        rfi (Union[Unset, RFIStored]):
    """

    rfi: Union[Unset, "RFIStored"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rfi: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rfi, Unset):
            rfi = self.rfi.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rfi is not UNSET:
            field_dict["rfi"] = rfi

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rfi_stored import RFIStored

        d = src_dict.copy()
        _rfi = d.pop("rfi", UNSET)
        rfi: Union[Unset, RFIStored]
        if isinstance(_rfi, Unset):
            rfi = UNSET
        else:
            rfi = RFIStored.from_dict(_rfi)

        create_rfi_response_200 = cls(
            rfi=rfi,
        )

        create_rfi_response_200.additional_properties = d
        return create_rfi_response_200

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
