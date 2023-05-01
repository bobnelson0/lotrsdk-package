""" Quotes """
from __future__ import annotations
from lotrsdk.api import QuotesApi
from .base_entity import BaseEntity
from .collection import Collection


class Quote(BaseEntity):
    """ A class representing a LOTR Quote entity in `The One API` """

    CLIENT_CLASS = QuotesApi

    def __init__(self, id: str = None, dialog: str = None,
                 movie_id: str = None, character_id = None, client = None) -> Quote:
        """Create a new quote object with a client

        Args:
            id (str, optional): The quote id. Defaults to None.
            dialog (str, optional): The dialog contents. Defaults to None.
            movie_id (str, optional): The id of the movie where the quote appears. Defaults to None.
            character_id (_type_, optional): The id of the character who said it. Defaults to None.
            client (QuotesApi, optional): A valid QuotesApi client. 
                                          If None, looks to env vars. Defaults to None.

        Returns:
            Quote: A Quote object
        """
        # Parent method assigns self.id
        super().__init__(id)
        self.dialog = dialog
        self.movie_id = movie_id
        self.character_id = character_id
        self.client = self.check_client(client, self.CLIENT_CLASS)

    @staticmethod
    def get_by_id(id: str, client = None) -> Quote:
        """Get a Quote object by the ID given

        Args:
            id (str): ID of the quote
            client (QuotesApi, optional): For overriding the client. Defaults to None

        Returns:
            Quote: A Quote object
        """
        client = Quote.check_client(client, Quote.CLIENT_CLASS)
        response = Quote.check_entity(client.get_by_id(id))
        return Quote.extract(response)

    @staticmethod
    def get_all(client = None) -> Collection:
        """Get all the quotes as a collection of Quote objects
        Collection object also contains metadata like total, pages, etc

        Args:
            client (QuotesApi, optional): For overriding the client. Defaults to None

        Returns:
            Collection: A Collection of Quote objects and metadata
        """
        client = Quote.check_client(client, Quote.CLIENT_CLASS)
        return Collection.extract(Quote, client.get_all())

    @staticmethod
    def query(params: dict, client = None) -> Collection:
        """Get all the quotes, based on filters, as a collection of Quote objects
        Collection object also contains metadata like total, pages, etc
        Query example: `dialog=/Hornburg/i` will return Quotes with `Hornburg`
        Filtering documentation here: https://the-one-api.dev/documentation
        Does not support negation (!=) yet.

        Args:
            params (dict): Dict of key value query pairs (ex. {'dialog': '/Hornburg/i'}). 
                           Defaults to None.
            client (QuotesApi, optional): For overriding the client. Defaults to None

        Returns:
            Collection: A Collection of Quote objects plus metadata
        """
        client = Quote.check_client(client, Quote.CLIENT_CLASS)
        return Collection.extract(Quote, client.query(params))

    @staticmethod
    def extract(response: dict) -> Quote:
        """Extract a Quote object from a dict

        Args:
            response (dict): Dict representing a Quote

        Returns:
            Quote: A quote Object
        """
        return Quote(response['_id'], response['dialog'],
                     response['movie'], response['character'])


    def __str__(self) -> str:
        """
        Pretty print this object
        Strictly for debugging purposes
        """
        return f"Quote{{ id: {self.id}, name: {self.dialog}, \
            movie_id: {self.movie_id}, \
            character_id: {self.character_id}, \
        }}"
