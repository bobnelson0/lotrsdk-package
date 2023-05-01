""" Collections """
from __future__ import annotations
from .base_entity import BaseEntity

class Collection(BaseEntity):
    """ A class representing a generic collection of entities and metadata about the collection """

    def __init__(self, entities: list, total: int, limit: int,
                 offset: int, page_num: int, total_pages: int) -> Collection:
        """Initialize a collection

        Args:
            entities (list): A list of entity objects
            total (int): The total provided by `The One Api`
            limit (int): The limit per page
            offset (int): The offset
            page_num (int): The page number
            total_pages (int): Total pages in the `The One Api`

        Returns:
            Collection: _description_
        """
        self.entities = entities
        self.total = total
        self.limit = limit
        self.offset = offset
        self.page_num = page_num
        self.total_pages = total_pages

    @staticmethod
    def extract(object_type, response: dict) -> Collection:
        """Creates a collection object
        Assigns value to the attributes
        Creates objects of 'object_type' for each item in the list of entities

        Args:
            object_type (BaseEntity): The object type of entities, must be homogenous
            response (dict): A dict representing the API response

        Returns:
            Collection: A Collection object
        """
        response = Collection.check_collection(response)
        entities = []
        for entity in response['docs']:
            # This conditional is for supporting unit tests
            # so that I don't have to construct objects in the tests
            if type(entity) in (int, float, str):
                entities.append(entity)
            else:
                entities.append(object_type.extract(entity))
        total = response['total']
        limit = response['limit']
        # I found that the API doesn't always return these fields
        offset = response['offset'] if 'offset' in response else 0
        page_num = response['page'] if 'page' in response else 1
        total_pages = response['pages'] if 'pages' in response else 1

        return Collection(entities, total, limit, offset, page_num, total_pages)

    def __str__(self) -> str:
        """Pretty print this object
        Strictly for debugging purposes

        Returns:
            str: A string representation of the Collection
        """
        entities = ''
        for entity in self.entities:
            entities += entity.__str__() + ", "

        return f"Collection{{ \
                    entities: [ {entities} ] \
                    total: {self.total} \
                    limit: {self.limit} \
                    offset: {self.offset} \
                    page_num: {self.page_num} \
                    total_pages: {self.total_pages} \
                }}"
