from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datum import Datum
    from ..models.project_datums_sites_additional_property_systems import ProjectDatumsSitesAdditionalPropertySystems
    from ..models.source_datum import SourceDatum


T = TypeVar("T", bound="ProjectDatumsSitesAdditionalProperty")


@_attrs_define
class ProjectDatumsSitesAdditionalProperty:
    """
    Attributes:
        code (Union[Unset, str]):
        name (Union[Unset, str]):
        peak_consumption (Union[Unset, float]):
        peak_generation (Union[Unset, float]):
        aggregated_totals (Union[Unset, list['Datum']]):
        sources (Union[Unset, list['SourceDatum']]):
        systems (Union[Unset, ProjectDatumsSitesAdditionalPropertySystems]): Keyed by System ID
    """

    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    peak_consumption: Union[Unset, float] = UNSET
    peak_generation: Union[Unset, float] = UNSET
    aggregated_totals: Union[Unset, list["Datum"]] = UNSET
    sources: Union[Unset, list["SourceDatum"]] = UNSET
    systems: Union[Unset, "ProjectDatumsSitesAdditionalPropertySystems"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        peak_consumption = self.peak_consumption

        peak_generation = self.peak_generation

        aggregated_totals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.aggregated_totals, Unset):
            aggregated_totals = []
            for aggregated_totals_item_data in self.aggregated_totals:
                aggregated_totals_item = aggregated_totals_item_data.to_dict()
                aggregated_totals.append(aggregated_totals_item)

        sources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        systems: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.systems, Unset):
            systems = self.systems.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if peak_consumption is not UNSET:
            field_dict["peakConsumption"] = peak_consumption
        if peak_generation is not UNSET:
            field_dict["peakGeneration"] = peak_generation
        if aggregated_totals is not UNSET:
            field_dict["aggregatedTotals"] = aggregated_totals
        if sources is not UNSET:
            field_dict["sources"] = sources
        if systems is not UNSET:
            field_dict["systems"] = systems

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datum import Datum
        from ..models.project_datums_sites_additional_property_systems import (
            ProjectDatumsSitesAdditionalPropertySystems,
        )
        from ..models.source_datum import SourceDatum

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        peak_consumption = d.pop("peakConsumption", UNSET)

        peak_generation = d.pop("peakGeneration", UNSET)

        aggregated_totals = []
        _aggregated_totals = d.pop("aggregatedTotals", UNSET)
        for aggregated_totals_item_data in _aggregated_totals or []:
            aggregated_totals_item = Datum.from_dict(aggregated_totals_item_data)

            aggregated_totals.append(aggregated_totals_item)

        sources = []
        _sources = d.pop("sources", UNSET)
        for sources_item_data in _sources or []:
            sources_item = SourceDatum.from_dict(sources_item_data)

            sources.append(sources_item)

        _systems = d.pop("systems", UNSET)
        systems: Union[Unset, ProjectDatumsSitesAdditionalPropertySystems]
        if isinstance(_systems, Unset):
            systems = UNSET
        else:
            systems = ProjectDatumsSitesAdditionalPropertySystems.from_dict(_systems)

        project_datums_sites_additional_property = cls(
            code=code,
            name=name,
            peak_consumption=peak_consumption,
            peak_generation=peak_generation,
            aggregated_totals=aggregated_totals,
            sources=sources,
            systems=systems,
        )

        project_datums_sites_additional_property.additional_properties = d
        return project_datums_sites_additional_property

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
