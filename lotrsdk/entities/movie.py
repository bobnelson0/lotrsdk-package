""" Movie object """
from __future__ import annotations
from lotrsdk.api import MoviesApi
from .base_entity import BaseEntity
from .quote import Quote
from .collection import Collection


class Movie(BaseEntity):
    """ A class representing a LOTR movie entity in `The One API` """

    CLIENT_CLASS = MoviesApi

    def __init__(self, id: str = None, name: str = None, runtime_in_minutes: int = None, 
                 budget_in_millions: int = None, box_office_revenue_in_millions: int = None, 
                 academy_award_nominations: int = None, academy_award_wins: int = None,
                 rotten_tomatoes_score: int = None, client = None) -> Movie:
        """Create a new movie object with a client

        Args:
            id (str, optional): id of movie. Defaults to None.
            name (str, optional): name of movie. Defaults to None.
            runtime_in_minutes (int, optional): Runtime. Defaults to None.
            budget_in_millions (int, optional): Budget. Defaults to None.
            box_office_revenue_in_millions (int, optional): Revenue from box office. 
                                                            Defaults to None.
            academy_award_nominations (int, optional): Academy nominations. Defaults to None.
            academy_award_wins (int, optional): Academy wins. Defaults to None.
            rotten_tomatoes_score (int, optional): RT score. Defaults to None.
            client (MoviesApi, optional): A valid MoviesApi client. 
                                          If None, looks to env vars. Defaults to None.

        Returns:
            Movie: A movie object
        """
        # Parent method assigns self.id
        super().__init__(id)
        self.name = name
        self.runtime_in_minutes = runtime_in_minutes
        self.budget_in_millions = budget_in_millions
        self.box_office_revenue_in_millions = box_office_revenue_in_millions
        self.academy_award_nominations = academy_award_nominations
        self.academy_award_wins = academy_award_wins
        self.rotten_tomatoes_score = rotten_tomatoes_score
        self.client = self.check_client(client, self.CLIENT_CLASS)

    @staticmethod
    def get_by_id(id: str, client = None) -> Movie:
        """Get a Movie object by the ID given

        Args:
            id (str): id of the movie
            client (MoviesApi, optional): For overriding the client. Defaults to None

        Returns:
            Movie: a movie object
        """
        client = Movie.check_client(client, Movie.CLIENT_CLASS)
        response = Movie.check_entity(client.get_by_id(id))
        return Movie.extract(response)

    @staticmethod
    def get_all(client = None) -> Collection:
        """Get all the movies as a collection of Movie objects
        Collection object also contains metadata like total, pages, etc

        Args:
            client (MoviesApi, optional): For overriding the client. Defaults to None

        Returns:
            Collection: A Collection of Movie objects plus metadata
        """
        client = Movie.check_client(client, Movie.CLIENT_CLASS)
        return Collection.extract(Movie, client.get_all())

    @staticmethod
    def query(params: dict, client = None) -> Collection:
        """Get all the movies, based on filters, as a collection of Movie objects
        Collection object also contains metadata like total, pages, etc
        Query example: `name=/towe/i` will return `The Two Towers` movie entity
        Filtering documentation here: https://the-one-api.dev/documentation
        Does not support negation (!=) yet.

        Args:
            params (dict): Dict of key value query pairs (ex. {'name': '/towe/i'}). 
                           Defaults to None.
            client (MoviesApi, optional): For overriding the client. Defaults to None

        Returns:
            Collection: A Collection of Movie objects plus metadata
        """
        client = Movie.check_client(client, Movie.CLIENT_CLASS)
        return Collection.extract(Movie, client.query(params))
    
    @staticmethod
    def get_quotes(id: str, params: dict, client = None) -> Collection:
        """Get all the quotes from a movie, as a collection of Quote objects
        Collection object also contains metadata like total, pages, etc

        Args:
            id (str): id of the movie
            params (dict): paging and filtering params
            client (MoviesApi, optional): For overriding the client. Defaults to None

        Returns:
            Collection: A Collection of Quote objects plus metadata
        """
        client = Movie.check_client(client, Movie.CLIENT_CLASS)
        return Collection.extract(Quote, client.get_quotes(id, params))

    @staticmethod
    def extract(response: dict) -> Movie:
        """Extract a Movie object from a dict

        Args:
            response (dict): Dict representing a Movie

        Returns:
            Movie: A movie Object
        """
        return Movie(response['_id'], response['name'], response['runtimeInMinutes'],
                     response['budgetInMillions'], response['boxOfficeRevenueInMillions'],
                     response['academyAwardNominations'], response['academyAwardWins'],
                     response['rottenTomatoesScore'])


    def __str__(self) -> str:
        """
        Pretty print this object
        Strictly for debugging purposes
        """
        return f"Movie{{ id: {self.id}, name: {self.name}, \
            runtime_in_minutes: {self.runtime_in_minutes}, \
            budget_in_millions: {self.budget_in_millions}, \
            box_office_revenue_in_millions: {self.box_office_revenue_in_millions}, \
            academy_award_nominations: {self.academy_award_nominations}, \
            academy_award_wins: {self.academy_award_wins}, \
            rotten_tomatoes_score:  {self.rotten_tomatoes_score}, \
        }}"
