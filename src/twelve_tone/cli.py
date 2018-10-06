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
@click.option('--midi', '-m', help='MIDI output file')
def main(midi):
    c = Composer()
    c.compose()
    click.echo(c.get_melody())
    if midi is not None:
        c.save_to_midi(filename=midi)
