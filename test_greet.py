import unittest

from greet import greet


class GreetTests(unittest.TestCase):
    def test_greets_with_name(self):
        self.assertEqual(greet("Mundo"), "Hello, Mundo!")

    def test_raises_on_empty_name(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
