#!/usr/bin/env python3
"""
Unit tests for utils module.
"""

from parameterized import parameterized
import unittest
from typing import Mapping, Sequence, Any, Dict
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    
    Verifies correct value retrieval from nested dictionaries
    and raises KeyError for invalid paths.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # Test single key access
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Test nested access, first key
        ({"a": {"b": 2}}, ("a", "b"), 2),  # Test nested access, second key
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        """
        Test valid paths for access_nested_map.
        
        Args:
            nested_map: The dictionary to search in.
            path: The sequence of keys to navigate.
            expected: The expected result of the function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),  # Test missing key in empty dict
        ({"a": 1}, ("a", "b"), "KeyError: 'b'"),  # Test invalid nested key
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence, expected_message: str) -> None:
        """
        Test invalid paths for access_nested_map to ensure KeyError is raised.
        
        Args:
            nested_map: The dictionary to search in.
            path: The sequence of keys to navigate.
            expected_message: The expected KeyError message.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), expected_message)


if __name__ == '__main__':
    unittest.main()
