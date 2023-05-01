""" BaseEntity Object """
from __future__ import annotations
import os

class BaseEntity:
    """ A class representing a LOTR object in The One API """

    LOTRSDK_API_KEY = 'lotrsdk-api-key'

    def __init__(self, id: str = None):
        """
        Create a new  object with a client
        All entities have IDs, making this required property on all entities
        """
        self.id = id

    @staticmethod
    def check_client(client, client_class):
        """Validate the client

        Returns:
            client: A client of the proper class
        """
        if client is None:
            client = client_class(BaseEntity.get_api_key())
        return client

    @staticmethod
    def get_api_key() -> str:
        """Get the api-key from the environment variables

        Raises:
            EnvironmentError: If the api-key is missing from the env vars

        Returns:
            str: The api-key string
        """
        if os.environ.get(BaseEntity.LOTRSDK_API_KEY) is not None:
            return os.environ.get(BaseEntity.LOTRSDK_API_KEY)
        raise OSError("ApiClient failed to initialize, no api-key")

    @staticmethod
    def check_entity(response: dict) -> dict:
        """Validates the response dict of a single entity and 
        whittles down to the entity in the dict structure

        Args:
            response (dict): A dict representing the API response

        Raises:
            ValueError: Missing `docs` from response, expected in response
            TypeError: Wrong type for `docs`, expects list
            ValueError: For a single entity call, there should only be one
            ValueError: No entity was returned

        Returns:
            dict: The single entry from the response data
        """
        if 'docs' not in response:
            raise ValueError('Unexpected payload, `docs` missing from response')
        response = response['docs']
        if not isinstance(response, list):
            raise TypeError('Unexpected type, `docs` is not a list')
        if len(response) > 1:
            raise ValueError('Unexpected payload, more than one result returned')
        if len(response) < 1:
            raise ValueError('No entity found')

        return response[0]

    @staticmethod
    def check_collection(response: dict) -> dict:
        """Validates the response dict of an expected collection of entities

        Args:
            response (dict): A dict representing the API response

        Raises:
            ValueError: Missing `docs` from response, expected in response
            TypeError: Wrong type for `docs`, expects list
            ValueError: No entity was returned

        Returns:
            dict: The response dict, untouched
        """
        if 'docs' not in response:
            raise ValueError('Unexpected payload, `docs` missing from response')
        if not isinstance(response['docs'], list):
            raise TypeError('Unexpected type, `docs` is not a list')
        if len(response['docs']) < 1:
            raise ValueError('No entities found')

        return response
