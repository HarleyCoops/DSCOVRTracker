# DSCOVR Space Weather Data Tracker

## Overview
This Python-based tool provides real-time analysis and visualization of DSCOVR (Deep Space Climate Observatory) space weather data from NOAA's National Geophysical Data Center. The application offers interactive visualizations and analysis of magnetometer and plasma data, making space weather monitoring accessible and intuitive.

## Features
- **Portal Analysis**: Comprehensive overview of DSCOVR data products and access protocols
- **Magnetometer Data**: 
  - Real-time magnetic field component visualization
  - Data validation and quality checks
  - Derived parameter calculations
- **Plasma Analysis**:
  - Solar wind parameter visualization
  - Real-time updates of proton density, speed, and temperature
- **Statistical Analysis**:
  - Detailed statistical summaries
  - Cross-parameter correlations
  - Data quality metrics

## Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Setup
1. Clone the repository:
```bash
git clone https://github.com/HarleyCoops/DSCOVRTracker.git
cd DSCOVRTracker
```

2. Install required packages:
```bash
pip install streamlit pandas plotly requests numpy
```

3. Configure Streamlit:
Create a `.streamlit/config.toml` file with:
```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000
```

## Usage

1. Start the application:
```bash
streamlit run main.py
```

2. Navigate to `http://localhost:5000` in your web browser

3. Use the sidebar to select different data views:
   - Portal Analysis: Overview of available data products
   - Magnetometer: Real-time magnetic field data
   - Plasma: Solar wind parameters
   - Statistics: Data analysis and summaries

## Data Structure
- **Magnetometer Data**:
  - Bx, By, Bz: Magnetic field components
  - Bt: Total field magnitude
- **Plasma Data**:
  - Density: Proton density (n/cc)
  - Speed: Solar wind velocity (km/s)
  - Temperature: Proton temperature (K)

## Components
- `main.py`: Primary Streamlit application
- `data_portal.py`: DSCOVR portal interface
- `data_fetcher.py`: Data retrieval functions
- `visualizer.py`: Data visualization tools
- `utils.py`: Utility functions and data validation

## Dependencies
- streamlit: Web application framework
- pandas: Data manipulation
- plotly: Interactive visualizations
- requests: HTTP requests
- numpy: Numerical computations

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
