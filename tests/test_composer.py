import unittest

from twelve_tone.composer import Composer


class TestMatrix(unittest.TestCase):

    def test_get_tone_row(self):
        m = Composer()
        m.compose()
        row = m._get_tone_row(1, None)
        self.assertEquals(list(row), list(m.matrix[1]))
        col = m._get_tone_row(0, 1)
        self.assertEquals(list(col), list(m.matrix[:, 1]))

    def test_top_row(self):
        m = Composer().compose()
        # check top row is unique
        duplicate_val = False
        if len(m[0]) > len(set(m[0])):
            duplicate_val = True
        self.assertFalse(duplicate_val)
        self.assertEquals(len(m[0]), 12)

    def test_transform_cell(self):
        negative = -3
        transformed_num = Composer()._transform_cell(negative)
        self.assertEqual(transformed_num, 9)

    def test_translate_pitch(self):
        cell = 3
        pitch = Composer().get_pitch(cell)
        self.assertEqual(pitch, 'D')

    def test_master(self):
        row = [3, 1, 9, 5, 4, 6, 8, 7, 12, 10, 11, 2]
        m = Composer().compose(top_row=row)
        self.assertEqual(m[0][0], 3)
        self.assertEqual(m[11][0], 4)
        self.assertEqual(m[0][11], 2)
        self.assertEqual(m[11][11], 3)
        # check for 3s all the way diagonal
        for x in range(0, 12):
            self.assertEqual(m[x][x], 3)
