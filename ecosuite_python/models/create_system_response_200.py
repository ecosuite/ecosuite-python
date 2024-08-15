from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system import System


T = TypeVar("T", bound="CreateSystemResponse200")


@_attrs_define
class CreateSystemResponse200:
    """
    Attributes:
        site (Union[Unset, System]): Refer to the /schemas/system endpoint for the full JSON Schema definition
    """

    site: Union[Unset, "System"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        site: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site is not UNSET:
            field_dict["site"] = site

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.system import System

        d = src_dict.copy()
        _site = d.pop("site", UNSET)
        site: Union[Unset, System]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = System.from_dict(_site)

        create_system_response_200 = cls(
            site=site,
        )

        create_system_response_200.additional_properties = d
        return create_system_response_200

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
