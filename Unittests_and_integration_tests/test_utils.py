#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a", "b")),
        ({}, ("a",)),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised with the correct message."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        # Check if the exception message matches the missing key
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")


if __name__ == "__main__":
    unittest.main()
