import pytest

from think_as_tester.views.default import my_view, register_passage, seen_passages
from think_as_tester.views.notfound import notfound_view
from pyramid.testing import DummyRequest


@pytest.fixture(autouse=True)
def clean_data():
    seen_passages.tons = 0
    seen_passages.lorries = 0


def test_my_view(app_request):
    info = my_view(app_request)
    assert app_request.response.status_int == 200
    assert info["station"] == "Station One"


def test_starts_with_0_lorries(app_request):
    info = my_view(app_request)
    assert info['lorries'] == 0


def test_starts_with_0_tons(app_request):
    info = my_view(app_request)
    assert info['lorries'] == 0


def test_passing_lorrie_should_be_counted():
    info = register_passage(DummyRequest(json={"lorries": 1, "tons": 22}, method="POST"))
    assert info['lorries'] == 1


def test_passing_lorrie_should_add_tonnage():
    info = register_passage(DummyRequest(json={"lorries": 1, "tons": 22}, method="POST"))
    assert info['tons'] == 22


def test_passing_lorries_should_be_added():
    register_passage(DummyRequest(json={"lorries": 1, "tons": 22}, method="POST"))
    info = register_passage(DummyRequest(json={"lorries": 1, "tons": 22}, method="POST"))
    assert info['lorries'] == 2


def test_passing_lorries_should_add_tonnage():
    register_passage(DummyRequest(json={"lorries": 1, "tons": 22}, method="POST"))
    info = register_passage(DummyRequest(json={"lorries": 1, "tons": 33}, method="POST"))
    assert info['tons'] == 55


def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}
