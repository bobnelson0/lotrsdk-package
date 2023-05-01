import unittest
import os
from lotrsdk.entities.collection import Collection

class TestCollection(unittest.TestCase):
    """ Testing Collection class """

    def test_extract(self):
        """ Collection.extract() """
        # Good response
        good_response = {'docs': ['item1', 'item2'],
                    'total': 2,
                    'limit': 1000,
                    'offset': 0,
                    'page': 1,
                    'pages': 1
                    }
        expected = Collection(['item1', 'item2'], 2, 1000, 0, 1, 1)
        actual = Collection.extract(str, good_response)
        self.assertEqual(expected.entities, actual.entities, "Expected a matching entities")
        self.assertEqual(expected.total, actual.total, "Expected a matching total")
        self.assertEqual(expected.limit, actual.limit, "Expected a matching limit")
        self.assertEqual(expected.offset, actual.offset, "Expected a matching offset")
        self.assertEqual(expected.page_num, actual.page_num, "Expected a matching page_num")
        self.assertEqual(expected.total_pages, actual.total_pages, "Expected a matching total_pages")

        # Missing fields in response default to expected values
        good_response = {'docs': ['item1', 'item2'],
                    'total': 2,
                    'limit': 1000,
                    }
        expected = Collection(['item1', 'item2'], 2, 1000, 0, 1, 1)
        actual = Collection.extract(str, good_response)
        self.assertEqual(expected.entities, actual.entities, "Expected a matching entities")
        self.assertEqual(expected.total, actual.total, "Expected a matching total")
        self.assertEqual(expected.limit, actual.limit, "Expected a matching limit")
        self.assertEqual(expected.offset, actual.offset, "Expected a matching offset")
        self.assertEqual(expected.page_num, actual.page_num, "Expected a matching page_num")
        self.assertEqual(expected.total_pages, actual.total_pages, "Expected a matching total_pages")


if __name__ == '__main__':
    unittest.main()
