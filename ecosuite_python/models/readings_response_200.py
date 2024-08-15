from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_ import Range
    from ..models.readings_response_200_projects import ReadingsResponse200Projects


T = TypeVar("T", bound="ReadingsResponse200")


@_attrs_define
class ReadingsResponse200:
    """
    Attributes:
        projects (Union[Unset, ReadingsResponse200Projects]): Keyed by Project ID, lists the readings for each project
        range_ (Union[Unset, Range]):
        generation (Union[Unset, float]):
        consumption (Union[Unset, float]):
        storage (Union[Unset, float]):
        export (Union[Unset, float]):
        avoided_emissions (Union[Unset, float]):
        emissions (Union[Unset, float]):
    """

    projects: Union[Unset, "ReadingsResponse200Projects"] = UNSET
    range_: Union[Unset, "Range"] = UNSET
    generation: Union[Unset, float] = UNSET
    consumption: Union[Unset, float] = UNSET
    storage: Union[Unset, float] = UNSET
    export: Union[Unset, float] = UNSET
    avoided_emissions: Union[Unset, float] = UNSET
    emissions: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        projects: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects.to_dict()

        range_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        generation = self.generation

        consumption = self.consumption

        storage = self.storage

        export = self.export

        avoided_emissions = self.avoided_emissions

        emissions = self.emissions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projects is not UNSET:
            field_dict["projects"] = projects
        if range_ is not UNSET:
            field_dict["range"] = range_
        if generation is not UNSET:
            field_dict["generation"] = generation
        if consumption is not UNSET:
            field_dict["consumption"] = consumption
        if storage is not UNSET:
            field_dict["storage"] = storage
        if export is not UNSET:
            field_dict["export"] = export
        if avoided_emissions is not UNSET:
            field_dict["avoidedEmissions"] = avoided_emissions
        if emissions is not UNSET:
            field_dict["emissions"] = emissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.range_ import Range
        from ..models.readings_response_200_projects import ReadingsResponse200Projects

        d = src_dict.copy()
        _projects = d.pop("projects", UNSET)
        projects: Union[Unset, ReadingsResponse200Projects]
        if isinstance(_projects, Unset):
            projects = UNSET
        else:
            projects = ReadingsResponse200Projects.from_dict(_projects)

        _range_ = d.pop("range", UNSET)
        range_: Union[Unset, Range]
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)

        generation = d.pop("generation", UNSET)

        consumption = d.pop("consumption", UNSET)

        storage = d.pop("storage", UNSET)

        export = d.pop("export", UNSET)

        avoided_emissions = d.pop("avoidedEmissions", UNSET)

        emissions = d.pop("emissions", UNSET)

        readings_response_200 = cls(
            projects=projects,
            range_=range_,
            generation=generation,
            consumption=consumption,
            storage=storage,
            export=export,
            avoided_emissions=avoided_emissions,
            emissions=emissions,
        )

        readings_response_200.additional_properties = d
        return readings_response_200

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
