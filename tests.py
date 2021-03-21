import pytest
import requests
from mocket import Mocket, mocketize
from mocket.mockhttp import Entry
from redis import Redis


@pytest.fixture
def redis_client() -> Redis:
    client = Redis(host='localhost', port=6379, db=0)
    yield client


@mocketize
def test_random_url_with_redis(redis_client: Redis):
    url = "http://www.example.com"
    Entry.single_register(Entry.GET, url)

    redis_client.set("key", "value")

    requests.get(url)

    assert Mocket.has_requests()


@mocketize
def test_random_url():
    url = "http://www.example.com"
    Entry.single_register(Entry.GET, url)

    requests.get(url)

    assert Mocket.has_requests()
