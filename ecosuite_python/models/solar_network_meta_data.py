from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.solar_network_meta_data_sources import SolarNetworkMetaDataSources


T = TypeVar("T", bound="SolarNetworkMetaData")


@_attrs_define
class SolarNetworkMetaData:
    """
    Attributes:
        sources (Union[Unset, SolarNetworkMetaDataSources]): Keyed by source ID
    """

    sources: Union[Unset, "SolarNetworkMetaDataSources"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.solar_network_meta_data_sources import SolarNetworkMetaDataSources

        d = src_dict.copy()
        _sources = d.pop("sources", UNSET)
        sources: Union[Unset, SolarNetworkMetaDataSources]
        if isinstance(_sources, Unset):
            sources = UNSET
        else:
            sources = SolarNetworkMetaDataSources.from_dict(_sources)

        solar_network_meta_data = cls(
            sources=sources,
        )

        solar_network_meta_data.additional_properties = d
        return solar_network_meta_data

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
