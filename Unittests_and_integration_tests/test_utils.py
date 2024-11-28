#!/usr/bin/env python3
from parameterized import parameterized
import unittest
from typing import Dict, Tuple, Any
from utils import access_nested_map  # Import the actual function you're testing


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    
    This test case verifies that the access_nested_map function correctly retrieves
    values from nested dictionaries based on the given path.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # Test for simple dictionary with direct access
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Test for nested dictionary with first key access
        ({"a": {"b": 2}}, ("a", "b"), 2)  # Test for nested dictionary with second key access
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any) -> None:
        """
        Test the access_nested_map function with various inputs.
        
        Args:
            nested_map: The dictionary to search in.
            path: The path to access the value in the dictionary.
            expected: The expected result that should be returned by the function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
