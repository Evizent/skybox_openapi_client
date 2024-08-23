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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    Address
    """ # noqa: E501
    id: Optional[StrictInt] = None
    account_id: Optional[StrictInt] = Field(default=None, alias="accountId")
    first_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, alias="firstName")
    last_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, alias="lastName")
    company: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = None
    address1: Annotated[str, Field(min_length=0, strict=True, max_length=255)]
    address2: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = None
    city: Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    state: StrictStr
    postal_code: Annotated[str, Field(min_length=1, strict=True, max_length=45)] = Field(alias="postalCode")
    country: Annotated[str, Field(min_length=1, strict=True, max_length=45)]
    phone1: Annotated[str, Field(min_length=0, strict=True, max_length=45)]
    phone2: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=45)]] = None
    fax: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=45)]] = None
    __properties: ClassVar[List[str]] = ["id", "accountId", "firstName", "lastName", "company", "address1", "address2", "city", "state", "postalCode", "country", "phone1", "phone2", "fax"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY', 'AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK', 'NT', 'NU', 'YT', 'OTHER', 'UNKNOWN']):
            raise ValueError("must be one of enum values ('AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY', 'AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK', 'NT', 'NU', 'YT', 'OTHER', 'UNKNOWN')")
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
        """Create an instance of Address from a JSON string"""
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
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "accountId": obj.get("accountId"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "company": obj.get("company"),
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postalCode": obj.get("postalCode"),
            "country": obj.get("country"),
            "phone1": obj.get("phone1"),
            "phone2": obj.get("phone2"),
            "fax": obj.get("fax")
        })
        return _obj


