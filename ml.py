from breeze_connect import BreezeConnect
import pandas as pd
import os
import datetime

# Set up connection using your App Key
isec = BreezeConnect(api_key="z011318$623428Q9796rO8eg55os979*")

# Generate session using the provided session key
isec.generate_session(api_secret="96N92`&y41K285Q8b(5+63UK3~140755", session_token="21659745")

# Read the processed data from processed_response.txt
with open("processed_response.txt", "r") as f:
    lines = f.readlines()
    stock_code = lines[0].split(":")[1].strip()
    interval = lines[1].split(":")[1].strip()
    from_date = lines[2].split(":")[1].strip()
    to_date = lines[3].split(":")[1].strip()
    processed_isec_stock_code = lines[4].split(":")[1].strip()

# Convert from_date and to_date to datetime objects
from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')

# ...

# Define the file path
csv_file_path = f"{stock_code}_historical_data.csv"

# Check if the CSV file already exists
if os.path.exists(csv_file_path):
    # Delete the existing CSV file
    os.remove(csv_file_path)
    print(f"Existing CSV file for {stock_code} deleted.")

# Retrieve historical data for the specified date range and processed isec stock code
exchange_code = "NSE"
data = isec.get_historical_data(interval=interval,
                                 from_date=from_date.isoformat(),
                                 to_date=to_date.isoformat(),
                                 stock_code=processed_isec_stock_code,
                                 exchange_code=exchange_code,
                                 product_type="cash")

# Store data in a DataFrame
df = pd.DataFrame(data["Success"])

# Remove empty columns
df = df.dropna(axis=1, how="all")

# Save data as a CSV file
df.to_csv(csv_file_path, index=False)
print("CSV file created and data saved.")
