import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def response(client):
    response = client.get(reverse('core:home'))
    return response


def test_status_code(response):
    assert response.status_code == 200


def test_page_title(response):
    assert_contains(response, '<title>Python Pro</title>')


def test_home_link(response):
    assert_contains(response, f'href="{reverse("core:home")}">Home')
