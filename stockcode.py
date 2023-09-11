import os
from flask import Flask, request, jsonify
import redis
from breeze_connect import BreezeConnect

app = Flask(__name__)

# Use Redis to retrieve data
redis_client = redis.StrictRedis.from_url(os.environ.get("REDIS_URL"))

@app.route('/python-endpoint', methods=['POST'])
def python_endpoint():
    data = request.json

    # Process data here

    # Read the data from user_response.txt
    with open("user_response.txt", "r") as f:
        stock_code = f.readline().strip()  # Read stock code
        interval = f.readline().strip()  # Read interval
        from_date = f.readline().strip()  # Read from date
        to_date = f.readline().strip()  # Read to date

    # Process the stock code using BreezeConnect
    exchange_code = 'NSE'
    breeze = BreezeConnect(api_key="z011318$623428Q9796rO8eg55os979*")
    breeze.generate_session(api_secret="96N92`&y41K285Q8b(5+63UK3~140755", session_token="21181357")
    response = breeze.get_names(exchange_code=exchange_code, stock_code=stock_code)
    isec_stock_code = response.get('isec_stock_code', '')

    # Save the processed data to Redis
    redis_client.set("processed_data", f"Stock Code: {stock_code}\nInterval: {interval}\nFrom Date: {from_date}\nTo Date: {to_date}\nProcessed isec_stock_code: {isec_stock_code}")

    return jsonify({"message": "Data received and processed successfully"})

if __name__ == "__main__":
    app.run(debug=True)
