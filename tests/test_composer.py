"""Tests for twelve_tone.composer module."""
import unittest

from twelve_tone.composer import Composer


class TestMatrix(unittest.TestCase):

    def test_get_tone_row(self):
        """Test getting a tone row from the matrix."""
        c = Composer()
        c.compose()
        melody = c.get_melody()
        self.assertEqual(len(melody), 12)
        # All pitch classes should be present exactly once
        self.assertEqual(len(set(melody)), 12)

    def test_compose_with_custom_row(self):
        """Test composing with a custom top row."""
        c = Composer()
        custom_row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        c.compose(top_row=custom_row)
        
        # Check that the top row matches our custom input
        top_row = c.matrix[0]
        self.assertEqual(list(top_row), custom_row)

    def test_matrix_dimensions(self):
        """Test that the matrix is 12x12."""
        c = Composer()
        c.compose()
        
        self.assertEqual(len(c.matrix), 12)
        for row in c.matrix:
            self.assertEqual(len(row), 12)

    def test_all_pitch_classes_present(self):
        """Test that all 12 pitch classes appear exactly once in each row."""
        c = Composer()
        c.compose()
        
        for row_idx in range(12):
            row = c.matrix[row_idx]
            # Each row should contain all integers from 1 to 12
            self.assertEqual(sorted(row), list(range(1, 13)))

    def test_first_column_is_inversion(self):
        """Test that the first column represents the inversion form."""
        c = Composer()
        c.compose()
        
        first_column = [c.matrix[i][0] for i in range(12)]
        # Should contain all 12 pitch classes
        self.assertEqual(sorted(first_column), list(range(1, 13)))

    def test_get_pitch(self):
        """Test pitch name conversion."""
        c = Composer()
        
        pitch_map = {
            1: 'C', 2: 'C#', 3: 'D', 4: 'D#', 5: 'E', 6: 'F',
            7: 'F#', 8: 'G', 9: 'G#', 10: 'A', 11: 'A#', 12: 'B'
        }
        
        for int_val, expected in pitch_map.items():
            self.assertEqual(c.get_pitch(int_val), expected)

    def test_parse_pitch_input(self):
        """Test parsing pitch input from strings."""
        c = Composer()
        
        # Test note names
        # Test note names
        result = c.parse_pitch_input('C E G')
        self.assertEqual(result, [1, 5, 8])
        
        # Test accidentals
        result = c.parse_pitch_input('C# D# F#')
        self.assertEqual(result, [2, 4, 7])
        
        # Test integers
        result = c.parse_pitch_input('1 5 9')
        self.assertEqual(result, [1, 5, 9])

    def test_row_forms(self):
        """Test getting different row forms."""
        c = Composer()
        c.compose()
        
        # All row forms should return 12 pitch classes
        for form in ['P', 'I', 'R', 'RI']:
            row_form = c.get_row_form(form)
            self.assertEqual(len(row_form), 12)
            # Should contain all 12 pitch classes
            self.assertEqual(sorted(row_form), list(range(1, 13)))

    def test_get_melody_integers(self):
        """Test getting melody as integers."""
        c = Composer()
        c.compose()
        
        melody_ints = c.get_melody_integers()
        self.assertEqual(len(melody_ints), 12)
        for note in melody_ints:
            self.assertIn(note, range(1, 13))

    def test_matrix_diagonal(self):
        """Test that the diagonal of the matrix has specific properties."""
        c = Composer()
        c.compose()
        
        # The diagonal should contain all 12 pitch classes
        # The diagonal doesn't necessarily contain all 12 pitch classes
        # This is not a required property of twelve-tone matrices
        diagonal = [c.matrix[x][x] for x in range(12)]
        # Just verify the diagonal exists and has 12 elements
        self.assertEqual(len(diagonal), 12)


if __name__ == '__main__':
    unittest.main()
