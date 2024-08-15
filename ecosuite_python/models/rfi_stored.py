import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rfi_stored_resolution_history import RFIStoredResolutionHistory


T = TypeVar("T", bound="RFIStored")


@_attrs_define
class RFIStored:
    """
    Attributes:
        id (str): The RFI ID.
        created_date_time (datetime.date): When the RFI was created.
        author (str): Who authored RFI.
        number (float): The RFI number.
        last_updated_date_time (datetime.date): When the RFI was last updated.
        last_updated_by (str): Who made the last update.
        version (str): The version of the RFI.
        resolved (bool): Whether the RFI is currently resolved.
        resolution_history (RFIStoredResolutionHistory): The RFI resolution history.
        code (str): The RFI code.
        name (str): The RFI name.
        due_date_time (datetime.date): The RFI due date.
        linked (List[str]): The linked RFIs.
        media (List[str]): The linked media.
        cost_impacts (Union[Unset, str]): The RFI cost impacts.
        schedule_impacts (Union[Unset, str]): The RFI schedule impacts.
        description (Union[Unset, str]): The RFI description.
        assigned (Union[Unset, List[str]]): Assigned organizations (in the form of email domains, e.g. ecogyenergy.com).
    """

    id: str
    created_date_time: datetime.date
    author: str
    number: float
    last_updated_date_time: datetime.date
    last_updated_by: str
    version: str
    resolved: bool
    resolution_history: "RFIStoredResolutionHistory"
    code: str
    name: str
    due_date_time: datetime.date
    linked: List[str]
    media: List[str]
    cost_impacts: Union[Unset, str] = UNSET
    schedule_impacts: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    assigned: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        created_date_time = self.created_date_time.isoformat()

        author = self.author

        number = self.number

        last_updated_date_time = self.last_updated_date_time.isoformat()

        last_updated_by = self.last_updated_by

        version = self.version

        resolved = self.resolved

        resolution_history = self.resolution_history.to_dict()

        code = self.code

        name = self.name

        due_date_time = self.due_date_time.isoformat()

        linked = self.linked

        media = self.media

        cost_impacts = self.cost_impacts

        schedule_impacts = self.schedule_impacts

        description = self.description

        assigned: Union[Unset, List[str]] = UNSET
        if not isinstance(self.assigned, Unset):
            assigned = self.assigned

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdDateTime": created_date_time,
                "author": author,
                "number": number,
                "lastUpdatedDateTime": last_updated_date_time,
                "lastUpdatedBy": last_updated_by,
                "version": version,
                "resolved": resolved,
                "resolutionHistory": resolution_history,
                "code": code,
                "name": name,
                "dueDateTime": due_date_time,
                "linked": linked,
                "media": media,
            }
        )
        if cost_impacts is not UNSET:
            field_dict["costImpacts"] = cost_impacts
        if schedule_impacts is not UNSET:
            field_dict["scheduleImpacts"] = schedule_impacts
        if description is not UNSET:
            field_dict["description"] = description
        if assigned is not UNSET:
            field_dict["assigned"] = assigned

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rfi_stored_resolution_history import RFIStoredResolutionHistory

        d = src_dict.copy()
        id = d.pop("id")

        created_date_time = isoparse(d.pop("createdDateTime")).date()

        author = d.pop("author")

        number = d.pop("number")

        last_updated_date_time = isoparse(d.pop("lastUpdatedDateTime")).date()

        last_updated_by = d.pop("lastUpdatedBy")

        version = d.pop("version")

        resolved = d.pop("resolved")

        resolution_history = RFIStoredResolutionHistory.from_dict(d.pop("resolutionHistory"))

        code = d.pop("code")

        name = d.pop("name")

        due_date_time = isoparse(d.pop("dueDateTime")).date()

        linked = cast(List[str], d.pop("linked"))

        media = cast(List[str], d.pop("media"))

        cost_impacts = d.pop("costImpacts", UNSET)

        schedule_impacts = d.pop("scheduleImpacts", UNSET)

        description = d.pop("description", UNSET)

        assigned = cast(List[str], d.pop("assigned", UNSET))

        rfi_stored = cls(
            id=id,
            created_date_time=created_date_time,
            author=author,
            number=number,
            last_updated_date_time=last_updated_date_time,
            last_updated_by=last_updated_by,
            version=version,
            resolved=resolved,
            resolution_history=resolution_history,
            code=code,
            name=name,
            due_date_time=due_date_time,
            linked=linked,
            media=media,
            cost_impacts=cost_impacts,
            schedule_impacts=schedule_impacts,
            description=description,
            assigned=assigned,
        )

        rfi_stored.additional_properties = d
        return rfi_stored

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
