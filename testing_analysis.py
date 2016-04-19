import pandas as pd
import unittest

def normalize(x):
    assert(any(x.year == 2000))
    return pd.Series(x.Value.values /
                     sum(x.Value[x.year == 2000]),
                     index=x.year)

class TestNormalize(unittest.TestCase):
    """Testing the normaize function."""
    def test_with_known_values(self):
        test_data = pd.DataFrame({'year': [2000, 2001],
                                  'Value': [2, 4]})
        expected_result = pd.Series([1, 2],
                                   index=[2000, 2001])
        expected_result.index.name = 'year'
        pd.util.testing.assert_series_equal(
            normalize(test_data),
            expected_result)
    def test_y2k_not_in_years_asserts(self):
        with self.assertRaises(AssertionError):
            normalize(pd.DataFrame({'year': []}))

if __name__ == "__main__":
    unittest.main()
