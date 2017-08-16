# -*- coding: utf-8 -*-
"""
goodreads_web_scraper.tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unit test package for goodreads_web_scraper.
"""

import unittest


if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.', pattern='test_*.py')
    unittest.main(verbosity=2)
