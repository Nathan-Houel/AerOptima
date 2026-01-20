import pandas as pd

# Data loading
def load_data(file1, file2):
    '''
    Loading CSV files and return dataframes.

    Args :
        fileX (str) : path of the CSV file

    Returns :
        tuple : tuple de dataframe from the import file
    
    Raises:
        FileNotFoundError: if one the file doesn't exist
        pd.errors.EmptyDataError: if one CSV file is empty
        pd.errors.ParserError: if one CSV file isn't valid
    '''
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    return df1, df2

# Merging data
def merge_data(df_f, df_a):
    df = df_f.merge(df_a, left_on='AIRLINE', right_on='IATA_CODE')
    return df

# Cleaning
def clean_data(df):
    df.rename(columns={'AIRLINE_y': 'AIRLINE'}, inplace=True)
    df.drop(columns=['AIRLINE_x'], inplace=True)
    return df

# Temporal conversion
def process_time_data(df):
    df['SCHEDULED_DEPARTURE'] = df['SCHEDULED_DEPARTURE'].apply(str)
    df['SCHEDULED_DEPARTURE'] = df['SCHEDULED_DEPARTURE'].str.zfill(4)
    df['DATE_STR'] = df['YEAR'].astype(str) + '-' + df['MONTH'].astype(str) + '-' + df['DAY'].astype(str)
    df['STR_TIMESTAMP'] = df['DATE_STR'] + ' ' + df['SCHEDULED_DEPARTURE']
    df['TIMESTAMP'] = pd.to_datetime(df['STR_TIMESTAMP'], format = '%Y-%m-%d' + ' ' + '%H%M')
    df.drop(columns=['DATE_STR', 'STR_TIMESTAMP'], inplace=True)
    cols = df.columns.tolist()
    new_cols = cols[:4] + cols[-1:] + cols[-2:-1] + cols[4:-2]
    df = df[new_cols]
    return df


# Main block
flights_path = 'Dataset/flights.csv'
airlines_path = 'Dataset/airlines.csv'
output = 'clean_flights.csv'

[flights, airlines] = load_data(flights_path, airlines_path)
df_merged = merge_data(flights, airlines)
df_cleaned = clean_data(df_merged)
df_flights = process_time_data(df_cleaned)
print("🧹 Dataframe cleaned !")

df_flights.to_csv(output, index=False)
print(f"✅​ {output} created !")