"""
Main Streamlit application for DSCOVR data analysis
"""
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

from data_portal import DSCOVRPortalAnalyzer
from data_fetcher import DSCOVRDataFetcher
from visualizer import DSCOVRVisualizer
from utils import validate_mag_data, validate_plasma_data, calculate_derived_parameters

def main():
    st.set_page_config(page_title="DSCOVR Data Analysis", layout="wide")
    st.title("DSCOVR Space Weather Data Analysis")

    # Initialize components
    analyzer = DSCOVRPortalAnalyzer()
    fetcher = DSCOVRDataFetcher()
    visualizer = DSCOVRVisualizer()

    # Sidebar
    st.sidebar.header("Data Selection")
    data_type = st.sidebar.selectbox(
        "Select Data Type",
        ["Portal Analysis", "Magnetometer", "Plasma", "Statistics"]
    )

    # Main content
    if data_type == "Portal Analysis":
        st.header("DSCOVR Data Portal Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Data Products")
            st.json(analyzer.get_data_products())
            
        with col2:
            st.subheader("Access Protocols")
            st.json(analyzer.get_access_protocols())
            
        st.subheader("Endpoint Health Status")
        st.json(analyzer.analyze_endpoint_health())

    elif data_type == "Magnetometer":
        st.header("Magnetometer Data Analysis")
        
        try:
            with st.spinner("Fetching MAG data..."):
                mag_data = fetcher.fetch_mag_data()
                
            if not mag_data.empty:
                st.plotly_chart(visualizer.create_mag_plot(mag_data))
                
                # Data validation
                validation_results = validate_mag_data(mag_data)
                st.subheader("Data Validation")
                st.json(validation_results)
                
                # Derived parameters
                st.subheader("Derived Parameters")
                st.json(calculate_derived_parameters(mag_data))
            else:
                st.error("No magnetometer data available")
                
        except Exception as e:
            st.error(f"Error fetching magnetometer data: {str(e)}")

    elif data_type == "Plasma":
        st.header("Solar Wind Plasma Analysis")
        
        try:
            with st.spinner("Fetching plasma data..."):
                plasma_data = fetcher.fetch_plasma_data()
                
            if not plasma_data.empty:
                st.plotly_chart(visualizer.create_plasma_plot(plasma_data))
                
                # Data validation
                validation_results = validate_plasma_data(plasma_data)
                st.subheader("Data Validation")
                st.json(validation_results)
            else:
                st.error("No plasma data available")
                
        except Exception as e:
            st.error(f"Error fetching plasma data: {str(e)}")

    elif data_type == "Statistics":
        st.header("Statistical Analysis")
        
        try:
            with st.spinner("Fetching data..."):
                mag_data = fetcher.fetch_mag_data()
                plasma_data = fetcher.fetch_plasma_data()
                
            if not mag_data.empty and not plasma_data.empty:
                # MAG Statistics
                st.subheader("Magnetometer Statistics")
                st.plotly_chart(visualizer.create_statistics_table(
                    mag_data, ['Bx', 'By', 'Bz', 'Bt']
                ))
                
                # Plasma Statistics
                st.subheader("Plasma Statistics")
                st.plotly_chart(visualizer.create_statistics_table(
                    plasma_data, ['density', 'speed', 'temperature']
                ))
            else:
                st.error("No data available for statistical analysis")
                
        except Exception as e:
            st.error(f"Error performing statistical analysis: {str(e)}")

if __name__ == "__main__":
    main()
