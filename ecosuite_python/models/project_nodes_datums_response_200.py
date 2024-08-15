from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_nodes_datums_response_200_aggregation import ProjectNodesDatumsResponse200Aggregation
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_ import Range
    from ..models.solar_network_datum import SolarNetworkDatum


T = TypeVar("T", bound="ProjectNodesDatumsResponse200")


@_attrs_define
class ProjectNodesDatumsResponse200:
    """
    Attributes:
        data (Union[Unset, List['SolarNetworkDatum']]):
        range_ (Union[Unset, Range]):
        aggregation (Union[Unset, ProjectNodesDatumsResponse200Aggregation]):
        source_ids (Union[Unset, str]):
    """

    data: Union[Unset, List["SolarNetworkDatum"]] = UNSET
    range_: Union[Unset, "Range"] = UNSET
    aggregation: Union[Unset, ProjectNodesDatumsResponse200Aggregation] = UNSET
    source_ids: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        range_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        aggregation: Union[Unset, str] = UNSET
        if not isinstance(self.aggregation, Unset):
            aggregation = self.aggregation.value

        source_ids = self.source_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if range_ is not UNSET:
            field_dict["range"] = range_
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if source_ids is not UNSET:
            field_dict["sourceIds"] = source_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.range_ import Range
        from ..models.solar_network_datum import SolarNetworkDatum

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = SolarNetworkDatum.from_dict(data_item_data)

            data.append(data_item)

        _range_ = d.pop("range", UNSET)
        range_: Union[Unset, Range]
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)

        _aggregation = d.pop("aggregation", UNSET)
        aggregation: Union[Unset, ProjectNodesDatumsResponse200Aggregation]
        if isinstance(_aggregation, Unset):
            aggregation = UNSET
        else:
            aggregation = ProjectNodesDatumsResponse200Aggregation(_aggregation)

        source_ids = d.pop("sourceIds", UNSET)

        project_nodes_datums_response_200 = cls(
            data=data,
            range_=range_,
            aggregation=aggregation,
            source_ids=source_ids,
        )

        project_nodes_datums_response_200.additional_properties = d
        return project_nodes_datums_response_200

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
