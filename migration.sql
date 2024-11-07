/* 
Task 5: SQL Data Migration - This SQL script migrates data from a JSON file into the SQL database schema.
*/

-- Load JSON data from the file into a variable
DECLARE @json_data NVARCHAR(MAX);

SELECT @json_data = BulkColumn
FROM OPENROWSET(
    BULK 'G:\My Drive\iffah\Test\AHAM_assessment\funds.json', -- Adjust the path to the JSON file
    SINGLE_CLOB
) AS datasource;

-- Insert unique manager names into FundManagers
INSERT INTO FundManagers (name)
SELECT DISTINCT JSON_VALUE(fund.value, '$.fund_manager_name') AS manager_name
FROM OPENJSON(@json_data) AS fund
WHERE JSON_VALUE(fund.value, '$.fund_manager_name') IS NOT NULL
    AND JSON_VALUE(fund.value, '$.fund_manager_name') NOT IN (SELECT name FROM FundManagers);

-- Insert Data into Funds Table
INSERT INTO Funds (id, name, manager_name, description, nav, created_at, performance)
SELECT
    JSON_VALUE(fund.value, '$.fund_id') AS id,
    JSON_VALUE(fund.value, '$.fund_name') AS name,
    JSON_VALUE(fund.value, '$.fund_manager_name') AS manager_name,
    JSON_VALUE(fund.value, '$.fund_description') AS description,
    JSON_VALUE(fund.value, '$.fund_nav') AS nav,
    JSON_VALUE(fund.value, '$.fund_creation_date') AS created_at,
    JSON_VALUE(fund.value, '$.fund_performance') AS performance
FROM OPENJSON(@json_data) AS fund;

-- View Tables
SELECT * FROM FundManagers;
SELECT * FROM Funds;
