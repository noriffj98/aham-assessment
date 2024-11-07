import uuid

# Task 1: Data Model Design - A Python class for representing an investment fund

class InvestmentFund:
    def __init__(self, fund_id, fund_name, fund_manager_name,
                 fund_description, fund_nav, 
                 fund_creation_date, fund_performance):
        self.fund_id = fund_id  # Unique identifier for the fund
        self.fund_name = fund_name  # Name of the fund
        self.fund_manager_name = fund_manager_name  # Manager overseeing the fund
        self.fund_description = fund_description  # Detailed description of the fund
        self.fund_nav = fund_nav  # Net Asset Value (NAV) of the fund
        self.fund_creation_date = fund_creation_date  # Date the fund was created
        self.fund_performance = fund_performance  # Fund's performance percentage

    def to_dict(self):
        # Convert the investment fund's data to a dictionary format
        return {
            "fund_id": self.fund_id,
            "fund_name": self.fund_name,
            "fund_manager_name": self.fund_manager_name,
            "fund_description": self.fund_description,
            "fund_nav": self.fund_nav,
            "fund_creation_date": self.fund_creation_date,
            "fund_performance": self.fund_performance
        }

def generate_fund_id():
    return str(uuid.uuid4())  # Generate a unique UUID for new funds
