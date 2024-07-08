import unittest
from unittest.mock import patch
from utils import memoize  # Make sure to import the actual memoize decorator

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()
            
            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            
            # Check that the method was called only once
            mock_method.assert_called_once()
            
            # Check that the returned results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

if __name__ == '__main__':
    unittest.main()
