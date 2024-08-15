from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.finance_category_categories import FinanceCategoryCategories


T = TypeVar("T", bound="FinanceCategory")


@_attrs_define
class FinanceCategory:
    """
    Attributes:
        name (Union[Unset, str]):
        categories (Union[Unset, FinanceCategoryCategories]): Finance sub category keyed by sub category name
    """

    name: Union[Unset, str] = UNSET
    categories: Union[Unset, "FinanceCategoryCategories"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.finance_category_categories import FinanceCategoryCategories

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _categories = d.pop("categories", UNSET)
        categories: Union[Unset, FinanceCategoryCategories]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = FinanceCategoryCategories.from_dict(_categories)

        finance_category = cls(
            name=name,
            categories=categories,
        )

        finance_category.additional_properties = d
        return finance_category

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
