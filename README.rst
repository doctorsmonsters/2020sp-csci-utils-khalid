========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis|
        |
        | |codeclimate|
    * - package
      - | |commits-since|

.. |travis| image:: https://api.travis-ci.org/doctorsmonsters/2020sp-csci-utils-doctorsmonsters.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/doctorsmonsters/2020sp-csci-utils-doctorsmonsters

.. |codeclimate| image:: https://codeclimate.com/github/doctorsmonsters/2020sp-csci-utils-doctorsmonsters/badges/gpa.svg
   :target: https://codeclimate.com/github/doctorsmonsters/2020sp-csci-utils-doctorsmonsters
   :alt: CodeClimate Quality Status

.. |commits-since| image:: https://img.shields.io/github/commits-since/doctorsmonsters/2020sp-csci-utils-doctorsmonsters/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/doctorsmonsters/2020sp-csci-utils-doctorsmonsters/compare/v0.0.0...master



.. end-badges

An example package. Generated with cookiecutter-pylibrary.

Installation
============

::

    pip install csci-utils

You can also install the in-development version with::

    pip install https://github.com/doctorsmonsters/2020sp-csci-utils-doctorsmonsters/archive/master.zip


Documentation
=============


To use the project:

.. code-block:: python

    import csci_utils
    csci_utils.longest()


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
