import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_webhook_api(api_client, events_json):
    url_ = reverse("api:mandrill:hook")

    response = api_client.post(url_, events_json, content_type="application/json")

    assert response.status_code == 204

@pytest.mark.django_db
def test_empty_webhook_api(api_client):
    url_ = reverse("api:mandrill:hook")

    response = api_client.post(url_, {}, content_type="application/json")

    assert response.status_code == 400
