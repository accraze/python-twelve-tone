"""
Command-line interface for twelve-tone composition.

Supports multiple output formats and row form selection using standard
music theory notation (P, I, R, RI).
"""
import click
import sys
from typing import Optional

from twelve_tone.composer import Composer


@click.group()
@click.version_option(version='0.5.0')
def main():
    """
    Twelve-tone matrix generator.
    
    Generate twelve-tone matrices and melodies using the serial composition
    technique developed by Arnold Schoenberg.
    
    Examples:
    
        # Generate a random twelve-tone row
        $ twelve-tone
        
        # Generate with specific starting pitch
        $ twelve-tone --pitch C E G
        
        # Get prime form (row 0)
        $ twelve-tone P
        
        # Get inversion form (row 0)
        $ twelve-tone I
        
        # Get retrograde form
        $ twelve-tone R
        
        # Get retrograde-inversion form
        $ twelve-tone RI
        
        # Output as integers
        $ twelve-tone --format integer
        
        # Output matrix with rich formatting
        $ twelve-tone --matrix --format rich
    """
    pass


@main.command()
@click.option('--pitch', '-p', default=None,
              help='Space-separated pitch classes (e.g., "C E G" or "1 5 9")')
@click.option('--row', '-r', default=0, type=int,
              help='Row index to use (0-11)')
@click.option('--column', '-c', default=None, type=int,
              help='Column index to use (0-11)')
@click.option('--format', '-f', 'output_format', default='text',
              type=click.Choice(['text', 'integer', 'rich']),
              help='Output format')
@click.option('--matrix', '-m', is_flag=True,
              help='Display full matrix instead of single row')
@click.option('--midi', '-M', default=None,
              help='Save to MIDI file')
@click.option('--lilypond', '-l', is_flag=True,
              help='Output as LilyPond notation')
def generate(pitch: Optional[str], row: int, column: Optional[int],
             output_format: str, matrix: bool, midi: Optional[str],
             lilypond: bool):
    """
    Generate a twelve-tone matrix and output a row.
    
    By default, generates a random twelve-tone row and outputs it as text.
    Use --pitch to specify custom pitch classes.
    """
    c = Composer()
    
    # Parse pitch input if provided
    top_row = None
    if pitch:
        try:
            top_row = c.parse_pitch_input(pitch)
            if len(top_row) != 12:
                click.echo("Error: Pitch input must contain exactly 12 pitch classes.", err=True)
                sys.exit(1)
        except ValueError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)
    
    # Compose the matrix
    c.compose(top_row=top_row)
    
    # Output full matrix if requested
    if matrix:
        click.echo(c.format_matrix_text(output_format))
    else:
        # Output single row
        if lilypond:
            # LilyPond output
            melody = c.get_melody(row=row, column=column)
            lilypond_notes = []
            for note in melody:
                # Convert pitch name to lilypond format
                note_map = {
                    'C': "c'", 'C#': "cis'", 'D': "d'", 'D#': "dis'",
                    'E': "e'", 'F': "f'", 'F#': "fis'", 'G': "g'",
                    'G#': "gis'", 'A': "a'", 'A#': "ais'", 'B': "b'"
                }
                lilypond_notes.append(note_map.get(note, note.lower()))
            click.echo(' '.join(lilypond_notes))
        elif output_format == 'integer':
            melody = c.get_melody_integers(row=row, column=column)
            click.echo(' '.join(str(n) for n in melody))
        else:
            melody = c.get_melody(row=row, column=column)
            click.echo(' '.join(melody))
    
    # Save to MIDI if requested
    if midi:
        c.save_to_midi(tone_rows=1, filename=midi)
        click.echo(f"Saved to MIDI: {midi}", err=True)


# Add subcommands for row forms
@main.command()
@click.option('--pitch', '-p', default=None,
              help='Space-separated pitch classes (e.g., "C E G" or "1 5 9")')
@click.option('--row', '-r', default=0, type=int,
              help='Row index to use (0-11)')
@click.option('--format', '-f', 'output_format', default='text',
              type=click.Choice(['text', 'integer', 'rich']),
              help='Output format')
def p(pitch: Optional[str], row: int, output_format: str):
    """Prime form - the original tone row."""
    _output_row_form('P', pitch, row, output_format)


@main.command()
@click.option('--pitch', '-p', default=None,
              help='Space-separated pitch classes (e.g., "C E G" or "1 5 9")')
@click.option('--row', '-r', default=0, type=int,
              help='Row index to use (0-11)')
@click.option('--format', '-f', 'output_format', default='text',
              type=click.Choice(['text', 'integer', 'rich']),
              help='Output format')
def i(pitch: Optional[str], row: int, output_format: str):
    """Inversion form - inverted intervals."""
    _output_row_form('I', pitch, row, output_format)


@main.command()
@click.option('--pitch', '-p', default=None,
              help='Space-separated pitch classes (e.g., "C E G" or "1 5 9")')
@click.option('--row', '-r', default=0, type=int,
              help='Row index to use (0-11)')
@click.option('--format', '-f', 'output_format', default='text',
              type=click.Choice(['text', 'integer', 'rich']),
              help='Output format')
def r(pitch: Optional[str], row: int, output_format: str):
    """Retrograde form - backwards prime form."""
    _output_row_form('R', pitch, row, output_format)


@main.command()
@click.option('--pitch', '-p', default=None,
              help='Space-separated pitch classes (e.g., "C E G" or "1 5 9")')
@click.option('--row', '-r', default=0, type=int,
              help='Row index to use (0-11)')
@click.option('--format', '-f', 'output_format', default='text',
              type=click.Choice(['text', 'integer', 'rich']),
              help='Output format')
def ri(pitch: Optional[str], row: int, output_format: str):
    """Retrograde-inversion form - backwards inversion."""
    _output_row_form('RI', pitch, row, output_format)


def _output_row_form(form: str, pitch: Optional[str], row: int, output_format: str):
    """Helper function to output a row form."""
    c = Composer()
    
    # Parse pitch input if provided
    top_row = None
    if pitch:
        try:
            top_row = c.parse_pitch_input(pitch)
            if len(top_row) != 12:
                click.echo("Error: Pitch input must contain exactly 12 pitch classes.", err=True)
                sys.exit(1)
        except ValueError as e:
            click.echo(f"Error: {e}", err=True)
            sys.exit(1)
    
    # Compose the matrix
    c.compose(top_row=top_row)
    
    # Get the row form
    melody_ints = c.get_row_form(form, row_num=row)
    
    # Format output
    if output_format == 'integer':
        click.echo(' '.join(str(n) for n in melody_ints))
    else:
        melody = [c.get_pitch(n) for n in melody_ints]
        click.echo(' '.join(melody))


# Maintain backward compatibility with old CLI
@main.command('compose', hidden=True)
@click.option('--row', '-r', default=0, type=int)
@click.option('--column', '-c', default=None, type=int)
@click.option('--midi', '-m', default=None)
def compose_old(row, column, midi):
    """Backward compatibility for old CLI interface."""
    c = Composer()
    c.compose()
    
    if row < 0 or (column is not None and column < 0):
        click.echo("Invalid row or column arguments.")
        sys.exit(1)
    elif row >= 12:
        click.echo("Row number exceeds matrix dimensions.")
        sys.exit(1)
    elif column is not None and column >= 12:
        click.echo("Column number exceeds matrix dimensions.")
        sys.exit(1)
    
    melody = c.get_melody(row=row, column=column)
    click.echo(melody)
    
    if midi is not None:
        c.save_to_midi(filename=midi)


if __name__ == '__main__':
    main()
