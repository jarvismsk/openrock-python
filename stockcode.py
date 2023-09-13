from breeze_connect import BreezeConnect

# Set up connection using your App Key
breeze = BreezeConnect(api_key="z011318$623428Q9796rO8eg55os979*")

# Generate session using the provided session key
breeze.generate_session(api_secret="96N92`&y41K285Q8b(5+63UK3~140755", session_token="21485296")

# Read the data from user_response.txt
with open("user_response.txt", "r") as f:
    stock_code = f.readline().strip()  # Read stock code
    interval = f.readline().strip()  # Read interval
    from_date = f.readline().strip()  # Read from date
    to_date = f.readline().strip()  # Read to date

# Process the stock code
exchange_code = 'NSE'
response = breeze.get_names(exchange_code=exchange_code, stock_code=stock_code)
isec_stock_code = response.get('isec_stock_code', '')

# Save the processed data to processed_response.txt
with open("processed_response.txt", "w") as f:
    f.write(f"Stock Code: {stock_code}\n")
    f.write(f"Interval: {interval}\n")
    f.write(f"From Date: {from_date}\n")
    f.write(f"To Date: {to_date}\n")
    f.write(f"Processed isec_stock_code: {isec_stock_code}\n")

# Print the processed data
print(f"Stock Code: {stock_code}")
print(f"Interval: {interval}")
print(f"From Date: {from_date}")
print(f"To Date: {to_date}")
print(f"Processed isec_stock_code: {isec_stock_code}")