"""Module for fetching compound information from KEGG."""

import logging
from typing import Dict, List, Optional, Union
import pandas as pd
import requests
from utils.config import load_config

# Set up logging
logger = logging.getLogger(__name__)

def get_compound_info(compound_id: Optional[str] = None) -> pd.DataFrame:
    """Fetch compound information from KEGG.
    
    Args:
        compound_id: KEGG compound ID (e.g., 'C00031'). If None, uses the default ID from config.
        
    Returns:
        DataFrame containing compound information.
        
    Raises:
        ValueError: If the compound ID is invalid.
        requests.RequestException: If there's an error fetching data from KEGG.
    """
    config = load_config()
    
    if compound_id is None:
        compound_id = config['compound']['default_id']
    
    # Validate compound ID format
    if not compound_id.startswith('C'):
        raise ValueError(f"Invalid compound ID format: {compound_id}. Must start with 'C'.")
    
    # Construct API URL
    base_url = config['kegg']['base_url']
    url = f"{base_url}/get/cpd:{compound_id}"
    
    try:
        response = requests.get(url, timeout=config['kegg']['timeout'])
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error fetching compound {compound_id}: {e}")
        raise
    
    # Parse response
    data = parse_kegg_response(response.text)
    
    # Create DataFrame
    df = pd.DataFrame([data])
    
    # Select fields based on configuration
    fields = config['compound']['fields']
    df = df[fields]
    
    return df

def parse_kegg_response(response_text: str) -> Dict[str, Union[str, List[str]]]:
    """Parse KEGG API response into structured data.
    
    Args:
        response_text: Raw response text from KEGG API.
        
    Returns:
        Dictionary containing parsed compound information.
    """
    data = {
        'compound_id': '',
        'name': '',
        'formula': '',
        'exact_mass': '',
        'molecular_weight': '',
        'reactions': '',
        'enzymes': '',
        'pathways': '',
        'modules': '',
        'dblinks': ''
    }
    
    current_section = None
    for line in response_text.split('\n'):
        if not line.strip():
            continue
            
        if line.startswith(' '):
            # Continuation of previous section
            if current_section == 'NAME':
                data['name'] += ' ' + line.strip()
            elif current_section == 'FORMULA':
                data['formula'] += ' ' + line.strip()
            elif current_section == 'EXACT_MASS':
                data['exact_mass'] += ' ' + line.strip()
            elif current_section == 'MOL_WEIGHT':
                data['molecular_weight'] += ' ' + line.strip()
            elif current_section == 'REACTION':
                data['reactions'] += ' ' + line.strip()
            elif current_section == 'ENZYME':
                data['enzymes'] += ' ' + line.strip()
            elif current_section == 'PATHWAY':
                data['pathways'] += ' ' + line.strip()
            elif current_section == 'MODULE':
                data['modules'] += ' ' + line.strip()
            elif current_section == 'DBLINKS':
                data['dblinks'] += ' ' + line.strip()
        else:
            # New section
            if ' ' in line:
                section, content = line.split(' ', 1)
                current_section = section
                
                if section == 'ENTRY':
                    data['compound_id'] = content.split()[0]
                elif section == 'NAME':
                    data['name'] = content.strip()
                elif section == 'FORMULA':
                    data['formula'] = content.strip()
                elif section == 'EXACT_MASS':
                    data['exact_mass'] = content.strip()
                elif section == 'MOL_WEIGHT':
                    data['molecular_weight'] = content.strip()
                elif section == 'REACTION':
                    data['reactions'] = content.strip()
                elif section == 'ENZYME':
                    data['enzymes'] = content.strip()
                elif section == 'PATHWAY':
                    data['pathways'] = content.strip()
                elif section == 'MODULE':
                    data['modules'] = content.strip()
                elif section == 'DBLINKS':
                    data['dblinks'] = content.strip()
    
    return data

# Example usage
if __name__ == "__main__":
    # Create data directory if it doesn't exist
    config = load_config()
    os.makedirs(config['output']['data_dir'], exist_ok=True)
    
    compound_id = config['compound']['default_id']
    try:
        df = get_compound_info(compound_id)
        print("\nCompound Information DataFrame:")
        print(df)
        
        # Save to CSV in data directory
        output_file = os.path.join(
            config['output']['data_dir'],
            f"kegg_compound_{compound_id}.{config['output']['file_format']}"
        )
        df.to_csv(output_file, index=config['output']['index'])
        print(f"\nData saved to {output_file}")
        logger.info(f"Successfully saved compound data for {compound_id}")
    except Exception as e:
        error_msg = f"Error processing compound {compound_id}: {str(e)}"
        print(error_msg)
        logger.error(error_msg) 