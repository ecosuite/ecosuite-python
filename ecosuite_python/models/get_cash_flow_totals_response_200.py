from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_cash_flow_totals_response_200_project_totals import GetCashFlowTotalsResponse200ProjectTotals


T = TypeVar("T", bound="GetCashFlowTotalsResponse200")


@_attrs_define
class GetCashFlowTotalsResponse200:
    """
    Attributes:
        project_totals (Union[Unset, GetCashFlowTotalsResponse200ProjectTotals]): Cash Flows keyed by project ID
    """

    project_totals: Union[Unset, "GetCashFlowTotalsResponse200ProjectTotals"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_totals, Unset):
            project_totals = self.project_totals.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_totals is not UNSET:
            field_dict["projectTotals"] = project_totals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_cash_flow_totals_response_200_project_totals import GetCashFlowTotalsResponse200ProjectTotals

        d = src_dict.copy()
        _project_totals = d.pop("projectTotals", UNSET)
        project_totals: Union[Unset, GetCashFlowTotalsResponse200ProjectTotals]
        if isinstance(_project_totals, Unset):
            project_totals = UNSET
        else:
            project_totals = GetCashFlowTotalsResponse200ProjectTotals.from_dict(_project_totals)

        get_cash_flow_totals_response_200 = cls(
            project_totals=project_totals,
        )

        get_cash_flow_totals_response_200.additional_properties = d
        return get_cash_flow_totals_response_200

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
