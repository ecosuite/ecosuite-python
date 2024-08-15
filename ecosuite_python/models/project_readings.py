from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_readings_sites import ProjectReadingsSites
    from ..models.project_readings_sources import ProjectReadingsSources


T = TypeVar("T", bound="ProjectReadings")


@_attrs_define
class ProjectReadings:
    """
    Attributes:
        generation (Union[Unset, float]):
        consumption (Union[Unset, float]):
        export (Union[Unset, float]):
        storage (Union[Unset, float]):
        irradiance_hours (Union[Unset, float]):
        avoided_emissions (Union[Unset, float]):
        emissions (Union[Unset, float]):
        sources (Union[Unset, ProjectReadingsSources]): Keyed by Source ID
        sites (Union[Unset, ProjectReadingsSites]): Keyed by Site ID
    """

    generation: Union[Unset, float] = UNSET
    consumption: Union[Unset, float] = UNSET
    export: Union[Unset, float] = UNSET
    storage: Union[Unset, float] = UNSET
    irradiance_hours: Union[Unset, float] = UNSET
    avoided_emissions: Union[Unset, float] = UNSET
    emissions: Union[Unset, float] = UNSET
    sources: Union[Unset, "ProjectReadingsSources"] = UNSET
    sites: Union[Unset, "ProjectReadingsSites"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        generation = self.generation

        consumption = self.consumption

        export = self.export

        storage = self.storage

        irradiance_hours = self.irradiance_hours

        avoided_emissions = self.avoided_emissions

        emissions = self.emissions

        sources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources.to_dict()

        sites: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if generation is not UNSET:
            field_dict["generation"] = generation
        if consumption is not UNSET:
            field_dict["consumption"] = consumption
        if export is not UNSET:
            field_dict["export"] = export
        if storage is not UNSET:
            field_dict["storage"] = storage
        if irradiance_hours is not UNSET:
            field_dict["irradianceHours"] = irradiance_hours
        if avoided_emissions is not UNSET:
            field_dict["avoidedEmissions"] = avoided_emissions
        if emissions is not UNSET:
            field_dict["emissions"] = emissions
        if sources is not UNSET:
            field_dict["sources"] = sources
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_readings_sites import ProjectReadingsSites
        from ..models.project_readings_sources import ProjectReadingsSources

        d = src_dict.copy()
        generation = d.pop("generation", UNSET)

        consumption = d.pop("consumption", UNSET)

        export = d.pop("export", UNSET)

        storage = d.pop("storage", UNSET)

        irradiance_hours = d.pop("irradianceHours", UNSET)

        avoided_emissions = d.pop("avoidedEmissions", UNSET)

        emissions = d.pop("emissions", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: Union[Unset, ProjectReadingsSources]
        if isinstance(_sources, Unset):
            sources = UNSET
        else:
            sources = ProjectReadingsSources.from_dict(_sources)

        _sites = d.pop("sites", UNSET)
        sites: Union[Unset, ProjectReadingsSites]
        if isinstance(_sites, Unset):
            sites = UNSET
        else:
            sites = ProjectReadingsSites.from_dict(_sites)

        project_readings = cls(
            generation=generation,
            consumption=consumption,
            export=export,
            storage=storage,
            irradiance_hours=irradiance_hours,
            avoided_emissions=avoided_emissions,
            emissions=emissions,
            sources=sources,
            sites=sites,
        )

        project_readings.additional_properties = d
        return project_readings

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
