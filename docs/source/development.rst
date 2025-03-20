Development
===========

This guide will help you set up your development environment and contribute to the KEGG Data Fetcher project.

Setting Up Development Environment
--------------------------------

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/yourusername/kegg-data-fetcher.git
      cd kegg-data-fetcher

2. Create and activate a virtual environment:

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install development dependencies:

   .. code-block:: bash

      pip install -e ".[dev]"

Development Tools
--------------

The project uses several development tools to ensure code quality:

* **pytest**: For running tests
* **black**: For code formatting
* **flake8**: For code linting
* **mypy**: For type checking
* **sphinx**: For documentation generation

Running Tests
-----------

Run the test suite:

.. code-block:: bash

   pytest

Run tests with coverage report:

.. code-block:: bash

   pytest --cov=src tests/

Code Formatting
-------------

Format code using black:

.. code-block:: bash

   black src/ tests/

Linting
------

Run flake8 to check for code style issues:

.. code-block:: bash

   flake8 src/ tests/

Type Checking
-----------

Run mypy to check type hints:

.. code-block:: bash

   mypy src/

Documentation
-----------

Build the documentation:

.. code-block:: bash

   cd docs
   make html

The documentation will be available in ``docs/_build/html/``.

Project Structure
--------------

The project follows a standard Python package structure:

.. code-block::

   kegg-data-fetcher/
   ├── src/
   │   └── kegg/
   │       ├── __init__.py
   │       ├── fetch_reaction.py
   │       └── fetch_compound.py
   ├── tests/
   │   ├── __init__.py
   │   └── test_kegg_fetch.py
   ├── docs/
   │   ├── source/
   │   └── _build/
   ├── config.yaml
   ├── setup.py
   ├── requirements.txt
   └── README.md

Contributing
----------

1. Fork the repository
2. Create a feature branch:

   .. code-block:: bash

      git checkout -b feature/your-feature-name

3. Make your changes
4. Run tests and ensure all checks pass:

   .. code-block:: bash

      pytest
      black src/ tests/
      flake8 src/ tests/
      mypy src/

5. Commit your changes:

   .. code-block:: bash

      git commit -m "Add your feature"

6. Push to your fork:

   .. code-block:: bash

      git push origin feature/your-feature-name

7. Create a Pull Request

Code Style Guide
-------------

* Follow PEP 8 guidelines
* Use type hints for all function parameters and return values
* Write docstrings for all public functions and classes
* Keep functions focused and single-purpose
* Write meaningful variable and function names
* Add comments for complex logic
* Write tests for new features

Release Process
------------

1. Update version in ``setup.py``
2. Update changelog in ``docs/source/changelog.rst``
3. Create a release tag:

   .. code-block:: bash

      git tag -a vX.Y.Z -m "Release vX.Y.Z"
      git push origin vX.Y.Z

4. Build and upload to PyPI:

   .. code-block:: bash

      python -m build
      python -m twine upload dist/*

Getting Help
----------

* Open an issue on GitHub for bug reports or feature requests
* Join our community chat (if available)
* Check the documentation for common questions

License
------

This project is licensed under the MIT License - see the LICENSE file for details. 