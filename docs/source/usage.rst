Usage Guide
===========

This guide provides examples of how to use the KEGG Data Fetcher package for various tasks.

Basic Usage
----------

Fetching Reaction Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To fetch information about a specific reaction:

.. code-block:: python

   from kegg.fetch_reaction import get_reaction_info

   # Fetch information for reaction R00200
   reaction_df = get_reaction_info("R00200")
   print(reaction_df)

The returned DataFrame contains the following columns:

* reaction_id: The KEGG reaction ID
* name: The reaction name
* definition: The reaction definition
* equation: The reaction equation
* reactants: List of reactants with stoichiometric coefficients
* products: List of products with stoichiometric coefficients
* is_reversible: Boolean indicating if the reaction is reversible
* enzyme: Associated enzyme(s)
* pathways: Associated metabolic pathways
* modules: Associated KEGG modules
* orthology: Associated KEGG orthology
* dblinks: Database links

Fetching Compound Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To fetch information about a specific compound:

.. code-block:: python

   from kegg.fetch_compound import get_compound_info

   # Fetch information for compound C00031
   compound_df = get_compound_info("C00031")
   print(compound_df)

The returned DataFrame contains the following columns:

* compound_id: The KEGG compound ID
* name: The compound name
* formula: The chemical formula
* exact_mass: The exact molecular mass
* molecular_weight: The molecular weight
* reactions: Associated reactions
* enzymes: Associated enzymes
* pathways: Associated metabolic pathways
* modules: Associated KEGG modules
* dblinks: Database links

Advanced Usage
-------------

Parsing Reaction Equations
~~~~~~~~~~~~~~~~~~~~~~~~

The package automatically parses reaction equations into structured data:

.. code-block:: python

   from kegg.fetch_reaction import get_reaction_info

   # Fetch reaction information
   reaction_df = get_reaction_info("R00200")
   
   # Access parsed reactants and products
   reactants = reaction_df['reactants'].iloc[0]
   products = reaction_df['products'].iloc[0]
   
   print("Reactants:")
   for reactant in reactants:
       print(f"{reactant['coefficient']} {reactant['compound']}")
   
   print("\nProducts:")
   for product in products:
       print(f"{product['coefficient']} {product['compound']}")

Saving Data to CSV
~~~~~~~~~~~~~~~~

You can easily save the fetched data to CSV files:

.. code-block:: python

   from kegg.fetch_reaction import get_reaction_info
   from kegg.fetch_compound import get_compound_info

   # Fetch and save reaction data
   reaction_df = get_reaction_info("R00200")
   reaction_df.to_csv("reaction_data.csv", index=False)

   # Fetch and save compound data
   compound_df = get_compound_info("C00031")
   compound_df.to_csv("compound_data.csv", index=False)

Error Handling
-------------

The package includes proper error handling for invalid IDs and API issues:

.. code-block:: python

   from kegg.fetch_reaction import get_reaction_info
   from kegg.fetch_compound import get_compound_info

   try:
       # This will raise an exception
       reaction_df = get_reaction_info("INVALID_ID")
   except Exception as e:
       print(f"Error fetching reaction: {e}")

   try:
       # This will raise an exception
       compound_df = get_compound_info("INVALID_ID")
   except Exception as e:
       print(f"Error fetching compound: {e}")

Configuration
------------

You can customize the package behavior by modifying the `config.yaml` file. See the :doc:`configuration` section for more details about available options. 