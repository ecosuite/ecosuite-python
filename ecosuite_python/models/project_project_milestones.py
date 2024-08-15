import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectProjectMilestones")


@_attrs_define
class ProjectProjectMilestones:
    """
    Attributes:
        initiated (Union[Unset, datetime.date]):
        interconnection (Union[Unset, datetime.date]):
        permitting (Union[Unset, datetime.date]):
        pre_construction (Union[Unset, datetime.date]):
        construction (Union[Unset, datetime.date]):
        pto (Union[Unset, datetime.date]):
        operational (Union[Unset, datetime.date]):
    """

    initiated: Union[Unset, datetime.date] = UNSET
    interconnection: Union[Unset, datetime.date] = UNSET
    permitting: Union[Unset, datetime.date] = UNSET
    pre_construction: Union[Unset, datetime.date] = UNSET
    construction: Union[Unset, datetime.date] = UNSET
    pto: Union[Unset, datetime.date] = UNSET
    operational: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        initiated: Union[Unset, str] = UNSET
        if not isinstance(self.initiated, Unset):
            initiated = self.initiated.isoformat()

        interconnection: Union[Unset, str] = UNSET
        if not isinstance(self.interconnection, Unset):
            interconnection = self.interconnection.isoformat()

        permitting: Union[Unset, str] = UNSET
        if not isinstance(self.permitting, Unset):
            permitting = self.permitting.isoformat()

        pre_construction: Union[Unset, str] = UNSET
        if not isinstance(self.pre_construction, Unset):
            pre_construction = self.pre_construction.isoformat()

        construction: Union[Unset, str] = UNSET
        if not isinstance(self.construction, Unset):
            construction = self.construction.isoformat()

        pto: Union[Unset, str] = UNSET
        if not isinstance(self.pto, Unset):
            pto = self.pto.isoformat()

        operational: Union[Unset, str] = UNSET
        if not isinstance(self.operational, Unset):
            operational = self.operational.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if initiated is not UNSET:
            field_dict["initiated"] = initiated
        if interconnection is not UNSET:
            field_dict["interconnection"] = interconnection
        if permitting is not UNSET:
            field_dict["permitting"] = permitting
        if pre_construction is not UNSET:
            field_dict["preConstruction"] = pre_construction
        if construction is not UNSET:
            field_dict["construction"] = construction
        if pto is not UNSET:
            field_dict["pto"] = pto
        if operational is not UNSET:
            field_dict["operational"] = operational

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _initiated = d.pop("initiated", UNSET)
        initiated: Union[Unset, datetime.date]
        if isinstance(_initiated, Unset):
            initiated = UNSET
        else:
            initiated = isoparse(_initiated).date()

        _interconnection = d.pop("interconnection", UNSET)
        interconnection: Union[Unset, datetime.date]
        if isinstance(_interconnection, Unset):
            interconnection = UNSET
        else:
            interconnection = isoparse(_interconnection).date()

        _permitting = d.pop("permitting", UNSET)
        permitting: Union[Unset, datetime.date]
        if isinstance(_permitting, Unset):
            permitting = UNSET
        else:
            permitting = isoparse(_permitting).date()

        _pre_construction = d.pop("preConstruction", UNSET)
        pre_construction: Union[Unset, datetime.date]
        if isinstance(_pre_construction, Unset):
            pre_construction = UNSET
        else:
            pre_construction = isoparse(_pre_construction).date()

        _construction = d.pop("construction", UNSET)
        construction: Union[Unset, datetime.date]
        if isinstance(_construction, Unset):
            construction = UNSET
        else:
            construction = isoparse(_construction).date()

        _pto = d.pop("pto", UNSET)
        pto: Union[Unset, datetime.date]
        if isinstance(_pto, Unset):
            pto = UNSET
        else:
            pto = isoparse(_pto).date()

        _operational = d.pop("operational", UNSET)
        operational: Union[Unset, datetime.date]
        if isinstance(_operational, Unset):
            operational = UNSET
        else:
            operational = isoparse(_operational).date()

        project_project_milestones = cls(
            initiated=initiated,
            interconnection=interconnection,
            permitting=permitting,
            pre_construction=pre_construction,
            construction=construction,
            pto=pto,
            operational=operational,
        )

        project_project_milestones.additional_properties = d
        return project_project_milestones

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
