from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.finance_category import FinanceCategory


T = TypeVar("T", bound="GetFinanceCategoriesResponse200Categories")


@_attrs_define
class GetFinanceCategoriesResponse200Categories:
    """Finance category keyed by category name"""

    additional_properties: Dict[str, "FinanceCategory"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.finance_category import FinanceCategory

        d = src_dict.copy()
        get_finance_categories_response_200_categories = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FinanceCategory.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_finance_categories_response_200_categories.additional_properties = additional_properties
        return get_finance_categories_response_200_categories

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "FinanceCategory":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "FinanceCategory") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
