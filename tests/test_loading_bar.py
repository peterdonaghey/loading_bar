import sys
import os

# Add the root directory of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from loading_bar.loading_bar import loading_bar
import unittest
from io import StringIO

class TestLoadingBar(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_loading_bar_in_loop(self):
        # Test the loading bar functionality within a loop
        total_iterations = 10
        for i in range(total_iterations):
            # Reset the StringIO object before each call
            sys.stdout = StringIO()
            loading_bar(i, total_iterations, 10)

            # Construct the expected output for this iteration
            percent = (i + 1) / total_iterations * 100
            filled_length = int(10 * (i + 1) // total_iterations)
            bar = '█' * filled_length + '-' * (10 - filled_length)
            expected_output = f"[{bar}] {i+1}/{total_iterations} ({percent:.2f}%)"

            # Get the actual output and compare
            actual_output = sys.stdout.getvalue().replace('\r', '').strip()
            self.assertEqual(actual_output, expected_output)




    def test_loading_bar_progress(self):
        # Test normal functionality
        loading_bar(4, 10, 10)
        self.assertEqual(sys.stdout.getvalue().strip(), "[█████-----] 5/10 (50.00%)")

    def test_invalid_i_type(self):
        # Test invalid 'i' type
        with self.assertRaises(ValueError):
            loading_bar("a", 10, 10)

    def test_invalid_total_type(self):
        # Test invalid 'total' type
        with self.assertRaises(ValueError):
            loading_bar(5, "10", 10)

    def test_invalid_length_type(self):
        # Test invalid 'length' type
        with self.assertRaises(ValueError):
            loading_bar(5, 10, "10")

    def test_i_out_of_range(self):
        # Test 'i' out of range
        with self.assertRaises(ValueError):
            loading_bar(11, 10, 10)

    def test_negative_total(self):
        # Test negative 'total'
        with self.assertRaises(ValueError):
            loading_bar(5, -10, 10)

    def test_negative_length(self):
        # Test negative 'length'
        with self.assertRaises(ValueError):
            loading_bar(5, 10, -10)

    def tearDown(self):
        # Reset stdout
        sys.stdout = self.held

if __name__ == '__main__':
    unittest.main()
