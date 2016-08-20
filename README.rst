========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |coveralls| |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

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

.. |downloads| image:: https://img.shields.io/pypi/dm/twelve-tone.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/twelve-tone

.. |wheel| image:: https://img.shields.io/pypi/wheel/twelve-tone.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/twelve-tone

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/twelve-tone.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/twelve-tone

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/twelve-tone.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/twelve-tone


.. end-badges

Twelve-tone matrix to generate dodecaphonic melodies.

Following a process created by the composer Arnold Schoenberg, this library
computes a matrix to create twelve-tone serialism melodies which compose each
of the 12 semitones of the chromatic scale with equal importance.


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
