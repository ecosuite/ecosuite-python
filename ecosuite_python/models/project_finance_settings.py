import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.project_finance_settings_accounting_provider import ProjectFinanceSettingsAccountingProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_finance_settings_disabled_accounts import ProjectFinanceSettingsDisabledAccounts
    from ..models.project_finance_settings_disabled_categories import ProjectFinanceSettingsDisabledCategories


T = TypeVar("T", bound="ProjectFinanceSettings")


@_attrs_define
class ProjectFinanceSettings:
    """Refer to the /schemas/finance endpoint for the full JSON Schema definition

    Attributes:
        id (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        updated (Union[Unset, datetime.datetime]):
        path (Union[Unset, str]):
        financial_model_url (Union[Unset, str]):
        external_financial_model_url (Union[Unset, str]):
        epc_bid_sheet_url (Union[Unset, str]):
        smartsheet_sheet_url (Union[Unset, str]):
        provider (Union[Unset, ProjectFinanceSettingsAccountingProvider]):
        disabled_accounts (Union[Unset, ProjectFinanceSettingsDisabledAccounts]): Category keyed by category name
        disabled_categories (Union[Unset, ProjectFinanceSettingsDisabledCategories]): Disabled sub categories keyed by
            category name
    """

    id: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    path: Union[Unset, str] = UNSET
    financial_model_url: Union[Unset, str] = UNSET
    external_financial_model_url: Union[Unset, str] = UNSET
    epc_bid_sheet_url: Union[Unset, str] = UNSET
    smartsheet_sheet_url: Union[Unset, str] = UNSET
    provider: Union[Unset, ProjectFinanceSettingsAccountingProvider] = UNSET
    disabled_accounts: Union[Unset, "ProjectFinanceSettingsDisabledAccounts"] = UNSET
    disabled_categories: Union[Unset, "ProjectFinanceSettingsDisabledCategories"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        path = self.path

        financial_model_url = self.financial_model_url

        external_financial_model_url = self.external_financial_model_url

        epc_bid_sheet_url = self.epc_bid_sheet_url

        smartsheet_sheet_url = self.smartsheet_sheet_url

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        disabled_accounts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.disabled_accounts, Unset):
            disabled_accounts = self.disabled_accounts.to_dict()

        disabled_categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.disabled_categories, Unset):
            disabled_categories = self.disabled_categories.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if path is not UNSET:
            field_dict["path"] = path
        if financial_model_url is not UNSET:
            field_dict["financialModelUrl"] = financial_model_url
        if external_financial_model_url is not UNSET:
            field_dict["externalFinancialModelUrl"] = external_financial_model_url
        if epc_bid_sheet_url is not UNSET:
            field_dict["epcBidSheetUrl"] = epc_bid_sheet_url
        if smartsheet_sheet_url is not UNSET:
            field_dict["smartsheetSheetUrl"] = smartsheet_sheet_url
        if provider is not UNSET:
            field_dict["provider"] = provider
        if disabled_accounts is not UNSET:
            field_dict["disabledAccounts"] = disabled_accounts
        if disabled_categories is not UNSET:
            field_dict["disabledCategories"] = disabled_categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_finance_settings_disabled_accounts import ProjectFinanceSettingsDisabledAccounts
        from ..models.project_finance_settings_disabled_categories import ProjectFinanceSettingsDisabledCategories

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        path = d.pop("path", UNSET)

        financial_model_url = d.pop("financialModelUrl", UNSET)

        external_financial_model_url = d.pop("externalFinancialModelUrl", UNSET)

        epc_bid_sheet_url = d.pop("epcBidSheetUrl", UNSET)

        smartsheet_sheet_url = d.pop("smartsheetSheetUrl", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, ProjectFinanceSettingsAccountingProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ProjectFinanceSettingsAccountingProvider(_provider)

        _disabled_accounts = d.pop("disabledAccounts", UNSET)
        disabled_accounts: Union[Unset, ProjectFinanceSettingsDisabledAccounts]
        if isinstance(_disabled_accounts, Unset):
            disabled_accounts = UNSET
        else:
            disabled_accounts = ProjectFinanceSettingsDisabledAccounts.from_dict(_disabled_accounts)

        _disabled_categories = d.pop("disabledCategories", UNSET)
        disabled_categories: Union[Unset, ProjectFinanceSettingsDisabledCategories]
        if isinstance(_disabled_categories, Unset):
            disabled_categories = UNSET
        else:
            disabled_categories = ProjectFinanceSettingsDisabledCategories.from_dict(_disabled_categories)

        project_finance_settings = cls(
            id=id,
            created=created,
            updated=updated,
            path=path,
            financial_model_url=financial_model_url,
            external_financial_model_url=external_financial_model_url,
            epc_bid_sheet_url=epc_bid_sheet_url,
            smartsheet_sheet_url=smartsheet_sheet_url,
            provider=provider,
            disabled_accounts=disabled_accounts,
            disabled_categories=disabled_categories,
        )

        project_finance_settings.additional_properties = d
        return project_finance_settings

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
