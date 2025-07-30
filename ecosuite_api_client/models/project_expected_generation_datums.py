from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_expected_generation_datums_aggregated_totals import (
        ProjectExpectedGenerationDatumsAggregatedTotals,
    )
    from ..models.project_expected_generation_datums_sites import ProjectExpectedGenerationDatumsSites


T = TypeVar("T", bound="ProjectExpectedGenerationDatums")


@_attrs_define
class ProjectExpectedGenerationDatums:
    """
    Attributes:
        expected_generation (Union[Unset, float]):
        irradiance_hours (Union[Unset, float]):
        aggregated_totals (Union[Unset, ProjectExpectedGenerationDatumsAggregatedTotals]): Keyed by datum date
        sites (Union[Unset, ProjectExpectedGenerationDatumsSites]): Keyed by Site ID
    """

    expected_generation: Union[Unset, float] = UNSET
    irradiance_hours: Union[Unset, float] = UNSET
    aggregated_totals: Union[Unset, "ProjectExpectedGenerationDatumsAggregatedTotals"] = UNSET
    sites: Union[Unset, "ProjectExpectedGenerationDatumsSites"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_generation = self.expected_generation

        irradiance_hours = self.irradiance_hours

        aggregated_totals: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.aggregated_totals, Unset):
            aggregated_totals = self.aggregated_totals.to_dict()

        sites: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expected_generation is not UNSET:
            field_dict["expectedGeneration"] = expected_generation
        if irradiance_hours is not UNSET:
            field_dict["irradianceHours"] = irradiance_hours
        if aggregated_totals is not UNSET:
            field_dict["aggregatedTotals"] = aggregated_totals
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_expected_generation_datums_aggregated_totals import (
            ProjectExpectedGenerationDatumsAggregatedTotals,
        )
        from ..models.project_expected_generation_datums_sites import ProjectExpectedGenerationDatumsSites

        d = dict(src_dict)
        expected_generation = d.pop("expectedGeneration", UNSET)

        irradiance_hours = d.pop("irradianceHours", UNSET)

        _aggregated_totals = d.pop("aggregatedTotals", UNSET)
        aggregated_totals: Union[Unset, ProjectExpectedGenerationDatumsAggregatedTotals]
        if isinstance(_aggregated_totals, Unset):
            aggregated_totals = UNSET
        else:
            aggregated_totals = ProjectExpectedGenerationDatumsAggregatedTotals.from_dict(_aggregated_totals)

        _sites = d.pop("sites", UNSET)
        sites: Union[Unset, ProjectExpectedGenerationDatumsSites]
        if isinstance(_sites, Unset):
            sites = UNSET
        else:
            sites = ProjectExpectedGenerationDatumsSites.from_dict(_sites)

        project_expected_generation_datums = cls(
            expected_generation=expected_generation,
            irradiance_hours=irradiance_hours,
            aggregated_totals=aggregated_totals,
            sites=sites,
        )

        project_expected_generation_datums.additional_properties = d
        return project_expected_generation_datums

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
