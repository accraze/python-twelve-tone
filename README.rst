========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |travis| |codecov|
    * - package
      - |version| |wheel| |supported-versions|

.. |docs| image:: https://readthedocs.org/projects/python-twelve-tone/badge/?style=flat
   :target: https://readthedocs.org/projects/python-twelve-tone
   :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/accraze/python-twelve-tone.svg?branch=master
   :alt: Travis-CI Build Status
   :target: https://travis-ci.org/accraze/python-twelve-tone

.. |codecov| image:: https://codecov.io/github/accraze/python-twelve-tone/coverage.svg?branch=master
   :alt: Coverage Status
   :target: https://codecov.io/github/accraze/python-twelve-tone

.. |version| image:: https://img.shields.io/pypi/v/twelve-tone.svg?style=flat
   :alt: PyPI Package latest release
   :target: https://pypi.python.org/pypi/twelve-tone

.. |wheel| image:: https://img.shields.io/pypi/wheel/twelve-tone.svg?style=flat
   :alt: PyPI Wheel
   :target: https://pypi.python.org/pypi/twelve-tone

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/twelve-tone.svg?style=flat
   :alt: Supported versions
   :target: https://pypi.python.org/pypi/twelve-tone


.. end-badges

Twelve-tone matrix to generate dodecaphonic melodies.

Following a process created by the composer Arnold Schoenberg, this library
computes a matrix to create twelve-tone serialism melodies which compose each
of the 12 semitones of the chromatic scale with equal importance.

* Save your compositions to MIDI
* Free software: BSD license
* No numpy dependency - pure Python implementation
* Multiple output formats (text, integer, rich table, LilyPond)
* Support for all row forms (Prime, Inversion, Retrograde, Retrograde-Inversion)

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Schoenberg_-_Piano_Piece_op.33a_tone_row.png/640px-Schoenberg_-_Piano_Piece_op.33a_tone_row.png


Installation
============

::

    pip install twelve-tone

The `GuixRUs <https://git.sr.ht/~whereiseveryone/guixrus>`_ channel also provides ``twelve-tone``.


Quick Start
===========

Generate a random twelve-tone row::

    $ twelve-tone generate
    C F# D G# A# E F C# G D# A B

Generate with specific pitch classes::

    $ twelve-tone generate --pitch C E G
    C E G F# A D# G# D A# C# F

Output as integers (1-12)::

    $ twelve-tone generate --format integer
    1 7 3 9 11 5 6 2 8 4 10 12

Output the full matrix::

    $ twelve-tone generate --matrix
    $ twelve-tone generate --matrix --format rich

Save to MIDI::

    $ twelve-tone generate --midi my_composition.mid


Row Forms
=========

The library supports all four standard row forms used in twelve-tone composition:

**Prime (P)** - The original tone row::

    $ twelve-tone P
    C F# D G# A# E F C# G D# A B

**Inversion (I)** - Inverted intervals::

    $ twelve-tone I
    C F# D# A G D C# F A# G# E B

**Retrograde (R)** - Backwards prime form::

    $ twelve-tone R
    B A D# G C# F E A# G# D F# C

**Retrograde-Inversion (RI)** - Backwards inversion::

    $ twelve-tone RI
    B E G# A# F C# D G F# D# A C


Custom Pitch Input
==================

Specify your own tone row using pitch names or integers::

    $ twelve-tone generate --pitch C E G B D F
    C E G B D F A C# F# G# A# D#

Or using integers::

    $ twelve-tone generate --pitch 1 5 9 2 6 10 3 7 11 4 8 12
    C E G# C# F A D F# A# D# G B


Output Formats
==============

**Text format (default)**::

    $ twelve-tone generate
    C F# D G# A# E F C# G D# A B

**Integer notation**::

    $ twelve-tone generate --format integer
    1 7 3 9 11 5 6 2 8 4 10 12

**Rich table format**::

    $ twelve-tone generate --matrix --format rich

**LilyPond notation**::

    $ twelve-tone generate --lilypond
    c' fis' d' gis' ais' e' f' cis' g' d'' a' b'

Save LilyPond output to a file and compile::

    $ twelve-tone generate --lilypond > reihe.ly && lilypond reihe.ly


MIDI Export
===========

Save your composition to MIDI::

    $ twelve-tone generate --midi composition.mid
    Saved to MIDI: composition.mid

Or use the Python API::

    >>> from twelve_tone.composer import Composer
    >>> c = Composer()
    >>> c.compose()
    >>> c.save_to_midi(filename='TWELVE_TONE.mid')


Python API
==========

Basic usage::

    >>> from twelve_tone.composer import Composer
    >>> c = Composer()
    >>> c.compose()
    >>> c.get_melody()
    ['C', 'F#', 'D', 'G#', 'A#', 'E', 'F', 'C#', 'G', 'D#', 'A', 'B']

With custom pitch row::

    >>> c.compose(top_row=[1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10, 12])
    >>> c.get_melody()
    ['C', 'D', 'E', 'F', 'G', 'A', 'C#', 'D#', 'F#', 'G#', 'A#', 'B']

Get specific row or column::

    >>> c.get_melody(row=2)  # Get row 2
    >>> c.get_melody(column=5)  # Get column 5

Get row forms::

    >>> c.get_row_form('P')  # Prime
    >>> c.get_row_form('I')  # Inversion
    >>> c.get_row_form('R')  # Retrograde
    >>> c.get_row_form('RI')  # Retrograde-Inversion

Output formats::

    >>> c.format_matrix_text('text')  # Text format
    >>> c.format_matrix_text('integer')  # Integer format
    >>> c.format_matrix_text('rich')  # Rich table format


Documentation
=============

https://python-twelve-tone.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOTIONS=--cov-append tox


License
=======

Free software: BSD license


Credits
=======

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
