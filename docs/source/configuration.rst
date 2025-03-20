Configuration
=============

The KEGG Data Fetcher package can be configured using a YAML file named `config.yaml`. This file should be placed in your project directory.

Configuration File Structure
-------------------------

Here's a complete example of the configuration file:

.. code-block:: yaml

   # KEGG API Configuration
   kegg:
     base_url: "https://rest.kegg.jp"  # KEGG API base URL
     timeout: 30                        # API request timeout in seconds

   # Output Configuration
   output:
     data_dir: "data"                  # Directory for output files
     file_format: "csv"                # Output file format
     index: false                      # Whether to include index in output

   # Reaction Configuration
   reaction:
     default_id: "R00200"             # Default reaction ID for examples
     fields:                          # Fields to include in reaction data
       - reaction_id
       - name
       - definition
       - equation
       - reactants
       - products
       - is_reversible
       - enzyme
       - pathways
       - modules
       - orthology
       - dblinks

   # Compound Configuration
   compound:
     default_id: "C00031"             # Default compound ID for examples
     fields:                          # Fields to include in compound data
       - compound_id
       - name
       - formula
       - exact_mass
       - molecular_weight
       - reactions
       - enzymes
       - pathways
       - modules
       - dblinks

   # Logging Configuration
   logging:
     level: "INFO"                    # Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
     format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Log message format
     file: "logs/kegg_fetch.log"      # Log file path

Configuration Options
------------------

KEGG API Configuration
~~~~~~~~~~~~~~~~~~~

* ``base_url``: The base URL for the KEGG API. Default is "https://rest.kegg.jp".
* ``timeout``: The timeout in seconds for API requests. Default is 30 seconds.

Output Configuration
~~~~~~~~~~~~~~~~~

* ``data_dir``: The directory where output files will be saved. Default is "data".
* ``file_format``: The format for output files. Currently supports "csv". Default is "csv".
* ``index``: Whether to include the DataFrame index in the output. Default is false.

Reaction Configuration
~~~~~~~~~~~~~~~~~~~

* ``default_id``: The default reaction ID to use in examples. Default is "R00200".
* ``fields``: List of fields to include in the reaction data. See the API documentation for available fields.

Compound Configuration
~~~~~~~~~~~~~~~~~~~

* ``default_id``: The default compound ID to use in examples. Default is "C00031".
* ``fields``: List of fields to include in the compound data. See the API documentation for available fields.

Logging Configuration
~~~~~~~~~~~~~~~~~~

* ``level``: The logging level to use. Options are:
  * DEBUG: Detailed information for debugging
  * INFO: General information about program execution
  * WARNING: Warning messages for potential issues
  * ERROR: Error messages for serious problems
  * CRITICAL: Critical errors that may prevent program execution
* ``format``: The format string for log messages. Default includes timestamp, logger name, level, and message.
* ``file``: The path to the log file. Default is "logs/kegg_fetch.log".

Using Configuration
-----------------

The configuration is automatically loaded when importing the package. You can also load it manually:

.. code-block:: python

   from kegg.utils.config import load_config, validate_config

   # Load configuration
   config = load_config("path/to/config.yaml")

   # Validate configuration
   validate_config(config)

The configuration is used throughout the package to customize its behavior. For example:

.. code-block:: python

   from kegg.fetch_reaction import get_reaction_info
   from kegg.fetch_compound import get_compound_info

   # These will use the configured default IDs
   reaction_df = get_reaction_info()  # Uses config['reaction']['default_id']
   compound_df = get_compound_info()  # Uses config['compound']['default_id'] 