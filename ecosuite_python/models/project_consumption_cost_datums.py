from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_consumption_cost_datums_consumption_cost import ProjectConsumptionCostDatumsConsumptionCost


T = TypeVar("T", bound="ProjectConsumptionCostDatums")


@_attrs_define
class ProjectConsumptionCostDatums:
    """
    Attributes:
        consumption_cost (Union[Unset, ProjectConsumptionCostDatumsConsumptionCost]):
    """

    consumption_cost: Union[Unset, "ProjectConsumptionCostDatumsConsumptionCost"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        consumption_cost: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.consumption_cost, Unset):
            consumption_cost = self.consumption_cost.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consumption_cost is not UNSET:
            field_dict["consumptionCost"] = consumption_cost

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_consumption_cost_datums_consumption_cost import (
            ProjectConsumptionCostDatumsConsumptionCost,
        )

        d = src_dict.copy()
        _consumption_cost = d.pop("consumptionCost", UNSET)
        consumption_cost: Union[Unset, ProjectConsumptionCostDatumsConsumptionCost]
        if isinstance(_consumption_cost, Unset):
            consumption_cost = UNSET
        else:
            consumption_cost = ProjectConsumptionCostDatumsConsumptionCost.from_dict(_consumption_cost)

        project_consumption_cost_datums = cls(
            consumption_cost=consumption_cost,
        )

        project_consumption_cost_datums.additional_properties = d
        return project_consumption_cost_datums

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
