"""
Twelve-tone matrix composer.

Generates twelve-tone matrices using the standard serial composition technique
developed by Arnold Schoenberg. The matrix contains all 48 possible row forms:
- Prime (P)
- Inversion (I)
- Retrograde (R)
- Retrograde-Inversion (RI)
"""
import random
from typing import List, Optional, Tuple


class Composer(object):
    """
    A twelve-tone matrix composer.
    
    The matrix is a 12x12 grid where:
    - Row 0 is the prime form (P)
    - Column 0 is the inversion form (I)
    - Row 11 reversed is the retrograde form (R)
    - Column 11 reversed is the retrograde-inversion form (RI)
    """
    
    PITCH_NAMES = {
        1: 'C', 2: 'C#', 3: 'D', 4: 'D#', 5: 'E', 6: 'F',
        7: 'F#', 8: 'G', 9: 'G#', 10: 'A', 11: 'A#', 12: 'B'
    }
    
    PITCH_TO_INT = {
        'C': 1, 'C#': 2, 'D': 3, 'D#': 4, 'E': 5, 'F': 6,
        'F#': 7, 'G': 8, 'G#': 9, 'A': 10, 'A#': 11, 'B': 12,
        'Db': 2, 'Eb': 4, 'Gb': 7, 'Ab': 9, 'Bb': 11
    }
    
    def __init__(self):
        self.matrix: List[List[int]] = []
        self._initialize_matrix()
    
    def _initialize_matrix(self) -> None:
        """Initialize an empty 12x12 matrix."""
        self.matrix = [[0] * 12 for _ in range(12)]
    
    def compose(self, top_row: Optional[List[int]] = None) -> List[List[int]]:
        """
        Compose a twelve-tone matrix.
        
        Args:
            top_row: Optional list of 12 integers (1-12) for the prime form.
                    If None, generates a random tone row.
        
        Returns:
            The completed 12x12 matrix.
        """
        self._initialize_matrix()
        self._load_top_row(top_row)
        self._load_first_column()
        self._compute_matrix()
        return self.matrix
    
    def _load_top_row(self, top_row: Optional[List[int]] = None) -> None:
        """Load the top row (prime form) of the matrix."""
        if top_row:
            row = top_row
        else:
            row = random.sample(range(1, 13), 12)
        
        for x in range(12):
            self.matrix[0][x] = row[x]
    
    def _load_first_column(self) -> None:
        """Load the first column (inversion form) of the matrix."""
        for x in range(11):
            self._load_col_cell(x)
    
    def _load_col_cell(self, x: int) -> None:
        """
        Calculate and load a cell in the first column.
        
        The first column represents the inversion of the prime form.
        """
        diff = self.matrix[0][x + 1] - self.matrix[0][x]
        opposite = diff * -1
        result = opposite + self.matrix[x][0]
        
        if result in range(1, 13):
            self.matrix[x + 1][0] = result
        else:
            self.matrix[x + 1][0] = self._transform_cell(result)
    
    def _compute_matrix(self) -> None:
        """Compute the remaining cells of the matrix."""
        for x in range(1, 12):
            for y in range(11):
                calc = (self.matrix[x][y] - self.matrix[x - 1][y]) + self.matrix[x - 1][y + 1]
                if calc not in range(1, 13):
                    calc = self._transform_cell(calc)
                self.matrix[x][y + 1] = calc
    
    def _transform_cell(self, cell: int) -> int:
        """
        Transform a cell value to be within the range 1-12.
        
        Uses modulo arithmetic to wrap values outside the valid range.
        """
        if cell in range(1, 13):
            return cell
        if cell < 0 or cell == 0:
            return self._transform_cell(cell + 12)
        else:
            return self._transform_cell(cell - 12)
    
    def get_melody(self, row: int = 0, column: Optional[int] = None) -> List[str]:
        """
        Get a melody as pitch names from a specific row or column.
        
        Args:
            row: Row index (0-11)
            column: Optional column index (0-11). If None, returns the row.
        
        Returns:
            List of pitch names (e.g., ['C', 'C#', 'D', ...])
        """
        tone_row = self._get_tone_row(row, column)
        return [self.get_pitch(int(cell)) for cell in tone_row]
    
    def get_melody_integers(self, row: int = 0, column: Optional[int] = None) -> List[int]:
        """
        Get a melody as integers from a specific row or column.
        
        Args:
            row: Row index (0-11)
            column: Optional column index (0-11). If None, returns the row.
        
        Returns:
            List of integers (1-12)
        """
        tone_row = self._get_tone_row(row, column)
        return [int(cell) for cell in tone_row]
    
    def _get_tone_row(self, row: int, column: Optional[int]) -> List[int]:
        """Get a tone row or column from the matrix."""
        if column is not None:
            return [self.matrix[i][column] for i in range(12)]
        return self.matrix[row]
    
    def get_row_form(self, form: str = 'P', row_num: int = 0) -> List[int]:
        """
        Get a specific row form.
        
        Args:
            form: Row form - 'P' (Prime), 'I' (Inversion), 'R' (Retrograde), 
                  'RI' (Retrograde-Inversion)
            row_num: Which row to use (0-11)
        
        Returns:
            List of integers representing the pitch classes
        """
        form = form.upper()
        
        if form == 'P':
            return self.matrix[row_num]
        elif form == 'I':
            return [self.matrix[i][0] for i in range(12)] if row_num == 0 else self.matrix[row_num]
        elif form == 'R':
            row = self.matrix[row_num]
            return list(reversed(row))
        elif form == 'RI':
            col = [self.matrix[i][row_num] for i in range(12)]
            return list(reversed(col))
        else:
            raise ValueError(f"Unknown row form: {form}. Use P, I, R, or RI.")
    
    def get_pitch(self, cell: int) -> str:
        """Convert an integer pitch class to a pitch name."""
        return self.PITCH_NAMES.get(cell, str(cell))
    
    def get_pitch_integer(self, pitch_name: str) -> int:
        """Convert a pitch name to an integer pitch class."""
        pitch_name = pitch_name.strip()
        if pitch_name in self.PITCH_TO_INT:
            return self.PITCH_TO_INT[pitch_name]
        try:
            return int(pitch_name)
        except ValueError:
            raise ValueError(f"Unknown pitch: {pitch_name}")
    
    def parse_pitch_input(self, pitch_str: str) -> List[int]:
        """
        Parse a pitch string input into a list of integers.
        
        Supports:
        - Note names: 'C', 'C#', 'Db', etc.
        - Integers: '1', '2', etc.
        - Space-separated: 'C E G'
        
        Args:
            pitch_str: String containing pitch notation
        
        Returns:
            List of integers (1-12)
        """
        pitches = pitch_str.strip().split()
        result = []
        
        for pitch in pitches:
            result.append(self.get_pitch_integer(pitch))
        
        return result
    
    def save_to_midi(self, tone_rows: int = 1, filename: str = 'example.mid') -> None:
        """
        Save the composition to a MIDI file.
        
        Args:
            tone_rows: Number of rows to include
            filename: Output filename
        """
        from .midi import MIDIFile
        m = MIDIFile(filename=filename)
        for index in range(min(tone_rows, 12)):
            row = self.matrix[index]
            m.create(row)
    
    def format_matrix_text(self, format: str = 'text') -> str:
        """
        Format the matrix for display.
        
        Args:
            format: Output format - 'text', 'integer', 'rich'
        
        Returns:
            Formatted string representation
        """
        if format == 'text':
            return self._format_text()
        elif format == 'integer':
            return self._format_integer()
        elif format == 'rich':
            return self._format_rich()
        else:
            raise ValueError(f"Unknown format: {format}")
    
    def _format_text(self) -> str:
        """Format as simple text with pitch names."""
        lines = []
        for row in self.matrix:
            pitches = [self.get_pitch(cell) for cell in row]
            lines.append(' '.join(f'{p:8}' for p in pitches))
        return '\n'.join(lines)
    
    def _format_integer(self) -> str:
        """Format as integers."""
        lines = []
        for row in self.matrix:
            lines.append(' '.join(f'{cell:2}' for cell in row))
        return '\n'.join(lines)
    
    def _format_rich(self) -> str:
        """Format using Rich library for pretty terminal output."""
        try:
            from rich.table import Table
            from rich.console import Console
            from io import StringIO
            
            table = Table(show_header=True, header_style="bold magenta")
            
            # Add column headers
            for i in range(12):
                table.add_column(f"{i}", justify="center")
            
            # Add rows
            for row_idx, row in enumerate(self.matrix):
                pitches = [self.get_pitch(cell) for cell in row]
                table.add_row(*pitches)
            
            # Render to string
            console = Console(file=StringIO(), force_terminal=True)
            console.print(table)
            return console.file.getvalue()
        except ImportError:
            # Fallback to text format if rich is not installed
            return self._format_text()
