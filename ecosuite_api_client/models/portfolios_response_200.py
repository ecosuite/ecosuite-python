from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project import Project


T = TypeVar("T", bound="PortfoliosResponse200")


@_attrs_define
class PortfoliosResponse200:
    """
    Attributes:
        portfolios (Union[Unset, list['Project']]):
    """

    portfolios: Union[Unset, list["Project"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        portfolios: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.portfolios, Unset):
            portfolios = []
            for portfolios_item_data in self.portfolios:
                portfolios_item = portfolios_item_data.to_dict()
                portfolios.append(portfolios_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portfolios is not UNSET:
            field_dict["portfolios"] = portfolios

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project import Project

        d = dict(src_dict)
        portfolios = []
        _portfolios = d.pop("portfolios", UNSET)
        for portfolios_item_data in _portfolios or []:
            portfolios_item = Project.from_dict(portfolios_item_data)

            portfolios.append(portfolios_item)

        portfolios_response_200 = cls(
            portfolios=portfolios,
        )

        portfolios_response_200.additional_properties = d
        return portfolios_response_200

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
