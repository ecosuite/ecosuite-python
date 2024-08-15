from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.energy_node_status import EnergyNodeStatus
    from ..models.energy_status_sites import EnergyStatusSites


T = TypeVar("T", bound="EnergyStatus")


@_attrs_define
class EnergyStatus:
    """
    Attributes:
        code (Union[Unset, str]):
        name (Union[Unset, str]):
        sites (Union[Unset, EnergyStatusSites]): Keyed by Site ID
        nodes_satus (Union[Unset, List['EnergyNodeStatus']]):
        status (Union[Unset, str]):
    """

    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    sites: Union[Unset, "EnergyStatusSites"] = UNSET
    nodes_satus: Union[Unset, List["EnergyNodeStatus"]] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        name = self.name

        sites: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites.to_dict()

        nodes_satus: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nodes_satus, Unset):
            nodes_satus = []
            for nodes_satus_item_data in self.nodes_satus:
                nodes_satus_item = nodes_satus_item_data.to_dict()
                nodes_satus.append(nodes_satus_item)

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if sites is not UNSET:
            field_dict["sites"] = sites
        if nodes_satus is not UNSET:
            field_dict["nodesSatus"] = nodes_satus
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.energy_node_status import EnergyNodeStatus
        from ..models.energy_status_sites import EnergyStatusSites

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        _sites = d.pop("sites", UNSET)
        sites: Union[Unset, EnergyStatusSites]
        if isinstance(_sites, Unset):
            sites = UNSET
        else:
            sites = EnergyStatusSites.from_dict(_sites)

        nodes_satus = []
        _nodes_satus = d.pop("nodesSatus", UNSET)
        for nodes_satus_item_data in _nodes_satus or []:
            nodes_satus_item = EnergyNodeStatus.from_dict(nodes_satus_item_data)

            nodes_satus.append(nodes_satus_item)

        status = d.pop("status", UNSET)

        energy_status = cls(
            code=code,
            name=name,
            sites=sites,
            nodes_satus=nodes_satus,
            status=status,
        )

        energy_status.additional_properties = d
        return energy_status

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
