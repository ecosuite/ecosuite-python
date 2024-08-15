from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_log_diff import AuditLogDiff


T = TypeVar("T", bound="AuditLog")


@_attrs_define
class AuditLog:
    """
    Attributes:
        diff (Union[Unset, AuditLogDiff]):
    """

    diff: Union[Unset, "AuditLogDiff"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        diff: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.diff, Unset):
            diff = self.diff.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if diff is not UNSET:
            field_dict["diff"] = diff

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.audit_log_diff import AuditLogDiff

        d = src_dict.copy()
        _diff = d.pop("diff", UNSET)
        diff: Union[Unset, AuditLogDiff]
        if isinstance(_diff, Unset):
            diff = UNSET
        else:
            diff = AuditLogDiff.from_dict(_diff)

        audit_log = cls(
            diff=diff,
        )

        audit_log.additional_properties = d
        return audit_log

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
