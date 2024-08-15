from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_request import ServiceRequest


T = TypeVar("T", bound="GetServiceRequestResponse200")


@_attrs_define
class GetServiceRequestResponse200:
    """
    Attributes:
        service_request (Union[Unset, ServiceRequest]): Refer to the /schemas/service-request endpoint for the full JSON
            Schema definition
    """

    service_request: Union[Unset, "ServiceRequest"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service_request, Unset):
            service_request = self.service_request.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_request is not UNSET:
            field_dict["serviceRequest"] = service_request

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_request import ServiceRequest

        d = src_dict.copy()
        _service_request = d.pop("serviceRequest", UNSET)
        service_request: Union[Unset, ServiceRequest]
        if isinstance(_service_request, Unset):
            service_request = UNSET
        else:
            service_request = ServiceRequest.from_dict(_service_request)

        get_service_request_response_200 = cls(
            service_request=service_request,
        )

        get_service_request_response_200.additional_properties = d
        return get_service_request_response_200

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
