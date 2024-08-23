# coding: utf-8

"""
    SkyBox API

    The SkyBox APIs allow our users to create, update, delete, and export information within the SkyBox platform. These APIs allow SkyBox to be extensible, giving you the flexibility to grow, develop, and integrate third-party tooling to help scale out your business. To begin using the SkyBox APIs, you will need to generate two unique tokens: an Application_Token and an API Token.  To request a unique Application_Token, click here (<a href='https://skybox.vividseats.com/application-sign-up'>https://skybox.vividseats.com/application-sign-up</a>) and refer to this <a href='https://skybox.zendesk.com/hc/en-us/articles/6769735238043-Getting-Started-with-Skybox-APIs'>Zendesk Article</a> for detailed instructions on getting started with SkyBox APIs.  To generate an API Token when logged in to SkyBox, click on the drop-down under 'Logged In As:', select 'External Accounts', and then select 'API Invitation +'. A modal will appear and you will be prompted to enter the email address to which you want the token sent as well as to provide a brief description of the account.  Once you have both your Application_Token and API Token, there are two ways in which you can make requests: through the UI and through a third party. See below for detailed steps for each process.  Requests through the UI:  To begin, enter your Account ID in the X-Account field. Once complete, select _Authorize_. Next, enter your API Token in the X-Api-Token field. If you do not currently have an API Token, please follow the steps above to request one. Once complete, select _Authorize_. Last, enter your Application_Token in the X-Application-Token field. If you do not have an Application_Token, a sample is provided or you can follow the link above to request one. Once complete, select _Authorize_.  Requests through a third party (i.e. Postman):  The same information is required as it is through the UI, but it will be passed in through headers. It should look something like this:  X-Account: Account ID goes here!  X-Api-Token: API Token goes here!  X-Application-Token: Application_Token goes here!  Once these three items are successfully passed in as headers, you will be able to make sample requests.  <h2><a href='https://skybox.zendesk.com/hc/en-us/articles/5999881334427-SkyBox-API-Rate-Limits'>API Rate Limits</a> </h2>  A rate limit consists of two variables: an interval and a limit. An interval is a period of time, measured in seconds. A limit is the number of calls that can be made to an endpoint in an interval.  For example, SkyBox’s ‘GET /reports/‘ endpoint has an interval of 1 second and a limit of 1 call per interval. This means that this endpoint has a rate limit of 1 call/second.  Each endpoint, and its respective rate limit, is displayed in this <a href='https://skybox.zendesk.com/hc/en-us/articles/5999881334427-SkyBox-API-Rate-Limits'>Support Article</a>. If the endpoint is not listed, its rate limit is the default, indicated by the ‘*’ at the bottom of the table. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from skybox_openapi_client.models.ticket import Ticket

class TestTicket(unittest.TestCase):
    """Ticket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Ticket:
        """Test Ticket
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Ticket`
        """
        model = Ticket()
        if include_optional:
            return Ticket(
                id = 56,
                seat_number = 1,
                file_name = '',
                bar_code = '',
                external_ticket_id = '',
                inventory_id = 56,
                invoice_line_id = 56,
                purchase_line_id = 56,
                friendly_section = '',
                section = '0',
                friendly_row = '',
                row = '0',
                notes = '',
                cost = 1.337,
                face_value = 0,
                taxed_cost = 1.337,
                sell_price = 0,
                stock_type = 'HARD',
                event_id = 56,
                account_id = 56,
                status = 'AVAILABLE',
                base64_file_bytes = '',
                disclosures = [
                    ''
                    ],
                attributes = [
                    ''
                    ],
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_by = '',
                date_cancelled = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                cancelled_by_user_id = 56,
                audit_note = ''
            )
        else:
            return Ticket(
                seat_number = 1,
                section = '0',
                row = '0',
                cost = 1.337,
                face_value = 0,
                sell_price = 0,
                stock_type = 'HARD',
                status = 'AVAILABLE',
        )
        """

    def testTicket(self):
        """Test Ticket"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
