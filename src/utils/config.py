"""Configuration handling for the KEGG Data Fetcher package."""

import os
import yaml
from typing import Dict, Any

def load_config(config_path: str = "config.yaml") -> Dict[str, Any]:
    """Load configuration from a YAML file.
    
    Args:
        config_path: Path to the configuration file.
        
    Returns:
        Dictionary containing the configuration.
        
    Raises:
        FileNotFoundError: If the configuration file does not exist.
        yaml.YAMLError: If the configuration file is not valid YAML.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, 'r') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing configuration file: {e}")
    
    # Create necessary directories
    if 'output' in config and 'data_dir' in config['output']:
        os.makedirs(config['output']['data_dir'], exist_ok=True)
    
    if 'logging' in config and 'file' in config['logging']:
        log_dir = os.path.dirname(config['logging']['file'])
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
    
    return config

def validate_config(config: Dict[str, Any]) -> None:
    """Validate the configuration structure.
    
    Args:
        config: Configuration dictionary to validate.
        
    Raises:
        ValueError: If the configuration is invalid.
    """
    required_sections = ['kegg', 'output', 'reaction', 'compound', 'logging']
    
    for section in required_sections:
        if section not in config:
            raise ValueError(f"Missing required configuration section: {section}")
    
    # Validate KEGG configuration
    if 'base_url' not in config['kegg']:
        raise ValueError("Missing required KEGG configuration: base_url")
    if 'timeout' not in config['kegg']:
        raise ValueError("Missing required KEGG configuration: timeout")
    
    # Validate output configuration
    if 'data_dir' not in config['output']:
        raise ValueError("Missing required output configuration: data_dir")
    if 'file_format' not in config['output']:
        raise ValueError("Missing required output configuration: file_format")
    
    # Validate reaction configuration
    if 'default_id' not in config['reaction']:
        raise ValueError("Missing required reaction configuration: default_id")
    if 'fields' not in config['reaction']:
        raise ValueError("Missing required reaction configuration: fields")
    
    # Validate compound configuration
    if 'default_id' not in config['compound']:
        raise ValueError("Missing required compound configuration: default_id")
    if 'fields' not in config['compound']:
        raise ValueError("Missing required compound configuration: fields")
    
    # Validate logging configuration
    if 'level' not in config['logging']:
        raise ValueError("Missing required logging configuration: level")
    if 'format' not in config['logging']:
        raise ValueError("Missing required logging configuration: format")
    if 'file' not in config['logging']:
        raise ValueError("Missing required logging configuration: file") 