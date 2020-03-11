========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis|
        | |codeclimate|
    * - package
      - | |commits-since|

.. |travis| image:: https://travis-ci.com/csci-e-29/2020sp-csci-utils-nawab.svg?token=C7QfynRr4iayskJBhGpp&branch=master
    :target: https://travis-ci.com/csci-e-29/2020sp-csci-utils-nawab

.. |codeclimate| image:: https://api.codeclimate.com/v1/badges/feba4c5a512835d74e98/maintainability
   :target: https://codeclimate.com/github/doctorsmonsters/2020sp-csci-utils-doctorsmonsters/maintainability
   :alt: Maintainability


.. |commits-since| image:: https://img.shields.io/github/commits-since/csci-e-29/2020sp-csci-utils-nawab/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/csci-e-29/2020sp-csci-utils-nawab/compare/v0.0.0...master



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
