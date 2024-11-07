/* 
Task 4: SQL Database Schema - This SQL script defines the schema to store investment fund data.

Tables
1. FundManagers: Contains list of fund managers.
2. Funds: Stores information about each investment fund

Relationships
- Each Fund is managed by a single FundManager (one-to-many relationship).

*/

-- Drop the foreign key constraint in Funds if it exists
DECLARE @fk_name NVARCHAR(255);

SELECT @fk_name = name
FROM sys.foreign_keys
WHERE parent_object_id = OBJECT_ID('dbo.Funds');

IF @fk_name IS NOT NULL
BEGIN
    DECLARE @sql NVARCHAR(MAX);
    SET @sql = 'ALTER TABLE Funds DROP CONSTRAINT ' + @fk_name;
    EXEC sp_executesql @sql;
END;

-- Drop the Funds table if it exists
IF OBJECT_ID('dbo.Funds', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.Funds;
END;

-- Drop the FundManagers table if it exists
IF OBJECT_ID('dbo.FundManagers', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.FundManagers;
END;

-- Create FundManagers table
CREATE TABLE FundManagers (
    name NVARCHAR(255) PRIMARY KEY
);

-- Create Funds table
CREATE TABLE Funds (
    id UNIQUEIDENTIFIER PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    manager_name NVARCHAR(255) REFERENCES FundManagers(name) ON DELETE SET NULL,
    description NVARCHAR(MAX),
    nav DECIMAL(15, 2) NOT NULL,
    created_at DATE,
    performance DECIMAL(5, 2) NOT NULL
);
