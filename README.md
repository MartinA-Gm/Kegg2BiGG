# Kegg2BiGG

A Python tool for converting KEGG reaction IDs to BiGG model format. This tool helps bridge the gap between KEGG and BiGG databases, making it easier to work with metabolic models across different databases.

## Features

- Fetches reaction information from KEGG database
- Converts KEGG reaction IDs to BiGG format
- Easy-to-use Python interface

## Prerequisites

- Python 3.9 or higher
- Conda package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Kegg2BiGG.git
cd Kegg2BiGG
```

2. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate kegg2bigg
```

## Usage

The main script `Kegg2Bigg.py` can be used to fetch reaction information from KEGG. Here's a basic example:

```python
from Kegg2Bigg import get_reaction_info

# Get information for a specific KEGG reaction ID
reaction_id = "R00200"
reaction_info = get_reaction_info(reaction_id)
```

## Project Structure

- `Kegg2Bigg.py`: Main script for KEGG to BiGG conversion
- `environment.yml`: Conda environment configuration
- `README.md`: This documentation file

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- KEGG database for providing reaction information
- BiGG database for metabolic model standards 