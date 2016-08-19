========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-twelve-tone/badge/?style=flat
    :target: https://readthedocs.org/projects/python-twelve-tone
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/accraze/python-twelve-tone.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/accraze/python-twelve-tone

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/accraze/python-twelve-tone?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/accraze/python-twelve-tone

.. |requires| image:: https://requires.io/github/accraze/python-twelve-tone/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/accraze/python-twelve-tone/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/accraze/python-twelve-tone/badge.svg?branch=master&service=github
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

A Twelve-Tone matrix to generate random meelodies

* Free software: BSD license

Installation
============

::

    pip install twelve-tone

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
