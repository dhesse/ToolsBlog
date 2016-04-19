import pandas as pd
import unittest

def normalize(x):
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

if __name__ == "__main__":
    unittest.main()
