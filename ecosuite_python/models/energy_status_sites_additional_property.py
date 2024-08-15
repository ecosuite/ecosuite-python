from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.energy_node_status import EnergyNodeStatus
    from ..models.energy_status_sites_additional_property_systems import EnergyStatusSitesAdditionalPropertySystems


T = TypeVar("T", bound="EnergyStatusSitesAdditionalProperty")


@_attrs_define
class EnergyStatusSitesAdditionalProperty:
    """
    Attributes:
        code (Union[Unset, str]):
        name (Union[Unset, str]):
        systems (Union[Unset, EnergyStatusSitesAdditionalPropertySystems]): Keyed by System ID
        status (Union[Unset, str]):
        nodes_satus (Union[Unset, List['EnergyNodeStatus']]):
    """

    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    systems: Union[Unset, "EnergyStatusSitesAdditionalPropertySystems"] = UNSET
    status: Union[Unset, str] = UNSET
    nodes_satus: Union[Unset, List["EnergyNodeStatus"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        name = self.name

        systems: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.systems, Unset):
            systems = self.systems.to_dict()

        status = self.status

        nodes_satus: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nodes_satus, Unset):
            nodes_satus = []
            for nodes_satus_item_data in self.nodes_satus:
                nodes_satus_item = nodes_satus_item_data.to_dict()
                nodes_satus.append(nodes_satus_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if systems is not UNSET:
            field_dict["systems"] = systems
        if status is not UNSET:
            field_dict["status"] = status
        if nodes_satus is not UNSET:
            field_dict["nodesSatus"] = nodes_satus

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.energy_node_status import EnergyNodeStatus
        from ..models.energy_status_sites_additional_property_systems import EnergyStatusSitesAdditionalPropertySystems

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        _systems = d.pop("systems", UNSET)
        systems: Union[Unset, EnergyStatusSitesAdditionalPropertySystems]
        if isinstance(_systems, Unset):
            systems = UNSET
        else:
            systems = EnergyStatusSitesAdditionalPropertySystems.from_dict(_systems)

        status = d.pop("status", UNSET)

        nodes_satus = []
        _nodes_satus = d.pop("nodesSatus", UNSET)
        for nodes_satus_item_data in _nodes_satus or []:
            nodes_satus_item = EnergyNodeStatus.from_dict(nodes_satus_item_data)

            nodes_satus.append(nodes_satus_item)

        energy_status_sites_additional_property = cls(
            code=code,
            name=name,
            systems=systems,
            status=status,
            nodes_satus=nodes_satus,
        )

        energy_status_sites_additional_property.additional_properties = d
        return energy_status_sites_additional_property

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
