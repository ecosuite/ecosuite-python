from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_interconnection_ieee1547_disturbance_category import (
    ProjectInterconnectionIEEE1547DisturbanceCategory,
)
from ..models.project_interconnection_ieee1547_reactive_power_category import (
    ProjectInterconnectionIEEE1547ReactivePowerCategory,
)
from ..models.project_interconnection_withdrawal_reason import ProjectInterconnectionWithdrawalReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectInterconnection")


@_attrs_define
class ProjectInterconnection:
    """
    Attributes:
        ieee_1547_reactive_power_category (Union[Unset, ProjectInterconnectionIEEE1547ReactivePowerCategory]): Voltage
            and reactive power capability.
        ieee_1547_disturbance_category (Union[Unset, ProjectInterconnectionIEEE1547DisturbanceCategory]): Voltage and
            frequency ride-through capability.
        fips_location (Union[Unset, str]): FIPS code for the location of the project.
        withdrawal_reason (Union[Unset, ProjectInterconnectionWithdrawalReason]): Reason for withdrawal. Default:
            ProjectInterconnectionWithdrawalReason.NOTAPPLICABLE.
        estimated_cost_of_studies_and_fees (Union[Unset, float]): Estimated cost of studies and fees. Quoted from
            utility. Default: 0.0.
        estimated_cost_of_system_upgrades (Union[Unset, float]): Estimated cost of system upgrades. Quoted from utility.
            Default: 0.0.
        final_cost_of_interconnection (Union[Unset, float]): Final cost of interconnection billed from the utility.
            Captures the difference from the sum of the two estimates. Default: 0.0.
    """

    ieee_1547_reactive_power_category: Union[Unset, ProjectInterconnectionIEEE1547ReactivePowerCategory] = UNSET
    ieee_1547_disturbance_category: Union[Unset, ProjectInterconnectionIEEE1547DisturbanceCategory] = UNSET
    fips_location: Union[Unset, str] = UNSET
    withdrawal_reason: Union[Unset, ProjectInterconnectionWithdrawalReason] = (
        ProjectInterconnectionWithdrawalReason.NOTAPPLICABLE
    )
    estimated_cost_of_studies_and_fees: Union[Unset, float] = 0.0
    estimated_cost_of_system_upgrades: Union[Unset, float] = 0.0
    final_cost_of_interconnection: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ieee_1547_reactive_power_category: Union[Unset, str] = UNSET
        if not isinstance(self.ieee_1547_reactive_power_category, Unset):
            ieee_1547_reactive_power_category = self.ieee_1547_reactive_power_category.value

        ieee_1547_disturbance_category: Union[Unset, str] = UNSET
        if not isinstance(self.ieee_1547_disturbance_category, Unset):
            ieee_1547_disturbance_category = self.ieee_1547_disturbance_category.value

        fips_location = self.fips_location

        withdrawal_reason: Union[Unset, str] = UNSET
        if not isinstance(self.withdrawal_reason, Unset):
            withdrawal_reason = self.withdrawal_reason.value

        estimated_cost_of_studies_and_fees = self.estimated_cost_of_studies_and_fees

        estimated_cost_of_system_upgrades = self.estimated_cost_of_system_upgrades

        final_cost_of_interconnection = self.final_cost_of_interconnection

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ieee_1547_reactive_power_category is not UNSET:
            field_dict["ieee1547ReactivePowerCategory"] = ieee_1547_reactive_power_category
        if ieee_1547_disturbance_category is not UNSET:
            field_dict["ieee1547DisturbanceCategory"] = ieee_1547_disturbance_category
        if fips_location is not UNSET:
            field_dict["fipsLocation"] = fips_location
        if withdrawal_reason is not UNSET:
            field_dict["withdrawalReason"] = withdrawal_reason
        if estimated_cost_of_studies_and_fees is not UNSET:
            field_dict["estimatedCostOfStudiesAndFees"] = estimated_cost_of_studies_and_fees
        if estimated_cost_of_system_upgrades is not UNSET:
            field_dict["estimatedCostOfSystemUpgrades"] = estimated_cost_of_system_upgrades
        if final_cost_of_interconnection is not UNSET:
            field_dict["finalCostOfInterconnection"] = final_cost_of_interconnection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _ieee_1547_reactive_power_category = d.pop("ieee1547ReactivePowerCategory", UNSET)
        ieee_1547_reactive_power_category: Union[Unset, ProjectInterconnectionIEEE1547ReactivePowerCategory]
        if isinstance(_ieee_1547_reactive_power_category, Unset):
            ieee_1547_reactive_power_category = UNSET
        else:
            ieee_1547_reactive_power_category = ProjectInterconnectionIEEE1547ReactivePowerCategory(
                _ieee_1547_reactive_power_category
            )

        _ieee_1547_disturbance_category = d.pop("ieee1547DisturbanceCategory", UNSET)
        ieee_1547_disturbance_category: Union[Unset, ProjectInterconnectionIEEE1547DisturbanceCategory]
        if isinstance(_ieee_1547_disturbance_category, Unset):
            ieee_1547_disturbance_category = UNSET
        else:
            ieee_1547_disturbance_category = ProjectInterconnectionIEEE1547DisturbanceCategory(
                _ieee_1547_disturbance_category
            )

        fips_location = d.pop("fipsLocation", UNSET)

        _withdrawal_reason = d.pop("withdrawalReason", UNSET)
        withdrawal_reason: Union[Unset, ProjectInterconnectionWithdrawalReason]
        if isinstance(_withdrawal_reason, Unset):
            withdrawal_reason = UNSET
        else:
            withdrawal_reason = ProjectInterconnectionWithdrawalReason(_withdrawal_reason)

        estimated_cost_of_studies_and_fees = d.pop("estimatedCostOfStudiesAndFees", UNSET)

        estimated_cost_of_system_upgrades = d.pop("estimatedCostOfSystemUpgrades", UNSET)

        final_cost_of_interconnection = d.pop("finalCostOfInterconnection", UNSET)

        project_interconnection = cls(
            ieee_1547_reactive_power_category=ieee_1547_reactive_power_category,
            ieee_1547_disturbance_category=ieee_1547_disturbance_category,
            fips_location=fips_location,
            withdrawal_reason=withdrawal_reason,
            estimated_cost_of_studies_and_fees=estimated_cost_of_studies_and_fees,
            estimated_cost_of_system_upgrades=estimated_cost_of_system_upgrades,
            final_cost_of_interconnection=final_cost_of_interconnection,
        )

        project_interconnection.additional_properties = d
        return project_interconnection

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
