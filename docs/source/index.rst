Welcome to KEGG Data Fetcher's documentation!
==========================================

Overview
========

KEGG Data Fetcher is a Python package that provides a simple interface to fetch and parse data from the KEGG (Kyoto Encyclopedia of Genes and Genomes) database. The package focuses on retrieving reaction and compound information, making it easy to integrate KEGG data into your bioinformatics workflows.

Features
========

- Fetch reaction information from KEGG
- Fetch compound information from KEGG
- Parse reaction equations into structured data
- Export data to CSV format
- Configurable through YAML file
- Comprehensive error handling
- Detailed logging

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   configuration
   development
   changelog

Quick Start
==========

Installation:

.. code-block:: bash

   pip install kegg-data-fetcher

Basic usage:

.. code-block:: python

   from kegg.fetch_reaction import get_reaction_info
   from kegg.fetch_compound import get_compound_info

   # Fetch reaction information
   reaction_data = get_reaction_info('R00200')
   print(reaction_data)

   # Fetch compound information
   compound_data = get_compound_info('C00031')
   print(compound_data)

Indices and tables
================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search` 