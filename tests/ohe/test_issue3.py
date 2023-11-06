import unittest

from one_hot_encoder import fit_transform


class TestOHE(unittest.TestCase):
    """Test one_hot_encoder.py."""

    def test_fit_transform_not_none(self):
        """Test case when fit_transform returns not None."""
        categories = ["Moscow", "New York", "London"]
        result = fit_transform(categories)
        self.assertIsNotNone(result)

    def test_fit_transform_type(self):
        """Test case when fit_transform returns list."""
        categories = ["Moscow", "New York", "London"]
        result = fit_transform(categories)
        self.assertIsInstance(result, list)

    def test_fit_transform_single_category(self):
        """Test case with single category."""
        categories = ["Moscow"]
        expected_result = [("Moscow", [1])]
        self.assertEqual(fit_transform(categories), expected_result)

    def test_fit_transform_duplicate_categories(self):
        """Test case with duplicate categories."""
        categories = ["Moscow", "Moscow"]
        expected_result = [("Moscow", [1]), ("Moscow", [1])]
        self.assertEqual(fit_transform(categories), expected_result)

    def test_fit_transform(self):
        """Test case with multiply categories."""
        cities = ["Moscow", "New York", "Moscow", "London"]
        expected_result = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(cities), expected_result)

    def test_fit_transform_no_categories(self):
        """Test case with empty input."""
        with self.assertRaises(TypeError):
            fit_transform()

if __name__ == "__main__":
    pass
