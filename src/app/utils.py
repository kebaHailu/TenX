import pandas as pd 
import os 


def load_city_data(city_name): 
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '../../data', f'{city_name}.csv')

    try:
        df = pd.read_csv(file_path, parse_dates=['Timestamp'])
    except Exception as e:
        print(e)
        return pd.DataFrame()
    
    return df 


def filter_data_by_date(df,day):
    filtered_df = df[df['Timestamp'].dt.date == day]
    return filtered_df 
