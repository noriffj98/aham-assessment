import unittest
import json
from app import create_app
from .models import InvestmentFund

# Task 7: Testing - This tests ensures the proper functioning of both the API endpoints and the SQL database.

class TestInvestmentFund(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

        # Set up test client and test data
        self.client = self.app.test_client()
        self.client.testing = True

        self.sample_fund = InvestmentFund(
            fund_id="e64d43b4-d26c-4e6d-9049-c6f3f62c588f",
            fund_name="Test Fund",
            fund_manager_name="David Suh",
            fund_description="A test fund.",
            fund_nav=150.75,
            fund_creation_date="2024-11-05",
            fund_performance=12.5
        )

        self.sample_fund_dict = self.sample_fund.to_dict()

        self.json_data = '''
        {
            "e64d43b4-d26c-4e6d-9049-c6f3f62c588f": {
                "fund_id": "e64d43b4-d26c-4e6d-9049-c6f3f62c588f",
                "fund_name": "Test Fund",
                "fund_manager_name": "David Suh",
                "fund_description": "A test fund.",
                "fund_nav": 150.75,
                "fund_creation_date": "2024-11-05",
                "fund_performance": 12.5
            },
            "216dae2a-3463-4728-9df7-b4aa2aece4e5": {
                "fund_id": "216dae2a-3463-4728-9df7-b4aa2aece4e5",
                "fund_name": "Test Fund 2",
                "fund_manager_name": "Alice Wong",
                "fund_description": "A test fund.",
                "fund_nav": 450000,
                "fund_creation_date": "2020-01-01",
                "fund_performance": 16.5
            }
        }
        '''

    def test_initialization(self):
        # Test if the attributes are set correctly
        self.assertEqual(self.sample_fund.fund_id, "e64d43b4-d26c-4e6d-9049-c6f3f62c588f")
        self.assertEqual(self.sample_fund.fund_name, "Test Fund")
        self.assertEqual(self.sample_fund.fund_manager_name, "David Suh")
        self.assertEqual(self.sample_fund.fund_description, "A test fund.")
        self.assertEqual(self.sample_fund.fund_nav, 150.75)
        self.assertEqual(self.sample_fund.fund_creation_date, "2024-11-05")
        self.assertEqual(self.sample_fund.fund_performance, 12.5)

    def test_to_dict(self):
        # Test if the to_dict method returns the correct dictionary
        expected_dict = {
            "fund_id": "e64d43b4-d26c-4e6d-9049-c6f3f62c588f",
            "fund_name": "Test Fund",
            "fund_manager_name": "David Suh",
            "fund_description": "A test fund.",
            "fund_nav": 150.75,
            "fund_creation_date": "2024-11-05",
            "fund_performance": 12.5
        }
        self.assertEqual(self.sample_fund.to_dict(), expected_dict)

    def test_get_all_funds(self):
        # Test the /funds endpoint to get all funds
        response = self.client.get('/funds')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_create_fund(self):
        # Test the /funds endpoint with POST to create a fund
        response = self.client.post('/funds', data=json.dumps(self.sample_fund_dict), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['fund_name'], self.sample_fund_dict['fund_name'])
        self.assertIn('fund_id', data)

    def test_create_fund_missing_field(self):
        # Test creating a fund with missing required field
        incomplete_data = self.sample_fund_dict.copy()
        incomplete_data.pop("fund_name")  # Remove a required field
        response = self.client.post('/funds', data=json.dumps(incomplete_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing field", response.get_json()["message"])

    def test_get_fund_details(self):
        # First, create a fund to retrieve later
        create_response = self.client.post('/funds', data=json.dumps(self.sample_fund_dict), content_type='application/json')
        fund_id = create_response.get_json()["fund_id"]

        # Retrieve the created fund
        response = self.client.get(f'/funds/{fund_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["fund_id"], fund_id)

    def test_get_fund_details_not_found(self):
        # Try to retrieve a non-existent fund
        response = self.client.get('/funds/nonexistent_id')
        self.assertEqual(response.status_code, 404)

    def test_update_fund_performance(self):
        # Create a fund to update
        create_response = self.client.post('/funds', data=json.dumps(self.sample_fund_dict), content_type='application/json')
        fund_id = create_response.get_json()["fund_id"]

        # Update the performance
        update_data = {"fund_performance": 15.5}
        response = self.client.put(f'/funds/{fund_id}/performance', data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["fund_performance"], 15.5)

    def test_update_fund_performance_invalid(self):
        # Test updating fund performance with invalid data
        create_response = self.client.post('/funds', data=json.dumps(self.sample_fund_dict), content_type='application/json')
        fund_id = create_response.get_json()["fund_id"]

        # Send invalid data (non-numeric performance)
        update_data = {"fund_performance": "invalid"}
        response = self.client.put(f'/funds/{fund_id}/performance', data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_fund(self):
        # Create a fund to delete
        create_response = self.client.post('/funds', data=json.dumps(self.sample_fund_dict), content_type='application/json')
        fund_id = create_response.get_json()["fund_id"]

        # Delete the fund
        response = self.client.delete(f'/funds/{fund_id}')
        self.assertEqual(response.status_code, 204)

        # Verify deletion by trying to retrieve it
        response = self.client.get(f'/funds/{fund_id}')
        self.assertEqual(response.status_code, 404)

    def test_parse_json(self):
        # Load JSON data into a Python object
        data = json.loads(self.json_data)

        # Test that JSON is parsed correctly
        self.assertEqual(len(data), 2)  # Expecting 2 funds in the data
        funds = list(data.values())
        self.assertEqual(funds[0]['fund_name'], "Test Fund")
        self.assertEqual(funds[1]['fund_manager_name'], "Alice Wong")

    def test_insert_fund_managers(self):
        # Sample fund managers
        fund_managers = [
            {"fund_manager_name": "David Suh"},
            {"fund_manager_name": "Alice Wong"}
        ]

        # Mock of SQL query for inserting fund managers (Testing the string construction)
        insert_statements = []
        for manager in fund_managers:
            insert_statement = f"INSERT INTO FundManagers (name) VALUES ('{manager['fund_manager_name']}')"
            insert_statements.append(insert_statement)

        # Assert that the SQL insert statements are correctly constructed
        self.assertEqual(len(insert_statements), 2)
        self.assertEqual(insert_statements[0], "INSERT INTO FundManagers (name) VALUES ('David Suh')")
        self.assertEqual(insert_statements[1], "INSERT INTO FundManagers (name) VALUES ('Alice Wong')")

    def test_insert_funds(self):
        funds = json.loads(self.json_data)
        
        # Mock of SQL query for inserting funds
        insert_statements = []
        for fund in funds.values():
            insert_statement = f"""
            INSERT INTO Funds (id, name, manager_name, description, nav, created_at, performance)
            VALUES ('{fund['fund_id']}', '{fund['fund_name']}', '{fund['fund_manager_name']}', 
                    '{fund['fund_description']}', {fund['fund_nav']}, '{fund['fund_creation_date']}', {fund['fund_performance']})
            """
            insert_statements.append(insert_statement)

        # Assert that the SQL insert statements are correctly constructed
        self.assertEqual(len(insert_statements), 2)
        self.assertIn("INSERT INTO Funds", insert_statements[0])
        self.assertIn("Fund 2", insert_statements[1])


if __name__ == "__main__":
    unittest.main()