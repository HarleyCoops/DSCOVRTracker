"""
Module for fetching data from DSCOVR portal
"""
from typing import Dict, Optional
import requests
from datetime import datetime, timedelta
import pandas as pd

class DSCOVRDataFetcher:
    def __init__(self):
        self.base_url = "https://www.ngdc.noaa.gov/dscovr/portal"

    def fetch_mag_data(self, start_time: Optional[datetime] = None) -> pd.DataFrame:
        """Fetch magnetometer data"""
        if start_time is None:
            start_time = datetime.now() - timedelta(hours=1)
        
        try:
            params = {
                'startTime': start_time.isoformat(),
                'format': 'json'
            }
            response = requests.get(f"{self.base_url}/mag/data", params=params)
            response.raise_for_status()
            
            data = response.json()
            return pd.DataFrame(data['data'])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch MAG data: {str(e)}")

    def fetch_plasma_data(self, start_time: Optional[datetime] = None) -> pd.DataFrame:
        """Fetch solar wind plasma data"""
        if start_time is None:
            start_time = datetime.now() - timedelta(hours=1)
        
        try:
            params = {
                'startTime': start_time.isoformat(),
                'format': 'json'
            }
            response = requests.get(f"{self.base_url}/plasma/data", params=params)
            response.raise_for_status()
            
            data = response.json()
            return pd.DataFrame(data['data'])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch plasma data: {str(e)}")

    def fetch_epic_metadata(self) -> Dict:
        """Fetch latest EPIC image metadata"""
        try:
            response = requests.get(f"{self.base_url}/epic/latest")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch EPIC metadata: {str(e)}")

    def validate_data(self, df: pd.DataFrame, data_type: str) -> bool:
        """Validate fetched data"""
        if df.empty:
            return False
            
        required_columns = {
            'mag': ['timestamp', 'Bx', 'By', 'Bz', 'Bt'],
            'plasma': ['timestamp', 'density', 'speed', 'temperature']
        }
        
        return all(col in df.columns for col in required_columns.get(data_type, []))
