from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SolarNetworkSshSession")


@_attrs_define
class SolarNetworkSshSession:
    """
    Attributes:
        session_id (Union[Unset, str]):
        created (Union[Unset, float]):
        node_id (Union[Unset, float]):
        host (Union[Unset, str]):
        port (Union[Unset, float]):
        reverse_port (Union[Unset, float]):
        start_instruction_id (Union[Unset, float]):
        stop_instruction_id (Union[Unset, float]):
        established (Union[Unset, bool]):
    """

    session_id: Union[Unset, str] = UNSET
    created: Union[Unset, float] = UNSET
    node_id: Union[Unset, float] = UNSET
    host: Union[Unset, str] = UNSET
    port: Union[Unset, float] = UNSET
    reverse_port: Union[Unset, float] = UNSET
    start_instruction_id: Union[Unset, float] = UNSET
    stop_instruction_id: Union[Unset, float] = UNSET
    established: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_id = self.session_id

        created = self.created

        node_id = self.node_id

        host = self.host

        port = self.port

        reverse_port = self.reverse_port

        start_instruction_id = self.start_instruction_id

        stop_instruction_id = self.stop_instruction_id

        established = self.established

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if created is not UNSET:
            field_dict["created"] = created
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if reverse_port is not UNSET:
            field_dict["reversePort"] = reverse_port
        if start_instruction_id is not UNSET:
            field_dict["startInstructionId"] = start_instruction_id
        if stop_instruction_id is not UNSET:
            field_dict["stopInstructionId"] = stop_instruction_id
        if established is not UNSET:
            field_dict["established"] = established

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        session_id = d.pop("sessionId", UNSET)

        created = d.pop("created", UNSET)

        node_id = d.pop("nodeId", UNSET)

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        reverse_port = d.pop("reversePort", UNSET)

        start_instruction_id = d.pop("startInstructionId", UNSET)

        stop_instruction_id = d.pop("stopInstructionId", UNSET)

        established = d.pop("established", UNSET)

        solar_network_ssh_session = cls(
            session_id=session_id,
            created=created,
            node_id=node_id,
            host=host,
            port=port,
            reverse_port=reverse_port,
            start_instruction_id=start_instruction_id,
            stop_instruction_id=stop_instruction_id,
            established=established,
        )

        solar_network_ssh_session.additional_properties = d
        return solar_network_ssh_session

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
