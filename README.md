# Fund Management System - Backend Developer Assessment

## Overview
This repository contains my implementation for the Backend Developer Practical Assessment: Fund Management System. The goal was to develop a RESTful API for managing investment funds, create a database schema, implement data persistence, and write test cases, among other tasks.

## Task Breakdown

### Task 1: Data Model Design
- **File**: `models.py`
- **Description**: Contains the `InvestmentFund` class, which represents an investment fund with attributes such as fund ID, name, manager name, description, NAV, creation date, and performance. It also includes a `to_dict` method for serialization and a function `generate_fund_id` to create unique UUIDs.

### Task 2: REST API Development
- **File**: `routes.py`, `__init__.py`
- **Description**: Implements the RESTful API using Flask with endpoints for:
  - Retrieving a list of all funds
  - Creating a new fund
  - Retrieving details of a specific fund by its ID
  - Updating the performance of a fund by its ID
  - Deleting a fund by its ID
- The API routes are registered in `__init__.py` through the `setup_routes` function from `routes.py`.

### Task 3: Data Persistence
- **File**: `routes.py`
- **Description**: Utilizes a JSON file (`funds.json`) for data persistence. The `load_funds` and `save_funds` functions handle reading from and writing to the JSON file to store fund data persistently.

### Task 4: SQL Database Schema
- **File**: `initial.sql`
- **Description**: Contains SQL statements to create the necessary database tables and relationships for storing investment fund data.

### Task 5: SQL Data Migration
- **File**: `migration.sql`
- **Description**: Provides SQL scripts to migrate data from the JSON file used in Task 3 to the SQL database designed in Task 4.

### Task 6: Error Handling
- **File**: `errors.py`
- **Description**: Implements error handling for the API to manage invalid inputs, missing resources, and other potential issues, ensuring robust and user-friendly error messages.

### Task 7: Testing
- **File**: `test_app.py`
- **Description**: Contains unit test cases for testing the API endpoints and the SQL database. It covers various scenarios such as creating, updating, retrieving, and deleting funds, as well as testing data parsing and SQL insert statements.

### Task 8: Documentation
- **File**: `docs.md`
- **Description**: Provides documentation on how to interact with the API endpoints, describes the SQL schema, and includes sample requests and responses for the endpoints.

## How to Run the Project
1. **Run the Flask Application**:
   - Use the `run.py` file to start the Flask app:
     ```bash
     python run.py
     ```

2. **Execute SQL Scripts**:
   - Run the `initial.sql` script to set up the database schema.
   - Use the `migration.sql` script to migrate data from `funds.json` to the SQL database.

3. **Run Tests**:
   - Execute `test_app.py` to verify the API and database functionality:
     ```bash
     python -m unittest test_app.py
     ```

## Contact
For any questions or further clarifications, please reach out or submit an issue.

---

Thank you for reviewing my submission!
