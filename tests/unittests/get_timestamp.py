import unittest

from items import get_timestamp


class TestGetTimestamp(unittest.TestCase):
    def test_get_timestamp(self):
        result = get_timestamp()
        self.assertEqual(len(result), 19)
        self.assertEqual(str(type(result)), "<class 'str'>")


if __name__ == "__main__":
    unittest.main()
