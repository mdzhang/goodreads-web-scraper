import unittest

from goodreads_web_scraper.spiders import GenresNewReleasesSpider
from goodreads_web_scraper.tests.utils import get_fake_response, get_data


class TestGenresNewReleasesSpider(unittest.TestCase):
    def setUp(self):
        self.spider = GenresNewReleasesSpider()

    def test_parse(self):
        response = get_fake_response(GenresNewReleasesSpider)

        books = list(self.spider.parse(response))
        data = get_data(GenresNewReleasesSpider)
        expected_books = data.books

        self.assertEqual(books, expected_books)
