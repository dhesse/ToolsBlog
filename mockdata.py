import pandas as pd
import unittest
import StringIO

def readData(data_file):
    return pd.read_csv(data_file, sep="|")

class TestReader(unittest.TestCase):
    def test_gets_separator_right(self):
        """Make sure we have '|' as separator."""
        mockData = StringIO.StringIO("a|b\n1|2\n3|4")
        df = readData(mockData)
        self.assertTrue(all(df.columns.values == ["a", "b"]))

if __name__ == "__main__":
    unittest.main()
