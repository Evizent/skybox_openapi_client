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
from skybox_openapi_client.models.inventory import Inventory
from typing import Optional, Set
from typing_extensions import Self

class Line(BaseModel):
    """
    Line
    """ # noqa: E501
    id: Optional[StrictInt] = None
    account_id: StrictInt = Field(alias="accountId")
    target_id: Optional[StrictInt] = Field(default=None, alias="targetId")
    quantity: Optional[StrictInt] = None
    description: Optional[StrictStr] = Field(default=None, description="The description of the line. Ignored for inventory lines.")
    amount: Union[StrictFloat, StrictInt] = Field(description="The total for this line. Passed through to ticket.sellPrice or ticket.cost for inventory items.")
    line_type: Optional[StrictStr] = Field(default=None, alias="lineType")
    line_item_type: StrictStr = Field(description="The type of the line item.", alias="lineItemType")
    item_ids: Optional[List[StrictInt]] = Field(default=None, description="The itemIds, representing ticketIds if the line item is Inventory. Required for invoice line inserts, ignored otherwise.", alias="itemIds")
    inventory: Optional[Inventory] = None
    cancelled: Optional[StrictBool] = Field(default=None, description="True if the tickets on this line are cancelled, false otherwise. Read-only.")
    delete: Optional[StrictBool] = None
    cancel: Optional[StrictBool] = None
    fill_line_id: Optional[StrictInt] = Field(default=None, alias="fillLineId")
    inventory_ids: Optional[List[StrictInt]] = Field(default=None, alias="inventoryIds")
    created_date: Optional[datetime] = Field(default=None, alias="createdDate")
    created_by: Optional[StrictStr] = Field(default=None, alias="createdBy")
    last_update: Optional[datetime] = Field(default=None, alias="lastUpdate")
    last_update_by: Optional[StrictStr] = Field(default=None, alias="lastUpdateBy")
    __properties: ClassVar[List[str]] = ["id", "accountId", "targetId", "quantity", "description", "amount", "lineType", "lineItemType", "itemIds", "inventory", "cancelled", "delete", "cancel", "fillLineId", "inventoryIds", "createdDate", "createdBy", "lastUpdate", "lastUpdateBy"]

    @field_validator('line_type')
    def line_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PURCHASE', 'INVOICE']):
            raise ValueError("must be one of enum values ('PURCHASE', 'INVOICE')")
        return value

    @field_validator('line_item_type')
    def line_item_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['GENERIC', 'INVENTORY']):
            raise ValueError("must be one of enum values ('GENERIC', 'INVENTORY')")
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
        """Create an instance of Line from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of inventory
        if self.inventory:
            _dict['inventory'] = self.inventory.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Line from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "accountId": obj.get("accountId"),
            "targetId": obj.get("targetId"),
            "quantity": obj.get("quantity"),
            "description": obj.get("description"),
            "amount": obj.get("amount"),
            "lineType": obj.get("lineType"),
            "lineItemType": obj.get("lineItemType"),
            "itemIds": obj.get("itemIds"),
            "inventory": Inventory.from_dict(obj["inventory"]) if obj.get("inventory") is not None else None,
            "cancelled": obj.get("cancelled"),
            "delete": obj.get("delete"),
            "cancel": obj.get("cancel"),
            "fillLineId": obj.get("fillLineId"),
            "inventoryIds": obj.get("inventoryIds"),
            "createdDate": obj.get("createdDate"),
            "createdBy": obj.get("createdBy"),
            "lastUpdate": obj.get("lastUpdate"),
            "lastUpdateBy": obj.get("lastUpdateBy")
        })
        return _obj


