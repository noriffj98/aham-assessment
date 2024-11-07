# API Documentation

## Overview
This API allows you to interact with the Investment Fund Management system. It provides endpoints for managing funds, retrieving data about investments, and updating records.

## Endpoints

### GET /funds

#### Description:
Retrieves a list of all investment funds in the system.

#### Request:
- **Method**: GET

#### Response:
- **Status Code**: 200 OK
- **Body**:
```json
[
    {
        "fund_id": "e64d43b4-d26c-4e6d-9049-c6f3f62c588f",
        "fund_name": "Test Fund",
        "fund_manager_name": "David Suh",
        "fund_description": "A test fund.",
        "fund_nav": 150.75,
        "fund_creation_date": "2024-11-05",
        "fund_performance": 12.5
    },
    {
        "fund_id": "216dae2a-3463-4728-9df7-b4aa2aece4e5",
        "fund_name": "Test Fund 2",
        "fund_manager_name": "Alice Wong",
        "fund_description": "A test fund.",
        "fund_nav": 450000,
        "fund_creation_date": "2020-01-01",
        "fund_performance": 16.5
    }
]
```

### POST /funds

#### Description:
Creates a new investment fund in the system.

#### Request:
- **Method**: POST
- **Body**:
```json
    {
        "fund_name": "Test Fund",
        "fund_manager_name": "David Suh",
        "fund_description": "A test fund.",
        "fund_nav": 150.75,
        "fund_creation_date": "2024-11-05",
        "fund_performance": 12.5
    }
```

#### Response:
- **Status Code**: 201 Created
- **Body**:
```json
    {
        "fund_id": "e64d43b4-d26c-4e6d-9049-c6f3f62c588f",
        "fund_name": "Test Fund",
        "fund_manager_name": "David Suh",
        "fund_description": "A test fund.",
        "fund_nav": 150.75,
        "fund_creation_date": "2024-11-05",
        "fund_performance": 12.5
    }
```

### GET /funds/<fund_id>

#### Description:
Retrieve an investment fund by ID.

#### Request:
- **Method**: GET

#### Response:
- **Status Code**: 200 OK
- **Body**:
```json
    {
        "fund_id": "e64d43b4-d26c-4e6d-9049-c6f3f62c588f",
        "fund_name": "Test Fund",
        "fund_manager_name": "David Suh",
        "fund_description": "A test fund.",
        "fund_nav": 150.75,
        "fund_creation_date": "2024-11-05",
        "fund_performance": 12.5
    }
```

### PUT /funds/<fund_id>/performance

#### Description:
Update the performance of a specific fund.

#### Request:
- **Method**: PUT
- **Body**:
```json
  {
    "fund_performance": 15.0
  }
```

#### Response:
- **Status Code**: 200 OK
- **Body**:
```json
    {
        "fund_id": "e64d43b4-d26c-4e6d-9049-c6f3f62c588f",
        "fund_name": "Test Fund",
        "fund_manager_name": "David Suh",
        "fund_description": "A test fund.",
        "fund_nav": 150.75,
        "fund_creation_date": "2024-11-05",
        "fund_performance": 15.0
    }
```

### DELETE /funds/<fund_id>

#### Description:
Deletes an investment fund from the system.

#### Request:
- **Method**: DELETE

#### Response:
- **Status Code**: 204 No Content

# Database Schema

## Tables
1. FundManagers: Contains list of fund managers.
2. Funds: Stores information about each investment fund

## Relationships
- Each Fund is managed by a single FundManager (one-to-many relationship).

## FundManagers Table
- `name`: Text, Name of the fund manager

## Funds Table
- `id`: UUID, Primary Key
- `name`: Text, Name of the fund
- `manager_name`: Text, Manager of the fund
- `description`: Text, Description of the fund
- `nav`: Real, Net Asset Value
- `created_at`: Text, Date of creation
- `performance`: Real, Performance percentage

# Notes

- **Error Handling**: All responses should include an appropriate status code and a meaningful message. Common status codes include:

  - `200 OK`: Request succeeded.
  - `201 Created`: Resource successfully created.
  - `204 No Content`: Resource successfully deleted.
  - `401 Unauthorized`: Invalid authentication credentials.
  - `404 Not Found`: Resource not found.
  - `500 Internal Server Error`: General server error.
