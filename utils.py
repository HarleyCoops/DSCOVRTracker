"""
Utility functions for DSCOVR data analysis
"""
from typing import Dict, List
import pandas as pd
import numpy as np

def validate_mag_data(data: pd.DataFrame) -> Dict[str, bool]:
    """Validate magnetometer data"""
    checks = {
        "complete_data": not data.empty,
        "valid_components": all(col in data.columns for col in ['Bx', 'By', 'Bz', 'Bt']),
        "physical_limits": all(
            data[col].between(-1000, 1000).all() 
            for col in ['Bx', 'By', 'Bz', 'Bt']
        ),
        "no_duplicates": not data.index.duplicated().any()
    }
    return checks

def validate_plasma_data(data: pd.DataFrame) -> Dict[str, bool]:
    """Validate plasma data"""
    checks = {
        "complete_data": not data.empty,
        "valid_parameters": all(col in data.columns for col in ['density', 'speed', 'temperature']),
        "physical_limits": {
            "density": data['density'].between(0, 100).all(),
            "speed": data['speed'].between(200, 2000).all(),
            "temperature": data['temperature'].between(1000, 1e7).all()
        },
        "no_duplicates": not data.index.duplicated().any()
    }
    return checks

def calculate_derived_parameters(mag_data: pd.DataFrame) -> Dict[str, float]:
    """Calculate derived parameters from magnetometer data"""
    return {
        "mean_field_magnitude": mag_data['Bt'].mean(),
        "std_deviation": mag_data['Bt'].std(),
        "max_variation": mag_data['Bt'].max() - mag_data['Bt'].min(),
        "southward_bz_duration": (mag_data['Bz'] < 0).sum() / len(mag_data) * 100
    }
