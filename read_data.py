import unittest
import pandas as pd

def extract_year(df):
    df['year'] = df.Date.apply(lambda x: int(x[4:8]))
    return df

class TestExtractYear(unittest.TestCase):
    def test_known_values(self):
        test_data = pd.DataFrame({'Date': ["1-1-1234"]})
        expected_result = pd.Series([1234], name='year')
        pd.util.testing.assert_series_equal(
            extract_year(test_data).year,
            expected_result)

if __name__ == "__main__":
    unittest.main()
