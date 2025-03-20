import requests
import pandas as pd
from typing import Dict, List, Optional

def parse_kegg_compound(response_text: str) -> Dict:
    """Parse KEGG compound information into a structured dictionary."""
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

def get_compound_info(compound_id: str) -> pd.DataFrame:
    """
    Fetch and parse KEGG compound information for a given compound ID.
    
    Args:
        compound_id (str): KEGG compound ID (e.g., 'C00002')
        
    Returns:
        pd.DataFrame: DataFrame containing the compound information
    """
    url = f"https://rest.kegg.jp/get/{compound_id}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch compound information for {compound_id}")
    
    info = parse_kegg_compound(response.text)
    
    # Create a dictionary for the DataFrame
    df_dict = {
        'compound_id': compound_id,
        'name': info.get('NAME', ''),
        'formula': info.get('FORMULA', ''),
        'exact_mass': info.get('EXACT_MASS', ''),
        'molecular_weight': info.get('MOL_WEIGHT', '')
    }
    
    return pd.DataFrame([df_dict])

# Example usage
if __name__ == "__main__":
    compound_id = "C00002"  # ATP
    try:
        df = get_compound_info(compound_id)
        print("\nCompound Information DataFrame:")
        print(df)
        
        # Save to CSV
        df.to_csv(f"kegg_compound_{compound_id}.csv", index=False)
        print(f"\nData saved to kegg_compound_{compound_id}.csv")
    except Exception as e:
        print(f"Error: {e}")
