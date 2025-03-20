"""Module for fetching reaction information from KEGG."""

import logging
from typing import Dict, List, Optional, Union
import pandas as pd
import requests
from utils.config import load_config

# Set up logging
logger = logging.getLogger(__name__)

def get_reaction_info(reaction_id: Optional[str] = None) -> pd.DataFrame:
    """Fetch reaction information from KEGG.
    
    Args:
        reaction_id: KEGG reaction ID (e.g., 'R00200'). If None, uses the default ID from config.
        
    Returns:
        DataFrame containing reaction information.
        
    Raises:
        ValueError: If the reaction ID is invalid.
        requests.RequestException: If there's an error fetching data from KEGG.
    """
    config = load_config()
    
    if reaction_id is None:
        reaction_id = config['reaction']['default_id']
    
    # Validate reaction ID format
    if not reaction_id.startswith('R'):
        raise ValueError(f"Invalid reaction ID format: {reaction_id}. Must start with 'R'.")
    
    # Construct API URL
    base_url = config['kegg']['base_url']
    url = f"{base_url}/get/rn:{reaction_id}"
    
    try:
        response = requests.get(url, timeout=config['kegg']['timeout'])
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error fetching reaction {reaction_id}: {e}")
        raise
    
    # Parse response
    data = parse_kegg_response(response.text)
    
    # Create DataFrame
    df = pd.DataFrame([data])
    
    # Select fields based on configuration
    fields = config['reaction']['fields']
    df = df[fields]
    
    return df

def parse_kegg_response(response_text: str) -> Dict[str, Union[str, List[Dict[str, str]], bool]]:
    """Parse KEGG API response into structured data.
    
    Args:
        response_text: Raw response text from KEGG API.
        
    Returns:
        Dictionary containing parsed reaction information.
    """
    data = {
        'reaction_id': '',
        'name': '',
        'definition': '',
        'equation': '',
        'reactants': [],
        'products': [],
        'is_reversible': False,
        'enzyme': '',
        'pathways': '',
        'modules': '',
        'orthology': '',
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
            elif current_section == 'DEFINITION':
                data['definition'] += ' ' + line.strip()
            elif current_section == 'EQUATION':
                data['equation'] += ' ' + line.strip()
            elif current_section == 'ENZYME':
                data['enzyme'] += ' ' + line.strip()
            elif current_section == 'PATHWAY':
                data['pathways'] += ' ' + line.strip()
            elif current_section == 'MODULE':
                data['modules'] += ' ' + line.strip()
            elif current_section == 'ORTHOLOGY':
                data['orthology'] += ' ' + line.strip()
            elif current_section == 'DBLINKS':
                data['dblinks'] += ' ' + line.strip()
        else:
            # New section
            if ' ' in line:
                section, content = line.split(' ', 1)
                current_section = section
                
                if section == 'ENTRY':
                    data['reaction_id'] = content.split()[0]
                elif section == 'NAME':
                    data['name'] = content.strip()
                elif section == 'DEFINITION':
                    data['definition'] = content.strip()
                elif section == 'EQUATION':
                    data['equation'] = content.strip()
                    # Parse equation into reactants and products
                    reactants, products = parse_equation(content.strip())
                    data['reactants'] = reactants
                    data['products'] = products
                    data['is_reversible'] = '<=>' in content
                elif section == 'ENZYME':
                    data['enzyme'] = content.strip()
                elif section == 'PATHWAY':
                    data['pathways'] = content.strip()
                elif section == 'MODULE':
                    data['modules'] = content.strip()
                elif section == 'ORTHOLOGY':
                    data['orthology'] = content.strip()
                elif section == 'DBLINKS':
                    data['dblinks'] = content.strip()
    
    return data

def parse_equation(equation: str) -> tuple[List[Dict[str, str]], List[Dict[str, str]]]:
    """Parse reaction equation into reactants and products.
    
    Args:
        equation: Reaction equation string.
        
    Returns:
        Tuple of (reactants, products) where each is a list of dictionaries
        containing 'coefficient' and 'compound' keys.
    """
    # Split equation into reactants and products
    if '<=>' in equation:
        reactants_str, products_str = equation.split('<=>')
    elif '=>' in equation:
        reactants_str, products_str = equation.split('=>')
    else:
        raise ValueError(f"Invalid equation format: {equation}")
    
    # Parse reactants and products
    reactants = parse_compounds(reactants_str.strip())
    products = parse_compounds(products_str.strip())
    
    return reactants, products

def parse_compounds(compounds_str: str) -> List[Dict[str, str]]:
    """Parse compound string into list of compounds with coefficients.
    
    Args:
        compounds_str: String containing compounds and coefficients.
        
    Returns:
        List of dictionaries containing 'coefficient' and 'compound' keys.
    """
    compounds = []
    for term in compounds_str.split(' + '):
        term = term.strip()
        if not term:
            continue
            
        # Split coefficient and compound
        parts = term.split(' ', 1)
        if len(parts) == 1:
            coefficient = '1'
            compound = parts[0]
        else:
            coefficient, compound = parts
            
        compounds.append({
            'coefficient': coefficient,
            'compound': compound
        })
    
    return compounds

# Example usage
if __name__ == "__main__":
    # Create data directory if it doesn't exist
    os.makedirs(config['output']['data_dir'], exist_ok=True)
    
    reaction_id = config['reaction']['default_id']
    try:
        df = get_reaction_info(reaction_id)
        print("\nReaction Information DataFrame:")
        print(df)
        
        # Save to CSV in data directory
        output_file = os.path.join(
            config['output']['data_dir'],
            f"kegg_reaction_{reaction_id}.{config['output']['file_format']}"
        )
        df.to_csv(output_file, index=config['output']['index'])
        print(f"\nData saved to {output_file}")
        logging.info(f"Successfully saved reaction data for {reaction_id}")
    except Exception as e:
        error_msg = f"Error processing reaction {reaction_id}: {str(e)}"
        print(error_msg)
        logging.error(error_msg) 