from db import get_connection

def assign_case():
    conn = get_connection()
    cursor = conn.cursor()

    fir_id = input("Enter FIR ID: ")
    officer_id = input("Enter Officer ID: ")

    if not fir_id.isdigit() or not officer_id.isdigit():
        print("Invalid input!")
        return

    # Check FIR exists
    cursor.execute("SELECT * FROM FIR WHERE FIR_ID = %s", (fir_id,))
    if cursor.fetchone() is None:
        print("FIR does not exist!")
        return

    # Check Officer exists
    cursor.execute("SELECT * FROM Officer WHERE Officer_ID = %s", (officer_id,))
    if cursor.fetchone() is None:
        print("Officer does not exist!")
        return

    cursor.execute(
        "INSERT INTO Case_Table (FIR_ID, Officer_ID) VALUES (%s, %s)",
        (fir_id, officer_id)
    )
    conn.commit()

    print("Case assigned successfully!")
    conn.close()


def view_cases():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT C.Case_ID, F.Name, F.Crime_Type, O.Name, C.Status
    FROM Case_Table C
    JOIN FIR F ON C.FIR_ID = F.FIR_ID
    JOIN Officer O ON C.Officer_ID = O.Officer_ID
    """

    cursor.execute(query)
    records = cursor.fetchall()

    print("\n--- Cases ---")
    print("CaseID | Name | Crime | Officer | Status")
    print("--------------------------------------------")

    for r in records:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]}")

    conn.close()


def update_case_status():
    conn = get_connection()
    cursor = conn.cursor()

    case_id = input("Enter Case ID: ")
    status = input("Enter new status: ")

    if not case_id.isdigit():
        print("Invalid Case ID!")
        return

    cursor.execute(
        "UPDATE Case_Table SET Status = %s WHERE Case_ID = %s",
        (status, case_id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        print("Case not found!")
    else:
        print("Case updated successfully!")

    conn.close()