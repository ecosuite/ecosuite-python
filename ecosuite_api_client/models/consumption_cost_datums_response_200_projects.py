from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_consumption_cost_datums import ProjectConsumptionCostDatums


T = TypeVar("T", bound="ConsumptionCostDatumsResponse200Projects")


@_attrs_define
class ConsumptionCostDatumsResponse200Projects:
    """Keyed by Project ID, lists the datums for each project"""

    additional_properties: dict[str, "ProjectConsumptionCostDatums"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_consumption_cost_datums import ProjectConsumptionCostDatums

        d = dict(src_dict)
        consumption_cost_datums_response_200_projects = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ProjectConsumptionCostDatums.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        consumption_cost_datums_response_200_projects.additional_properties = additional_properties
        return consumption_cost_datums_response_200_projects

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ProjectConsumptionCostDatums":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ProjectConsumptionCostDatums") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
