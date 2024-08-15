from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rfi_stored import RFIStored


T = TypeVar("T", bound="GetAllRFIVersionsResponse200")


@_attrs_define
class GetAllRFIVersionsResponse200:
    """
    Attributes:
        rfi_versions (Union[Unset, List['RFIStored']]):
    """

    rfi_versions: Union[Unset, List["RFIStored"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rfi_versions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rfi_versions, Unset):
            rfi_versions = []
            for rfi_versions_item_data in self.rfi_versions:
                rfi_versions_item = rfi_versions_item_data.to_dict()
                rfi_versions.append(rfi_versions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rfi_versions is not UNSET:
            field_dict["rfiVersions"] = rfi_versions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rfi_stored import RFIStored

        d = src_dict.copy()
        rfi_versions = []
        _rfi_versions = d.pop("rfiVersions", UNSET)
        for rfi_versions_item_data in _rfi_versions or []:
            rfi_versions_item = RFIStored.from_dict(rfi_versions_item_data)

            rfi_versions.append(rfi_versions_item)

        get_all_rfi_versions_response_200 = cls(
            rfi_versions=rfi_versions,
        )

        get_all_rfi_versions_response_200.additional_properties = d
        return get_all_rfi_versions_response_200

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
