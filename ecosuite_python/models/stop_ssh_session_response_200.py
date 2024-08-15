from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.solar_network_ssh_session import SolarNetworkSshSession


T = TypeVar("T", bound="StopSshSessionResponse200")


@_attrs_define
class StopSshSessionResponse200:
    """
    Attributes:
        session (Union[Unset, SolarNetworkSshSession]):
    """

    session: Union[Unset, "SolarNetworkSshSession"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session, Unset):
            session = self.session.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session is not UNSET:
            field_dict["session"] = session

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.solar_network_ssh_session import SolarNetworkSshSession

        d = src_dict.copy()
        _session = d.pop("session", UNSET)
        session: Union[Unset, SolarNetworkSshSession]
        if isinstance(_session, Unset):
            session = UNSET
        else:
            session = SolarNetworkSshSession.from_dict(_session)

        stop_ssh_session_response_200 = cls(
            session=session,
        )

        stop_ssh_session_response_200.additional_properties = d
        return stop_ssh_session_response_200

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
