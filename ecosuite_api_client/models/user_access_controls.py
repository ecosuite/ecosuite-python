import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_access_controls_limit_access_to import UserAccessControlsLimitAccessTo
from ..models.user_access_controls_prevent_downloading_data import UserAccessControlsPreventDownloadingData
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAccessControls")


@_attrs_define
class UserAccessControls:
    """
    Attributes:
        prevent_download (UserAccessControlsPreventDownloadingData):  Default:
            UserAccessControlsPreventDownloadingData.NO.
        restrict_projects (UserAccessControlsLimitAccessTo):  Default: UserAccessControlsLimitAccessTo.NO.
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
    """

    prevent_download: UserAccessControlsPreventDownloadingData = UserAccessControlsPreventDownloadingData.NO
    restrict_projects: UserAccessControlsLimitAccessTo = UserAccessControlsLimitAccessTo.NO
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prevent_download = self.prevent_download.value

        restrict_projects = self.restrict_projects.value

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "preventDownload": prevent_download,
                "restrictProjects": restrict_projects,
            }
        )
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prevent_download = UserAccessControlsPreventDownloadingData(d.pop("preventDownload"))

        restrict_projects = UserAccessControlsLimitAccessTo(d.pop("restrictProjects"))

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        user_access_controls = cls(
            prevent_download=prevent_download,
            restrict_projects=restrict_projects,
            start_date=start_date,
            end_date=end_date,
        )

        user_access_controls.additional_properties = d
        return user_access_controls

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
