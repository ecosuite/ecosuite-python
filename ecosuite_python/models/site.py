import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.site_preferred_option_for_co2_emissions_data import SitePreferredOptionForCO2EmissionsData
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_contacts_item import SiteContactsItem
    from ..models.site_links_item import SiteLinksItem


T = TypeVar("T", bound="Site")


@_attrs_define
class Site:
    """Refer to the /schemas/site endpoint for the full JSON Schema definition

    Attributes:
        code (str):
        name (str):
        address (str):
        town (str):
        state (str):
        lat (float):
        long (float):
        production_start_date (Union[Unset, datetime.date]):
        generation_start_date (Union[Unset, datetime.date]):
        consumption_start_date (Union[Unset, datetime.date]):
        storage_start_date (Union[Unset, datetime.date]):
        service_id (Union[Unset, str]):
        parcel_id (Union[Unset, str]):
        parcel_acreage (Union[Unset, str]):
        zoning_district (Union[Unset, str]):
        owner_of_record (Union[Unset, str]):
        location_id (Union[Unset, int]): The ID of a SolarNetwork location; used to retrieve weather details
        plant_id (Union[Unset, str]):
        utility (Union[Unset, str]):
        emissions_approximation_method (Union[Unset, SitePreferredOptionForCO2EmissionsData]):
        timezone (Union[Unset, str]):
        expected_daily_data (Union[Unset, float]):
        links (Union[Unset, List['SiteLinksItem']]):
        access_notes (Union[Unset, str]):
        contacts (Union[Unset, List['SiteContactsItem']]):
    """

    code: str
    name: str
    address: str
    town: str
    state: str
    lat: float
    long: float
    production_start_date: Union[Unset, datetime.date] = UNSET
    generation_start_date: Union[Unset, datetime.date] = UNSET
    consumption_start_date: Union[Unset, datetime.date] = UNSET
    storage_start_date: Union[Unset, datetime.date] = UNSET
    service_id: Union[Unset, str] = UNSET
    parcel_id: Union[Unset, str] = UNSET
    parcel_acreage: Union[Unset, str] = UNSET
    zoning_district: Union[Unset, str] = UNSET
    owner_of_record: Union[Unset, str] = UNSET
    location_id: Union[Unset, int] = UNSET
    plant_id: Union[Unset, str] = UNSET
    utility: Union[Unset, str] = UNSET
    emissions_approximation_method: Union[Unset, SitePreferredOptionForCO2EmissionsData] = UNSET
    timezone: Union[Unset, str] = UNSET
    expected_daily_data: Union[Unset, float] = UNSET
    links: Union[Unset, List["SiteLinksItem"]] = UNSET
    access_notes: Union[Unset, str] = UNSET
    contacts: Union[Unset, List["SiteContactsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        name = self.name

        address = self.address

        town = self.town

        state = self.state

        lat = self.lat

        long = self.long

        production_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.production_start_date, Unset):
            production_start_date = self.production_start_date.isoformat()

        generation_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.generation_start_date, Unset):
            generation_start_date = self.generation_start_date.isoformat()

        consumption_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.consumption_start_date, Unset):
            consumption_start_date = self.consumption_start_date.isoformat()

        storage_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.storage_start_date, Unset):
            storage_start_date = self.storage_start_date.isoformat()

        service_id = self.service_id

        parcel_id = self.parcel_id

        parcel_acreage = self.parcel_acreage

        zoning_district = self.zoning_district

        owner_of_record = self.owner_of_record

        location_id = self.location_id

        plant_id = self.plant_id

        utility = self.utility

        emissions_approximation_method: Union[Unset, str] = UNSET
        if not isinstance(self.emissions_approximation_method, Unset):
            emissions_approximation_method = self.emissions_approximation_method.value

        timezone = self.timezone

        expected_daily_data = self.expected_daily_data

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        access_notes = self.access_notes

        contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
                "address": address,
                "town": town,
                "state": state,
                "lat": lat,
                "long": long,
            }
        )
        if production_start_date is not UNSET:
            field_dict["productionStartDate"] = production_start_date
        if generation_start_date is not UNSET:
            field_dict["generationStartDate"] = generation_start_date
        if consumption_start_date is not UNSET:
            field_dict["consumptionStartDate"] = consumption_start_date
        if storage_start_date is not UNSET:
            field_dict["storageStartDate"] = storage_start_date
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if parcel_id is not UNSET:
            field_dict["parcelID"] = parcel_id
        if parcel_acreage is not UNSET:
            field_dict["parcelAcreage"] = parcel_acreage
        if zoning_district is not UNSET:
            field_dict["zoningDistrict"] = zoning_district
        if owner_of_record is not UNSET:
            field_dict["ownerOfRecord"] = owner_of_record
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if plant_id is not UNSET:
            field_dict["plantId"] = plant_id
        if utility is not UNSET:
            field_dict["utility"] = utility
        if emissions_approximation_method is not UNSET:
            field_dict["emissionsApproximationMethod"] = emissions_approximation_method
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if expected_daily_data is not UNSET:
            field_dict["expectedDailyData"] = expected_daily_data
        if links is not UNSET:
            field_dict["links"] = links
        if access_notes is not UNSET:
            field_dict["accessNotes"] = access_notes
        if contacts is not UNSET:
            field_dict["contacts"] = contacts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.site_contacts_item import SiteContactsItem
        from ..models.site_links_item import SiteLinksItem

        d = src_dict.copy()
        code = d.pop("code")

        name = d.pop("name")

        address = d.pop("address")

        town = d.pop("town")

        state = d.pop("state")

        lat = d.pop("lat")

        long = d.pop("long")

        _production_start_date = d.pop("productionStartDate", UNSET)
        production_start_date: Union[Unset, datetime.date]
        if isinstance(_production_start_date, Unset):
            production_start_date = UNSET
        else:
            production_start_date = isoparse(_production_start_date).date()

        _generation_start_date = d.pop("generationStartDate", UNSET)
        generation_start_date: Union[Unset, datetime.date]
        if isinstance(_generation_start_date, Unset):
            generation_start_date = UNSET
        else:
            generation_start_date = isoparse(_generation_start_date).date()

        _consumption_start_date = d.pop("consumptionStartDate", UNSET)
        consumption_start_date: Union[Unset, datetime.date]
        if isinstance(_consumption_start_date, Unset):
            consumption_start_date = UNSET
        else:
            consumption_start_date = isoparse(_consumption_start_date).date()

        _storage_start_date = d.pop("storageStartDate", UNSET)
        storage_start_date: Union[Unset, datetime.date]
        if isinstance(_storage_start_date, Unset):
            storage_start_date = UNSET
        else:
            storage_start_date = isoparse(_storage_start_date).date()

        service_id = d.pop("serviceId", UNSET)

        parcel_id = d.pop("parcelID", UNSET)

        parcel_acreage = d.pop("parcelAcreage", UNSET)

        zoning_district = d.pop("zoningDistrict", UNSET)

        owner_of_record = d.pop("ownerOfRecord", UNSET)

        location_id = d.pop("locationId", UNSET)

        plant_id = d.pop("plantId", UNSET)

        utility = d.pop("utility", UNSET)

        _emissions_approximation_method = d.pop("emissionsApproximationMethod", UNSET)
        emissions_approximation_method: Union[Unset, SitePreferredOptionForCO2EmissionsData]
        if isinstance(_emissions_approximation_method, Unset):
            emissions_approximation_method = UNSET
        else:
            emissions_approximation_method = SitePreferredOptionForCO2EmissionsData(_emissions_approximation_method)

        timezone = d.pop("timezone", UNSET)

        expected_daily_data = d.pop("expectedDailyData", UNSET)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = SiteLinksItem.from_dict(links_item_data)

            links.append(links_item)

        access_notes = d.pop("accessNotes", UNSET)

        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = SiteContactsItem.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        site = cls(
            code=code,
            name=name,
            address=address,
            town=town,
            state=state,
            lat=lat,
            long=long,
            production_start_date=production_start_date,
            generation_start_date=generation_start_date,
            consumption_start_date=consumption_start_date,
            storage_start_date=storage_start_date,
            service_id=service_id,
            parcel_id=parcel_id,
            parcel_acreage=parcel_acreage,
            zoning_district=zoning_district,
            owner_of_record=owner_of_record,
            location_id=location_id,
            plant_id=plant_id,
            utility=utility,
            emissions_approximation_method=emissions_approximation_method,
            timezone=timezone,
            expected_daily_data=expected_daily_data,
            links=links,
            access_notes=access_notes,
            contacts=contacts,
        )

        site.additional_properties = d
        return site

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
