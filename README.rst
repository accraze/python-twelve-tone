========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |travis| |coveralls| |codecov|
    * - package
      - |version| |wheel| |supported-versions|

.. |docs| image:: https://readthedocs.org/projects/python-twelve-tone/badge/?style=flat
    :target: https://readthedocs.org/projects/python-twelve-tone
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/accraze/python-twelve-tone.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/accraze/python-twelve-tone

.. |coveralls| image:: https://coveralls.io/repos/accraze/python-twelve-tone/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://coveralls.io/r/accraze/python-twelve-tone

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

Installation
============

::

    pip install twelve-tone

Quick Start
===========

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
