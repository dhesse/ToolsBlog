import unittest
import pandas as pd

class NoDateInDataError(Exception):
    pass

class NoSisalInDataError(Exception):
    pass

class NoStandardCurrencyInDataError(Exception):
    pass

def extract_year(df):
    if 'Date' not in df:
        raise NoDateInDataError()
    df['year'] = df.Date.apply(lambda x: int(x[4:8]))
    return df

SLU = 'Standard Local Currency/tonne'

def clean_data(df):
    if not any(df.item == 'Sisal'):
        raise NoSisalInDataError
    if not any(df.Unit == SLU):
        raise NoStandardCurrencyInDataError
    return df[(df.item == 'Sisal') &
              (df.Unit == SLU)]

class TestExtractYear(unittest.TestCase):
    """You should test more here, connected to the expected string
    format in the date column."""
    def test_no_Date_column_raises(self):
        with self.assertRaises(NoDateInDataError):
            extract_year(pd.DataFrame({}))
    def test_known_values(self):
        test_data = pd.DataFrame({'Date': ["1-1-1234"]})
        expected_result = pd.Series([1234], name='year')
        pd.util.testing.assert_series_equal(
            extract_year(test_data).year,
            expected_result)

class TestCleanData(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.DataFrame(
            {'item': ["Sisal", "Hay"]*2,
             'Unit': [SLU, SLU, 'dollar', 'dollar']})
    def test_cleans_non_sisal(self):
        result = clean_data(self.test_data)
        self.assertTrue(all(result.item == "Sisal"))
    def test_cleans_non_slc(self):
        result = clean_data(self.test_data)
        self.assertTrue(all(result.Unit == SLU))
    def test_no_sisal_raises(self):
        with self.assertRaises(NoSisalInDataError):
            clean_data(pd.DataFrame(
                {'item': [None],
                 'Unit': [SLU]}))
    def test_no_slc_raises(self):
        with self.assertRaises(NoStandardCurrencyInDataError):
            clean_data(pd.DataFrame(
                {'item': ['Sisal'],
                 'Unit': [None]}))
            
        
if __name__ == "__main__":
    unittest.main()
