from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_billing import ProjectBilling


T = TypeVar("T", bound="GetProjectBillingResponse200")


@_attrs_define
class GetProjectBillingResponse200:
    """
    Attributes:
        line_items (Union[Unset, List['ProjectBilling']]):
        month (Union[Unset, str]): In the format: YYYY-MM
    """

    line_items: Union[Unset, List["ProjectBilling"]] = UNSET
    month: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        month = self.month

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_items is not UNSET:
            field_dict["lineItems"] = line_items
        if month is not UNSET:
            field_dict["month"] = month

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_billing import ProjectBilling

        d = src_dict.copy()
        line_items = []
        _line_items = d.pop("lineItems", UNSET)
        for line_items_item_data in _line_items or []:
            line_items_item = ProjectBilling.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        month = d.pop("month", UNSET)

        get_project_billing_response_200 = cls(
            line_items=line_items,
            month=month,
        )

        get_project_billing_response_200.additional_properties = d
        return get_project_billing_response_200

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
