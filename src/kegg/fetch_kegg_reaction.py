import requests
import pandas as pd
from typing import Dict, List, Optional, Tuple
import re

def parse_kegg_reaction(response_text: str) -> Dict:
    """Parse KEGG reaction information into a structured dictionary."""
    info = {}
    current_key = None
    
    for line in response_text.split('\n'):
        if not line.strip():
            continue
            
        if line.startswith(' '):
            # Continuation of previous key
            if current_key and current_key in info:
                if isinstance(info[current_key], list):
                    info[current_key].append(line.strip())
                else:
                    info[current_key] = [info[current_key], line.strip()]
        else:
            # New key
            if ' ' in line:
                key, value = line.split(' ', 1)
                info[key] = value.strip()
                current_key = key
            else:
                current_key = line.strip()
                info[current_key] = []
    
    return info

def parse_compounds(compound_str: str) -> List[Dict[str, str]]:
    """
    Parse a string of compounds into a list of dictionaries containing compound information.
    
    Args:
        compound_str (str): String containing compounds with stoichiometric coefficients
        
    Returns:
        List[Dict[str, str]]: List of dictionaries with 'coefficient' and 'compound' keys
    """
    if not compound_str:
        return []
    
    # Split by '+' and handle stoichiometric coefficients
    compounds = []
    for comp in compound_str.split('+'):
        comp = comp.strip()
        if not comp:
            continue
            
        # Match coefficient and compound name
        match = re.match(r'^(\d+)\s*(.+)$', comp)
        if match:
            coefficient, compound = match.groups()
            compounds.append({
                'coefficient': coefficient,
                'compound': compound.strip()
            })
        else:
            compounds.append({
                'coefficient': '1',
                'compound': comp.strip()
            })
    
    return compounds

def split_equation(equation: str) -> Tuple[List[Dict[str, str]], List[Dict[str, str]], bool]:
    """
    Split KEGG equation into reactants and products, and determine reversibility.
    
    Args:
        equation (str): KEGG equation string
        
    Returns:
        Tuple[List[Dict[str, str]], List[Dict[str, str]], bool]: (reactants, products, is_reversible)
    """
    if not equation:
        return [], [], False
    
    # Handle different types of arrows
    if '<=>' in equation:
        reactants_str, products_str = equation.split('<=>')
        is_reversible = True
    elif '=>' in equation:
        reactants_str, products_str = equation.split('=>')
        is_reversible = False
    else:
        return [], [], False
    
    # Parse reactants and products into lists of compounds
    reactants = parse_compounds(reactants_str.strip())
    products = parse_compounds(products_str.strip())
    
    return reactants, products, is_reversible

def get_reaction_info(reaction_id: str) -> pd.DataFrame:
    """
    Fetch and parse KEGG reaction information for a given reaction ID.
    
    Args:
        reaction_id (str): KEGG reaction ID (e.g., 'R00200')
        
    Returns:
        pd.DataFrame: DataFrame containing the reaction information
    """
    url = f"https://rest.kegg.jp/get/{reaction_id}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch reaction information for {reaction_id}")
    
    info = parse_kegg_reaction(response.text)
    
    # Split equation into reactants and products, and get reversibility
    equation = info.get('EQUATION', '')
    reactants, products, is_reversible = split_equation(equation)
    
    # Create a dictionary for the DataFrame
    df_dict = {
        'reaction_id': reaction_id,
        'name': info.get('NAME', ''),
        'definition': info.get('DEFINITION', ''),
        'equation': equation,
        'reactants': reactants,
        'products': products,
        'is_reversible': is_reversible,
        'enzyme': info.get('ENZYME', ''),
        'pathways': '; '.join(info.get('PATHWAY', [])),
        'modules': '; '.join(info.get('MODULE', [])),
        'orthology': '; '.join(info.get('ORTHOLOGY', [])),
        'dblinks': info.get('DBLINKS', '')
    }
    
    return pd.DataFrame([df_dict])

# Example usage
if __name__ == "__main__":
    reaction_id = "R00200"
    try:
        df = get_reaction_info(reaction_id)
        
        # Save to CSV
        df.to_csv(f"./data/kegg_reaction_{reaction_id}.csv", index=False)
        print(f"\nData saved to kegg_reaction_{reaction_id}.csv")
    except Exception as e:
        print(f"Error: {e}")

### multiple possibilities to be tested 
## Either ModelSeed, MetaNetX, or BiGG database

## In this script i will try to use ...


