# coding: utf-8

"""
    SkyBox API

    The SkyBox APIs allow our users to create, update, delete, and export information within the SkyBox platform. These APIs allow SkyBox to be extensible, giving you the flexibility to grow, develop, and integrate third-party tooling to help scale out your business. To begin using the SkyBox APIs, you will need to generate two unique tokens: an Application_Token and an API Token.  To request a unique Application_Token, click here (<a href='https://skybox.vividseats.com/application-sign-up'>https://skybox.vividseats.com/application-sign-up</a>) and refer to this <a href='https://skybox.zendesk.com/hc/en-us/articles/6769735238043-Getting-Started-with-Skybox-APIs'>Zendesk Article</a> for detailed instructions on getting started with SkyBox APIs.  To generate an API Token when logged in to SkyBox, click on the drop-down under 'Logged In As:', select 'External Accounts', and then select 'API Invitation +'. A modal will appear and you will be prompted to enter the email address to which you want the token sent as well as to provide a brief description of the account.  Once you have both your Application_Token and API Token, there are two ways in which you can make requests: through the UI and through a third party. See below for detailed steps for each process.  Requests through the UI:  To begin, enter your Account ID in the X-Account field. Once complete, select _Authorize_. Next, enter your API Token in the X-Api-Token field. If you do not currently have an API Token, please follow the steps above to request one. Once complete, select _Authorize_. Last, enter your Application_Token in the X-Application-Token field. If you do not have an Application_Token, a sample is provided or you can follow the link above to request one. Once complete, select _Authorize_.  Requests through a third party (i.e. Postman):  The same information is required as it is through the UI, but it will be passed in through headers. It should look something like this:  X-Account: Account ID goes here!  X-Api-Token: API Token goes here!  X-Application-Token: Application_Token goes here!  Once these three items are successfully passed in as headers, you will be able to make sample requests.  <h2><a href='https://skybox.zendesk.com/hc/en-us/articles/5999881334427-SkyBox-API-Rate-Limits'>API Rate Limits</a> </h2>  A rate limit consists of two variables: an interval and a limit. An interval is a period of time, measured in seconds. A limit is the number of calls that can be made to an endpoint in an interval.  For example, SkyBox’s ‘GET /reports/‘ endpoint has an interval of 1 second and a limit of 1 call per interval. This means that this endpoint has a rate limit of 1 call/second.  Each endpoint, and its respective rate limit, is displayed in this <a href='https://skybox.zendesk.com/hc/en-us/articles/5999881334427-SkyBox-API-Rate-Limits'>Support Article</a>. If the endpoint is not listed, its rate limit is the default, indicated by the ‘*’ at the bottom of the table. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from skybox_openapi_client.models.event import Event
from skybox_openapi_client.models.event_mapping import EventMapping
from skybox_openapi_client.models.hold import Hold
from skybox_openapi_client.models.purchase import Purchase
from skybox_openapi_client.models.tax_tags import TaxTags
from skybox_openapi_client.models.ticket import Ticket
from typing import Optional, Set
from typing_extensions import Self

class PurchasedInventorySummary(BaseModel):
    """
    PurchasedInventorySummary
    """ # noqa: E501
    in_hand_date: Optional[date] = Field(default=None, description="The  date that the tickets will be in hand", alias="inHandDate")
    id: Optional[StrictInt] = Field(default=None, description="Required for updates, ignored on inserts.")
    account_id: Optional[StrictInt] = Field(default=None, alias="accountId")
    event_id: StrictInt = Field(description="Required on inserts if event mapping is empty.", alias="eventId")
    quantity: Annotated[int, Field(strict=True, ge=1)] = Field(description="Number of tickets available, implied from tickets array if present.")
    notes: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1000)]] = None
    section: Annotated[str, Field(min_length=1, strict=True, max_length=51)]
    friendly_section: Optional[StrictStr] = Field(default=None, description="Friendly name for Section.", alias="friendlySection")
    row: Annotated[str, Field(min_length=1, strict=True, max_length=44)]
    friendly_row: Optional[StrictStr] = Field(default=None, description="Friendly name for Row.", alias="friendlyRow")
    second_row: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=44)]] = Field(default=None, alias="secondRow")
    low_seat: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Required on inserts if tickets array is empty.", alias="lowSeat")
    high_seat: Optional[StrictInt] = Field(default=None, description="Required on inserts if tickets array is empty.", alias="highSeat")
    cost: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]
    taxed_cost: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, alias="taxedCost")
    taxed_cost_average: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, alias="taxedCostAverage")
    face_value: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, alias="faceValue")
    tickets: Optional[List[Ticket]] = None
    ticket_ids: Optional[List[StrictInt]] = Field(default=None, alias="ticketIds")
    stock_type: StrictStr = Field(alias="stockType")
    split_type: StrictStr = Field(description="How the tickets may be split", alias="splitType")
    custom_split: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="customSplit")
    list_price: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, alias="listPrice")
    vivid_retail_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="vividRetailPrice")
    expected_value: Optional[Union[Annotated[float, Field(strict=True, ge=0.0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, alias="expectedValue")
    public_notes: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1000)]] = Field(default=None, alias="publicNotes")
    attributes: Optional[List[StrictStr]] = None
    status: Optional[StrictStr] = None
    in_hand_days_before_event: Optional[StrictInt] = Field(default=None, alias="inHandDaysBeforeEvent")
    last_price_update: Optional[datetime] = Field(default=None, alias="lastPriceUpdate")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    created_by: Optional[StrictStr] = Field(default=None, alias="createdBy")
    created_by_user_id: Optional[StrictInt] = Field(default=None, alias="createdByUserId")
    last_update: Optional[datetime] = Field(default=None, alias="lastUpdate")
    last_update_by: Optional[StrictStr] = Field(default=None, alias="lastUpdateBy")
    last_delta_update: Optional[datetime] = Field(default=None, alias="lastDeltaUpdate")
    version: Optional[StrictInt] = None
    tags: Optional[StrictStr] = None
    seat_type: StrictStr = Field(description="Seat type.", alias="seatType")
    event_mapping: Optional[EventMapping] = Field(default=None, alias="eventMapping")
    mapping_id: Optional[StrictInt] = Field(default=None, description="Mapping id if this inventory was sent to mapping. Read-only.", alias="mappingId")
    exchange_pos_id: Optional[StrictInt] = Field(default=None, description="Id to provide to exchanges for listing delete and regeneration compatibility. This id is automatically regenerated when files or bar codes are edited or remove and section or rows get updated. Read-only.", alias="exchangePosId")
    broadcast: Optional[StrictBool] = Field(default=None, description="Broadcast.")
    zone_seating: Optional[StrictBool] = Field(default=None, description="Zone seating", alias="zoneSeating")
    electronic_transfer: Optional[StrictBool] = Field(default=None, alias="electronicTransfer")
    opt_out_auto_price: Optional[StrictBool] = Field(default=None, alias="optOutAutoPrice")
    hide_seat_numbers: Optional[StrictBool] = Field(default=None, description="Hide seat numbers from exchanges.", alias="hideSeatNumbers")
    vsr_option: Optional[StrictStr] = Field(default=None, alias="vsrOption")
    replenishment_group_id: Optional[StrictInt] = Field(default=None, alias="replenishmentGroupId")
    replenishment_group: Optional[StrictStr] = Field(default=None, alias="replenishmentGroup")
    shown_quantity: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, alias="shownQuantity")
    integrated_listing: Optional[StrictBool] = Field(default=None, alias="integratedListing")
    tickets_merged: Optional[StrictBool] = Field(default=None, alias="ticketsMerged")
    tickets_split: Optional[StrictBool] = Field(default=None, alias="ticketsSplit")
    audit_note: Optional[StrictStr] = Field(default=None, alias="auditNote")
    files_uploaded: Optional[StrictBool] = Field(default=None, alias="filesUploaded")
    bar_codes_entered: Optional[StrictBool] = Field(default=None, alias="barCodesEntered")
    external_ticket_id_entered: Optional[StrictBool] = Field(default=None, alias="externalTicketIdEntered")
    instant_transfer: Optional[StrictBool] = Field(default=None, description="Is instant transfer.", alias="instantTransfer")
    seat_numbers: Optional[StrictStr] = Field(default=None, alias="seatNumbers")
    listed: Optional[StrictBool] = None
    consignment_status: Optional[StrictStr] = Field(default=None, alias="consignmentStatus")
    cooperative: Optional[StrictBool] = None
    hold_id: Optional[StrictInt] = Field(default=None, alias="holdId")
    hold: Optional[Hold] = None
    unit_cost_average: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Unit Cost Average", alias="unitCostAverage")
    face_value_average: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="faceValueAverage")
    currencies: Optional[List[StrictStr]] = None
    received: Optional[StrictStr] = None
    vendor_id: Optional[List[StrictInt]] = Field(default=None, alias="vendorId")
    in_hand: Optional[StrictBool] = Field(default=None, alias="inHand")
    has_taxed_cost: Optional[StrictStr] = Field(default=None, alias="hasTaxedCost")
    days_old: Optional[StrictInt] = Field(default=None, description="Days old since the listing was created", alias="daysOld")
    vendor_display_name: Optional[StrictStr] = Field(default=None, alias="vendorDisplayName")
    purchase: Optional[Purchase] = None
    invoice_id: Optional[List[StrictInt]] = Field(default=None, alias="invoiceId")
    inventory_ids: Optional[List[StrictInt]] = Field(default=None, alias="inventoryIds")
    purchase_line_id: Optional[StrictInt] = Field(default=None, alias="purchaseLineId")
    ticket_status: Optional[StrictStr] = Field(default=None, alias="ticketStatus")
    tax_tags: Optional[TaxTags] = Field(default=None, alias="taxTags")
    ticket_id_string: Optional[StrictStr] = Field(default=None, alias="ticketIdString")
    event: Optional[Event] = None
    __properties: ClassVar[List[str]] = ["inHandDate", "id", "accountId", "eventId", "quantity", "notes", "section", "friendlySection", "row", "friendlyRow", "secondRow", "lowSeat", "highSeat", "cost", "taxedCost", "taxedCostAverage", "faceValue", "tickets", "ticketIds", "stockType", "splitType", "customSplit", "listPrice", "vividRetailPrice", "expectedValue", "publicNotes", "attributes", "status", "inHandDaysBeforeEvent", "lastPriceUpdate", "createdDate", "createdBy", "createdByUserId", "lastUpdate", "lastUpdateBy", "lastDeltaUpdate", "version", "tags", "seatType", "eventMapping", "mappingId", "exchangePosId", "broadcast", "zoneSeating", "electronicTransfer", "optOutAutoPrice", "hideSeatNumbers", "vsrOption", "replenishmentGroupId", "replenishmentGroup", "shownQuantity", "integratedListing", "ticketsMerged", "ticketsSplit", "auditNote", "filesUploaded", "barCodesEntered", "externalTicketIdEntered", "instantTransfer", "seatNumbers", "listed", "consignmentStatus", "cooperative", "holdId", "hold", "unitCostAverage", "faceValueAverage", "currencies", "received", "vendorId", "inHand", "hasTaxedCost", "daysOld", "vendorDisplayName", "purchase", "invoiceId", "inventoryIds", "purchaseLineId", "ticketStatus", "taxTags", "ticketIdString", "event"]

    @field_validator('stock_type')
    def stock_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['HARD', 'ELECTRONIC', 'FLASH', 'PAPERLESS', 'PAPERLESS_CARD', 'MOBILE_TRANSFER', 'MOBILE_SCREENCAP']):
            raise ValueError("must be one of enum values ('HARD', 'ELECTRONIC', 'FLASH', 'PAPERLESS', 'PAPERLESS_CARD', 'MOBILE_TRANSFER', 'MOBILE_SCREENCAP')")
        return value

    @field_validator('split_type')
    def split_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DEFAULT', 'ANY', 'CUSTOM', 'NEVERLEAVEONE']):
            raise ValueError("must be one of enum values ('DEFAULT', 'ANY', 'CUSTOM', 'NEVERLEAVEONE')")
        return value

    @field_validator('custom_split')
    def custom_split_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d*(,\d*)*$", value):
            raise ValueError(r"must validate the regular expression /^\d*(,\d*)*$/")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AVAILABLE', 'ON_HOLD', 'DEPLETED']):
            raise ValueError("must be one of enum values ('AVAILABLE', 'ON_HOLD', 'DEPLETED')")
        return value

    @field_validator('seat_type')
    def seat_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CONSECUTIVE', 'ALTERNATING', 'GA', 'PIGGYBACK']):
            raise ValueError("must be one of enum values ('CONSECUTIVE', 'ALTERNATING', 'GA', 'PIGGYBACK')")
        return value

    @field_validator('vsr_option')
    def vsr_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ALL', 'EVENT_INVENTORY', 'OTHER', 'NONE']):
            raise ValueError("must be one of enum values ('ALL', 'EVENT_INVENTORY', 'OTHER', 'NONE')")
        return value

    @field_validator('currencies')
    def currencies_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['USD', 'CAD', 'EUR', 'GBP', 'JPY', 'BRL', 'XBT', 'AUD', 'MXN']):
                raise ValueError("each list item must be one of ('USD', 'CAD', 'EUR', 'GBP', 'JPY', 'BRL', 'XBT', 'AUD', 'MXN')")
        return value

    @field_validator('ticket_status')
    def ticket_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AVAILABLE', 'SOLD', 'ERROR', 'CANCELLED']):
            raise ValueError("must be one of enum values ('AVAILABLE', 'SOLD', 'ERROR', 'CANCELLED')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PurchasedInventorySummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "tickets_merged",
            "tickets_split",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tickets (list)
        _items = []
        if self.tickets:
            for _item_tickets in self.tickets:
                if _item_tickets:
                    _items.append(_item_tickets.to_dict())
            _dict['tickets'] = _items
        # override the default output from pydantic by calling `to_dict()` of event_mapping
        if self.event_mapping:
            _dict['eventMapping'] = self.event_mapping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hold
        if self.hold:
            _dict['hold'] = self.hold.to_dict()
        # override the default output from pydantic by calling `to_dict()` of purchase
        if self.purchase:
            _dict['purchase'] = self.purchase.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_tags
        if self.tax_tags:
            _dict['taxTags'] = self.tax_tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PurchasedInventorySummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "inHandDate": obj.get("inHandDate"),
            "id": obj.get("id"),
            "accountId": obj.get("accountId"),
            "eventId": obj.get("eventId"),
            "quantity": obj.get("quantity"),
            "notes": obj.get("notes"),
            "section": obj.get("section"),
            "friendlySection": obj.get("friendlySection"),
            "row": obj.get("row"),
            "friendlyRow": obj.get("friendlyRow"),
            "secondRow": obj.get("secondRow"),
            "lowSeat": obj.get("lowSeat"),
            "highSeat": obj.get("highSeat"),
            "cost": obj.get("cost"),
            "taxedCost": obj.get("taxedCost"),
            "taxedCostAverage": obj.get("taxedCostAverage"),
            "faceValue": obj.get("faceValue"),
            "tickets": [Ticket.from_dict(_item) for _item in obj["tickets"]] if obj.get("tickets") is not None else None,
            "ticketIds": obj.get("ticketIds"),
            "stockType": obj.get("stockType"),
            "splitType": obj.get("splitType"),
            "customSplit": obj.get("customSplit"),
            "listPrice": obj.get("listPrice"),
            "vividRetailPrice": obj.get("vividRetailPrice"),
            "expectedValue": obj.get("expectedValue"),
            "publicNotes": obj.get("publicNotes"),
            "attributes": obj.get("attributes"),
            "status": obj.get("status"),
            "inHandDaysBeforeEvent": obj.get("inHandDaysBeforeEvent"),
            "lastPriceUpdate": obj.get("lastPriceUpdate"),
            "createdDate": obj.get("createdDate"),
            "createdBy": obj.get("createdBy"),
            "createdByUserId": obj.get("createdByUserId"),
            "lastUpdate": obj.get("lastUpdate"),
            "lastUpdateBy": obj.get("lastUpdateBy"),
            "lastDeltaUpdate": obj.get("lastDeltaUpdate"),
            "version": obj.get("version"),
            "tags": obj.get("tags"),
            "seatType": obj.get("seatType"),
            "eventMapping": EventMapping.from_dict(obj["eventMapping"]) if obj.get("eventMapping") is not None else None,
            "mappingId": obj.get("mappingId"),
            "exchangePosId": obj.get("exchangePosId"),
            "broadcast": obj.get("broadcast"),
            "zoneSeating": obj.get("zoneSeating"),
            "electronicTransfer": obj.get("electronicTransfer"),
            "optOutAutoPrice": obj.get("optOutAutoPrice"),
            "hideSeatNumbers": obj.get("hideSeatNumbers"),
            "vsrOption": obj.get("vsrOption"),
            "replenishmentGroupId": obj.get("replenishmentGroupId"),
            "replenishmentGroup": obj.get("replenishmentGroup"),
            "shownQuantity": obj.get("shownQuantity"),
            "integratedListing": obj.get("integratedListing"),
            "ticketsMerged": obj.get("ticketsMerged"),
            "ticketsSplit": obj.get("ticketsSplit"),
            "auditNote": obj.get("auditNote"),
            "filesUploaded": obj.get("filesUploaded"),
            "barCodesEntered": obj.get("barCodesEntered"),
            "externalTicketIdEntered": obj.get("externalTicketIdEntered"),
            "instantTransfer": obj.get("instantTransfer"),
            "seatNumbers": obj.get("seatNumbers"),
            "listed": obj.get("listed"),
            "consignmentStatus": obj.get("consignmentStatus"),
            "cooperative": obj.get("cooperative"),
            "holdId": obj.get("holdId"),
            "hold": Hold.from_dict(obj["hold"]) if obj.get("hold") is not None else None,
            "unitCostAverage": obj.get("unitCostAverage"),
            "faceValueAverage": obj.get("faceValueAverage"),
            "currencies": obj.get("currencies"),
            "received": obj.get("received"),
            "vendorId": obj.get("vendorId"),
            "inHand": obj.get("inHand"),
            "hasTaxedCost": obj.get("hasTaxedCost"),
            "daysOld": obj.get("daysOld"),
            "vendorDisplayName": obj.get("vendorDisplayName"),
            "purchase": Purchase.from_dict(obj["purchase"]) if obj.get("purchase") is not None else None,
            "invoiceId": obj.get("invoiceId"),
            "inventoryIds": obj.get("inventoryIds"),
            "purchaseLineId": obj.get("purchaseLineId"),
            "ticketStatus": obj.get("ticketStatus"),
            "taxTags": TaxTags.from_dict(obj["taxTags"]) if obj.get("taxTags") is not None else None,
            "ticketIdString": obj.get("ticketIdString"),
            "event": Event.from_dict(obj["event"]) if obj.get("event") is not None else None
        })
        return _obj


