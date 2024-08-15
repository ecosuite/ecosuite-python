from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_completes import AutoCompletes
    from ..models.refinements import Refinements


T = TypeVar("T", bound="RefinementsResponse200")


@_attrs_define
class RefinementsResponse200:
    """
    Attributes:
        refinements (Union[Unset, Refinements]): Keyed by refinement name
        auto_completes (Union[Unset, AutoCompletes]): Keyed by property name
    """

    refinements: Union[Unset, "Refinements"] = UNSET
    auto_completes: Union[Unset, "AutoCompletes"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refinements: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.refinements, Unset):
            refinements = self.refinements.to_dict()

        auto_completes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auto_completes, Unset):
            auto_completes = self.auto_completes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refinements is not UNSET:
            field_dict["refinements"] = refinements
        if auto_completes is not UNSET:
            field_dict["autoCompletes"] = auto_completes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.auto_completes import AutoCompletes
        from ..models.refinements import Refinements

        d = src_dict.copy()
        _refinements = d.pop("refinements", UNSET)
        refinements: Union[Unset, Refinements]
        if isinstance(_refinements, Unset):
            refinements = UNSET
        else:
            refinements = Refinements.from_dict(_refinements)

        _auto_completes = d.pop("autoCompletes", UNSET)
        auto_completes: Union[Unset, AutoCompletes]
        if isinstance(_auto_completes, Unset):
            auto_completes = UNSET
        else:
            auto_completes = AutoCompletes.from_dict(_auto_completes)

        refinements_response_200 = cls(
            refinements=refinements,
            auto_completes=auto_completes,
        )

        refinements_response_200.additional_properties = d
        return refinements_response_200

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
