"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mtwelve_tone` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``twelve_tone.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``twelve_tone.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click

from twelve_tone.composer import Composer


@click.command()
@click.option('--row', '-r', default=0, help='Row to use as row tone')
@click.option('--column', '-c', default=0, help='Column to use as column tone')
@click.option('--midi', '-m', help='MIDI output file')
def main(row, column, midi):
    c = Composer()
    c.compose()
    if row < 0 or column < 0:
        click.echo("Invalid row or column arguments.")
        exit(1)
    elif row >= c.matrix.shape[0]:
        click.echo("Row number exceeds melody row count.")
        exit(1)
    elif column >= c.matrix.shape[1]:
        click.echo("Column number exceeds melody column count.")
        exit(1)
    click.echo(c.get_melody(row=row, column=column))
    if midi is not None:
        c.save_to_midi(filename=midi)
