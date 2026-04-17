# Crime Record Management System

A clean console-based crime record system built with Python and MySQL. It manages FIRs, officers, case assignments, and audit history in a simple menu-driven workflow.

## At A Glance

| What It Does | Why It Matters |
| --- | --- |
| FIR management | Create, review, and remove complaint records |
| Officer tracking | Keep a list of officers and their ranks |
| Case handling | Assign FIRs to officers and update case progress |
| Audit logging | Record key database actions automatically |

## Highlights

- Fast console menu for day-to-day record handling
- MySQL-backed storage with foreign keys and triggers
- Built-in audit trail for inserts and deletes
- Lightweight structure that is easy to extend

## Tech Stack

- Python 3
- MySQL
- mysql-connector-python

## Project Layout

- main.py - Application entry point and menu
- db.py - Database connection helper
- fir.py - FIR create, view, and delete actions
- officer.py - Officer create and list actions
- case.py - Case assignment and status updates
- schema.sql - Database tables, keys, and triggers
- audit.sql - Additional SQL helper script

## Setup

1. Install MySQL and make sure the server is running.
2. Create the database and tables using schema.sql.
3. Install the Python dependency:

```bash
pip install mysql-connector-python
```

4. Update db.py with your local MySQL credentials if needed.

## Database Initialization

Run the schema script in MySQL:

```sql
SOURCE schema.sql;
```

If your client does not support SOURCE, open schema.sql and run it manually.

## Run The App

From the project folder:

```bash
python main.py
```

## Menu

The console menu includes:

- Add FIR
- View FIR
- Delete FIR
- Add Officer
- View Officers
- Assign Case
- View Cases
- Update Case Status
- View Audit Logs
- Exit

## Flow

1. Add an FIR.
2. Add an officer.
3. Assign the FIR to that officer.
4. Update the case status as the investigation moves forward.
5. Review audit logs to see what changed in the database.

## Notes

- FIR inserts and deletes, plus case inserts, are logged automatically in Audit_Log through MySQL triggers.
- Deleting an FIR also removes related cases because of the foreign key cascade rule.
- If a case officer is removed, the assigned officer field is set to NULL.