import unittest
from my_lambdata.date_split import date

print("hi")

class TestDate(unittest.TestCase):

    def test_day(self):
        self.assertEqual(date('2/29/12').day, '29')

    def test_month(self):
        self.assertEqual(date('2/2/12').month, '2')

    def test_year(self):
        self.assertEqual(date('11/2/12').year, '12')

if __name__ == "__main":
    unittest.main()