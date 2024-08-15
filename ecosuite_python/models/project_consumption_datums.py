from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_consumption_datums_aggregated_totals import ProjectConsumptionDatumsAggregatedTotals
    from ..models.project_consumption_datums_sites import ProjectConsumptionDatumsSites


T = TypeVar("T", bound="ProjectConsumptionDatums")


@_attrs_define
class ProjectConsumptionDatums:
    """
    Attributes:
        aggregated_totals (Union[Unset, ProjectConsumptionDatumsAggregatedTotals]): Keyed by datum date
        sites (Union[Unset, ProjectConsumptionDatumsSites]): Keyed by Site ID
    """

    aggregated_totals: Union[Unset, "ProjectConsumptionDatumsAggregatedTotals"] = UNSET
    sites: Union[Unset, "ProjectConsumptionDatumsSites"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aggregated_totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregated_totals, Unset):
            aggregated_totals = self.aggregated_totals.to_dict()

        sites: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregated_totals is not UNSET:
            field_dict["aggregatedTotals"] = aggregated_totals
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_consumption_datums_aggregated_totals import ProjectConsumptionDatumsAggregatedTotals
        from ..models.project_consumption_datums_sites import ProjectConsumptionDatumsSites

        d = src_dict.copy()
        _aggregated_totals = d.pop("aggregatedTotals", UNSET)
        aggregated_totals: Union[Unset, ProjectConsumptionDatumsAggregatedTotals]
        if isinstance(_aggregated_totals, Unset):
            aggregated_totals = UNSET
        else:
            aggregated_totals = ProjectConsumptionDatumsAggregatedTotals.from_dict(_aggregated_totals)

        _sites = d.pop("sites", UNSET)
        sites: Union[Unset, ProjectConsumptionDatumsSites]
        if isinstance(_sites, Unset):
            sites = UNSET
        else:
            sites = ProjectConsumptionDatumsSites.from_dict(_sites)

        project_consumption_datums = cls(
            aggregated_totals=aggregated_totals,
            sites=sites,
        )

        project_consumption_datums.additional_properties = d
        return project_consumption_datums

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
