import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py' ."""

    def test_first_last_name(self):
        """Do names like 'Tylor Roth' work?"""
        formatted_name = get_formatted_name('tylor', 'roth')
        self.assertEqual(formatted_name, 'Tylor Roth')

    def test_first_middle_last(self):
        """Do names like 'Tylor James Roth' work?"""
        formatted_name = get_formatted_name(
            'Tylor', 'Roth', 'James'
        )
        self.assertEqual(formatted_name, 'Tylor James Roth')
        
if __name__ == '__main__':
    unittest.main()

    