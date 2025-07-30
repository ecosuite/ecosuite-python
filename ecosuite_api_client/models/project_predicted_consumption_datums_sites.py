from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_predicted_consumption_datums_sites_additional_property import (
        ProjectPredictedConsumptionDatumsSitesAdditionalProperty,
    )


T = TypeVar("T", bound="ProjectPredictedConsumptionDatumsSites")


@_attrs_define
class ProjectPredictedConsumptionDatumsSites:
    """Keyed by Site ID"""

    additional_properties: dict[str, "ProjectPredictedConsumptionDatumsSitesAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_predicted_consumption_datums_sites_additional_property import (
            ProjectPredictedConsumptionDatumsSitesAdditionalProperty,
        )

        d = dict(src_dict)
        project_predicted_consumption_datums_sites = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ProjectPredictedConsumptionDatumsSitesAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        project_predicted_consumption_datums_sites.additional_properties = additional_properties
        return project_predicted_consumption_datums_sites

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ProjectPredictedConsumptionDatumsSitesAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ProjectPredictedConsumptionDatumsSitesAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
