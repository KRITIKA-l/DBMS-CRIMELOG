USE crime_db;

-- FIR INSERT LOG
DELIMITER $$

CREATE TRIGGER fir_insert_log
AFTER INSERT ON FIR
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Action, Table_Name, Record_ID)
    VALUES ('INSERT', 'FIR', NEW.FIR_ID);
END$$

DELIMITER ;

-- CASE INSERT LOG
DELIMITER $$

CREATE TRIGGER case_insert_log
AFTER INSERT ON Case_Table
FOR EACH ROW
BEGIN
    INSERT INTO Audit_Log (Action, Table_Name, Record_ID)
    VALUES ('INSERT', 'CASE', NEW.Case_ID);
END$$

DELIMITER ;

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