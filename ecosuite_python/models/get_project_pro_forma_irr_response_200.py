from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pro_forma_irr import ProFormaIRR


T = TypeVar("T", bound="GetProjectProFormaIRRResponse200")


@_attrs_define
class GetProjectProFormaIRRResponse200:
    """
    Attributes:
        data (Union[Unset, ProFormaIRR]):
        month (Union[Unset, str]): In the format: YYYY-MM
    """

    data: Union[Unset, "ProFormaIRR"] = UNSET
    month: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        month = self.month

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if month is not UNSET:
            field_dict["month"] = month

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pro_forma_irr import ProFormaIRR

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, ProFormaIRR]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ProFormaIRR.from_dict(_data)

        month = d.pop("month", UNSET)

        get_project_pro_forma_irr_response_200 = cls(
            data=data,
            month=month,
        )

        get_project_pro_forma_irr_response_200.additional_properties = d
        return get_project_pro_forma_irr_response_200

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
