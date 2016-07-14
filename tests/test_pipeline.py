import unittest
from pipeline.temporalcv import make_fake_todays


class TemporalCVTest(unittest.TestCase):
    def test_one_year_fake_todays(self):
        actual_output = make_fake_todays(365)
        expected_output = ("[datetime.datetime(2014, 1, 1, 0, 0), "
                           "datetime.datetime(2015, 1, 1, 0, 0), "
                           "datetime.datetime(2016, 1, 1, 0, 0)]")
        self.assertEqual(str(actual_output), expected_output)


    def test_string_input_fake_todays(self):
        with self.assertRaises(TypeError):
            actual_output = make_fake_todays('string input')