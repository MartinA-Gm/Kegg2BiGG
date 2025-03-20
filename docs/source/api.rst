API Reference
============

This section provides detailed information about the KEGG Data Fetcher API.

Reaction Module
==============

Documentation for the ``kegg.fetch_reaction`` module.

Compound Module
==============

Documentation for the ``kegg.fetch_compound`` module.

Configuration Module
==================

Documentation for the ``kegg.utils.config`` module.

Data Structures
==============

Reaction Information
~~~~~~~~~~~~~~~~~~~

The reaction information is returned as a pandas DataFrame with the following columns:

- ``reaction_id``: KEGG reaction identifier
- ``name``: Reaction name
- ``definition``: Reaction definition
- ``equation``: Reaction equation
- ``reactants``: List of reactant compounds
- ``products``: List of product compounds
- ``is_reversible``: Boolean indicating if reaction is reversible
- ``enzyme``: Associated enzyme information
- ``pathways``: Associated pathway information
- ``modules``: Associated module information
- ``orthology``: Associated orthology information
- ``dblinks``: Database cross-references

Compound Information
~~~~~~~~~~~~~~~~~~

The compound information is returned as a pandas DataFrame with the following columns:

- ``compound_id``: KEGG compound identifier
- ``name``: Compound name
- ``formula``: Chemical formula
- ``exact_mass``: Exact mass
- ``molecular_weight``: Molecular weight
- ``reactions``: Associated reaction information
- ``enzymes``: Associated enzyme information
- ``pathways``: Associated pathway information
- ``modules``: Associated module information
- ``dblinks``: Database cross-references

Configuration Structure
~~~~~~~~~~~~~~~~~~~~~

The configuration is loaded from a YAML file with the following structure:

.. code-block:: yaml

    kegg_api:
      base_url: "https://rest.kegg.jp"
      timeout: 30
      default_reaction_ids: ["R00001", "R00002"]
      default_compound_ids: ["C00001", "C00002"]

    output:
      csv_directory: "data/csv"
      json_directory: "data/json"

    logging:
      level: "INFO"
      format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
      file: "kegg_fetcher.log" 