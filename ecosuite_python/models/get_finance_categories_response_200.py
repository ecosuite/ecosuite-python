from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_finance_categories_response_200_categories import GetFinanceCategoriesResponse200Categories


T = TypeVar("T", bound="GetFinanceCategoriesResponse200")


@_attrs_define
class GetFinanceCategoriesResponse200:
    """
    Attributes:
        categories (Union[Unset, GetFinanceCategoriesResponse200Categories]): Finance category keyed by category name
        month (Union[Unset, str]): In the format: YYYY-MM
    """

    categories: Union[Unset, "GetFinanceCategoriesResponse200Categories"] = UNSET
    month: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        month = self.month

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if month is not UNSET:
            field_dict["month"] = month

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_finance_categories_response_200_categories import GetFinanceCategoriesResponse200Categories

        d = src_dict.copy()
        _categories = d.pop("categories", UNSET)
        categories: Union[Unset, GetFinanceCategoriesResponse200Categories]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = GetFinanceCategoriesResponse200Categories.from_dict(_categories)

        month = d.pop("month", UNSET)

        get_finance_categories_response_200 = cls(
            categories=categories,
            month=month,
        )

        get_finance_categories_response_200.additional_properties = d
        return get_finance_categories_response_200

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
