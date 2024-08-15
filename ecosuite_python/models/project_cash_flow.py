from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_cash_flow_categories import ProjectCashFlowCategories


T = TypeVar("T", bound="ProjectCashFlow")


@_attrs_define
class ProjectCashFlow:
    """
    Attributes:
        currency (Union[Unset, str]):
        categories (Union[Unset, ProjectCashFlowCategories]): Category cash flows keyed by category name
    """

    currency: Union[Unset, str] = UNSET
    categories: Union[Unset, "ProjectCashFlowCategories"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency

        categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_cash_flow_categories import ProjectCashFlowCategories

        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        _categories = d.pop("categories", UNSET)
        categories: Union[Unset, ProjectCashFlowCategories]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = ProjectCashFlowCategories.from_dict(_categories)

        project_cash_flow = cls(
            currency=currency,
            categories=categories,
        )

        project_cash_flow.additional_properties = d
        return project_cash_flow

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
