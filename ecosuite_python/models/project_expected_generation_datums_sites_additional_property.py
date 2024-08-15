from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_expected_generation_datums_sites_additional_property_aggregated_totals import (
        ProjectExpectedGenerationDatumsSitesAdditionalPropertyAggregatedTotals,
    )
    from ..models.project_expected_generation_datums_sites_additional_property_systems import (
        ProjectExpectedGenerationDatumsSitesAdditionalPropertySystems,
    )


T = TypeVar("T", bound="ProjectExpectedGenerationDatumsSitesAdditionalProperty")


@_attrs_define
class ProjectExpectedGenerationDatumsSitesAdditionalProperty:
    """
    Attributes:
        expected_generation (Union[Unset, float]):
        irradiance_hours (Union[Unset, float]):
        aggregated_totals (Union[Unset, ProjectExpectedGenerationDatumsSitesAdditionalPropertyAggregatedTotals]): Keyed
            by datum date
        systems (Union[Unset, ProjectExpectedGenerationDatumsSitesAdditionalPropertySystems]): Keyed by System ID
    """

    expected_generation: Union[Unset, float] = UNSET
    irradiance_hours: Union[Unset, float] = UNSET
    aggregated_totals: Union[Unset, "ProjectExpectedGenerationDatumsSitesAdditionalPropertyAggregatedTotals"] = UNSET
    systems: Union[Unset, "ProjectExpectedGenerationDatumsSitesAdditionalPropertySystems"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expected_generation = self.expected_generation

        irradiance_hours = self.irradiance_hours

        aggregated_totals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aggregated_totals, Unset):
            aggregated_totals = self.aggregated_totals.to_dict()

        systems: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.systems, Unset):
            systems = self.systems.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expected_generation is not UNSET:
            field_dict["expectedGeneration"] = expected_generation
        if irradiance_hours is not UNSET:
            field_dict["irradianceHours"] = irradiance_hours
        if aggregated_totals is not UNSET:
            field_dict["aggregatedTotals"] = aggregated_totals
        if systems is not UNSET:
            field_dict["systems"] = systems

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_expected_generation_datums_sites_additional_property_aggregated_totals import (
            ProjectExpectedGenerationDatumsSitesAdditionalPropertyAggregatedTotals,
        )
        from ..models.project_expected_generation_datums_sites_additional_property_systems import (
            ProjectExpectedGenerationDatumsSitesAdditionalPropertySystems,
        )

        d = src_dict.copy()
        expected_generation = d.pop("expectedGeneration", UNSET)

        irradiance_hours = d.pop("irradianceHours", UNSET)

        _aggregated_totals = d.pop("aggregatedTotals", UNSET)
        aggregated_totals: Union[Unset, ProjectExpectedGenerationDatumsSitesAdditionalPropertyAggregatedTotals]
        if isinstance(_aggregated_totals, Unset):
            aggregated_totals = UNSET
        else:
            aggregated_totals = ProjectExpectedGenerationDatumsSitesAdditionalPropertyAggregatedTotals.from_dict(
                _aggregated_totals
            )

        _systems = d.pop("systems", UNSET)
        systems: Union[Unset, ProjectExpectedGenerationDatumsSitesAdditionalPropertySystems]
        if isinstance(_systems, Unset):
            systems = UNSET
        else:
            systems = ProjectExpectedGenerationDatumsSitesAdditionalPropertySystems.from_dict(_systems)

        project_expected_generation_datums_sites_additional_property = cls(
            expected_generation=expected_generation,
            irradiance_hours=irradiance_hours,
            aggregated_totals=aggregated_totals,
            systems=systems,
        )

        project_expected_generation_datums_sites_additional_property.additional_properties = d
        return project_expected_generation_datums_sites_additional_property

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
