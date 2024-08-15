from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portfolio import Portfolio


T = TypeVar("T", bound="UpdatePortfolioResponse200")


@_attrs_define
class UpdatePortfolioResponse200:
    """
    Attributes:
        portfolio (Union[Unset, Portfolio]): Refer to the /schemas/portfolio endpoint for the full JSON Schema
            definition
    """

    portfolio: Union[Unset, "Portfolio"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        portfolio: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.portfolio, Unset):
            portfolio = self.portfolio.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portfolio is not UNSET:
            field_dict["portfolio"] = portfolio

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.portfolio import Portfolio

        d = src_dict.copy()
        _portfolio = d.pop("portfolio", UNSET)
        portfolio: Union[Unset, Portfolio]
        if isinstance(_portfolio, Unset):
            portfolio = UNSET
        else:
            portfolio = Portfolio.from_dict(_portfolio)

        update_portfolio_response_200 = cls(
            portfolio=portfolio,
        )

        update_portfolio_response_200.additional_properties = d
        return update_portfolio_response_200

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
