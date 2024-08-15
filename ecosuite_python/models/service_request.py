import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_request_asset import ServiceRequestAsset
    from ..models.service_request_information_item import ServiceRequestInformationItem
    from ..models.service_request_site_visit_window import ServiceRequestSiteVisitWindow


T = TypeVar("T", bound="ServiceRequest")


@_attrs_define
class ServiceRequest:
    """Refer to the /schemas/service-request endpoint for the full JSON Schema definition

    Attributes:
        location (ServiceRequestAsset):
        task_summary (str):
        context (str):
        created (Union[Unset, datetime.datetime]):
        closed (Union[Unset, datetime.datetime]):
        site_visit_window (Union[Unset, ServiceRequestSiteVisitWindow]):
        on_site_contact_notes (Union[Unset, str]):
        contact_number (Union[Unset, str]):  Default: '718-395-3620'.
        tasks (Union[Unset, List[str]]):
        events (Union[Unset, List[str]]):
        tools (Union[Unset, List[str]]):
        information (Union[Unset, List['ServiceRequestInformationItem']]):
        checklist (Union[Unset, List[str]]):
    """

    location: "ServiceRequestAsset"
    task_summary: str
    context: str
    created: Union[Unset, datetime.datetime] = UNSET
    closed: Union[Unset, datetime.datetime] = UNSET
    site_visit_window: Union[Unset, "ServiceRequestSiteVisitWindow"] = UNSET
    on_site_contact_notes: Union[Unset, str] = UNSET
    contact_number: Union[Unset, str] = "718-395-3620"
    tasks: Union[Unset, List[str]] = UNSET
    events: Union[Unset, List[str]] = UNSET
    tools: Union[Unset, List[str]] = UNSET
    information: Union[Unset, List["ServiceRequestInformationItem"]] = UNSET
    checklist: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location = self.location.to_dict()

        task_summary = self.task_summary

        context = self.context

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        closed: Union[Unset, str] = UNSET
        if not isinstance(self.closed, Unset):
            closed = self.closed.isoformat()

        site_visit_window: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.site_visit_window, Unset):
            site_visit_window = self.site_visit_window.to_dict()

        on_site_contact_notes = self.on_site_contact_notes

        contact_number = self.contact_number

        tasks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = self.tasks

        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        tools: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tools, Unset):
            tools = self.tools

        information: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.information, Unset):
            information = []
            for information_item_data in self.information:
                information_item = information_item_data.to_dict()
                information.append(information_item)

        checklist: Union[Unset, List[str]] = UNSET
        if not isinstance(self.checklist, Unset):
            checklist = self.checklist

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
                "taskSummary": task_summary,
                "context": context,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if closed is not UNSET:
            field_dict["closed"] = closed
        if site_visit_window is not UNSET:
            field_dict["siteVisitWindow"] = site_visit_window
        if on_site_contact_notes is not UNSET:
            field_dict["onSiteContactNotes"] = on_site_contact_notes
        if contact_number is not UNSET:
            field_dict["contactNumber"] = contact_number
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if events is not UNSET:
            field_dict["events"] = events
        if tools is not UNSET:
            field_dict["tools"] = tools
        if information is not UNSET:
            field_dict["information"] = information
        if checklist is not UNSET:
            field_dict["checklist"] = checklist

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_request_asset import ServiceRequestAsset
        from ..models.service_request_information_item import ServiceRequestInformationItem
        from ..models.service_request_site_visit_window import ServiceRequestSiteVisitWindow

        d = src_dict.copy()
        location = ServiceRequestAsset.from_dict(d.pop("location"))

        task_summary = d.pop("taskSummary")

        context = d.pop("context")

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _closed = d.pop("closed", UNSET)
        closed: Union[Unset, datetime.datetime]
        if isinstance(_closed, Unset):
            closed = UNSET
        else:
            closed = isoparse(_closed)

        _site_visit_window = d.pop("siteVisitWindow", UNSET)
        site_visit_window: Union[Unset, ServiceRequestSiteVisitWindow]
        if isinstance(_site_visit_window, Unset):
            site_visit_window = UNSET
        else:
            site_visit_window = ServiceRequestSiteVisitWindow.from_dict(_site_visit_window)

        on_site_contact_notes = d.pop("onSiteContactNotes", UNSET)

        contact_number = d.pop("contactNumber", UNSET)

        tasks = cast(List[str], d.pop("tasks", UNSET))

        events = cast(List[str], d.pop("events", UNSET))

        tools = cast(List[str], d.pop("tools", UNSET))

        information = []
        _information = d.pop("information", UNSET)
        for information_item_data in _information or []:
            information_item = ServiceRequestInformationItem.from_dict(information_item_data)

            information.append(information_item)

        checklist = cast(List[str], d.pop("checklist", UNSET))

        service_request = cls(
            location=location,
            task_summary=task_summary,
            context=context,
            created=created,
            closed=closed,
            site_visit_window=site_visit_window,
            on_site_contact_notes=on_site_contact_notes,
            contact_number=contact_number,
            tasks=tasks,
            events=events,
            tools=tools,
            information=information,
            checklist=checklist,
        )

        service_request.additional_properties = d
        return service_request

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
