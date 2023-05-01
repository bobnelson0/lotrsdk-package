""" A REST API client """
import requests

class ApiClient():
    """ A rest based API client for The One Api """

    # Defaults
    BASE_URL = 'https://the-one-api.dev/v2/'
    API_KEY_ID = 'api-key'
    TIMEOUT = 30 # Connection timeout in seconds

    # REST verbs
    GET = 'GET'
    POST = 'POST'     # Not implemented yet
    PUT = 'PUT'       # Not implemented yet
    PATCH = 'PATCH'   # Not implemented yet
    DELETE = 'DELETE' # Not implemented yet

    def __init__(self, api_key: str, base_url: str = None):
        """Initializes class, sets defaults, and validates attributes

        Args:
            api_key (str): The API-KEY provided by `The One API`
            base_url (str, optional): Change the base URL. Defaults to BASE_URL if None.

        Raises:
            EnvironmentError: If not API-KEY is found in env vars
        """
        self.api_key = api_key
        self.base_url = base_url

        # If the key is not present, try to get it from the environment vars
        if not api_key:
            raise OSError("API Client failed: api_key has not been set")

        if base_url is None or base_url == '':
            self.base_url = self.BASE_URL

        # Set common headers, including api-key for all requests
        self.http_headers = {
            'Content-Type': 'application/json',
            'X-Api-Client': 'lotrsdk-rest-client-bsn',
            'X-Api-Client-Version': '0.1',
            'User-Agent': 'lotrsdk/0.1',
            'Authorization': f'Bearer {self.api_key}'
        }

    def get(self, relative_path, query_params = None) -> dict:
        """GET base request method
        Joins query params to the URL if provided

        Returns:
            dict: a dictionary representing the JSON payload
        """
        if not query_params:
            query_params = {}
        relative_path += self.params_join(query_params)
        return self.request(self.GET, relative_path)

    def request(self, method: str, relative_path: str) -> dict:
        """Performs request against the API.
        Decodes the JSON response as a dict()

        Returns:
            dict: a dictionary representing the JSON payload
        """
        url = self.url_join(self.base_url, relative_path)

        response = requests.request(method, url, headers=self.http_headers, timeout=self.TIMEOUT)
        response.raise_for_status()

        if not response.text:
            return dict()

        return response.json()

    def url_join(self, *args: str) -> str:
        """Joins the base URL and URL path correctly
        Avoids double // or missing /

        Returns:
            str: A fully formed URL
        """
        return '/'.join([str(x).strip('/') for x in args])

    def params_join(self, query_params: dict) -> str:
        """Joins GET query params if provided

        Returns:
            str: A fully formed query parameter string
        """
        if not query_params:
            return ''
        query_str = '?'
        for k in query_params:
            if query_params[k] is not None:
                query_str = query_str + f"{k}={query_params[k]}&"
        return query_str
