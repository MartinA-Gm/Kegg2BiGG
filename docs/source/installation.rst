Installation
============

KEGG Data Fetcher can be installed using pip. The package requires Python 3.8 or higher.

Basic Installation
-----------------

To install the latest stable version:

.. code-block:: bash

   pip install kegg-data-fetcher

Development Installation
-----------------------

To install the package in development mode with all development dependencies:

.. code-block:: bash

   git clone https://github.com/yourusername/kegg-data-fetcher.git
   cd kegg-data-fetcher
   pip install -e ".[dev]"

Dependencies
-----------

The package has the following dependencies:

* pandas >= 2.0.0
* requests >= 2.25.0
* pyyaml >= 6.0.0

Development dependencies include:

* pytest >= 7.0.0 (for testing)
* black >= 22.0.0 (for code formatting)
* flake8 >= 4.0.0 (for linting)
* mypy >= 0.900 (for type checking)
* sphinx >= 7.0.0 (for documentation)

Configuration
------------

After installation, you can configure the package by creating a `config.yaml` file in your project directory. See the :doc:`configuration` section for more details.

Verifying Installation
--------------------

To verify that the package is installed correctly, you can run the following Python code:

.. code-block:: python

   from kegg.fetch_reaction import get_reaction_info
   from kegg.fetch_compound import get_compound_info

   # Test reaction fetching
   reaction_df = get_reaction_info("R00200")
   print("Reaction data:")
   print(reaction_df)

   # Test compound fetching
   compound_df = get_compound_info("C00031")
   print("\nCompound data:")
   print(compound_df)

If no errors occur and you see the data printed, the installation was successful. 