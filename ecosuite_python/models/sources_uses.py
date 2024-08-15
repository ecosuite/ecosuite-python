from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sources_uses_sources import SourcesUsesSources
    from ..models.sources_uses_uses import SourcesUsesUses


T = TypeVar("T", bound="SourcesUses")


@_attrs_define
class SourcesUses:
    """
    Attributes:
        class_b_contributions (Union[Unset, float]):  Example: 5463.57.
        grants (Union[Unset, float]):  Example: 5463.57.
        debt_proceeds (Union[Unset, float]):  Example: 5463.57.
        non_dev_fee_fixed_assets (Union[Unset, float]):  Example: 5463.57.
        dev_fees (Union[Unset, float]):  Example: 5463.57.
        fixed_assets (Union[Unset, float]):  Example: 5463.57.
        sources (Union[Unset, SourcesUsesSources]):
        uses (Union[Unset, SourcesUsesUses]):
    """

    class_b_contributions: Union[Unset, float] = UNSET
    grants: Union[Unset, float] = UNSET
    debt_proceeds: Union[Unset, float] = UNSET
    non_dev_fee_fixed_assets: Union[Unset, float] = UNSET
    dev_fees: Union[Unset, float] = UNSET
    fixed_assets: Union[Unset, float] = UNSET
    sources: Union[Unset, "SourcesUsesSources"] = UNSET
    uses: Union[Unset, "SourcesUsesUses"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        class_b_contributions = self.class_b_contributions

        grants = self.grants

        debt_proceeds = self.debt_proceeds

        non_dev_fee_fixed_assets = self.non_dev_fee_fixed_assets

        dev_fees = self.dev_fees

        fixed_assets = self.fixed_assets

        sources: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources.to_dict()

        uses: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.uses, Unset):
            uses = self.uses.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_b_contributions is not UNSET:
            field_dict["classBContributions"] = class_b_contributions
        if grants is not UNSET:
            field_dict["grants"] = grants
        if debt_proceeds is not UNSET:
            field_dict["debtProceeds"] = debt_proceeds
        if non_dev_fee_fixed_assets is not UNSET:
            field_dict["nonDevFeeFixedAssets"] = non_dev_fee_fixed_assets
        if dev_fees is not UNSET:
            field_dict["devFees"] = dev_fees
        if fixed_assets is not UNSET:
            field_dict["fixedAssets"] = fixed_assets
        if sources is not UNSET:
            field_dict["sources"] = sources
        if uses is not UNSET:
            field_dict["uses"] = uses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sources_uses_sources import SourcesUsesSources
        from ..models.sources_uses_uses import SourcesUsesUses

        d = src_dict.copy()
        class_b_contributions = d.pop("classBContributions", UNSET)

        grants = d.pop("grants", UNSET)

        debt_proceeds = d.pop("debtProceeds", UNSET)

        non_dev_fee_fixed_assets = d.pop("nonDevFeeFixedAssets", UNSET)

        dev_fees = d.pop("devFees", UNSET)

        fixed_assets = d.pop("fixedAssets", UNSET)

        _sources = d.pop("sources", UNSET)
        sources: Union[Unset, SourcesUsesSources]
        if isinstance(_sources, Unset):
            sources = UNSET
        else:
            sources = SourcesUsesSources.from_dict(_sources)

        _uses = d.pop("uses", UNSET)
        uses: Union[Unset, SourcesUsesUses]
        if isinstance(_uses, Unset):
            uses = UNSET
        else:
            uses = SourcesUsesUses.from_dict(_uses)

        sources_uses = cls(
            class_b_contributions=class_b_contributions,
            grants=grants,
            debt_proceeds=debt_proceeds,
            non_dev_fee_fixed_assets=non_dev_fee_fixed_assets,
            dev_fees=dev_fees,
            fixed_assets=fixed_assets,
            sources=sources,
            uses=uses,
        )

        sources_uses.additional_properties = d
        return sources_uses

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
