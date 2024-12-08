# Streamlit Application

The Weather & Solar Dashboard is built using Streamlit, a powerful and easy-to-use framework for creating interactive web applications in Python. Streamlit allows developers to quickly build and deploy data-driven applications with minimal effort. Below is a detailed description of the Streamlit application used in this project.

## Streamlit Features

- **Interactive Widgets**: Streamlit provides a variety of interactive widgets such as sliders, dropdowns, and date pickers that allow users to interact with the data and customize their views. In this dashboard, users can select a city and a date to filter the weather and solar data.

- **Real-time Data Updates**: Streamlit automatically updates the displayed data and visualizations in real-time as users interact with the widgets. This ensures that users always see the most up-to-date information based on their selections.

- **Data Visualization**: Streamlit integrates seamlessly with popular data visualization libraries such as Plotly, Matplotlib, and Altair. In this dashboard, Plotly is used to create interactive and visually appealing plots for solar irradiance, temperature, humidity, wind data, and module temperatures.

- **Markdown Support**: Streamlit supports Markdown, allowing developers to easily add formatted text, headers, lists, and links to their applications. This README file, for example, is written in Markdown and can be displayed directly within the Streamlit app.

- **Easy Deployment**: Streamlit applications can be easily deployed to various platforms, including Streamlit Sharing, Heroku, and AWS. This makes it simple to share the dashboard with others and make it accessible online.

## Streamlit Application Structure

The Streamlit application for the Weather & Solar Dashboard is organized into several sections, each providing specific functionality:

1. **City and Date Selection**: Users can choose a city from a dropdown menu and select a date using a date picker. These selections filter the data to display only the relevant information for the chosen city and date.

2. **Solar Irradiance Plot**: This section displays a Plotly graph showing the Global, Direct, and Diffuse Irradiance over time. Users can hover over the plot to see detailed values for each data point.

3. **Temperature and Humidity Plot**: This section provides a Plotly graph visualizing the Ambient Temperature and Relative Humidity over time. The interactive plot allows users to explore the data in detail.

4. **Wind Data Plot**: This section includes a Plotly graph showing Wind Speed and Gusts over time. Users can analyze wind patterns and identify any significant changes in wind speed.

5. **Module Temperatures Plot**: This section displays a Plotly graph of the temperatures of solar modules A and B over time. Users can compare the temperature variations between the two modules.

6. **Raw Data Display**: Optionally, users can choose to display the raw data in a table format. This provides a detailed view of the underlying data used in the visualizations.

## Running the Streamlit Application

To run the Streamlit application locally, follow these steps:

1. Ensure you have all the required dependencies installed. You can install them using the following command:
    ```bash
    pip install -r src/requriment.txt
    ```

2. Run the Streamlit application using the following command:
    ```bash
    streamlit run src/app/main.py
    ```

3. Open your web browser and navigate to `http://localhost:8501` to view the dashboard.

By leveraging Streamlit's powerful features, the Weather & Solar Dashboard provides an interactive and user-friendly interface for exploring and analyzing weather and solar data.
