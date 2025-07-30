import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_notes_item_comments_item import ProjectNotesItemCommentsItem


T = TypeVar("T", bound="ProjectNotesItem")


@_attrs_define
class ProjectNotesItem:
    """
    Attributes:
        note (str):
        user_name (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        resolved (Union[Unset, bool]):
        comments (Union[Unset, list['ProjectNotesItemCommentsItem']]):
    """

    note: str
    user_name: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    resolved: Union[Unset, bool] = UNSET
    comments: Union[Unset, list["ProjectNotesItemCommentsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        note = self.note

        user_name = self.user_name

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        resolved = self.resolved

        comments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "note": note,
            }
        )
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if created is not UNSET:
            field_dict["created"] = created
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_notes_item_comments_item import ProjectNotesItemCommentsItem

        d = dict(src_dict)
        note = d.pop("note")

        user_name = d.pop("userName", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        resolved = d.pop("resolved", UNSET)

        comments = []
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            comments_item = ProjectNotesItemCommentsItem.from_dict(comments_item_data)

            comments.append(comments_item)

        project_notes_item = cls(
            note=note,
            user_name=user_name,
            created=created,
            resolved=resolved,
            comments=comments,
        )

        project_notes_item.additional_properties = d
        return project_notes_item

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
