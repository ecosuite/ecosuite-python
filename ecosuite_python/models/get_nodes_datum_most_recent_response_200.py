from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.solar_network_datum import SolarNetworkDatum


T = TypeVar("T", bound="GetNodesDatumMostRecentResponse200")


@_attrs_define
class GetNodesDatumMostRecentResponse200:
    """
    Attributes:
        datums (Union[Unset, List['SolarNetworkDatum']]):
    """

    datums: Union[Unset, List["SolarNetworkDatum"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        datums: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.datums, Unset):
            datums = []
            for datums_item_data in self.datums:
                datums_item = datums_item_data.to_dict()
                datums.append(datums_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datums is not UNSET:
            field_dict["datums"] = datums

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.solar_network_datum import SolarNetworkDatum

        d = src_dict.copy()
        datums = []
        _datums = d.pop("datums", UNSET)
        for datums_item_data in _datums or []:
            datums_item = SolarNetworkDatum.from_dict(datums_item_data)

            datums.append(datums_item)

        get_nodes_datum_most_recent_response_200 = cls(
            datums=datums,
        )

        get_nodes_datum_most_recent_response_200.additional_properties = d
        return get_nodes_datum_most_recent_response_200

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
