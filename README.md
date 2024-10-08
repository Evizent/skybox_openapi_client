# skybox_openapi_client
The SkyBox APIs allow our users to create, update, delete, and export information within the SkyBox platform. These APIs allow SkyBox to be extensible, giving you the flexibility to grow, develop, and integrate third-party tooling to help scale out your business. To begin using the SkyBox APIs, you will need to generate two unique tokens: an Application_Token and an API Token.

To request a unique Application_Token, click here (<a href='https://skybox.vividseats.com/application-sign-up'>https://skybox.vividseats.com/application-sign-up</a>) and refer to this <a href='https://skybox.zendesk.com/hc/en-us/articles/6769735238043-Getting-Started-with-Skybox-APIs'>Zendesk Article</a> for detailed instructions on getting started with SkyBox APIs.

To generate an API Token when logged in to SkyBox, click on the drop-down under 'Logged In As:', select 'External Accounts', and then select 'API Invitation +'. A modal will appear and you will be prompted to enter the email address to which you want the token sent as well as to provide a brief description of the account.

Once you have both your Application_Token and API Token, there are two ways in which you can make requests: through the UI and through a third party. See below for detailed steps for each process.

Requests through the UI:

To begin, enter your Account ID in the X-Account field. Once complete, select _Authorize_. Next, enter your API Token in the X-Api-Token field. If you do not currently have an API Token, please follow the steps above to request one. Once complete, select _Authorize_. Last, enter your Application_Token in the X-Application-Token field. If you do not have an Application_Token, a sample is provided or you can follow the link above to request one. Once complete, select _Authorize_.

Requests through a third party (i.e. Postman):

The same information is required as it is through the UI, but it will be passed in through headers. It should look something like this:

X-Account: Account ID goes here!

X-Api-Token: API Token goes here!

X-Application-Token: Application_Token goes here!

Once these three items are successfully passed in as headers, you will be able to make sample requests.

<h2><a href='https://skybox.zendesk.com/hc/en-us/articles/5999881334427-SkyBox-API-Rate-Limits'>API Rate Limits</a> </h2>

A rate limit consists of two variables: an interval and a limit. An interval is a period of time, measured in seconds. A limit is the number of calls that can be made to an endpoint in an interval.

For example, SkyBox’s ‘GET /reports/‘ endpoint has an interval of 1 second and a limit of 1 call per interval. This means that this endpoint has a rate limit of 1 call/second.

Each endpoint, and its respective rate limit, is displayed in this <a href='https://skybox.zendesk.com/hc/en-us/articles/5999881334427-SkyBox-API-Rate-Limits'>Support Article</a>. If the endpoint is not listed, its rate limit is the default, indicated by the ‘*’ at the bottom of the table.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.1
- Generator version: 7.9.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Evizent/skybox_openapi_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Evizent/skybox_openapi_client.git`)

Then import the package:
```python
import skybox_openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import skybox_openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import skybox_openapi_client
from skybox_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://skybox.vividseats.com/services
# See configuration.py for a list of all supported configuration parameters.
configuration = skybox_openapi_client.Configuration(
    host = "https://skybox.vividseats.com/services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Account
configuration.api_key['Account'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Account'] = 'Bearer'

# Configure API key authorization: Authorization_Token
configuration.api_key['Authorization_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization_Token'] = 'Bearer'

# Configure API key authorization: Application_Token
configuration.api_key['Application_Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Application_Token'] = 'Bearer'


# Enter a context with an instance of the API client
with skybox_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = skybox_openapi_client.AccountApi(api_client)

    try:
        api_response = api_instance.account_get()
        print("The response of AccountApi->account_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->account_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://skybox.vividseats.com/services*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**account_get**](docs/AccountApi.md#account_get) | **GET** /account | 
*AccountApi* | [**account_get_notifications**](docs/AccountApi.md#account_get_notifications) | **GET** /account/notifications | 
*AddressesApi* | [**addresses_delete_by_id**](docs/AddressesApi.md#addresses_delete_by_id) | **DELETE** /addresses/{address-id} | 
*AddressesApi* | [**addresses_get_by_id**](docs/AddressesApi.md#addresses_get_by_id) | **GET** /addresses/{address-id} | 
*AddressesApi* | [**addresses_insert**](docs/AddressesApi.md#addresses_insert) | **POST** /addresses | 
*AddressesApi* | [**addresses_update**](docs/AddressesApi.md#addresses_update) | **PUT** /addresses/{address-id} | 
*AlertsApi* | [**alerts_acknowledge**](docs/AlertsApi.md#alerts_acknowledge) | **DELETE** /alerts/{alert-id} | 
*AlertsApi* | [**alerts_get_by_account**](docs/AlertsApi.md#alerts_get_by_account) | **GET** /alerts | 
*AlertsApi* | [**alerts_get_by_id**](docs/AlertsApi.md#alerts_get_by_id) | **GET** /alerts/{alert-id} | 
*AssetsApi* | [**assets_get**](docs/AssetsApi.md#assets_get) | **GET** /assets/{filename} | 
*AssetsApi* | [**assets_upload**](docs/AssetsApi.md#assets_upload) | **POST** /assets | 
*CreditCardsApi* | [**credit_cards_delete**](docs/CreditCardsApi.md#credit_cards_delete) | **DELETE** /credit_card/{id} | 
*CreditCardsApi* | [**credit_cards_delete_group**](docs/CreditCardsApi.md#credit_cards_delete_group) | **DELETE** /credit_card/group/{id} | 
*CreditCardsApi* | [**credit_cards_get_by_id**](docs/CreditCardsApi.md#credit_cards_get_by_id) | **GET** /credit_card/{id} | 
*CreditCardsApi* | [**credit_cards_get_credit_cards**](docs/CreditCardsApi.md#credit_cards_get_credit_cards) | **GET** /credit_card/group/{group-id}/cards | 
*CreditCardsApi* | [**credit_cards_get_credit_cards_by_account_id**](docs/CreditCardsApi.md#credit_cards_get_credit_cards_by_account_id) | **GET** /credit_card | 
*CreditCardsApi* | [**credit_cards_get_group_by_id**](docs/CreditCardsApi.md#credit_cards_get_group_by_id) | **GET** /credit_card/group/{id} | 
*CreditCardsApi* | [**credit_cards_insert**](docs/CreditCardsApi.md#credit_cards_insert) | **POST** /credit_card | 
*CreditCardsApi* | [**credit_cards_insert_group**](docs/CreditCardsApi.md#credit_cards_insert_group) | **POST** /credit_card/group | 
*CreditCardsApi* | [**credit_cards_query**](docs/CreditCardsApi.md#credit_cards_query) | **GET** /credit_card/group | 
*CreditCardsApi* | [**credit_cards_update**](docs/CreditCardsApi.md#credit_cards_update) | **PUT** /credit_card | 
*CreditCardsApi* | [**credit_cards_update_group**](docs/CreditCardsApi.md#credit_cards_update_group) | **PUT** /credit_card/group | 
*CustomersApi* | [**customers_add_card**](docs/CustomersApi.md#customers_add_card) | **POST** /customers/{customer-id}/cards | 
*CustomersApi* | [**customers_bulk_remove_tags**](docs/CustomersApi.md#customers_bulk_remove_tags) | **POST** /customers/tags/remove | 
*CustomersApi* | [**customers_bulk_update**](docs/CustomersApi.md#customers_bulk_update) | **PUT** /customers/bulk | 
*CustomersApi* | [**customers_delete**](docs/CustomersApi.md#customers_delete) | **POST** /customers/{customer-id}/tags/actions/delete | 
*CustomersApi* | [**customers_get_by_id**](docs/CustomersApi.md#customers_get_by_id) | **GET** /customers/{customer-id} | 
*CustomersApi* | [**customers_get_card**](docs/CustomersApi.md#customers_get_card) | **GET** /customers/{customer-id}/cards/{card-id} | 
*CustomersApi* | [**customers_get_cards**](docs/CustomersApi.md#customers_get_cards) | **GET** /customers/{customer-id}/cards | 
*CustomersApi* | [**customers_get_defaults_by_id**](docs/CustomersApi.md#customers_get_defaults_by_id) | **GET** /customers/defaults | 
*CustomersApi* | [**customers_insert**](docs/CustomersApi.md#customers_insert) | **POST** /customers | 
*CustomersApi* | [**customers_remove_card**](docs/CustomersApi.md#customers_remove_card) | **DELETE** /customers/{customer-id}/cards/{card-id} | 
*CustomersApi* | [**customers_search**](docs/CustomersApi.md#customers_search) | **GET** /customers | 
*CustomersApi* | [**customers_set_default_card**](docs/CustomersApi.md#customers_set_default_card) | **PUT** /customers/{customer-id}/cards/{card-id}/default | 
*CustomersApi* | [**customers_tag**](docs/CustomersApi.md#customers_tag) | **POST** /customers/{customer-id}/tags | 
*CustomersApi* | [**customers_update**](docs/CustomersApi.md#customers_update) | **PUT** /customers/{customer-id} | 
*CustomersApi* | [**customers_update_default**](docs/CustomersApi.md#customers_update_default) | **PUT** /customers/defaults | 
*EnumerationsApi* | [**enumerations_enumeration**](docs/EnumerationsApi.md#enumerations_enumeration) | **GET** /enumerations/{enumtype} | 
*EventPositionsApi* | [**event_positions_event_positions_totals**](docs/EventPositionsApi.md#event_positions_event_positions_totals) | **GET** /event_positions/totals | 
*EventPositionsApi* | [**event_positions_event_positions_values**](docs/EventPositionsApi.md#event_positions_event_positions_values) | **GET** /event_positions/values | 
*EventPositionsApi* | [**event_positions_get_categories**](docs/EventPositionsApi.md#event_positions_get_categories) | **GET** /event_positions/categories | 
*EventPositionsApi* | [**event_positions_get_performers**](docs/EventPositionsApi.md#event_positions_get_performers) | **GET** /event_positions/performers | 
*EventPositionsApi* | [**event_positions_index**](docs/EventPositionsApi.md#event_positions_index) | **GET** /event_positions | 
*EventsApi* | [**events_bulk_remove_tags**](docs/EventsApi.md#events_bulk_remove_tags) | **POST** /events/tags/remove | 
*EventsApi* | [**events_delete**](docs/EventsApi.md#events_delete) | **POST** /events/{event-id}/tags/actions/delete | 
*EventsApi* | [**events_find_event_deltas**](docs/EventsApi.md#events_find_event_deltas) | **GET** /events/{event_id}/deltas | 
*EventsApi* | [**events_get**](docs/EventsApi.md#events_get) | **GET** /events/{event-id} | 
*EventsApi* | [**events_get_categories**](docs/EventsApi.md#events_get_categories) | **GET** /events/categories | 
*EventsApi* | [**events_get_performer_by_id**](docs/EventsApi.md#events_get_performer_by_id) | **GET** /events/performers/{performer-id} | 
*EventsApi* | [**events_get_performers**](docs/EventsApi.md#events_get_performers) | **GET** /events/performers | 
*EventsApi* | [**events_index**](docs/EventsApi.md#events_index) | **GET** /events | 
*EventsApi* | [**events_tag**](docs/EventsApi.md#events_tag) | **POST** /events/{event-id}/tags | 
*ExternalAccountsApi* | [**external_accounts_create**](docs/ExternalAccountsApi.md#external_accounts_create) | **POST** /external_accounts | 
*ExternalAccountsApi* | [**external_accounts_delete**](docs/ExternalAccountsApi.md#external_accounts_delete) | **DELETE** /external_accounts/{id} | 
*ExternalAccountsApi* | [**external_accounts_get_by_id**](docs/ExternalAccountsApi.md#external_accounts_get_by_id) | **GET** /external_accounts/{id} | 
*ExternalAccountsApi* | [**external_accounts_search**](docs/ExternalAccountsApi.md#external_accounts_search) | **GET** /external_accounts | 
*ExternalAccountsApi* | [**external_accounts_update**](docs/ExternalAccountsApi.md#external_accounts_update) | **PUT** /external_accounts/{id} | 
*HoldsApi* | [**holds_delete_by_id**](docs/HoldsApi.md#holds_delete_by_id) | **DELETE** /holds/{hold-id} | 
*HoldsApi* | [**holds_get_by_id**](docs/HoldsApi.md#holds_get_by_id) | **GET** /holds/{hold-id} | 
*HoldsApi* | [**holds_insert**](docs/HoldsApi.md#holds_insert) | **POST** /holds | 
*HoldsApi* | [**holds_search**](docs/HoldsApi.md#holds_search) | **GET** /holds | 
*HoldsApi* | [**holds_update**](docs/HoldsApi.md#holds_update) | **PUT** /holds/{hold-id} | 
*InventoryApi* | [**inventory_bulk_merge**](docs/InventoryApi.md#inventory_bulk_merge) | **POST** /inventory/bulk-merge | 
*InventoryApi* | [**inventory_bulk_remove_tags**](docs/InventoryApi.md#inventory_bulk_remove_tags) | **POST** /inventory/tags/remove | 
*InventoryApi* | [**inventory_bulk_swap_event**](docs/InventoryApi.md#inventory_bulk_swap_event) | **POST** /inventory/bulk-swap-event | 
*InventoryApi* | [**inventory_bulk_update**](docs/InventoryApi.md#inventory_bulk_update) | **PUT** /inventory/bulk-update | 
*InventoryApi* | [**inventory_bulk_update_expected_value**](docs/InventoryApi.md#inventory_bulk_update_expected_value) | **PUT** /inventory/bulk-update-expected-value | 
*InventoryApi* | [**inventory_bulk_update_face_value**](docs/InventoryApi.md#inventory_bulk_update_face_value) | **PUT** /inventory/bulk-update-face-value | 
*InventoryApi* | [**inventory_bulk_update_price**](docs/InventoryApi.md#inventory_bulk_update_price) | **PUT** /inventory | 
*InventoryApi* | [**inventory_bulk_update_taxed_cost**](docs/InventoryApi.md#inventory_bulk_update_taxed_cost) | **PUT** /inventory/bulk-taxed-cost-value | 
*InventoryApi* | [**inventory_delete**](docs/InventoryApi.md#inventory_delete) | **POST** /inventory/{inventory-id}/tags/actions/delete | 
*InventoryApi* | [**inventory_delete_holds_by_id**](docs/InventoryApi.md#inventory_delete_holds_by_id) | **DELETE** /inventory/{inventory-id}/hold | 
*InventoryApi* | [**inventory_export**](docs/InventoryApi.md#inventory_export) | **GET** /inventory/export | 
*InventoryApi* | [**inventory_export_delta**](docs/InventoryApi.md#inventory_export_delta) | **GET** /inventory/export/delta | 
*InventoryApi* | [**inventory_get_by_id**](docs/InventoryApi.md#inventory_get_by_id) | **GET** /inventory/{inventory-id} | 
*InventoryApi* | [**inventory_get_exchanges_pos_id**](docs/InventoryApi.md#inventory_get_exchanges_pos_id) | **GET** /inventory/exchange_pos_id/{exchangePosId} | 
*InventoryApi* | [**inventory_get_holds_by_id**](docs/InventoryApi.md#inventory_get_holds_by_id) | **GET** /inventory/{inventory-id}/hold | 
*InventoryApi* | [**inventory_get_inventory_barcodes**](docs/InventoryApi.md#inventory_get_inventory_barcodes) | **GET** /inventory/barcodes/{exchange-pos-id} | 
*InventoryApi* | [**inventory_get_inventory_deltas**](docs/InventoryApi.md#inventory_get_inventory_deltas) | **GET** /inventory/delta | 
*InventoryApi* | [**inventory_legacy_bulk_remove_tags**](docs/InventoryApi.md#inventory_legacy_bulk_remove_tags) | **DELETE** /inventory/tags | 
*InventoryApi* | [**inventory_merge**](docs/InventoryApi.md#inventory_merge) | **POST** /inventory/merge | 
*InventoryApi* | [**inventory_merge_as_piggyback**](docs/InventoryApi.md#inventory_merge_as_piggyback) | **POST** /inventory/merge-as-piggyback | 
*InventoryApi* | [**inventory_price_history**](docs/InventoryApi.md#inventory_price_history) | **GET** /inventory/{inventory-id}/price-history | 
*InventoryApi* | [**inventory_remove_tag**](docs/InventoryApi.md#inventory_remove_tag) | **DELETE** /inventory/{inventory-id}/tags/{tag} | 
*InventoryApi* | [**inventory_search**](docs/InventoryApi.md#inventory_search) | **GET** /inventory | 
*InventoryApi* | [**inventory_search_purchased**](docs/InventoryApi.md#inventory_search_purchased) | **GET** /inventory/purchased | 
*InventoryApi* | [**inventory_search_purchased_v2**](docs/InventoryApi.md#inventory_search_purchased_v2) | **GET** /inventory/purchased/V2 | 
*InventoryApi* | [**inventory_search_sold**](docs/InventoryApi.md#inventory_search_sold) | **GET** /inventory/sold | 
*InventoryApi* | [**inventory_sold_bulk_swap_event**](docs/InventoryApi.md#inventory_sold_bulk_swap_event) | **POST** /inventory/sold/bulk-swap-event | 
*InventoryApi* | [**inventory_split**](docs/InventoryApi.md#inventory_split) | **PUT** /inventory/{inventory-id}/split | 
*InventoryApi* | [**inventory_split_to_consecutive**](docs/InventoryApi.md#inventory_split_to_consecutive) | **PUT** /inventory/{inventory-id}/split-to-consecutive | 
*InventoryApi* | [**inventory_split_to_originals**](docs/InventoryApi.md#inventory_split_to_originals) | **POST** /inventory/{inventory-id}/actions/split-to-originals | 
*InventoryApi* | [**inventory_sync**](docs/InventoryApi.md#inventory_sync) | **PUT** /inventory/sync | 
*InventoryApi* | [**inventory_tag**](docs/InventoryApi.md#inventory_tag) | **POST** /inventory/{inventory-id}/tags | 
*InventoryApi* | [**inventory_update**](docs/InventoryApi.md#inventory_update) | **PUT** /inventory/{inventory-id} | 
*InventoryApi* | [**inventory_update_purchase_inventory**](docs/InventoryApi.md#inventory_update_purchase_inventory) | **POST** /inventory/actions/edit-section-row | 
*InvoicesApi* | [**invoices_bulk_remove_tags**](docs/InvoicesApi.md#invoices_bulk_remove_tags) | **POST** /invoices/tags/remove | 
*InvoicesApi* | [**invoices_delete**](docs/InvoicesApi.md#invoices_delete) | **POST** /invoices/{invoice-id}/tags/actions/delete | 
*InvoicesApi* | [**invoices_delete_invoice_line**](docs/InvoicesApi.md#invoices_delete_invoice_line) | **DELETE** /invoices/{invoice-id}/lines/{line-id} | 
*InvoicesApi* | [**invoices_get_assets**](docs/InvoicesApi.md#invoices_get_assets) | **GET** /invoices/{invoice-id}/assets | 
*InvoicesApi* | [**invoices_get_invoice_by_id**](docs/InvoicesApi.md#invoices_get_invoice_by_id) | **GET** /invoices/{invoice-id} | 
*InvoicesApi* | [**invoices_get_invoice_line**](docs/InvoicesApi.md#invoices_get_invoice_line) | **GET** /invoices/{invoice-id}/lines/{line-id} | 
*InvoicesApi* | [**invoices_get_invoice_line_tickets**](docs/InvoicesApi.md#invoices_get_invoice_line_tickets) | **GET** /invoices/{invoice-id}/lines/{line-id}/tickets | 
*InvoicesApi* | [**invoices_get_invoice_lines**](docs/InvoicesApi.md#invoices_get_invoice_lines) | **GET** /invoices/{invoice-id}/lines | 
*InvoicesApi* | [**invoices_get_invoice_tickets_by_external_ref_v2**](docs/InvoicesApi.md#invoices_get_invoice_tickets_by_external_ref_v2) | **GET** /invoices/external-ref | 
*InvoicesApi* | [**invoices_get_transaction_history**](docs/InvoicesApi.md#invoices_get_transaction_history) | **GET** /invoices/{invoice-id}/transactions | 
*InvoicesApi* | [**invoices_insert_invoice**](docs/InvoicesApi.md#invoices_insert_invoice) | **POST** /invoices | 
*InvoicesApi* | [**invoices_insert_invoice_line**](docs/InvoicesApi.md#invoices_insert_invoice_line) | **POST** /invoices/{invoice-id}/lines | 
*InvoicesApi* | [**invoices_print**](docs/InvoicesApi.md#invoices_print) | **GET** /invoices/{invoice-id}/print | 
*InvoicesApi* | [**invoices_print_custom_auth_form**](docs/InvoicesApi.md#invoices_print_custom_auth_form) | **GET** /invoices/{invoice-id}/print-auth-form | 
*InvoicesApi* | [**invoices_process_payment**](docs/InvoicesApi.md#invoices_process_payment) | **POST** /invoices/{invoice-id}/payment | 
*InvoicesApi* | [**invoices_process_refund**](docs/InvoicesApi.md#invoices_process_refund) | **POST** /invoices/{invoice-id}/transactions/{transaction-id}/refund | 
*InvoicesApi* | [**invoices_remove_tag**](docs/InvoicesApi.md#invoices_remove_tag) | **DELETE** /invoices/{invoice-id}/tags/{tag} | 
*InvoicesApi* | [**invoices_search**](docs/InvoicesApi.md#invoices_search) | **GET** /invoices | 
*InvoicesApi* | [**invoices_send**](docs/InvoicesApi.md#invoices_send) | **GET** /invoices/{invoice-id}/send | 
*InvoicesApi* | [**invoices_tag**](docs/InvoicesApi.md#invoices_tag) | **POST** /invoices/{invoice-id}/tags | 
*InvoicesApi* | [**invoices_update**](docs/InvoicesApi.md#invoices_update) | **PUT** /invoices/bulk | 
*InvoicesApi* | [**invoices_update_currency**](docs/InvoicesApi.md#invoices_update_currency) | **PUT** /invoices/actions/update-invoice-currency | 
*InvoicesApi* | [**invoices_update_invoice**](docs/InvoicesApi.md#invoices_update_invoice) | **PUT** /invoices/{invoice-id} | 
*InvoicesApi* | [**invoices_update_invoice_line**](docs/InvoicesApi.md#invoices_update_invoice_line) | **PUT** /invoices/{invoice-id}/lines/{line-id} | 
*LinesApi* | [**lines_cancel_invoice_lines**](docs/LinesApi.md#lines_cancel_invoice_lines) | **POST** /lines/invoice/bulk-cancel | 
*LinesApi* | [**lines_delete_invoice_lines**](docs/LinesApi.md#lines_delete_invoice_lines) | **POST** /lines/bulk-delete | 
*LinesApi* | [**lines_get_line_by_id**](docs/LinesApi.md#lines_get_line_by_id) | **GET** /lines/{line-id} | 
*MappingApi* | [**mapping_bulk_delete**](docs/MappingApi.md#mapping_bulk_delete) | **POST** /mappings/actions/bulk-cancel | 
*MappingApi* | [**mapping_delete**](docs/MappingApi.md#mapping_delete) | **DELETE** /mappings/{mapping-id} | 
*MappingApi* | [**mapping_find_pending_by_id**](docs/MappingApi.md#mapping_find_pending_by_id) | **GET** /mappings/{mapping-id} | 
*MappingApi* | [**mapping_get_pending_by_account**](docs/MappingApi.md#mapping_get_pending_by_account) | **GET** /mappings | 
*MappingApi* | [**mapping_resend_mapping_request**](docs/MappingApi.md#mapping_resend_mapping_request) | **GET** /mappings/{mapping-id}/resend | 
*PricingGroupApi* | [**pricing_group_insert_pricing_group**](docs/PricingGroupApi.md#pricing_group_insert_pricing_group) | **POST** /pricing_group | 
*PurchasesApi* | [**purchases_add_purchase_note**](docs/PurchasesApi.md#purchases_add_purchase_note) | **POST** /purchases/{purchase-id}/notes | 
*PurchasesApi* | [**purchases_bulk_cancel_lines**](docs/PurchasesApi.md#purchases_bulk_cancel_lines) | **POST** /purchases/actions/cancel-lines | 
*PurchasesApi* | [**purchases_bulk_remove_tags**](docs/PurchasesApi.md#purchases_bulk_remove_tags) | **POST** /purchases/tags/remove | 
*PurchasesApi* | [**purchases_cancel_purchase_line**](docs/PurchasesApi.md#purchases_cancel_purchase_line) | **PUT** /purchases/{purchase-id}/lines/{line-id}/cancel | 
*PurchasesApi* | [**purchases_delete**](docs/PurchasesApi.md#purchases_delete) | **POST** /purchases/{purchase-id}/tags/actions/delete | 
*PurchasesApi* | [**purchases_get_airbill**](docs/PurchasesApi.md#purchases_get_airbill) | **GET** /purchases/{purchase-id}/airbill | 
*PurchasesApi* | [**purchases_get_purchase_by_id**](docs/PurchasesApi.md#purchases_get_purchase_by_id) | **GET** /purchases/{purchase-id} | 
*PurchasesApi* | [**purchases_get_purchase_line**](docs/PurchasesApi.md#purchases_get_purchase_line) | **GET** /purchases/{purchase-id}/lines/{line-id} | 
*PurchasesApi* | [**purchases_get_purchase_line_tickets**](docs/PurchasesApi.md#purchases_get_purchase_line_tickets) | **GET** /purchases/{purchase-id}/lines/{line-id}/tickets | 
*PurchasesApi* | [**purchases_get_purchase_lines**](docs/PurchasesApi.md#purchases_get_purchase_lines) | **GET** /purchases/{purchase-id}/lines | 
*PurchasesApi* | [**purchases_insert_purchase**](docs/PurchasesApi.md#purchases_insert_purchase) | **POST** /purchases | 
*PurchasesApi* | [**purchases_insert_purchase_line**](docs/PurchasesApi.md#purchases_insert_purchase_line) | **POST** /purchases/{purchase-id}/lines | 
*PurchasesApi* | [**purchases_multi_with_purchase_id**](docs/PurchasesApi.md#purchases_multi_with_purchase_id) | **POST** /purchases/{purchase-id}/inventory | 
*PurchasesApi* | [**purchases_print**](docs/PurchasesApi.md#purchases_print) | **GET** /purchases/{purchase-id}/print | 
*PurchasesApi* | [**purchases_remove_tag**](docs/PurchasesApi.md#purchases_remove_tag) | **DELETE** /purchases/{purchase-id}/tags/{tag} | 
*PurchasesApi* | [**purchases_replace_purchase_line**](docs/PurchasesApi.md#purchases_replace_purchase_line) | **POST** /purchases/{purchase-id}/lines/{line-id}/actions/replace | 
*PurchasesApi* | [**purchases_search**](docs/PurchasesApi.md#purchases_search) | **GET** /purchases | 
*PurchasesApi* | [**purchases_search_auto_purchases**](docs/PurchasesApi.md#purchases_search_auto_purchases) | **GET** /purchases/auto-purchases | 
*PurchasesApi* | [**purchases_send**](docs/PurchasesApi.md#purchases_send) | **GET** /purchases/{purchase-id}/send | 
*PurchasesApi* | [**purchases_tag**](docs/PurchasesApi.md#purchases_tag) | **POST** /purchases/{purchase-id}/tags | 
*PurchasesApi* | [**purchases_update**](docs/PurchasesApi.md#purchases_update) | **PUT** /purchases/bulk | 
*PurchasesApi* | [**purchases_update_currency**](docs/PurchasesApi.md#purchases_update_currency) | **PUT** /purchases/actions/update-purchase-currency | 
*PurchasesApi* | [**purchases_update_purchase**](docs/PurchasesApi.md#purchases_update_purchase) | **PUT** /purchases/{purchase-id} | 
*PurchasesApi* | [**purchases_update_purchase_inventory**](docs/PurchasesApi.md#purchases_update_purchase_inventory) | **POST** /purchases/{purchase-id}/lines/{line-id}/inventory | 
*PurchasesApi* | [**purchases_update_purchase_line**](docs/PurchasesApi.md#purchases_update_purchase_line) | **PUT** /purchases/{purchase-id}/lines/{line-id} | 
*QuickReportsApi* | [**quick_reports_get_purchases**](docs/QuickReportsApi.md#quick_reports_get_purchases) | **GET** /quick-report/purchases | 
*QuickReportsApi* | [**quick_reports_get_sales**](docs/QuickReportsApi.md#quick_reports_get_sales) | **GET** /quick-report/sales | 
*QuickSearchApi* | [**quick_search_search**](docs/QuickSearchApi.md#quick_search_search) | **GET** /quicksearch | 
*ReportsApi* | [**reports_get_report_snapshot**](docs/ReportsApi.md#reports_get_report_snapshot) | **GET** /reports/snapshots/{id} | 
*ReportsApi* | [**reports_query_report_snapshots**](docs/ReportsApi.md#reports_query_report_snapshots) | **GET** /reports/snapshots | 
*ResearchDashboardApi* | [**researchdashboard_get_event_profitability**](docs/ResearchDashboardApi.md#researchdashboard_get_event_profitability) | **GET** /research-dashboard/past-events/events | 
*ResearchDashboardApi* | [**researchdashboard_get_events_profitability**](docs/ResearchDashboardApi.md#researchdashboard_get_events_profitability) | **GET** /research-dashboard/events-profitability | 
*ResearchDashboardApi* | [**researchdashboard_get_lifetime_pl**](docs/ResearchDashboardApi.md#researchdashboard_get_lifetime_pl) | **GET** /research-dashboard/lifetime-pl | 
*ResearchDashboardApi* | [**researchdashboard_get_performer_profitability**](docs/ResearchDashboardApi.md#researchdashboard_get_performer_profitability) | **GET** /research-dashboard/past-events/performers | 
*ResearchDashboardApi* | [**researchdashboard_get_seat_map_heat_map**](docs/ResearchDashboardApi.md#researchdashboard_get_seat_map_heat_map) | **GET** /research-dashboard/seat-map-heat-map | 
*ResearchDashboardApi* | [**researchdashboard_get_section_profitability**](docs/ResearchDashboardApi.md#researchdashboard_get_section_profitability) | **GET** /research-dashboard/past-events/sections | 
*ResearchDashboardApi* | [**researchdashboard_get_tickets_profitability**](docs/ResearchDashboardApi.md#researchdashboard_get_tickets_profitability) | **GET** /research-dashboard/tickets-profitability | 
*ResearchDashboardApi* | [**researchdashboard_get_tickets_sales**](docs/ResearchDashboardApi.md#researchdashboard_get_tickets_sales) | **GET** /research-dashboard/tickets-sales | 
*ResearchDashboardApi* | [**researchdashboard_get_venue_profitability**](docs/ResearchDashboardApi.md#researchdashboard_get_venue_profitability) | **GET** /research-dashboard/past-events/venues | 
*TagsApi* | [**tags_bulk**](docs/TagsApi.md#tags_bulk) | **PUT** /tags/bulk | 
*TagsApi* | [**tags_delete**](docs/TagsApi.md#tags_delete) | **POST** /tags/actions/delete | 
*TagsApi* | [**tags_get_filtered_tags**](docs/TagsApi.md#tags_get_filtered_tags) | **GET** /tags/filtered | 
*TagsApi* | [**tags_list**](docs/TagsApi.md#tags_list) | **GET** /tags | 
*TagsApi* | [**tags_tags_summary**](docs/TagsApi.md#tags_tags_summary) | **GET** /tags/summary | 
*TagsApi* | [**tags_update_color**](docs/TagsApi.md#tags_update_color) | **PUT** /tags/color | 
*TicketsApi* | [**tickets_get_by_id**](docs/TicketsApi.md#tickets_get_by_id) | **GET** /tickets/{ticket-id} | 
*TicketsApi* | [**tickets_search**](docs/TicketsApi.md#tickets_search) | **GET** /tickets | 
*UsersApi* | [**users_get_me**](docs/UsersApi.md#users_get_me) | **GET** /users/me | 
*UsersApi* | [**users_list_users**](docs/UsersApi.md#users_list_users) | **GET** /users | 
*VendorsApi* | [**vendors_bulk_remove_tags**](docs/VendorsApi.md#vendors_bulk_remove_tags) | **POST** /vendors/tags/remove | 
*VendorsApi* | [**vendors_bulk_update**](docs/VendorsApi.md#vendors_bulk_update) | **PUT** /vendors/bulk | 
*VendorsApi* | [**vendors_delete**](docs/VendorsApi.md#vendors_delete) | **POST** /vendors/{vendor-id}/tags/actions/delete | 
*VendorsApi* | [**vendors_get_by_id**](docs/VendorsApi.md#vendors_get_by_id) | **GET** /vendors/{vendor-id} | 
*VendorsApi* | [**vendors_get_default**](docs/VendorsApi.md#vendors_get_default) | **GET** /vendors/default | 
*VendorsApi* | [**vendors_insert**](docs/VendorsApi.md#vendors_insert) | **POST** /vendors | 
*VendorsApi* | [**vendors_search**](docs/VendorsApi.md#vendors_search) | **GET** /vendors | 
*VendorsApi* | [**vendors_tag**](docs/VendorsApi.md#vendors_tag) | **POST** /vendors/{vendor-id}/tags | 
*VendorsApi* | [**vendors_update**](docs/VendorsApi.md#vendors_update) | **PUT** /vendors/{vendor-id} | 
*VendorsApi* | [**vendors_update_default_vendor**](docs/VendorsApi.md#vendors_update_default_vendor) | **PUT** /vendors/default | 
*VenuesApi* | [**venues_get_by_id**](docs/VenuesApi.md#venues_get_by_id) | **GET** /venues/{venue-id} | 
*VenuesApi* | [**venues_search**](docs/VenuesApi.md#venues_search) | **GET** /venues | 
*WebhooksApi* | [**webhooks_create**](docs/WebhooksApi.md#webhooks_create) | **POST** /webhooks | 
*WebhooksApi* | [**webhooks_delete**](docs/WebhooksApi.md#webhooks_delete) | **DELETE** /webhooks/{id} | 
*WebhooksApi* | [**webhooks_find**](docs/WebhooksApi.md#webhooks_find) | **GET** /webhooks/{id} | 
*WebhooksApi* | [**webhooks_query**](docs/WebhooksApi.md#webhooks_query) | **GET** /webhooks | 
*WebhooksApi* | [**webhooks_update**](docs/WebhooksApi.md#webhooks_update) | **PUT** /webhooks/{id} | 


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountSetting](docs/AccountSetting.md)
 - [AccountSettingValue](docs/AccountSettingValue.md)
 - [Address](docs/Address.md)
 - [Alert](docs/Alert.md)
 - [BillingAddress](docs/BillingAddress.md)
 - [BulkCustomerUpdate](docs/BulkCustomerUpdate.md)
 - [BulkInventoryUpdateRequest](docs/BulkInventoryUpdateRequest.md)
 - [BulkInvoiceUpdate](docs/BulkInvoiceUpdate.md)
 - [BulkLineUpdate](docs/BulkLineUpdate.md)
 - [BulkPurchaseUpdate](docs/BulkPurchaseUpdate.md)
 - [BulkSoldSwapEventRequest](docs/BulkSoldSwapEventRequest.md)
 - [BulkSwapEventRequest](docs/BulkSwapEventRequest.md)
 - [BulkTagRequest](docs/BulkTagRequest.md)
 - [BulkVendorUpdate](docs/BulkVendorUpdate.md)
 - [Category](docs/Category.md)
 - [Consignment](docs/Consignment.md)
 - [ConsignmentLine](docs/ConsignmentLine.md)
 - [CreditCard](docs/CreditCard.md)
 - [CreditCardGroup](docs/CreditCardGroup.md)
 - [CurrencyUpdateBulkAction](docs/CurrencyUpdateBulkAction.md)
 - [Customer](docs/Customer.md)
 - [CustomerCard](docs/CustomerCard.md)
 - [DefaultCustomer](docs/DefaultCustomer.md)
 - [Event](docs/Event.md)
 - [EventDelta](docs/EventDelta.md)
 - [EventMapping](docs/EventMapping.md)
 - [EventPosition](docs/EventPosition.md)
 - [EventProfitability](docs/EventProfitability.md)
 - [ExchangePosIdHistoryResponse](docs/ExchangePosIdHistoryResponse.md)
 - [ExpectedValueUpdateBulk](docs/ExpectedValueUpdateBulk.md)
 - [ExternalAccount](docs/ExternalAccount.md)
 - [GroupProfitability](docs/GroupProfitability.md)
 - [HeatMapSeatMapResponse](docs/HeatMapSeatMapResponse.md)
 - [Hold](docs/Hold.md)
 - [HoldRequest](docs/HoldRequest.md)
 - [HoldSummary](docs/HoldSummary.md)
 - [Inventory](docs/Inventory.md)
 - [InventoryBarcodeResponse](docs/InventoryBarcodeResponse.md)
 - [InventoryFaceValueUpdateBulk](docs/InventoryFaceValueUpdateBulk.md)
 - [InventoryMapping](docs/InventoryMapping.md)
 - [InventoryMappingSummary](docs/InventoryMappingSummary.md)
 - [InventoryPriceHistory](docs/InventoryPriceHistory.md)
 - [InventoryPriceUpdateBulk](docs/InventoryPriceUpdateBulk.md)
 - [InventorySummary](docs/InventorySummary.md)
 - [InventoryTaxedCostUpdateBulk](docs/InventoryTaxedCostUpdateBulk.md)
 - [Invoice](docs/Invoice.md)
 - [InvoiceCurrencyUpdateBulkAction](docs/InvoiceCurrencyUpdateBulkAction.md)
 - [InvoiceDeliveryLink](docs/InvoiceDeliveryLink.md)
 - [InvoiceNote](docs/InvoiceNote.md)
 - [InvoicePayment](docs/InvoicePayment.md)
 - [InvoiceSummary](docs/InvoiceSummary.md)
 - [InvoiceTicket](docs/InvoiceTicket.md)
 - [Line](docs/Line.md)
 - [MergeInventoryRequest](docs/MergeInventoryRequest.md)
 - [Notification](docs/Notification.md)
 - [Payment](docs/Payment.md)
 - [PdfDetails](docs/PdfDetails.md)
 - [PdfUpload](docs/PdfUpload.md)
 - [Performer](docs/Performer.md)
 - [PerformerPosition](docs/PerformerPosition.md)
 - [PerformerProfitability](docs/PerformerProfitability.md)
 - [PricingGroup](docs/PricingGroup.md)
 - [PricingGroupInventory](docs/PricingGroupInventory.md)
 - [ProfitAndLoss](docs/ProfitAndLoss.md)
 - [Purchase](docs/Purchase.md)
 - [PurchaseLineReplaceAction](docs/PurchaseLineReplaceAction.md)
 - [PurchaseNote](docs/PurchaseNote.md)
 - [PurchasePayment](docs/PurchasePayment.md)
 - [PurchaseSummary](docs/PurchaseSummary.md)
 - [PurchasedInventorySummary](docs/PurchasedInventorySummary.md)
 - [PurchasedInventorySummaryV2](docs/PurchasedInventorySummaryV2.md)
 - [QuickSearchResult](docs/QuickSearchResult.md)
 - [RefundRequest](docs/RefundRequest.md)
 - [Report](docs/Report.md)
 - [ReportColumn](docs/ReportColumn.md)
 - [ReportDefinition](docs/ReportDefinition.md)
 - [ReportGroup](docs/ReportGroup.md)
 - [ReportParameter](docs/ReportParameter.md)
 - [ReportSnapshot](docs/ReportSnapshot.md)
 - [ReportSnapshotFilter](docs/ReportSnapshotFilter.md)
 - [ReportSnapshotResult](docs/ReportSnapshotResult.md)
 - [Role](docs/Role.md)
 - [SectionProfitability](docs/SectionProfitability.md)
 - [SkyboxWebhook](docs/SkyboxWebhook.md)
 - [SoldInventorySummary](docs/SoldInventorySummary.md)
 - [SyncInventoryRequest](docs/SyncInventoryRequest.md)
 - [TagColorUpdateRequest](docs/TagColorUpdateRequest.md)
 - [TagRequest](docs/TagRequest.md)
 - [TagSummary](docs/TagSummary.md)
 - [TaxTags](docs/TaxTags.md)
 - [TaxedCostMarketplaceOptIn](docs/TaxedCostMarketplaceOptIn.md)
 - [Ticket](docs/Ticket.md)
 - [TicketSale](docs/TicketSale.md)
 - [TicketSales](docs/TicketSales.md)
 - [TicketSummary](docs/TicketSummary.md)
 - [UpdatePurchaseInventoryRequest](docs/UpdatePurchaseInventoryRequest.md)
 - [User](docs/User.md)
 - [Vendor](docs/Vendor.md)
 - [Venue](docs/Venue.md)
 - [VenueProfitability](docs/VenueProfitability.md)
 - [VenueTimeZone](docs/VenueTimeZone.md)
 - [VenueTimeZoneRules](docs/VenueTimeZoneRules.md)
 - [VenueTimeZoneRulesTransitionRulesInner](docs/VenueTimeZoneRulesTransitionRulesInner.md)
 - [VenueTimeZoneRulesTransitionsInner](docs/VenueTimeZoneRulesTransitionsInner.md)
 - [VenueTimeZoneRulesTransitionsInnerDuration](docs/VenueTimeZoneRulesTransitionsInnerDuration.md)
 - [VenueTimeZoneRulesTransitionsInnerDurationUnitsInner](docs/VenueTimeZoneRulesTransitionsInnerDurationUnitsInner.md)
 - [VenueTimeZoneRulesTransitionsInnerOffsetBefore](docs/VenueTimeZoneRulesTransitionsInnerOffsetBefore.md)
 - [VividSeatsListingGlobal](docs/VividSeatsListingGlobal.md)
 - [VividSeatsMapGroups](docs/VividSeatsMapGroups.md)
 - [VividSeatsSection](docs/VividSeatsSection.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Account"></a>
### Account

- **Type**: API key
- **API key parameter name**: X-Account
- **Location**: HTTP header

<a id="Authorization_Token"></a>
### Authorization_Token

- **Type**: API key
- **API key parameter name**: X-Api-Token
- **Location**: HTTP header

<a id="Application_Token"></a>
### Application_Token

- **Type**: API key
- **API key parameter name**: X-Application-Token
- **Location**: HTTP header


## Author




