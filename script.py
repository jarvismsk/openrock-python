from flask import Flask, request, jsonify
import os
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

# Define allowed frontend origin(s)
allowed_origins = ['https://livedata.vercel.app', 'http://localhost:3002', 'https://openrock.co.in']  # Add more if needed

@app.route('/api/saveData', methods=['POST'])
def save_data():
    try:
        data = request.json
        stock_code = data['stockCode']
        interval = data['interval']
        from_date = data['fromDate']
        to_date = data['toDate']

        # Write data to user_response.txt
        user_response_path = os.path.join(os.path.dirname(__file__), 'user_response.txt')
        with open(user_response_path, 'w') as file:
            file.write(f"{stock_code}\n{interval}\n{from_date}\n{to_date}\n")

        return jsonify(message='Data saved successfully'), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify(error='Error saving data'), 500

@app.route('/api/getAllHistoricalData', methods=['GET'])
def get_all_historical_data():
    stock_code = request.args.get('stockCode')
    csv_file_path = os.path.join(os.path.dirname(__file__), f"{stock_code}_historical_data.csv")

    if os.path.exists(csv_file_path):
        try:
            with open(csv_file_path, 'r') as file:
                data = file.read()
            return data, 200
        except Exception as e:
            print(f"Error: {str(e)}")
            return 'Internal server error', 500
    else:
        return 'CSV file not found', 404

@app.route('/api/getHistoricalData', methods=['GET'])
def get_historical_data():
    stock_code = request.args.get('stockCode')
    page = int(request.args.get('page', 1))
    items_per_page = 50

    csv_file_path = os.path.join(os.path.dirname(__file__), f"{stock_code}_historical_data.csv")

    if os.path.exists(csv_file_path):
        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.reader(file)
                data = list(reader)

            start_index = (page - 1) * items_per_page
            end_index = start_index + items_per_page
            paginated_data = data[start_index:end_index]

            response = '\n'.join([','.join(row) for row in paginated_data])
            return response, 200
        except Exception as e:
            print(f"Error: {str(e)}")
            return 'Internal server error', 500
    else:
        return 'CSV file not found', 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3001))  # Use the Heroku-provided port or default to 3001
    app.run(host='0.0.0.0', port=port)
