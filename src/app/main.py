import streamlit as st
import pandas as pd
import plotly.express as px 
from datetime import datetime 
import numpy as np
from utils import load_city_data, filter_data_by_date 


CITIES = ['benin-malanville','sierraleone-bumbuna','togo-dapaong_qc']

# Title and sidebar for navigation 
st.sidebar.title('🌞 Weather & Solar Dashboard')
selected_city = st.sidebar.selectbox('Select a City', CITIES)
selected_date = st.sidebar.date_input('Select a Date', datetime.now().date())



# Load the data for selected city 
df = load_city_data(selected_city)
if not df.empty:
    st.sidebar.success(f"Loaded data for **{selected_city}**")

    daily_data = filter_data_by_date(df,selected_date)
    if daily_data.empty:
        st.warning(f"No data available for {selected_date} in {selected_city}.")
    else:
        st.title(f"📅 {selected_date} - {selected_city.capitalize()} Weather & Solar Data")
        st.subheader('📈 Summary Statistics')
        st.write(daily_data.describe())

        # Plot Solar Irradiance (GHI, DNI, DHI)
        st.subheader('☀️ Solar Irradiance Over Time')
        fig1 = px.line(daily_data, x='Timestamp', y=['GHI', 'DNI', 'DHI'], 
                    labels={'value': 'Irradiance (W/m²)', 'Timestamp': 'Time'}, 
                    title='Global, Direct, and Diffuse Irradiance')
        st.plotly_chart(fig1)

        # Plot Ambient Temperature and Humidity
        st.subheader('🌡️ Ambient Temperature and Relative Humidity')
        fig2 = px.line(daily_data, x='Timestamp', y=['Tamb', 'RH'], 
                    labels={'value': 'Measurement', 'Timestamp': 'Time'}, 
                    title='Temperature (°C) and Humidity (%)')
        st.plotly_chart(fig2)

        # Wind Data (Speed, Gust, Direction)
        st.subheader('💨 Wind Speed and Direction')
        fig3 = px.line(daily_data, x='Timestamp', y=['WS', 'WSgust'], 
                    labels={'value': 'Wind Speed (m/s)', 'Timestamp': 'Time'}, 
                    title='Wind Speed and Gusts')
        st.plotly_chart(fig3)

        # Temperature of Modules (A and B)
        st.subheader('🔋 Module Temperatures (A & B)')
        fig4 = px.line(daily_data, x='Timestamp', y=['TModA', 'TModB'], 
                    labels={'value': 'Temperature (°C)', 'Timestamp': 'Time'}, 
                    title='Temperature of Modules A and B')
        st.plotly_chart(fig4)

        # Display the raw data (optional)
        st.subheader('🗂️ Raw Data')
        st.dataframe(daily_data)
else:
    st.error("Failed to load data. Please check the data files.")

