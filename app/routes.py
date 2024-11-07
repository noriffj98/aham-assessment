from flask import request, jsonify, abort
from .models import InvestmentFund, generate_fund_id
import json
import os

# Task 3: Data Persistence - The API uses a JSON file ('funds.json') for data persistence.

FUND_FILE = 'funds.json'

def load_funds():
    # Load funds from the JSON file
    if os.path.exists(FUND_FILE):
        try:
            with open(FUND_FILE, 'r') as file:
                data = json.load(file)
                return {k: InvestmentFund(**v) for k, v in data.items()}
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            abort(500, "Error loading funds data.")
    return {}

funds = load_funds()

def save_funds():
    # Save funds to the JSON file
    with open(FUND_FILE, 'w') as file:
        json.dump({fund_id: fund.to_dict() for fund_id, fund in funds.items()}, file, indent=4)



# Task 2: REST API Development - Flask API to manage investment funds with routes for CRUD operations and performance updates

def setup_routes(app):
    @app.route('/funds')
    def get_funds():
        # Endpoint to retrieve a list of all funds
        return jsonify([fund.to_dict() for fund in funds.values()]), 200

    @app.route('/funds', methods=['POST'])
    def create_fund():
        # Endpoint to create a new fund
        data = request.get_json()
        try:
            fund_id = generate_fund_id()  # Generate a unique UUID
            fund = InvestmentFund(
                fund_id=fund_id,
                fund_name=data['fund_name'],
                fund_manager_name=data['fund_manager_name'],
                fund_description=data['fund_description'],
                fund_nav=float(data['fund_nav']),
                fund_creation_date=data['fund_creation_date'],
                fund_performance=float(data['fund_performance'])
            )
            funds[fund.fund_id] = fund
            save_funds()
            return jsonify(fund.to_dict()), 201
        except KeyError as e:
            abort(400, f"Missing field: {e.args[0]}")
        except ValueError:
            abort(400, "Invalid data type provided.")

    @app.route('/funds/<fund_id>', methods=['GET'])
    def get_fund_details(fund_id):
        # Endpoint to retrieve details of a specific fund by its ID
        fund = funds.get(fund_id)
        if not fund:
            abort(404, "Fund not found.")
        return jsonify(fund.to_dict()), 200

    @app.route('/funds/<fund_id>/performance', methods=['PUT'])
    def update_fund_performance(fund_id):
        # Endpoint to update the performance of a fund using its ID
        fund = funds.get(fund_id)
        if fund:
            data = request.get_json()
            try:
                fund.fund_performance = float(data['fund_performance'])
                save_funds()
                return jsonify(fund.to_dict()), 200
            except KeyError:
                abort(400, "Missing or invalid performance data.")
            except ValueError:
                abort(400, "Performance data must be a valid number.")
        else:
            abort(404, "Fund not found")

    @app.route('/funds/<fund_id>', methods=['DELETE'])
    def delete_fund(fund_id):
        # Endpoint to delete a fund using its ID
        if fund_id in funds:
            del funds[fund_id]
            save_funds()
            return '', 204
        else:
            abort(404, "Fund not found")
