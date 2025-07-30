from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceRequestGoogleDocument")


@_attrs_define
class ServiceRequestGoogleDocument:
    """A collection of helpful Google Document specific items.

    Attributes:
        service_request_folder (Union[Unset, str]): A link to the root service request folder. Permission must be
            granted to view the contents.
        uri (Union[Unset, str]): The actual link to the service request.
        data (Union[Unset, str]): A link to download a .pdf of the latest document revision.
    """

    service_request_folder: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_request_folder = self.service_request_folder

        uri = self.uri

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_request_folder is not UNSET:
            field_dict["serviceRequestFolder"] = service_request_folder
        if uri is not UNSET:
            field_dict["uri"] = uri
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_request_folder = d.pop("serviceRequestFolder", UNSET)

        uri = d.pop("uri", UNSET)

        data = d.pop("data", UNSET)

        service_request_google_document = cls(
            service_request_folder=service_request_folder,
            uri=uri,
            data=data,
        )

        service_request_google_document.additional_properties = d
        return service_request_google_document

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
