import unittest
# from sample import crawl, scrape, print_items
import sample


class TestSample(unittest.TestCase):
    """
    test class of sample.py
    """

    @classmethod
    def setUpClass(cls):
        print('test start')
        cls.html = ""

    @classmethod
    def tearDownClass(cls):
        print('test over')

    def test_crawl(self):
        """
        test case for crawl
        """
        resp = sample.crawl()
        self.assertEqual(201, resp.status_code)
        self.html = resp.text

    def test_scrape(self):
        """
        test case for crawl
        """
        items = sample.scrape(self.html)
        self.assertIsNotNone(items)


if __name__ == "__main__":
    unittest.main()
