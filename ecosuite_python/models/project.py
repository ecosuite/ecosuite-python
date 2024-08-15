import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.project_project_status import ProjectProjectStatus
from ..models.project_revenue_type import ProjectRevenueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_asset_management_team_contact import ProjectAssetManagementTeamContact
    from ..models.project_icons_item import ProjectIconsItem
    from ..models.project_interconnection import ProjectInterconnection
    from ..models.project_links_item import ProjectLinksItem
    from ..models.project_media import ProjectMedia
    from ..models.project_notes_item import ProjectNotesItem
    from ..models.project_project_milestones import ProjectProjectMilestones
    from ..models.project_reports import ProjectReports


T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """Refer to the /schemas/project endpoint for the full JSON Schema definition

    Attributes:
        code (str):
        status (ProjectProjectStatus):  Default: ProjectProjectStatus.NEW_PROJECT.
        name (str):
        address (str):
        town (str):
        state (str):
        lat (float):
        long (float):
        start_date (datetime.date):
        timezone (str):
        dc_size (Union[Unset, float]):
        system_status (Union[Unset, str]): The aggregated system status
        paused (Union[Unset, bool]):  Default: False.
        cancelled (Union[Unset, bool]):  Default: False.
        archived (Union[Unset, bool]):  Default: False.
        interconnection (Union[Unset, ProjectInterconnection]):
        discount_rate (Union[Unset, float]):
        ein_number (Union[Unset, str]):
        company_name (Union[Unset, str]):
        client_number (Union[Unset, str]):
        report_start_date (Union[Unset, datetime.date]):
        production_start_date (Union[Unset, datetime.date]):
        generation_start_date (Union[Unset, datetime.date]):
        consumption_start_date (Union[Unset, datetime.date]):
        storage_start_date (Union[Unset, datetime.date]):
        icons (Union[Unset, List['ProjectIconsItem']]):
        revenue_type (Union[Unset, ProjectRevenueType]):
        biz_dev_owner (Union[Unset, str]):
        site_surveyor (Union[Unset, str]):
        slack_channel (Union[Unset, str]):
        gantt_chart_last_updated (Union[Unset, datetime.date]):
        milestones (Union[Unset, ProjectProjectMilestones]):
        asset_management_team_contact (Union[Unset, ProjectAssetManagementTeamContact]):
        reports (Union[Unset, ProjectReports]):
        links (Union[Unset, List['ProjectLinksItem']]):
        tags (Union[Unset, List[str]]):
        notes (Union[Unset, List['ProjectNotesItem']]):
        media (Union[Unset, ProjectMedia]):
    """

    code: str
    name: str
    address: str
    town: str
    state: str
    lat: float
    long: float
    start_date: datetime.date
    timezone: str
    status: ProjectProjectStatus = ProjectProjectStatus.NEW_PROJECT
    dc_size: Union[Unset, float] = UNSET
    system_status: Union[Unset, str] = UNSET
    paused: Union[Unset, bool] = False
    cancelled: Union[Unset, bool] = False
    archived: Union[Unset, bool] = False
    interconnection: Union[Unset, "ProjectInterconnection"] = UNSET
    discount_rate: Union[Unset, float] = UNSET
    ein_number: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    client_number: Union[Unset, str] = UNSET
    report_start_date: Union[Unset, datetime.date] = UNSET
    production_start_date: Union[Unset, datetime.date] = UNSET
    generation_start_date: Union[Unset, datetime.date] = UNSET
    consumption_start_date: Union[Unset, datetime.date] = UNSET
    storage_start_date: Union[Unset, datetime.date] = UNSET
    icons: Union[Unset, List["ProjectIconsItem"]] = UNSET
    revenue_type: Union[Unset, ProjectRevenueType] = UNSET
    biz_dev_owner: Union[Unset, str] = UNSET
    site_surveyor: Union[Unset, str] = UNSET
    slack_channel: Union[Unset, str] = UNSET
    gantt_chart_last_updated: Union[Unset, datetime.date] = UNSET
    milestones: Union[Unset, "ProjectProjectMilestones"] = UNSET
    asset_management_team_contact: Union[Unset, "ProjectAssetManagementTeamContact"] = UNSET
    reports: Union[Unset, "ProjectReports"] = UNSET
    links: Union[Unset, List["ProjectLinksItem"]] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    notes: Union[Unset, List["ProjectNotesItem"]] = UNSET
    media: Union[Unset, "ProjectMedia"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        status = self.status.value

        name = self.name

        address = self.address

        town = self.town

        state = self.state

        lat = self.lat

        long = self.long

        start_date = self.start_date.isoformat()

        timezone = self.timezone

        dc_size = self.dc_size

        system_status = self.system_status

        paused = self.paused

        cancelled = self.cancelled

        archived = self.archived

        interconnection: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interconnection, Unset):
            interconnection = self.interconnection.to_dict()

        discount_rate = self.discount_rate

        ein_number = self.ein_number

        company_name = self.company_name

        client_number = self.client_number

        report_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.report_start_date, Unset):
            report_start_date = self.report_start_date.isoformat()

        production_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.production_start_date, Unset):
            production_start_date = self.production_start_date.isoformat()

        generation_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.generation_start_date, Unset):
            generation_start_date = self.generation_start_date.isoformat()

        consumption_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.consumption_start_date, Unset):
            consumption_start_date = self.consumption_start_date.isoformat()

        storage_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.storage_start_date, Unset):
            storage_start_date = self.storage_start_date.isoformat()

        icons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.icons, Unset):
            icons = []
            for icons_item_data in self.icons:
                icons_item = icons_item_data.to_dict()
                icons.append(icons_item)

        revenue_type: Union[Unset, str] = UNSET
        if not isinstance(self.revenue_type, Unset):
            revenue_type = self.revenue_type.value

        biz_dev_owner = self.biz_dev_owner

        site_surveyor = self.site_surveyor

        slack_channel = self.slack_channel

        gantt_chart_last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.gantt_chart_last_updated, Unset):
            gantt_chart_last_updated = self.gantt_chart_last_updated.isoformat()

        milestones: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.milestones, Unset):
            milestones = self.milestones.to_dict()

        asset_management_team_contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.asset_management_team_contact, Unset):
            asset_management_team_contact = self.asset_management_team_contact.to_dict()

        reports: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reports, Unset):
            reports = self.reports.to_dict()

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        notes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        media: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "status": status,
                "name": name,
                "address": address,
                "town": town,
                "state": state,
                "lat": lat,
                "long": long,
                "startDate": start_date,
                "timezone": timezone,
            }
        )
        if dc_size is not UNSET:
            field_dict["dcSize"] = dc_size
        if system_status is not UNSET:
            field_dict["systemStatus"] = system_status
        if paused is not UNSET:
            field_dict["paused"] = paused
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if archived is not UNSET:
            field_dict["archived"] = archived
        if interconnection is not UNSET:
            field_dict["interconnection"] = interconnection
        if discount_rate is not UNSET:
            field_dict["discountRate"] = discount_rate
        if ein_number is not UNSET:
            field_dict["einNumber"] = ein_number
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if client_number is not UNSET:
            field_dict["clientNumber"] = client_number
        if report_start_date is not UNSET:
            field_dict["reportStartDate"] = report_start_date
        if production_start_date is not UNSET:
            field_dict["productionStartDate"] = production_start_date
        if generation_start_date is not UNSET:
            field_dict["generationStartDate"] = generation_start_date
        if consumption_start_date is not UNSET:
            field_dict["consumptionStartDate"] = consumption_start_date
        if storage_start_date is not UNSET:
            field_dict["storageStartDate"] = storage_start_date
        if icons is not UNSET:
            field_dict["icons"] = icons
        if revenue_type is not UNSET:
            field_dict["revenueType"] = revenue_type
        if biz_dev_owner is not UNSET:
            field_dict["bizDevOwner"] = biz_dev_owner
        if site_surveyor is not UNSET:
            field_dict["siteSurveyor"] = site_surveyor
        if slack_channel is not UNSET:
            field_dict["slackChannel"] = slack_channel
        if gantt_chart_last_updated is not UNSET:
            field_dict["ganttChartLastUpdated"] = gantt_chart_last_updated
        if milestones is not UNSET:
            field_dict["milestones"] = milestones
        if asset_management_team_contact is not UNSET:
            field_dict["assetManagementTeamContact"] = asset_management_team_contact
        if reports is not UNSET:
            field_dict["reports"] = reports
        if links is not UNSET:
            field_dict["links"] = links
        if tags is not UNSET:
            field_dict["tags"] = tags
        if notes is not UNSET:
            field_dict["notes"] = notes
        if media is not UNSET:
            field_dict["media"] = media

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_asset_management_team_contact import ProjectAssetManagementTeamContact
        from ..models.project_icons_item import ProjectIconsItem
        from ..models.project_interconnection import ProjectInterconnection
        from ..models.project_links_item import ProjectLinksItem
        from ..models.project_media import ProjectMedia
        from ..models.project_notes_item import ProjectNotesItem
        from ..models.project_project_milestones import ProjectProjectMilestones
        from ..models.project_reports import ProjectReports

        d = src_dict.copy()
        code = d.pop("code")

        status = ProjectProjectStatus(d.pop("status"))

        name = d.pop("name")

        address = d.pop("address")

        town = d.pop("town")

        state = d.pop("state")

        lat = d.pop("lat")

        long = d.pop("long")

        start_date = isoparse(d.pop("startDate")).date()

        timezone = d.pop("timezone")

        dc_size = d.pop("dcSize", UNSET)

        system_status = d.pop("systemStatus", UNSET)

        paused = d.pop("paused", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        archived = d.pop("archived", UNSET)

        _interconnection = d.pop("interconnection", UNSET)
        interconnection: Union[Unset, ProjectInterconnection]
        if isinstance(_interconnection, Unset):
            interconnection = UNSET
        else:
            interconnection = ProjectInterconnection.from_dict(_interconnection)

        discount_rate = d.pop("discountRate", UNSET)

        ein_number = d.pop("einNumber", UNSET)

        company_name = d.pop("companyName", UNSET)

        client_number = d.pop("clientNumber", UNSET)

        _report_start_date = d.pop("reportStartDate", UNSET)
        report_start_date: Union[Unset, datetime.date]
        if isinstance(_report_start_date, Unset):
            report_start_date = UNSET
        else:
            report_start_date = isoparse(_report_start_date).date()

        _production_start_date = d.pop("productionStartDate", UNSET)
        production_start_date: Union[Unset, datetime.date]
        if isinstance(_production_start_date, Unset):
            production_start_date = UNSET
        else:
            production_start_date = isoparse(_production_start_date).date()

        _generation_start_date = d.pop("generationStartDate", UNSET)
        generation_start_date: Union[Unset, datetime.date]
        if isinstance(_generation_start_date, Unset):
            generation_start_date = UNSET
        else:
            generation_start_date = isoparse(_generation_start_date).date()

        _consumption_start_date = d.pop("consumptionStartDate", UNSET)
        consumption_start_date: Union[Unset, datetime.date]
        if isinstance(_consumption_start_date, Unset):
            consumption_start_date = UNSET
        else:
            consumption_start_date = isoparse(_consumption_start_date).date()

        _storage_start_date = d.pop("storageStartDate", UNSET)
        storage_start_date: Union[Unset, datetime.date]
        if isinstance(_storage_start_date, Unset):
            storage_start_date = UNSET
        else:
            storage_start_date = isoparse(_storage_start_date).date()

        icons = []
        _icons = d.pop("icons", UNSET)
        for icons_item_data in _icons or []:
            icons_item = ProjectIconsItem.from_dict(icons_item_data)

            icons.append(icons_item)

        _revenue_type = d.pop("revenueType", UNSET)
        revenue_type: Union[Unset, ProjectRevenueType]
        if isinstance(_revenue_type, Unset):
            revenue_type = UNSET
        else:
            revenue_type = ProjectRevenueType(_revenue_type)

        biz_dev_owner = d.pop("bizDevOwner", UNSET)

        site_surveyor = d.pop("siteSurveyor", UNSET)

        slack_channel = d.pop("slackChannel", UNSET)

        _gantt_chart_last_updated = d.pop("ganttChartLastUpdated", UNSET)
        gantt_chart_last_updated: Union[Unset, datetime.date]
        if isinstance(_gantt_chart_last_updated, Unset):
            gantt_chart_last_updated = UNSET
        else:
            gantt_chart_last_updated = isoparse(_gantt_chart_last_updated).date()

        _milestones = d.pop("milestones", UNSET)
        milestones: Union[Unset, ProjectProjectMilestones]
        if isinstance(_milestones, Unset):
            milestones = UNSET
        else:
            milestones = ProjectProjectMilestones.from_dict(_milestones)

        _asset_management_team_contact = d.pop("assetManagementTeamContact", UNSET)
        asset_management_team_contact: Union[Unset, ProjectAssetManagementTeamContact]
        if isinstance(_asset_management_team_contact, Unset):
            asset_management_team_contact = UNSET
        else:
            asset_management_team_contact = ProjectAssetManagementTeamContact.from_dict(_asset_management_team_contact)

        _reports = d.pop("reports", UNSET)
        reports: Union[Unset, ProjectReports]
        if isinstance(_reports, Unset):
            reports = UNSET
        else:
            reports = ProjectReports.from_dict(_reports)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = ProjectLinksItem.from_dict(links_item_data)

            links.append(links_item)

        tags = cast(List[str], d.pop("tags", UNSET))

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = ProjectNotesItem.from_dict(notes_item_data)

            notes.append(notes_item)

        _media = d.pop("media", UNSET)
        media: Union[Unset, ProjectMedia]
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = ProjectMedia.from_dict(_media)

        project = cls(
            code=code,
            status=status,
            name=name,
            address=address,
            town=town,
            state=state,
            lat=lat,
            long=long,
            start_date=start_date,
            timezone=timezone,
            dc_size=dc_size,
            system_status=system_status,
            paused=paused,
            cancelled=cancelled,
            archived=archived,
            interconnection=interconnection,
            discount_rate=discount_rate,
            ein_number=ein_number,
            company_name=company_name,
            client_number=client_number,
            report_start_date=report_start_date,
            production_start_date=production_start_date,
            generation_start_date=generation_start_date,
            consumption_start_date=consumption_start_date,
            storage_start_date=storage_start_date,
            icons=icons,
            revenue_type=revenue_type,
            biz_dev_owner=biz_dev_owner,
            site_surveyor=site_surveyor,
            slack_channel=slack_channel,
            gantt_chart_last_updated=gantt_chart_last_updated,
            milestones=milestones,
            asset_management_team_contact=asset_management_team_contact,
            reports=reports,
            links=links,
            tags=tags,
            notes=notes,
            media=media,
        )

        project.additional_properties = d
        return project

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
