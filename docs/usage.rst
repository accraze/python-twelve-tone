=====
Usage
=====

To use Twelve Tone in a project::

	import twelve_tone

You can quickly generate a random twelve-tone melody with the CLI

::

    $ twelve-tone
    ['C# / Db', 'A# / Bb', 'F', 'D', 'G# / Ab', 'D# / Eb', 'F# / Gb',
        'A', 'C', 'G', 'B', 'E']

Or you can use the following methods in a script:

::

    >>> from twelve_tone.composer import Composer
    >>> c = Composer()
    >>> c.compose()
    >>> c.get_melody()
    ['C# / Db', 'A# / Bb', 'F', 'D', 'G# / Ab', 'D# / Eb', 'F# / Gb',
        'A', 'C', 'G', 'B', 'E']

After you have composed a matrix of tone rows, you can save the composition to
MIDI:

::

    >>> c.compose()
    >>> c.save_to_midi(filename='TWELVE_TONE.mid')

