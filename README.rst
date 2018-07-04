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


.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Schoenberg_-_Piano_Piece_op.33a_tone_row.png/640px-Schoenberg_-_Piano_Piece_op.33a_tone_row.png

Following a process created by the composer Arnold Schoenberg, this library
computes a matrix to create twelve-tone serialism melodies which compose each
of the 12 semitones of the chromatic scale with equal importance.

* Save your compositions to MIDI
* Free software: BSD license

Installation
============

::

    pip install twelve-tone

Quick Start
===========

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

The new MIDI file will be created in your current working directory. If you do
not specify a `filename` for your file, it will default to `example.mid`.

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

            PYTEST_ADDOPTS=--cov-append tox
