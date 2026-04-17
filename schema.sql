-- Create Database
CREATE DATABASE IF NOT EXISTS crime_db;
USE crime_db;

-- =========================
-- FIR TABLE
-- =========================
CREATE TABLE FIR (
    FIR_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Crime_Type VARCHAR(50) NOT NULL,
    Location VARCHAR(100),
    Status VARCHAR(30) DEFAULT 'Pending'
);

-- =========================
-- OFFICER TABLE
-- =========================
CREATE TABLE Officer (
    Officer_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Officer_Rank VARCHAR(50)
);

-- =========================
-- CASE TABLE
-- =========================
CREATE TABLE Case_Table (
    Case_ID INT AUTO_INCREMENT PRIMARY KEY,
    FIR_ID INT,
    Officer_ID INT,
    Status VARCHAR(50) DEFAULT 'Under Investigation',

    FOREIGN KEY (FIR_ID) REFERENCES FIR(FIR_ID)
        ON DELETE CASCADE,

    FOREIGN KEY (Officer_ID) REFERENCES Officer(Officer_ID)
        ON DELETE SET NULL
);

-- =========================
-- AUDIT LOG TABLE
-- =========================
CREATE TABLE Audit_Log (
    Log_ID INT AUTO_INCREMENT PRIMARY KEY,
    Action VARCHAR(50),
    Table_Name VARCHAR(50),
    Record_ID INT,
    TimeStamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================
-- TRIGGER: FIR INSERT
-- =========================
DELIMITER $$

CREATE TRIGGER fir_insert_log
AFTER INSERT ON FIR
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Action, Table_Name, Record_ID)
    VALUES ('INSERT', 'FIR', NEW.FIR_ID);
END$$

DELIMITER ;

-- =========================
-- TRIGGER: CASE INSERT
-- =========================
DELIMITER $$

CREATE TRIGGER case_insert_log
AFTER INSERT ON Case_Table
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Action, Table_Name, Record_ID)
    VALUES ('INSERT', 'Case_Table', NEW.Case_ID);
END$$

DELIMITER ;

-- =========================
-- TRIGGER: FIR DELETE
-- =========================
DELIMITER $$

CREATE TRIGGER fir_delete_log
AFTER DELETE ON FIR
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Action, Table_Name, Record_ID)
    VALUES ('DELETE', 'FIR', OLD.FIR_ID);
END$$

DELIMITER ;