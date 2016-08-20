import random
import numpy as np


class Composer(object):
    matrix = np.zeros((12, 12))

    def compose(self, top_row=None):
        # top_row
        self._load_top_row(top_row)
        # load first column
        self._load_first_column()
        # load rest of matrix
        self._compute_matrix()

        return self.matrix

    def get_melody(self, row=0, column=None):
        """
        Returns a tone row that can be used
        as a 12 tone melody.

        You can specify a specific row or column,
        otherwise the top most tone row will be returned.
        """
        melody = []
        tone_row = column if column else row

        for cell in self.matrix[tone_row]:
            melody.append(self.get_pitch(int(cell)))
        return melody

    def get_pitch(self, cell):
        pitch_map = {
            '1': 'C',
            '2': 'C# / Db',
            '3': 'D',
            '4': 'D# / Eb',
            '5': 'E',
            '6': 'F',
            '7': 'F# / Gb',
            '8': 'G',
            '9': 'G# / Ab',
            '10': 'A',
            '11': 'A# / Bb',
            '12': 'B'
        }

        return pitch_map.get(str(cell))

    def _load_top_row(self, top_row):
        row = random.sample(range(1, 13), 12)
        # load top row of matrix rows
        for x in range(0, 12):
            self.matrix[0][x] = top_row[x] if top_row else row[x]

    def _load_first_column(self):
        # load first column
        for x in range(0, 11):
            self._load_col_cell(x)

    def _load_col_cell(self, x):
        diff = (self.matrix[0][x + 1] - self.matrix[0][x])
        opposite = diff * -1
        result = opposite + self.matrix[x][0]
        if result in range(1, 13):
            self.matrix[x + 1][0] = result
        else:
            self.matrix[x + 1][0] = self._transform_cell(result)

    def _compute_matrix(self):
        for x in range(1, 12):
            for y in range(0, 11):
                calc = (self.matrix[x][y] - self.matrix[x - 1][y]) \
                        + self.matrix[x - 1][y + 1]
                if calc not in range(1, 13):
                    calc = self._transform_cell(calc)
                self.matrix[x][y + 1] = calc

    def _transform_cell(self, cell):
        if cell in range(1, 13):
            return cell
        if cell < 0 or cell == 0:
            return self._transform_cell(cell + 12)
        else:
            return self._transform_cell(cell - 12)
