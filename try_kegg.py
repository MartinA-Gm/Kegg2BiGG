from kegg.fetch_reaction import get_reaction_info
from kegg.fetch_compound import get_compound_info
import pandas as pd

def print_reaction_details(df):
    """Print formatted reaction details."""
    print("\nReaction Details:")
    print(f"ID: {df['reaction_id'].iloc[0]}")
    print(f"Name: {df['name'].iloc[0]}")
    print(f"Definition: {df['definition'].iloc[0]}")
    print(f"Equation: {df['equation'].iloc[0]}")
    print(f"Enzyme: {df['enzyme'].iloc[0]}")
    print(f"Pathways: {df['pathways'].iloc[0]}")
    print("-" * 80)

def print_compound_details(df):
    """Print formatted compound details."""
    print("\nCompound Details:")
    print(f"ID: {df['compound_id'].iloc[0]}")
    print(f"Name: {df['name'].iloc[0]}")
    print(f"Formula: {df['formula'].iloc[0]}")
    print(f"Exact Mass: {df['exact_mass'].iloc[0]}")
    print(f"Molecular Weight: {df['molecular_weight'].iloc[0]}")
    print(f"Pathways: {df['pathways'].iloc[0]}")
    print("-" * 80)

def main():
    # Example 1: Glycolysis reactions
    glycolysis_reactions = [
        "R00200",  # Glucose-6-phosphate isomerase
        "R00259",  # Phosphofructokinase
        "R00756",  # Pyruvate kinase
    ]
    
    print("\n=== Testing Glycolysis Reactions ===")
    for rxn_id in glycolysis_reactions:
        reaction_data = get_reaction_info(rxn_id)
        print_reaction_details(reaction_data)
        # Save to CSV
        reaction_data.to_csv(f"data/csv/reaction_{rxn_id}.csv", index=False)
    
    # Example 2: Important compounds
    important_compounds = [
        "C00031",  # D-Glucose
        "C00033",  # Acetate
        "C00042",  # Succinate
    ]
    
    print("\n=== Testing Important Compounds ===")
    for comp_id in important_compounds:
        compound_data = get_compound_info(comp_id)
        print_compound_details(compound_data)
        # Save to CSV
        compound_data.to_csv(f"data/csv/compound_{comp_id}.csv", index=False)
    
    print("\nAll data has been saved to data/csv/")

if __name__ == "__main__":
    main() 