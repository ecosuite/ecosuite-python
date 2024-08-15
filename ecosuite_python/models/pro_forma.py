import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pro_forma_cash_flows_item import ProFormaCashFlowsItem
    from ..models.pro_forma_taxes import ProFormaTaxes


T = TypeVar("T", bound="ProForma")


@_attrs_define
class ProForma:
    """Refer to the /schemas/pro-forma endpoint for the full JSON Schema definition

    Attributes:
        project_start_date (datetime.date):
        system_size (float): The DC size of the system to use for forecasting of generation.
        system_production (float): The total kWhs generated per Year per kW of installed PV
        degradation (float):
        project_life (float): Used as default number of years for any recurring 'Expense' or 'Income' payment
        developer_fee_percent (Union[Unset, float]):
        archived (Union[Unset, bool]):  Default: False.
        taxes (Union[Unset, ProFormaTaxes]):
        cash_flows (Union[Unset, List['ProFormaCashFlowsItem']]): Cash Flows are used to calculate the Pro Forma IRR
    """

    project_start_date: datetime.date
    system_size: float
    system_production: float
    degradation: float
    project_life: float
    developer_fee_percent: Union[Unset, float] = UNSET
    archived: Union[Unset, bool] = False
    taxes: Union[Unset, "ProFormaTaxes"] = UNSET
    cash_flows: Union[Unset, List["ProFormaCashFlowsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_start_date = self.project_start_date.isoformat()

        system_size = self.system_size

        system_production = self.system_production

        degradation = self.degradation

        project_life = self.project_life

        developer_fee_percent = self.developer_fee_percent

        archived = self.archived

        taxes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = self.taxes.to_dict()

        cash_flows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cash_flows, Unset):
            cash_flows = []
            for cash_flows_item_data in self.cash_flows:
                cash_flows_item = cash_flows_item_data.to_dict()
                cash_flows.append(cash_flows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectStartDate": project_start_date,
                "systemSize": system_size,
                "systemProduction": system_production,
                "degradation": degradation,
                "projectLife": project_life,
            }
        )
        if developer_fee_percent is not UNSET:
            field_dict["developerFeePercent"] = developer_fee_percent
        if archived is not UNSET:
            field_dict["archived"] = archived
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if cash_flows is not UNSET:
            field_dict["cashFlows"] = cash_flows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pro_forma_cash_flows_item import ProFormaCashFlowsItem
        from ..models.pro_forma_taxes import ProFormaTaxes

        d = src_dict.copy()
        project_start_date = isoparse(d.pop("projectStartDate")).date()

        system_size = d.pop("systemSize")

        system_production = d.pop("systemProduction")

        degradation = d.pop("degradation")

        project_life = d.pop("projectLife")

        developer_fee_percent = d.pop("developerFeePercent", UNSET)

        archived = d.pop("archived", UNSET)

        _taxes = d.pop("taxes", UNSET)
        taxes: Union[Unset, ProFormaTaxes]
        if isinstance(_taxes, Unset):
            taxes = UNSET
        else:
            taxes = ProFormaTaxes.from_dict(_taxes)

        cash_flows = []
        _cash_flows = d.pop("cashFlows", UNSET)
        for cash_flows_item_data in _cash_flows or []:
            cash_flows_item = ProFormaCashFlowsItem.from_dict(cash_flows_item_data)

            cash_flows.append(cash_flows_item)

        pro_forma = cls(
            project_start_date=project_start_date,
            system_size=system_size,
            system_production=system_production,
            degradation=degradation,
            project_life=project_life,
            developer_fee_percent=developer_fee_percent,
            archived=archived,
            taxes=taxes,
            cash_flows=cash_flows,
        )

        pro_forma.additional_properties = d
        return pro_forma

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
