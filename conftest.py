import pytest
import json
from rest_framework.test import APIClient
from workgenius.mandrill.apis import WebhookApi

def events_dict():
    return {
    "mandrill_events": [
    {
        "event": "open",
        "msg": {
            "ts": 1365109999,
            "subject": "This an example webhook message",
            "email": "example.webhook@mandrillapp.com",
            "sender": "example.sender@mandrillapp.com",
            "tags": [
                "webhook-example"
            ],
            "opens": [
                {
                    "ts": 1365111111
                }
            ],
            "clicks": [
                {
                    "ts": 1365111111,
                    "url": "http://mandrill.com"
                }
            ],
            "state": "sent",
            "metadata": {
                "user_id": 111
            },
            "_id": "exampleaaaaaaaaaaaaaaaaaaaaaaaaa",
            "_version": "exampleaaaaaaaaaaaaaaa"
        },
        "_id": "exampleaaaaaaaaaaaaaaaaaaaaaaaaa",
        "ip": "127.0.0.1",
        "location": {
            "country_short": "US",
            "country": "United States",
            "region": "Oklahoma",
            "city": "Oklahoma City",
            "latitude": 35.4675598145,
            "longitude": -97.5164337158,
            "postal_code": "73101",
            "timezone": "-05:00"
        },
        "user_agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1.8) Gecko/20100317 Postbox/1.1.3",
        "user_agent_parsed": {
            "type": "Email Client",
            "ua_family": "Postbox",
            "ua_name": "Postbox 1.1.3",
            "ua_version": "1.1.3",
            "ua_url": "http://www.postbox-inc.com/",
            "ua_company": "Postbox, Inc.",
            "ua_company_url": "http://www.postbox-inc.com/",
            "ua_icon": "http://cdn.mandrill.com/img/email-client-icons/postbox.png",
            "os_family": "OS X",
            "os_name": "OS X 10.6 Snow Leopard",
            "os_url": "http://www.apple.com/osx/",
            "os_company": "Apple Computer, Inc.",
            "os_company_url": "http://www.apple.com/",
            "os_icon": "http://cdn.mandrill.com/img/email-client-icons/macosx.png",
            "mobile": False
        },
        "ts": 1679266475
    },
    {
        "event": "click",
        "msg": {
            "ts": 1365109999,
            "subject": "This an example webhook message",
            "email": "example.webhook@mandrillapp.com",
            "sender": "example.sender@mandrillapp.com",
            "tags": [
                "webhook-example"
            ],
            "opens": [
                {
                    "ts": 1365111111
                }
            ],
            "clicks": [
                {
                    "ts": 1365111111,
                    "url": "http://mandrill.com"
                }
            ],
            "state": "sent",
            "metadata": {
                "user_id": 111
            },
            "_id": "exampleaaaaaaaaaaaaaaaaaaaaaaaaa1",
            "_version": "exampleaaaaaaaaaaaaaaa"
        },
        "_id": "exampleaaaaaaaaaaaaaaaaaaaaaaaaa1",
        "ip": "127.0.0.1",
        "location": {
            "country_short": "US",
            "country": "United States",
            "region": "Oklahoma",
            "city": "Oklahoma City",
            "latitude": 35.4675598145,
            "longitude": -97.5164337158,
            "postal_code": "73101",
            "timezone": "-05:00"
        },
        "user_agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1.8) Gecko/20100317 Postbox/1.1.3",
        "user_agent_parsed": {
            "type": "Email Client",
            "ua_family": "Postbox",
            "ua_name": "Postbox 1.1.3",
            "ua_version": "1.1.3",
            "ua_url": "http://www.postbox-inc.com/",
            "ua_company": "Postbox, Inc.",
            "ua_company_url": "http://www.postbox-inc.com/",
            "ua_icon": "http://cdn.mandrill.com/img/email-client-icons/postbox.png",
            "os_family": "OS X",
            "os_name": "OS X 10.6 Snow Leopard",
            "os_url": "http://www.apple.com/osx/",
            "os_company": "Apple Computer, Inc.",
            "os_company_url": "http://www.apple.com/",
            "os_icon": "http://cdn.mandrill.com/img/email-client-icons/macosx.png",
            "mobile": False
        },
        "url": "http://mandrill.com",
        "ts": 1679266475
    }
]
    }

@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def events_json():
    data = events_dict()
    return json.dumps(data)

@pytest.fixture
def events_serialized():
    data = events_dict()
    serializer = WebhookApi.InputSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.validated_data.get("mandrill_events")

@pytest.fixture
def event_serialized():
    data = events_dict()
    serializer = WebhookApi.InputSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.validated_data.get("mandrill_events")[0]