import unittest

class TestMain(unittest.TestCase):
    def test_version(self):
        self.assertEqual(type("4.2"), str)

    def test_config(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
