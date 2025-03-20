import pytest
import pandas as pd
from kegg.fetch_reaction import get_reaction_info
from kegg.fetch_compound import get_compound_info

def test_get_reaction_info():
    """Test fetching reaction information."""
    # Test with a valid reaction ID
    df = get_reaction_info("R00200")
    assert isinstance(df, pd.DataFrame)
    assert "reaction_id" in df.columns
    assert "name" in df.columns
    assert "equation" in df.columns
    
    # Test with default reaction ID
    df_default = get_reaction_info()
    assert isinstance(df_default, pd.DataFrame)
    assert "reaction_id" in df_default.columns
    assert "name" in df_default.columns
    assert "equation" in df_default.columns

def test_get_compound_info():
    """Test fetching compound information."""
    # Test with a valid compound ID
    df = get_compound_info("C00031")
    assert isinstance(df, pd.DataFrame)
    assert "compound_id" in df.columns
    assert "name" in df.columns
    assert "formula" in df.columns
    
    # Test with default compound ID
    df_default = get_compound_info()
    assert isinstance(df_default, pd.DataFrame)
    assert "compound_id" in df_default.columns
    assert "name" in df_default.columns
    assert "formula" in df_default.columns

def test_invalid_reaction_id():
    """Test handling of invalid reaction ID."""
    with pytest.raises(Exception):
        get_reaction_info("INVALID_ID")

def test_invalid_compound_id():
    """Test handling of invalid compound ID."""
    with pytest.raises(Exception):
        get_compound_info("INVALID_ID")

def test_reaction_data_structure():
    """Test the structure of reaction data."""
    df = get_reaction_info("R00200")
    assert "reactants" in df.columns
    assert "products" in df.columns
    assert "is_reversible" in df.columns
    assert "enzyme" in df.columns
    assert "pathways" in df.columns

def test_compound_data_structure():
    """Test the structure of compound data."""
    df = get_compound_info("C00031")
    assert "exact_mass" in df.columns
    assert "molecular_weight" in df.columns
    assert "reactions" in df.columns
    assert "enzymes" in df.columns
    assert "pathways" in df.columns 