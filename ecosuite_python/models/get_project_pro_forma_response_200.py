from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pro_forma import ProForma


T = TypeVar("T", bound="GetProjectProFormaResponse200")


@_attrs_define
class GetProjectProFormaResponse200:
    """
    Attributes:
        pro_forma (Union[Unset, ProForma]): Refer to the /schemas/pro-forma endpoint for the full JSON Schema definition
    """

    pro_forma: Union[Unset, "ProForma"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pro_forma: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pro_forma, Unset):
            pro_forma = self.pro_forma.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pro_forma is not UNSET:
            field_dict["proForma"] = pro_forma

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pro_forma import ProForma

        d = src_dict.copy()
        _pro_forma = d.pop("proForma", UNSET)
        pro_forma: Union[Unset, ProForma]
        if isinstance(_pro_forma, Unset):
            pro_forma = UNSET
        else:
            pro_forma = ProForma.from_dict(_pro_forma)

        get_project_pro_forma_response_200 = cls(
            pro_forma=pro_forma,
        )

        get_project_pro_forma_response_200.additional_properties = d
        return get_project_pro_forma_response_200

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
