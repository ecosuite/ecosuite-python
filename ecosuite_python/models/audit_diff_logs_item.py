from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_diff_logs_item_item import AuditDiffLogsItemItem


T = TypeVar("T", bound="AuditDiffLogsItem")


@_attrs_define
class AuditDiffLogsItem:
    """
    Attributes:
        path (Union[Unset, str]):
        user_id (Union[Unset, str]):
        asset_type (Union[Unset, str]):
        timestamp (Union[Unset, int]):
        puser_nameath (Union[Unset, str]):
        project (Union[Unset, str]):
        item (Union[Unset, AuditDiffLogsItemItem]):
        id (Union[Unset, str]): The ID of the item that was edited
    """

    path: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    asset_type: Union[Unset, str] = UNSET
    timestamp: Union[Unset, int] = UNSET
    puser_nameath: Union[Unset, str] = UNSET
    project: Union[Unset, str] = UNSET
    item: Union[Unset, "AuditDiffLogsItemItem"] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path

        user_id = self.user_id

        asset_type = self.asset_type

        timestamp = self.timestamp

        puser_nameath = self.puser_nameath

        project = self.project

        item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if puser_nameath is not UNSET:
            field_dict["puserNameath"] = puser_nameath
        if project is not UNSET:
            field_dict["project"] = project
        if item is not UNSET:
            field_dict["item"] = item
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.audit_diff_logs_item_item import AuditDiffLogsItemItem

        d = src_dict.copy()
        path = d.pop("path", UNSET)

        user_id = d.pop("userId", UNSET)

        asset_type = d.pop("assetType", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        puser_nameath = d.pop("puserNameath", UNSET)

        project = d.pop("project", UNSET)

        _item = d.pop("item", UNSET)
        item: Union[Unset, AuditDiffLogsItemItem]
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = AuditDiffLogsItemItem.from_dict(_item)

        id = d.pop("id", UNSET)

        audit_diff_logs_item = cls(
            path=path,
            user_id=user_id,
            asset_type=asset_type,
            timestamp=timestamp,
            puser_nameath=puser_nameath,
            project=project,
            item=item,
            id=id,
        )

        audit_diff_logs_item.additional_properties = d
        return audit_diff_logs_item

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
