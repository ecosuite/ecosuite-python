from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.solar_network_ssh_session import SolarNetworkSshSession
    from ..models.start_ssh_session_response_200_data import StartSshSessionResponse200Data


T = TypeVar("T", bound="StartSshSessionResponse200")


@_attrs_define
class StartSshSessionResponse200:
    """
    Attributes:
        session (Union[Unset, SolarNetworkSshSession]):
        data (Union[Unset, StartSshSessionResponse200Data]):
        web_socket_url (Union[Unset, str]):
        solar_node_proxy_url (Union[Unset, str]):
        started (Union[Unset, bool]):
    """

    session: Union[Unset, "SolarNetworkSshSession"] = UNSET
    data: Union[Unset, "StartSshSessionResponse200Data"] = UNSET
    web_socket_url: Union[Unset, str] = UNSET
    solar_node_proxy_url: Union[Unset, str] = UNSET
    started: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session, Unset):
            session = self.session.to_dict()

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        web_socket_url = self.web_socket_url

        solar_node_proxy_url = self.solar_node_proxy_url

        started = self.started

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session is not UNSET:
            field_dict["session"] = session
        if data is not UNSET:
            field_dict["data"] = data
        if web_socket_url is not UNSET:
            field_dict["webSocketUrl"] = web_socket_url
        if solar_node_proxy_url is not UNSET:
            field_dict["solarNodeProxyUrl"] = solar_node_proxy_url
        if started is not UNSET:
            field_dict["started"] = started

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.solar_network_ssh_session import SolarNetworkSshSession
        from ..models.start_ssh_session_response_200_data import StartSshSessionResponse200Data

        d = src_dict.copy()
        _session = d.pop("session", UNSET)
        session: Union[Unset, SolarNetworkSshSession]
        if isinstance(_session, Unset):
            session = UNSET
        else:
            session = SolarNetworkSshSession.from_dict(_session)

        _data = d.pop("data", UNSET)
        data: Union[Unset, StartSshSessionResponse200Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = StartSshSessionResponse200Data.from_dict(_data)

        web_socket_url = d.pop("webSocketUrl", UNSET)

        solar_node_proxy_url = d.pop("solarNodeProxyUrl", UNSET)

        started = d.pop("started", UNSET)

        start_ssh_session_response_200 = cls(
            session=session,
            data=data,
            web_socket_url=web_socket_url,
            solar_node_proxy_url=solar_node_proxy_url,
            started=started,
        )

        start_ssh_session_response_200.additional_properties = d
        return start_ssh_session_response_200

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