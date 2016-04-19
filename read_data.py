import unittest
import pandas as pd

class NoDateInData(Exception):
    pass

class NoSisalInData(Exception):
    pass

class NoStandardCurrencyInData(Exception):
    pass

def extract_year(df):
    if 'Date' not in df:
        raise NoDateInData()
    df['year'] = df.Date.apply(lambda x: int(x[4:8]))
    return df

def clean_data(df):
    return df[(df.item == 'Sisal') &
              (df.Unit == 'Standard Local Currency/tonne')]

class TestExtractYear(unittest.TestCase):
    """You should test more here, connected to the expected string
    format in the date column."""
    def test_no_Date_column_raises(self):
        with self.assertRaises(NoDateInData):
            extract_year(pd.DataFrame({}))
    def test_known_values(self):
        test_data = pd.DataFrame({'Date': ["1-1-1234"]})
        expected_result = pd.Series([1234], name='year')
        pd.util.testing.assert_series_equal(
            extract_year(test_data).year,
            expected_result)

class TestCleanData(unittest.TestCase):
    def setUp(self):
        self.slc = 'Standard Local Currency/tonne'
        self.test_data = pd.DataFrame(
            {'item': ["Sisal", "Hay"]*2,
             'Unit': [self.slc, self.slc, 'dollar', 'dollar']})
    def test_cleans_non_sisal(self):
        result = clean_data(self.test_data)
        self.assertTrue(all(result.item == "Sisal"))
    def test_cleans_non_slc(self):
        result = clean_data(self.test_data)
        self.assertTrue(all(result.Unit == self.slc))
    def test_no_sisal_raises(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
