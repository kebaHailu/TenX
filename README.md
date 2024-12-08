# Weather & Solar Dashboard

This project is a Weather & Solar Dashboard built using Streamlit, Pandas, and Plotly. The dashboard allows users to select a city and a date to view weather and solar data, including solar irradiance, ambient temperature, relative humidity, wind speed, and module temperatures. Additionally, the project includes detailed data analysis such as correlation analysis, data cleaning, data quality checks, histograms, bubble charts, summary statistics, time series analysis, wind analysis, and temperature analysis.

## Features

- **City Selection**: Choose from a list of cities to view the corresponding weather and solar data.
- **Date Selection**: Select a specific date to filter the data.
- **Detailed Data Analysis**:
  - **Correlation Analysis**: Understand relationships between different weather and solar parameters.
  - **Data Cleaning**: Ensure the data is clean and ready for analysis.
  - **Data Quality Check**: Verify the integrity and quality of the data.
  - **Histograms and Bubble Charts**: Visualize data distributions and relationships.
  - **Summary Statistics**: View comprehensive statistics of the filtered data.
  - **Time Series Analysis**: Analyze trends and patterns over time.
  - **Wind Analysis**: Detailed examination of wind speed and direction.
  - **Temperature Analysis**: In-depth analysis of ambient and module temperatures.
- **Solar Irradiance Plot**: Visualize Global, Direct, and Diffuse Irradiance over time.
- **Temperature and Humidity Plot**: Visualize Ambient Temperature and Relative Humidity over time.
- **Wind Data Plot**: Visualize Wind Speed and Gusts over time.
- **Module Temperatures Plot**: Visualize the temperatures of solar modules A and B over time.
- **Raw Data Display**: Optionally display the raw data in a table format.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kebaHailu/TenX.git
    cd TenX
    ```

2. Install the required dependencies:
    ```bash
    pip install -r src/requriment.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run src/app/main.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to view the dashboard.

## Data

The data for this project is stored in CSV files located in the `data` directory. Each city has its own CSV file containing weather and solar data.

## Project Structure

The project has the following structure 
── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       ├── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
|------ src/
    ├── notebooks/
    │   ├── __init__.py
    │   ├── Correlation_analysis.ipynb
    │   ├── Data_cleaning.ipynb
    │   ├── Data_quality_check.ipynb
    │   ├── Histograms_and_bubble_chart.ipynb
    │   ├── Summary_statistics.ipynb
    │   ├── Time_series_analysis.ipynb
    │   ├── Wind_and_temp_analysis.ipynb
    │   └── README.md
    ├── app/
    │   ├── __init__.py
    |   ├── main.py
    |   ├── utils.py
    │   └── README.md
    ├── tests/
    │   ├── __init__.py
    └── scripts/
        ├── __init__.py
        └── README.md


