from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_cash_flow_total import ProjectCashFlowTotal


T = TypeVar("T", bound="GetCashFlowTotalsResponse200ProjectTotals")


@_attrs_define
class GetCashFlowTotalsResponse200ProjectTotals:
    """Cash Flows keyed by project ID"""

    additional_properties: Dict[str, "ProjectCashFlowTotal"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_cash_flow_total import ProjectCashFlowTotal

        d = src_dict.copy()
        get_cash_flow_totals_response_200_project_totals = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ProjectCashFlowTotal.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_cash_flow_totals_response_200_project_totals.additional_properties = additional_properties
        return get_cash_flow_totals_response_200_project_totals

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ProjectCashFlowTotal":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ProjectCashFlowTotal") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
