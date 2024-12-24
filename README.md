# TellCo Telecom Analysis Dashboard

This project is a TellCo Telecom Analysis Dashboard built using Streamlit, Pandas, and Plotly. The dashboard allows users to explore a telecommunication dataset that contains valuable information about customer activities on the network. Users can analyze opportunities for growth and make informed recommendations regarding the potential acquisition of TellCo, a mobile service provider in the Republic of Pefkakia. The analysis includes user engagement, experience, and satisfaction metrics, as well as detailed data visualizations.

## Features

- **User Overview Analysis**: Gain insights into customer behavior, including handset usage and application engagement.
- **User Engagement Metrics**: Track user activity through session frequency, duration, and total traffic.
- **User Experience Analysis**: Evaluate network performance metrics such as TCP retransmission and throughput.
- **Satisfaction Analysis**: Assess customer satisfaction based on engagement and experience scores.
- **Interactive Visualizations**: Utilize advanced plotting techniques to visualize key performance indicators and trends.
- **Data Quality Checks**: Ensure the integrity and quality of the dataset through thorough analysis.
- **Raw Data Display**: Optionally display the raw telecommunication data in a table format for detailed examination.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kebaHailu/TenX.git
    cd TenX
    ```

2. Install the required dependencies:
    ```bash
    pip install -r src/requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run src/app/main.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to view the dashboard.

## Data

The data for this project is sourced from a month's aggregation of xDR records and is stored in a PostgreSQL database. The dataset includes customer activities and can be analyzed to identify growth opportunities for TellCo.

## Project Structure

The project has the following structure 
```
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
    │   ├── user_engagement_analysis.ipynb
    │   ├── user_experiance_analysis.ipynb
    │   ├── user_overview_analysis.ipynb
    │   └── user_satisfaction_analysis.ipynb
    ├── app/
    │   └── __init__.py
    ├── tests/
    │   ├── __init__.py
    └── scripts/
        ├── __init__.py
        ├── plot.py
        ├── utils.py
        └── README.md
```

