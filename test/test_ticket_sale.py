# coding: utf-8

"""
    SkyBox API

    The SkyBox APIs allow our users to create, update, delete, and export information within the SkyBox platform. These APIs allow SkyBox to be extensible, giving you the flexibility to grow, develop, and integrate third-party tooling to help scale out your business. To begin using the SkyBox APIs, you will need to generate two unique tokens: an Application_Token and an API Token.  To request a unique Application_Token, click here (<a href='https://skybox.vividseats.com/application-sign-up'>https://skybox.vividseats.com/application-sign-up</a>) and refer to this <a href='https://skybox.zendesk.com/hc/en-us/articles/6769735238043-Getting-Started-with-Skybox-APIs'>Zendesk Article</a> for detailed instructions on getting started with SkyBox APIs.  To generate an API Token when logged in to SkyBox, click on the drop-down under 'Logged In As:', select 'External Accounts', and then select 'API Invitation +'. A modal will appear and you will be prompted to enter the email address to which you want the token sent as well as to provide a brief description of the account.  Once you have both your Application_Token and API Token, there are two ways in which you can make requests: through the UI and through a third party. See below for detailed steps for each process.  Requests through the UI:  To begin, enter your Account ID in the X-Account field. Once complete, select _Authorize_. Next, enter your API Token in the X-Api-Token field. If you do not currently have an API Token, please follow the steps above to request one. Once complete, select _Authorize_. Last, enter your Application_Token in the X-Application-Token field. If you do not have an Application_Token, a sample is provided or you can follow the link above to request one. Once complete, select _Authorize_.  Requests through a third party (i.e. Postman):  The same information is required as it is through the UI, but it will be passed in through headers. It should look something like this:  X-Account: Account ID goes here!  X-Api-Token: API Token goes here!  X-Application-Token: Application_Token goes here!  Once these three items are successfully passed in as headers, you will be able to make sample requests.  <h2><a href='https://skybox.zendesk.com/hc/en-us/articles/5999881334427-SkyBox-API-Rate-Limits'>API Rate Limits</a> </h2>  A rate limit consists of two variables: an interval and a limit. An interval is a period of time, measured in seconds. A limit is the number of calls that can be made to an endpoint in an interval.  For example, SkyBox’s ‘GET /reports/‘ endpoint has an interval of 1 second and a limit of 1 call per interval. This means that this endpoint has a rate limit of 1 call/second.  Each endpoint, and its respective rate limit, is displayed in this <a href='https://skybox.zendesk.com/hc/en-us/articles/5999881334427-SkyBox-API-Rate-Limits'>Support Article</a>. If the endpoint is not listed, its rate limit is the default, indicated by the ‘*’ at the bottom of the table. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from skybox_openapi_client.models.ticket_sale import TicketSale

class TestTicketSale(unittest.TestCase):
    """TicketSale unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TicketSale:
        """Test TicketSale
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TicketSale`
        """
        model = TicketSale()
        if include_optional:
            return TicketSale(
                performer = skybox_openapi_client.models.performer.Performer(
                    id = 56, 
                    name = '', 
                    event_type = 'CONCERT', 
                    category = skybox_openapi_client.models.category.Category(
                        id = 56, 
                        name = '', 
                        event_type = 'CONCERT', ), ),
                invoice = skybox_openapi_client.models.invoice.Invoice(
                    id = 56, 
                    customer_id = 1, 
                    account_id = 56, 
                    internal_id = 56, 
                    lines = [
                        skybox_openapi_client.models.line.Line(
                            id = 56, 
                            account_id = 56, 
                            target_id = 56, 
                            quantity = 56, 
                            description = '', 
                            amount = 1.337, 
                            line_type = 'PURCHASE', 
                            line_item_type = 'GENERIC', 
                            item_ids = [
                                56
                                ], 
                            inventory = skybox_openapi_client.models.inventory.Inventory(
                                in_hand_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                id = 56, 
                                account_id = 56, 
                                event_id = 56, 
                                quantity = 1, 
                                notes = '', 
                                section = '0', 
                                friendly_section = '', 
                                row = '0', 
                                friendly_row = '', 
                                second_row = '0', 
                                low_seat = 1, 
                                high_seat = 56, 
                                cost = 0, 
                                taxed_cost = 0, 
                                taxed_cost_average = 0, 
                                face_value = 0, 
                                tickets = [
                                    skybox_openapi_client.models.ticket.Ticket(
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
                                        audit_note = '', )
                                    ], 
                                ticket_ids = [
                                    56
                                    ], 
                                stock_type = 'HARD', 
                                split_type = 'DEFAULT', 
                                custom_split = '4807288800152802179809,255008507620686293393339756506851391026912917327294786014820265091272755041757701929816,8648829166332287705219191166478378563875565986836152,878442552846872099969768215793644284896713185763,391533822493516307450680571727935706066206649624154154344797905998687595406261514940126,6181911847617323796802,090825677715773090491175877238622700367804481067589385995284318716971548094372555181862421,6631124808712420936114222711109826538733395457796110376067381730053899,58052502169559516,317511280430869,82098685972204865559364120069172397203049557377344523466774717,4449209840863086849173308822430359428904006736855896821960928068797995608838959,041385259109,704397513785460606525286540688345617514578829587909743529410565030315,686343394018593255940640464666945860767061095947968670024686424498711844097758345981483,5747439303842842667316207163518984658452938633902215260909250934499,631299698075356553489099012599541496045392034315484230789910633798,741065423583407748473970635388115714470362628582763368571328507679471307057663772614811507328336,8014532683419131771650445447793276332359700,124140764715043219639372155212480899923898620805575064022142235164272625417,700754596620195593545684637094724768102535023420967,06988595732724768907776748452146645665151778811976918355637094533182866670344,59857454280902814134061655,74749770869218350540316507726288260364956,58106734443365577936485726893579926346,17427968697470131946717158098098282601203351088428110771393709047277577385387486073992891072,859268702658055751790737411222917393515542534497553753897182663419515939073,21826851629835862525497630,315734687416209252898739367954924953332055160325512091134780053069195057398544811038244094601365668,518080054275277651158741368550642588372630849643972383022183239711797459772511,4923863441930398200961371931098143675,4585597409655983725133283029307396684146151098129275,74031484748057048406763,012305390444429691146816683,62590162931989886063451943153002965663405257281696159185338421281471775129370554372880869,80068788028176591,57773947288750315322069854092495256368335932085407865981,79478141110392468074392913693096543554316761458065295743113605402703763231602541073670910718352952,538806000508604966645755808093721221269357011970272414812762,3184915565373102860524706494479794716186434371109630204722512789789631539877185658176164516026,558612060004170791344273602411081975908504454776508852705547431834446852464274776440429924093379,3334191301103817422345666161680881269273234178339540311,44198085893386085577489376,673801641334118116539205260279829380794272,2586146072038891330853121837080393273002702244330060,31683699021734864618825496589250642444961192316997606,9798590375844096559432,30231825331283,31747113750504035098,811557572531590733576,0697455241548389908041286519157465747250494386227435852744140117391950376636742308967405287857329832,8278099277,,545337671005390384191438526666080939090006101803384448730,906553089871091139007941371983034713864792761764611807161543201777652837379359938707602,31436693097199687718870478752664160044529218603485203892874235672,407,346175217622561451079129084002053973922446460250491,08480202318091412679608951994626419054828306376,8449609676061309,3215691217019343668773775,1845229046673,60897628985316977610549838730873227709908794623450439571022760172291259824751716198004105704713,92637696580005210077890321143954740376642,4918513,7020136920484535009773646552725072831900289667,5485096158329122577030795172540603354506143072998703,3943998184460086033877289718599814379453609220038153782182245281032099,721640337215,122467232398120256921340272291016980482242072082520436555402681562352681709415529694367,594023859622128910937603307445302343788,070910444985981794351908767348997791804305,4591346226553827185816779193441313727890921,28819402597631418607237301054680269917631643588804754,8544963310853711943149541590907146440504824846637067379537201236445727544677262832142', 
                                list_price = 0.0, 
                                vivid_retail_price = 1.337, 
                                expected_value = 0.0, 
                                public_notes = '', 
                                attributes = [
                                    ''
                                    ], 
                                status = 'AVAILABLE', 
                                in_hand_days_before_event = 56, 
                                last_price_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                created_by = '', 
                                created_by_user_id = 56, 
                                last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_update_by = '', 
                                last_delta_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                version = 56, 
                                tags = '', 
                                seat_type = 'CONSECUTIVE', 
                                event_mapping = skybox_openapi_client.models.event_mapping.EventMapping(
                                    event_name = '', 
                                    venue_name = '', 
                                    event_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    valid = True, ), 
                                mapping_id = 56, 
                                exchange_pos_id = 56, 
                                broadcast = True, 
                                zone_seating = True, 
                                electronic_transfer = True, 
                                opt_out_auto_price = True, 
                                hide_seat_numbers = True, 
                                vsr_option = 'ALL', 
                                replenishment_group_id = 56, 
                                replenishment_group = '', 
                                shown_quantity = 1, 
                                integrated_listing = True, 
                                tickets_merged = True, 
                                tickets_split = True, 
                                audit_note = '', 
                                files_uploaded = True, 
                                bar_codes_entered = True, 
                                external_ticket_id_entered = True, 
                                instant_transfer = True, ), 
                            cancelled = True, 
                            delete = True, 
                            cancel = True, 
                            fill_line_id = 56, 
                            inventory_ids = [
                                56
                                ], 
                            created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            created_by = '', 
                            last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            last_update_by = '', )
                        ], 
                    sales_term = 'NET0', 
                    payment_method = 'CREDITCARD', 
                    payment_ref = '', 
                    delivery_method = 'COURIER', 
                    shipping_address_id = 56, 
                    billing_address_id = 56, 
                    tax_amount = 1.337, 
                    shipping_amount = 1.337, 
                    other_amount = 1.337, 
                    internal_notes = '', 
                    public_notes = '', 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    tags = '', 
                    created_by = '', 
                    last_update_by = '', 
                    payment_status = 'UNPAID', 
                    fulfillment_status = 'PENDING', 
                    external_ref = '', 
                    airbill = '', 
                    status = 'CONTACT_NEEDED', 
                    currency_code = 'USD', 
                    payments = [
                        skybox_openapi_client.models.invoice_payment.InvoicePayment(
                            id = 56, 
                            account_id = 56, 
                            reference_number = '', 
                            amount = 1.337, 
                            payment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            user_id = 56, 
                            entity_id = 56, 
                            payment_type = 'INVOICE', 
                            payment_method = 'CREDITCARD', 
                            invoice_id = 1, )
                        ], 
                    invoice_delivery_link = skybox_openapi_client.models.invoice_delivery_link.InvoiceDeliveryLink(
                        enabled = True, 
                        description = '', 
                        all_tickets_with_barcodes = True, 
                        all_tickets_with_pdfs = True, ), 
                    notes = [
                        skybox_openapi_client.models.invoice_note.InvoiceNote(
                            id = 56, 
                            user_id = 56, 
                            account_id = 56, 
                            invoice_id = 56, 
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            text = '', 
                            author = '', )
                        ], 
                    fulfillment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    fulfillment_by_user_id = 56, 
                    outstanding_balance = 1.337, 
                    barcodes_entered = True, 
                    external_ticket_id_entered = True, 
                    files_uploaded = True, ),
                inventory = skybox_openapi_client.models.inventory.Inventory(
                    in_hand_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    id = 56, 
                    account_id = 56, 
                    event_id = 56, 
                    quantity = 1, 
                    notes = '', 
                    section = '0', 
                    friendly_section = '', 
                    row = '0', 
                    friendly_row = '', 
                    second_row = '0', 
                    low_seat = 1, 
                    high_seat = 56, 
                    cost = 0, 
                    taxed_cost = 0, 
                    taxed_cost_average = 0, 
                    face_value = 0, 
                    tickets = [
                        skybox_openapi_client.models.ticket.Ticket(
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
                            audit_note = '', )
                        ], 
                    ticket_ids = [
                        56
                        ], 
                    stock_type = 'HARD', 
                    split_type = 'DEFAULT', 
                    custom_split = '4807288800152802179809,255008507620686293393339756506851391026912917327294786014820265091272755041757701929816,8648829166332287705219191166478378563875565986836152,878442552846872099969768215793644284896713185763,391533822493516307450680571727935706066206649624154154344797905998687595406261514940126,6181911847617323796802,090825677715773090491175877238622700367804481067589385995284318716971548094372555181862421,6631124808712420936114222711109826538733395457796110376067381730053899,58052502169559516,317511280430869,82098685972204865559364120069172397203049557377344523466774717,4449209840863086849173308822430359428904006736855896821960928068797995608838959,041385259109,704397513785460606525286540688345617514578829587909743529410565030315,686343394018593255940640464666945860767061095947968670024686424498711844097758345981483,5747439303842842667316207163518984658452938633902215260909250934499,631299698075356553489099012599541496045392034315484230789910633798,741065423583407748473970635388115714470362628582763368571328507679471307057663772614811507328336,8014532683419131771650445447793276332359700,124140764715043219639372155212480899923898620805575064022142235164272625417,700754596620195593545684637094724768102535023420967,06988595732724768907776748452146645665151778811976918355637094533182866670344,59857454280902814134061655,74749770869218350540316507726288260364956,58106734443365577936485726893579926346,17427968697470131946717158098098282601203351088428110771393709047277577385387486073992891072,859268702658055751790737411222917393515542534497553753897182663419515939073,21826851629835862525497630,315734687416209252898739367954924953332055160325512091134780053069195057398544811038244094601365668,518080054275277651158741368550642588372630849643972383022183239711797459772511,4923863441930398200961371931098143675,4585597409655983725133283029307396684146151098129275,74031484748057048406763,012305390444429691146816683,62590162931989886063451943153002965663405257281696159185338421281471775129370554372880869,80068788028176591,57773947288750315322069854092495256368335932085407865981,79478141110392468074392913693096543554316761458065295743113605402703763231602541073670910718352952,538806000508604966645755808093721221269357011970272414812762,3184915565373102860524706494479794716186434371109630204722512789789631539877185658176164516026,558612060004170791344273602411081975908504454776508852705547431834446852464274776440429924093379,3334191301103817422345666161680881269273234178339540311,44198085893386085577489376,673801641334118116539205260279829380794272,2586146072038891330853121837080393273002702244330060,31683699021734864618825496589250642444961192316997606,9798590375844096559432,30231825331283,31747113750504035098,811557572531590733576,0697455241548389908041286519157465747250494386227435852744140117391950376636742308967405287857329832,8278099277,,545337671005390384191438526666080939090006101803384448730,906553089871091139007941371983034713864792761764611807161543201777652837379359938707602,31436693097199687718870478752664160044529218603485203892874235672,407,346175217622561451079129084002053973922446460250491,08480202318091412679608951994626419054828306376,8449609676061309,3215691217019343668773775,1845229046673,60897628985316977610549838730873227709908794623450439571022760172291259824751716198004105704713,92637696580005210077890321143954740376642,4918513,7020136920484535009773646552725072831900289667,5485096158329122577030795172540603354506143072998703,3943998184460086033877289718599814379453609220038153782182245281032099,721640337215,122467232398120256921340272291016980482242072082520436555402681562352681709415529694367,594023859622128910937603307445302343788,070910444985981794351908767348997791804305,4591346226553827185816779193441313727890921,28819402597631418607237301054680269917631643588804754,8544963310853711943149541590907146440504824846637067379537201236445727544677262832142', 
                    list_price = 0.0, 
                    vivid_retail_price = 1.337, 
                    expected_value = 0.0, 
                    public_notes = '', 
                    attributes = [
                        ''
                        ], 
                    status = 'AVAILABLE', 
                    in_hand_days_before_event = 56, 
                    last_price_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by = '', 
                    created_by_user_id = 56, 
                    last_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_update_by = '', 
                    last_delta_update = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    version = 56, 
                    tags = '', 
                    seat_type = 'CONSECUTIVE', 
                    event_mapping = skybox_openapi_client.models.event_mapping.EventMapping(
                        event_name = '', 
                        venue_name = '', 
                        event_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        valid = True, ), 
                    mapping_id = 56, 
                    exchange_pos_id = 56, 
                    broadcast = True, 
                    zone_seating = True, 
                    electronic_transfer = True, 
                    opt_out_auto_price = True, 
                    hide_seat_numbers = True, 
                    vsr_option = 'ALL', 
                    replenishment_group_id = 56, 
                    replenishment_group = '', 
                    shown_quantity = 1, 
                    integrated_listing = True, 
                    tickets_merged = True, 
                    tickets_split = True, 
                    audit_note = '', 
                    files_uploaded = True, 
                    bar_codes_entered = True, 
                    external_ticket_id_entered = True, 
                    instant_transfer = True, ),
                days_to_event = 56,
                profit = skybox_openapi_client.models.profit_and_loss.ProfitAndLoss(
                    sales = 1.337, 
                    pl_value = 1.337, 
                    pl_percentage = 1.337, 
                    roi = 1.337, 
                    avg_ticket_sales = 1.337, 
                    tickets_profitability = 1.337, 
                    num_tickets = 56, 
                    profitable_tickets = 56, 
                    costs = 1.337, )
            )
        else:
            return TicketSale(
        )
        """

    def testTicketSale(self):
        """Test TicketSale"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
