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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class BulkPurchaseUpdate(BaseModel):
    """
    BulkPurchaseUpdate
    """ # noqa: E501
    purchase_ids: List[StrictInt] = Field(description="Purchase id's which will be updated.", alias="purchaseIds")
    payment_status: Optional[StrictStr] = Field(default=None, description="Payment status to update.", alias="paymentStatus")
    external_ref: Optional[StrictStr] = Field(default=None, description="External reference to update.", alias="externalRef")
    received: Optional[StrictBool] = Field(default=None, description="Updates whether PO is received.")
    currency_code: Optional[StrictStr] = Field(default=None, alias="currencyCode")
    payment_ref: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=45)]] = Field(default=None, alias="paymentRef")
    payment_reference_number: Optional[StrictStr] = Field(default=None, alias="paymentReferenceNumber")
    payment_method: Optional[StrictStr] = Field(default=None, alias="paymentMethod")
    vendor_id: Optional[StrictInt] = Field(default=None, alias="vendorId")
    cooperative: Optional[StrictBool] = None
    status: Optional[StrictStr] = None
    split_amount: Optional[Union[Annotated[float, Field(le=100, strict=True, ge=0)], Annotated[int, Field(le=100, strict=True, ge=0)]]] = Field(default=None, alias="splitAmount")
    __properties: ClassVar[List[str]] = ["purchaseIds", "paymentStatus", "externalRef", "received", "currencyCode", "paymentRef", "paymentReferenceNumber", "paymentMethod", "vendorId", "cooperative", "status", "splitAmount"]

    @field_validator('payment_status')
    def payment_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UNPAID', 'PAID', 'PARTIAL', 'VOID']):
            raise ValueError("must be one of enum values ('UNPAID', 'PAID', 'PARTIAL', 'VOID')")
        return value

    @field_validator('currency_code')
    def currency_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['USD', 'CAD', 'EUR', 'GBP', 'JPY', 'BRL', 'XBT', 'AUD', 'MXN']):
            raise ValueError("must be one of enum values ('USD', 'CAD', 'EUR', 'GBP', 'JPY', 'BRL', 'XBT', 'AUD', 'MXN')")
        return value

    @field_validator('payment_method')
    def payment_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CREDITCARD', 'CASH', 'CHECK', 'PAYPAL', 'TRADE', 'VENMO', 'OTHER', 'ACCRUEDCREDIT', 'ACH', 'AR', 'AP', 'EVOPAY', 'MULTIPLE', 'COMPLIMENTARY', 'CUSTOMER_CREDIT', 'ZELLE']):
            raise ValueError("must be one of enum values ('CREDITCARD', 'CASH', 'CHECK', 'PAYPAL', 'TRADE', 'VENMO', 'OTHER', 'ACCRUEDCREDIT', 'ACH', 'AR', 'AP', 'EVOPAY', 'MULTIPLE', 'COMPLIMENTARY', 'CUSTOMER_CREDIT', 'ZELLE')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CONTACT_NEEDED', 'COMPLETED', 'DELIVERY_FAILURE', 'EVENT_CANCELLED', 'EVENT_RESCHEDULED', 'INVESTIGATION_CLOSED', 'INVESTIGATION_CLOSED_BUYER_FAVOR', 'INVESTIGATION_CLOSED_SELLER_FAVOR', 'INVESTIGATION_PENDING', 'MANAGER_REVIEW', 'ORDER_PARTIALLY_VOID_CANCELLED', 'ORDER_VOID_CANCELLED', 'WAITING_FOR_RESPONSE']):
            raise ValueError("must be one of enum values ('CONTACT_NEEDED', 'COMPLETED', 'DELIVERY_FAILURE', 'EVENT_CANCELLED', 'EVENT_RESCHEDULED', 'INVESTIGATION_CLOSED', 'INVESTIGATION_CLOSED_BUYER_FAVOR', 'INVESTIGATION_CLOSED_SELLER_FAVOR', 'INVESTIGATION_PENDING', 'MANAGER_REVIEW', 'ORDER_PARTIALLY_VOID_CANCELLED', 'ORDER_VOID_CANCELLED', 'WAITING_FOR_RESPONSE')")
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
        """Create an instance of BulkPurchaseUpdate from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BulkPurchaseUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "purchaseIds": obj.get("purchaseIds"),
            "paymentStatus": obj.get("paymentStatus"),
            "externalRef": obj.get("externalRef"),
            "received": obj.get("received"),
            "currencyCode": obj.get("currencyCode"),
            "paymentRef": obj.get("paymentRef"),
            "paymentReferenceNumber": obj.get("paymentReferenceNumber"),
            "paymentMethod": obj.get("paymentMethod"),
            "vendorId": obj.get("vendorId"),
            "cooperative": obj.get("cooperative"),
            "status": obj.get("status"),
            "splitAmount": obj.get("splitAmount")
        })
        return _obj


