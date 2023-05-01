import unittest
from lotrsdk.api.api_client import ApiClient

class TestApiClient(unittest.TestCase):
    """ Testing ApiClient class """

    def test_init(self):
        """ ApiClient.__init__() """
        # API key not set
        self.assertRaises(OSError, lambda: ApiClient(None, "base-url.com/"))

        # API key set
        client = ApiClient("My API Key", "base-url.com/")
        expected = "My API Key"
        actual = client.api_key
        self.assertEqual(expected, actual, "API Key strings should be equal")

    def test_url_join(self):
        """ ApiClient.url_join() """
        # Common case
        client = ApiClient('api-key')
        expected = "base-url.com/some-path"
        actual = client.url_join('base-url.com/', '/some-path/')
        self.assertEqual(expected, actual, "Paths are are not the same")

        # Missing slash on base
        client = ApiClient('api-key')
        expected = "base-url.com/some-path"
        actual = client.url_join('base-url.com', '/some-path/')
        self.assertEqual(expected, actual, "Paths are are not the same")

        # Missing slash on path
        client = ApiClient('api-key')
        expected = "base-url.com/some-path"
        actual = client.url_join('base-url.com/', 'some-path/')
        self.assertEqual(expected, actual, "Paths are are not the same")

        # Missing slashes everywhere
        client = ApiClient('api-key')
        expected = "base-url.com/some-path"
        actual = client.url_join('base-url.com', 'some-path')
        self.assertEqual(expected, actual, "Paths are are not the same")

        # Too many slashes
        client = ApiClient('api-key')
        expected = "base-url.com/some-path"
        actual = client.url_join('base-url.com//', '//some-path//')
        self.assertEqual(expected, actual, "Paths are are not the same")

        # Empty path
        client = ApiClient('api-key')
        expected = "base-url.com/"
        actual = client.url_join('base-url.com/', '')
        self.assertEqual(expected, actual, "Paths are are not the same")

    def test_params_join(self):
        """ ApiClient.params_join() """

        # Common case
        client = ApiClient('api-key')
        params = {'sort': 'name:asc', 'limit': 100, 'some_var': 'hi'}
        expected = "?sort=name:asc&limit=100&some_var=hi&"
        actual = client.params_join(params)
        self.assertEqual(expected, actual, "Params are the same")

        # A 'None' param
        client = ApiClient('api-key')
        params = {'sort': 'name:asc', 'limit': 100, 'some_var': None}
        expected = "?sort=name:asc&limit=100&"
        actual = client.params_join(params)
        self.assertEqual(expected, actual, "Params are the same")

        # No params
        client = ApiClient('api-key')
        params = {}
        expected = ""
        actual = client.params_join(params)
        self.assertEqual(expected, actual, "Params are the same")


if __name__ == '__main__':
    unittest.main()
