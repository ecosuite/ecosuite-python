from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_tag_response_s3 import MediaTagResponseS3


T = TypeVar("T", bound="MediaTagResponse")


@_attrs_define
class MediaTagResponse:
    """The media tag as it is stored in DynamoDB.

    Attributes:
        id (str):
        code (str):
        system_generated (bool):
        s3 (MediaTagResponseS3): The S3 information that is stored.
        label (str):
        description (Union[Unset, str]):
    """

    id: str
    code: str
    system_generated: bool
    s3: "MediaTagResponseS3"
    label: str
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        code = self.code

        system_generated = self.system_generated

        s3 = self.s3.to_dict()

        label = self.label

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "code": code,
                "systemGenerated": system_generated,
                "s3": s3,
                "label": label,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.media_tag_response_s3 import MediaTagResponseS3

        d = src_dict.copy()
        id = d.pop("id")

        code = d.pop("code")

        system_generated = d.pop("systemGenerated")

        s3 = MediaTagResponseS3.from_dict(d.pop("s3"))

        label = d.pop("label")

        description = d.pop("description", UNSET)

        media_tag_response = cls(
            id=id,
            code=code,
            system_generated=system_generated,
            s3=s3,
            label=label,
            description=description,
        )

        media_tag_response.additional_properties = d
        return media_tag_response

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
