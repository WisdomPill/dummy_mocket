import requests
from django.core.cache import cache
from django.test.testcases import TestCase
from mocket import Mocket, mocketize
from mocket.mockhttp import Entry


class TestMocketStrangeBehaviour(TestCase):
    def tearDown(self):
        cache.clear()

    @mocketize
    def test_b_random_url(self):
        url = "http://www.example.com"
        Entry.single_register(Entry.GET, url)

        requests.get(url)

        self.assertTrue(Mocket.has_requests())

    @mocketize
    def test_a_random_url(self):
        url = "http://www.example.com"
        Entry.single_register(Entry.GET, url)

        cache.set("key", "value")

        requests.get(url)

        self.assertTrue(Mocket.has_requests())
