import unittest
import os
from lotrsdk.entities.base_entity import BaseEntity

class TestBaseEntity(unittest.TestCase):

    def test_get_api_key(self):
        """ BaseEntity.get_api_key() """
        # API key not set
        self.assertRaises(OSError, lambda: BaseEntity.get_api_key())

        # API key set
        os.environ[BaseEntity.LOTRSDK_API_KEY] = "My API Key"
        expected = 'My API Key'
        actual = BaseEntity.get_api_key()
        self.assertEqual(expected, actual, "API Key strings should be equal")

    def test_check_entity(self):
        """ BaseEntity.check_entity() """
        # One item is successful
        good_response = {'docs': ['item1'],'total': 1}
        expected = 'item1'
        actual = BaseEntity.check_entity(good_response)
        self.assertEqual(expected, actual, "Expected payload did not pass")

        # Docs is missing
        bad_response = {'not_docs': 'item1','total': 1}
        self.assertRaises(ValueError, lambda: BaseEntity.check_entity(bad_response))

        # Docs is not a list
        bad_response = {'docs': 'item1','total': 1}
        self.assertRaises(TypeError, lambda: BaseEntity.check_entity(bad_response))

        # Docs has more than one item
        bad_response = {'docs': ['item1', 'item2'], 'total': 2}
        self.assertRaises(ValueError, lambda: BaseEntity.check_entity(bad_response))

        # Docs has no items
        bad_response = {'docs': [], 'total': 2}
        self.assertRaises(ValueError, lambda: BaseEntity.check_entity(bad_response))

    def test_check_collection(self):
        """ BaseEntity.check_collection() """
        # One item is successful
        good_response = {'docs': ['item1', 'item2'],'total': 2}
        expected = {'docs': ['item1', 'item2'],'total': 2}
        actual = BaseEntity.check_collection(good_response)
        self.assertEqual(expected, actual, "Expected payload did not pass")

        # Docs is missing
        bad_response = {'not_docs': ['item1', 'item2'],'total': 2}
        self.assertRaises(ValueError, lambda: BaseEntity.check_collection(bad_response))

        # Docs is not a list
        bad_response = {'docs': 'item1','total': 2}
        self.assertRaises(TypeError, lambda: BaseEntity.check_collection(bad_response))

        # Docs has no items
        bad_response = {'docs': [], 'total': 2}
        self.assertRaises(ValueError, lambda: BaseEntity.check_entity(bad_response))


if __name__ == '__main__':
    unittest.main()
