import unittest
import os
from lotrsdk.entities.quote import Quote

class TestQuote(unittest.TestCase):
    """ Testing Quote class """

    def test_extract(self):
        """ Quote.extract() """
        # Common response
        response = {'_id' : 'abc123',
                    'dialog': 'Something that was said!',
                    'movie': 'm_abc123',
                    'character': 'c_abc123'
                    }
        expected = Quote('abc123', 'Something that was said!', 'm_abc123', 'c_abc123')
        actual = Quote.extract(response)
        self.assertEqual(expected.id, actual.id, "Expected a matching id")
        self.assertEqual(expected.dialog, actual.dialog, "Expected a matching dialog")
        self.assertEqual(expected.movie_id, actual.movie_id, "Expected a matching movie_id")
        self.assertEqual(expected.character_id, actual.character_id, "Expected a matching character_id")


if __name__ == '__main__':
    unittest.main()
