""" The Movies API """
from .api_client import ApiClient

class MoviesApi:
    """
    A class containing all movie related API calls, defaults, and logic
    Uses the ApiClient to make requests
    """
    # Movie API defaults
    API_PATH = '/movie/'
    API_QUOTE_PATH = '/quote/'
    QUERY_LIMIT = 1000

    def __init__(self, api_key: str):
        """
        Initialize the ApiClient

        Args:
            api_key (str): The API key provided by `The One Ring`
        """
        self.client = ApiClient(api_key)

    def get_by_id(self, id: str) -> str:
        """
        Make an API call to get 1 movie based on id

        Args:
            id (str): An ID for the movie

        Returns:
            str: String payload from the API
        """
        response = self.client.get(self.API_PATH + id)
        return response

    def get_all(self, sort: str = None) -> str:
        """
        Make an API call to get all movies

        The limit is set to allow the full list to be returned
        Passing a sort string will sort the results (eg. `sort=name:asc`)
        Sort documentation here: https://the-one-api.dev/documentation

        Args:
            sort (str, optional): A sort string like 'name:asc'. Defaults to None.

        Returns:
            str: String payload from the API
        """
        return self.query({'limit': self.QUERY_LIMIT, 'page': 1, 'offset': 0, 'sort': sort})

    def query(self, params: dict = None) -> str:
        """
        Make and API call to get a list of movies based on a query

        Provided a query, returns a collection of Movies
        Query example: `name=/towe/i` will return `The Two Towers` movie entity
        Filtering documentation here: https://the-one-api.dev/documentation
        Does not support negation (!=) yet.

        Args:
            params (dict, optional): Dict of key value query pairs (ex. {'name': '/towe/i'}). Defaults to None.

        Returns:
            str: String payload from the API
        """
        response = self.client.get(self.API_PATH, params)
        return response
    
    def get_quotes(self, movie_id: str, params: dict = None) -> str:
        """
        Make and API call to get a list of quotes from a movie

        Provided a query, returns a collection of Quotes
        Query example: 'name=/towe/i' will return 'The Two Towers'
        Filtering documentation here: https://the-one-api.dev/documentation

        Args:
            movie_id (str): string ID of the movie
            params (dict, optional): Dict of key value query pairs. For filtering. 
                                     Defaults to None.

        Returns:
            str: String payload from the API
        """
        response = self.client.get(self.API_PATH + movie_id + self.API_QUOTE_PATH, params)
        return response
