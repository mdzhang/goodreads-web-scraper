import importlib
import os

from scrapy.http import Request, TextResponse


def get_fake_response(spider_cls):
    responses_dir = os.path.join(os.path.dirname(__file__),
                                 'fixtures',
                                 'spiders')

    response_file_path = os.path.join(responses_dir,
                                      spider_cls.__name__,
                                      'index.html')

    with open(response_file_path, 'r') as response_file:
        response = TextResponse(url=spider_cls.start_urls[0],
                                body=response_file.read(),
                                encoding='utf-8')

    return response


def get_data(spider_cls):
    module_name = ('goodreads_web_scraper.tests.fixtures.spiders.{}.data'
                   .format(spider_cls.__name__))

    mod = importlib.import_module(module_name)
    return mod
