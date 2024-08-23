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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from skybox_openapi_client.models.invoice_delivery_link import InvoiceDeliveryLink
from skybox_openapi_client.models.invoice_note import InvoiceNote
from skybox_openapi_client.models.invoice_payment import InvoicePayment
from skybox_openapi_client.models.line import Line
from typing import Optional, Set
from typing_extensions import Self

class Invoice(BaseModel):
    """
    Invoice
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Required for updates, ignored on inserts.")
    customer_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, alias="customerId")
    account_id: Optional[StrictInt] = Field(default=None, alias="accountId")
    internal_id: Optional[StrictInt] = Field(default=None, alias="internalId")
    lines: List[Line]
    sales_term: StrictStr = Field(alias="salesTerm")
    payment_method: Optional[StrictStr] = Field(default=None, alias="paymentMethod")
    payment_ref: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=45)]] = Field(default=None, alias="paymentRef")
    delivery_method: Optional[StrictStr] = Field(default=None, alias="deliveryMethod")
    shipping_address_id: Optional[StrictInt] = Field(default=None, alias="shippingAddressId")
    billing_address_id: Optional[StrictInt] = Field(default=None, alias="billingAddressId")
    tax_amount: Union[StrictFloat, StrictInt] = Field(alias="taxAmount")
    shipping_amount: Union[StrictFloat, StrictInt] = Field(alias="shippingAmount")
    other_amount: Union[StrictFloat, StrictInt] = Field(alias="otherAmount")
    internal_notes: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50000)]] = Field(default=None, alias="internalNotes")
    public_notes: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50000)]] = Field(default=None, alias="publicNotes")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    last_update: Optional[datetime] = Field(default=None, alias="lastUpdate")
    due_date: Optional[datetime] = Field(default=None, alias="dueDate")
    tags: Optional[StrictStr] = None
    created_by: Optional[StrictStr] = Field(default=None, alias="createdBy")
    last_update_by: Optional[StrictStr] = Field(default=None, alias="lastUpdateBy")
    payment_status: StrictStr = Field(description="Payment status.", alias="paymentStatus")
    fulfillment_status: StrictStr = Field(description="Inventory fulfillment status.", alias="fulfillmentStatus")
    external_ref: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="External reference number for invoice", alias="externalRef")
    airbill: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    currency_code: Optional[StrictStr] = Field(default=None, alias="currencyCode")
    payments: Optional[List[InvoicePayment]] = None
    invoice_delivery_link: Optional[InvoiceDeliveryLink] = Field(default=None, alias="invoiceDeliveryLink")
    notes: Optional[List[InvoiceNote]] = None
    fulfillment_date: Optional[datetime] = Field(default=None, alias="fulfillmentDate")
    fulfillment_by_user_id: Optional[StrictInt] = Field(default=None, alias="fulfillmentByUserId")
    outstanding_balance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="outstandingBalance")
    barcodes_entered: Optional[StrictBool] = Field(default=None, alias="barcodesEntered")
    external_ticket_id_entered: Optional[StrictBool] = Field(default=None, alias="externalTicketIdEntered")
    files_uploaded: Optional[StrictBool] = Field(default=None, alias="filesUploaded")
    __properties: ClassVar[List[str]] = ["id", "customerId", "accountId", "internalId", "lines", "salesTerm", "paymentMethod", "paymentRef", "deliveryMethod", "shippingAddressId", "billingAddressId", "taxAmount", "shippingAmount", "otherAmount", "internalNotes", "publicNotes", "createdDate", "lastUpdate", "dueDate", "tags", "createdBy", "lastUpdateBy", "paymentStatus", "fulfillmentStatus", "externalRef", "airbill", "status", "currencyCode", "payments", "invoiceDeliveryLink", "notes", "fulfillmentDate", "fulfillmentByUserId", "outstandingBalance", "barcodesEntered", "externalTicketIdEntered", "filesUploaded"]

    @field_validator('sales_term')
    def sales_term_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['NET0', 'NET10', 'NET15', 'NET25', 'NET30', 'NET45', 'NET60']):
            raise ValueError("must be one of enum values ('NET0', 'NET10', 'NET15', 'NET25', 'NET30', 'NET45', 'NET60')")
        return value

    @field_validator('payment_method')
    def payment_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CREDITCARD', 'CASH', 'CHECK', 'PAYPAL', 'TRADE', 'VENMO', 'OTHER', 'ACCRUEDCREDIT', 'ACH', 'AR', 'AP', 'EVOPAY', 'MULTIPLE', 'COMPLIMENTARY', 'CUSTOMER_CREDIT', 'ZELLE']):
            raise ValueError("must be one of enum values ('CREDITCARD', 'CASH', 'CHECK', 'PAYPAL', 'TRADE', 'VENMO', 'OTHER', 'ACCRUEDCREDIT', 'ACH', 'AR', 'AP', 'EVOPAY', 'MULTIPLE', 'COMPLIMENTARY', 'CUSTOMER_CREDIT', 'ZELLE')")
        return value

    @field_validator('delivery_method')
    def delivery_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['COURIER', 'EMAIL', 'USPS', 'UPS', 'FEDEX', 'WILLCALL', 'PAPERLESS', 'MEETANDGREET', 'FLASHSEATS', 'MOBILE_DELIVERY', 'OFFICE_PICKUP', 'OTHER']):
            raise ValueError("must be one of enum values ('COURIER', 'EMAIL', 'USPS', 'UPS', 'FEDEX', 'WILLCALL', 'PAPERLESS', 'MEETANDGREET', 'FLASHSEATS', 'MOBILE_DELIVERY', 'OFFICE_PICKUP', 'OTHER')")
        return value

    @field_validator('payment_status')
    def payment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['UNPAID', 'PAID', 'PARTIAL', 'VOID']):
            raise ValueError("must be one of enum values ('UNPAID', 'PAID', 'PARTIAL', 'VOID')")
        return value

    @field_validator('fulfillment_status')
    def fulfillment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PENDING', 'COMPLETE']):
            raise ValueError("must be one of enum values ('PENDING', 'COMPLETE')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CONTACT_NEEDED', 'COMPLETED', 'DELIVERY_FAILURE', 'EVENT_CANCELLED', 'EVENT_RESCHEDULED', 'INVESTIGATION_CLOSED', 'INVESTIGATION_CLOSED_BUYER_FAVOR', 'INVESTIGATION_CLOSED_SELLER_FAVOR', 'INVESTIGATION_PENDING', 'MANAGER_REVIEW', 'ORDER_PARTIALLY_VOID_CANCELLED', 'ORDER_VOID_CANCELLED', 'WAITING_FOR_RESPONSE']):
            raise ValueError("must be one of enum values ('CONTACT_NEEDED', 'COMPLETED', 'DELIVERY_FAILURE', 'EVENT_CANCELLED', 'EVENT_RESCHEDULED', 'INVESTIGATION_CLOSED', 'INVESTIGATION_CLOSED_BUYER_FAVOR', 'INVESTIGATION_CLOSED_SELLER_FAVOR', 'INVESTIGATION_PENDING', 'MANAGER_REVIEW', 'ORDER_PARTIALLY_VOID_CANCELLED', 'ORDER_VOID_CANCELLED', 'WAITING_FOR_RESPONSE')")
        return value

    @field_validator('currency_code')
    def currency_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['USD', 'CAD', 'EUR', 'GBP', 'JPY', 'BRL', 'XBT', 'AUD', 'MXN']):
            raise ValueError("must be one of enum values ('USD', 'CAD', 'EUR', 'GBP', 'JPY', 'BRL', 'XBT', 'AUD', 'MXN')")
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
        """Create an instance of Invoice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item_lines in self.lines:
                if _item_lines:
                    _items.append(_item_lines.to_dict())
            _dict['lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payments (list)
        _items = []
        if self.payments:
            for _item_payments in self.payments:
                if _item_payments:
                    _items.append(_item_payments.to_dict())
            _dict['payments'] = _items
        # override the default output from pydantic by calling `to_dict()` of invoice_delivery_link
        if self.invoice_delivery_link:
            _dict['invoiceDeliveryLink'] = self.invoice_delivery_link.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item_notes in self.notes:
                if _item_notes:
                    _items.append(_item_notes.to_dict())
            _dict['notes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Invoice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "customerId": obj.get("customerId"),
            "accountId": obj.get("accountId"),
            "internalId": obj.get("internalId"),
            "lines": [Line.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None,
            "salesTerm": obj.get("salesTerm"),
            "paymentMethod": obj.get("paymentMethod"),
            "paymentRef": obj.get("paymentRef"),
            "deliveryMethod": obj.get("deliveryMethod"),
            "shippingAddressId": obj.get("shippingAddressId"),
            "billingAddressId": obj.get("billingAddressId"),
            "taxAmount": obj.get("taxAmount"),
            "shippingAmount": obj.get("shippingAmount"),
            "otherAmount": obj.get("otherAmount"),
            "internalNotes": obj.get("internalNotes"),
            "publicNotes": obj.get("publicNotes"),
            "createdDate": obj.get("createdDate"),
            "lastUpdate": obj.get("lastUpdate"),
            "dueDate": obj.get("dueDate"),
            "tags": obj.get("tags"),
            "createdBy": obj.get("createdBy"),
            "lastUpdateBy": obj.get("lastUpdateBy"),
            "paymentStatus": obj.get("paymentStatus"),
            "fulfillmentStatus": obj.get("fulfillmentStatus"),
            "externalRef": obj.get("externalRef"),
            "airbill": obj.get("airbill"),
            "status": obj.get("status"),
            "currencyCode": obj.get("currencyCode"),
            "payments": [InvoicePayment.from_dict(_item) for _item in obj["payments"]] if obj.get("payments") is not None else None,
            "invoiceDeliveryLink": InvoiceDeliveryLink.from_dict(obj["invoiceDeliveryLink"]) if obj.get("invoiceDeliveryLink") is not None else None,
            "notes": [InvoiceNote.from_dict(_item) for _item in obj["notes"]] if obj.get("notes") is not None else None,
            "fulfillmentDate": obj.get("fulfillmentDate"),
            "fulfillmentByUserId": obj.get("fulfillmentByUserId"),
            "outstandingBalance": obj.get("outstandingBalance"),
            "barcodesEntered": obj.get("barcodesEntered"),
            "externalTicketIdEntered": obj.get("externalTicketIdEntered"),
            "filesUploaded": obj.get("filesUploaded")
        })
        return _obj


