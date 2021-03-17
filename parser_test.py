import unittest
from crawler import parse


class SimpleTest(unittest.TestCase):

    def test(self):
        with open('sites/sample.html') as f:
            content = f.read()
        actual = parse(content)
        self.assertEqual(('Kiel Leuchtturm', '15. März 2021, 11:40', '300 °, WNW', '10,34 m/s'), actual)


if __name__ == '__main__':
    unittest.main()
