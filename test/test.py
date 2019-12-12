import unittest
from scr.models.api_for_weather import get_wind_direction

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(get_wind_direction(0).replace(' ', ''), "N")
        self.assertEqual(get_wind_direction(45).replace(' ', ''), "NE")
        self.assertEqual(get_wind_direction(90).replace(' ', ''), "E")
        self.assertEqual(get_wind_direction(136).replace(' ', ''), "SE")
        self.assertEqual(get_wind_direction(389).replace(' ', ''), "NE")


if __name__ == '__main__':
    unittest.main()
