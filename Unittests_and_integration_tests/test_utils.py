#!/usr/bin/env python3
"""
Unit tests for the utils module.
"""
import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test cases for the memoize decorator."""

    def test_memoize(self):
        """Test that a_method is called only once when using memoize."""

        class TestClass:
            """Example class to test memoization."""

            def a_method(self):
                """A method to be memoized."""
                return 42

            @memoize
            def a_property(self):
                """A property using the memoize decorator."""
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Mock the a_method function
        with patch.object(test_instance, 'a_method', return_value=42) as mock_method:
            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assertions
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
