# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class ShortCodeTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .short_codes.create(sid="SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        values = {'Sid': "SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://proxy.twilio.com/v1/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ShortCodes',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "short_code": "12345",
                "iso_country": "US",
                "capabilities": {
                    "sms_outbound": true,
                    "voice_inbound": false
                },
                "url": "https://proxy.twilio.com/v1/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "is_reserved": false
            }
            '''
        ))

        actual = self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .short_codes.create(sid="SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .short_codes(sid="SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://proxy.twilio.com/v1/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ShortCodes/SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .short_codes(sid="SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .short_codes.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://proxy.twilio.com/v1/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ShortCodes',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://proxy.twilio.com/v1/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "next_page_url": null,
                    "key": "short_codes",
                    "url": "https://proxy.twilio.com/v1/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes?PageSize=50&Page=0"
                },
                "short_codes": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "short_code": "12345",
                        "iso_country": "US",
                        "capabilities": {
                            "sms_outbound": true,
                            "voice_inbound": false
                        },
                        "url": "https://proxy.twilio.com/v1/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "is_reserved": false
                    }
                ]
            }
            '''
        ))

        actual = self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .short_codes.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .short_codes(sid="SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://proxy.twilio.com/v1/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ShortCodes/SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "short_code": "12345",
                "iso_country": "US",
                "capabilities": {
                    "sms_outbound": true,
                    "voice_inbound": false
                },
                "url": "https://proxy.twilio.com/v1/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "is_reserved": false
            }
            '''
        ))

        actual = self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .short_codes(sid="SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .short_codes(sid="SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://proxy.twilio.com/v1/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ShortCodes/SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "short_code": "12345",
                "iso_country": "US",
                "capabilities": {
                    "sms_outbound": true,
                    "voice_inbound": false
                },
                "url": "https://proxy.twilio.com/v1/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ShortCodes/SCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "is_reserved": true
            }
            '''
        ))

        actual = self.client.proxy.v1.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .short_codes(sid="SCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
