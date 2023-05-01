import unittest
from lotrsdk.entities.movie import Movie

class TestMovie(unittest.TestCase):
    """ Testing Movie class """

    def test_extract(self):
        """ Movie.extract() """
        # Common response
        response = {'_id' : 'abc123',
                            'name': 'a movie',
                            'runtimeInMinutes': 90,
                            'budgetInMillions': 12,
                            'boxOfficeRevenueInMillions': 14,
                            'academyAwardNominations': 3,
                            'academyAwardWins': 2,
                            'rottenTomatoesScore': 75
                        }
        expected = Movie('abc123', 'a movie', 90, 12, 14, 3, 2, 75)
        actual = Movie.extract(response)
        self.assertEqual(expected.id, actual.id, "Expected a matching id")
        self.assertEqual(expected.name, actual.name, "Expected a matching name")
        self.assertEqual(expected.runtime_in_minutes, 
                         actual.runtime_in_minutes, 
                         "Expected a matching runtime_in_minutes")
        self.assertEqual(expected.budget_in_millions, 
                         actual.budget_in_millions, 
                         "Expected a matching budget_in_millions")
        self.assertEqual(expected.box_office_revenue_in_millions, 
                         actual.box_office_revenue_in_millions, 
                         "Expected a matching box_office_revenue_in_millions")
        self.assertEqual(expected.academy_award_nominations, 
                         actual.academy_award_nominations, 
                         "Expected a matching academy_award_nominations")
        self.assertEqual(expected.academy_award_wins, 
                         actual.academy_award_wins, 
                         "Expected a matching academy_award_wins")
        self.assertEqual(expected.rotten_tomatoes_score, 
                         actual.rotten_tomatoes_score, 
                         "Expected a matching rotten_tomatoes_score")


if __name__ == '__main__':
    unittest.main()
