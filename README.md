# KEGG Data Fetcher

A Python package for fetching and parsing reaction and compound information from the KEGG database.

## Features

* Fetch reaction information from KEGG
* Fetch compound information from KEGG
* Parse reaction equations into structured data
* Export data to CSV format
* Configurable through YAML file
* Comprehensive test suite

## Installation

### Basic Installation

To install the latest stable version:

```bash
pip install kegg-data-fetcher
```

### Development Installation

To install the package in development mode with all development dependencies:

```bash
git clone https://github.com/yourusername/kegg-data-fetcher.git
cd kegg-data-fetcher
pip install -e ".[dev]"
```

## Usage

### Basic Usage

```python
from kegg.fetch_reaction import get_reaction_info
from kegg.fetch_compound import get_compound_info

# Fetch reaction information
reaction_df = get_reaction_info("R00200")
print(reaction_df)

# Fetch compound information
compound_df = get_compound_info("C00031")
print(compound_df)
```

### Advanced Usage

```python
from kegg.fetch_reaction import get_reaction_info
from kegg.fetch_compound import get_compound_info

# Fetch and parse reaction data
reaction_df = get_reaction_info("R00200")
reactants = reaction_df['reactants'].iloc[0]
products = reaction_df['products'].iloc[0]

print("Reactants:")
for reactant in reactants:
    print(f"{reactant['coefficient']} {reactant['compound']}")

print("\nProducts:")
for product in products:
    print(f"{product['coefficient']} {product['compound']}")

# Save data to CSV
reaction_df.to_csv("reaction_data.csv", index=False)
compound_df.to_csv("compound_data.csv", index=False)
```

## Configuration

The package can be configured using a `config.yaml` file. See the [configuration documentation](docs/source/configuration.rst) for more details.

## Development

### Setting Up Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/kegg-data-fetcher.git
   cd kegg-data-fetcher
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black src/ tests/
```

### Linting

```bash
flake8 src/ tests/
```

### Type Checking

```bash
mypy src/
```

### Building Documentation

```bash
cd docs
make html
```

The documentation will be available in `docs/_build/html/`.

## Project Structure

```
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
```

## Contributing

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Run tests and ensure all checks pass:
   ```bash
   pytest
   black src/ tests/
   flake8 src/ tests/
   mypy src/
   ```
5. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
7. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 