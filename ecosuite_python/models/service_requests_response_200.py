from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.range_ import Range
    from ..models.service_request import ServiceRequest


T = TypeVar("T", bound="ServiceRequestsResponse200")


@_attrs_define
class ServiceRequestsResponse200:
    """
    Attributes:
        service_requests (Union[Unset, List['ServiceRequest']]):
        range_ (Union[Unset, Range]):
    """

    service_requests: Union[Unset, List["ServiceRequest"]] = UNSET
    range_: Union[Unset, "Range"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_requests: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.service_requests, Unset):
            service_requests = []
            for service_requests_item_data in self.service_requests:
                service_requests_item = service_requests_item_data.to_dict()
                service_requests.append(service_requests_item)

        range_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_requests is not UNSET:
            field_dict["serviceRequests"] = service_requests
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.range_ import Range
        from ..models.service_request import ServiceRequest

        d = src_dict.copy()
        service_requests = []
        _service_requests = d.pop("serviceRequests", UNSET)
        for service_requests_item_data in _service_requests or []:
            service_requests_item = ServiceRequest.from_dict(service_requests_item_data)

            service_requests.append(service_requests_item)

        _range_ = d.pop("range", UNSET)
        range_: Union[Unset, Range]
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)

        service_requests_response_200 = cls(
            service_requests=service_requests,
            range_=range_,
        )

        service_requests_response_200.additional_properties = d
        return service_requests_response_200

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
