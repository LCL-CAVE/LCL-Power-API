import requests
import pandas as pd
from datetime import datetime

# HTTP Basic Authentication Credentials
username = 'LCL'
password = 'pw'
url = 'http://127.0.0.1:5000/v1/table'

# Request parameters
payload = {
    'table': 'day_ahead_price',
    'bidding_zone': 'ES',  # Provide the desired bidding zone
    'date_from': '2020-02-01 00:00:00',  # Provide start date
    'date_to': '2021-02-01 23:59:59'  # Provide end date
}

# Send authenticated request to the API
response = requests.post(url, auth=(username, password), data=payload)

# Check if request was successful
if response.status_code == 200:
    # Convert JSON response to Pandas DataFrame
    df = pd.read_json(response.text)

    # Convert 'timestamp' column to Pandas datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Display the DataFrame
    print(df.head())

else:
    print(f"Error: {response.status_code} - {response.text}")
