from db import get_connection

def add_fir():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter Name: ")
    crime = input("Enter Crime Type: ")
    location = input("Enter Location: ")

    if not name.strip() or not crime.strip():
        print("Invalid input!")
        return

    query = "INSERT INTO FIR (Name, Crime_Type, Location) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, crime, location))
    conn.commit()

    print("FIR added successfully!")
    conn.close()

def view_fir():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM FIR")
    records = cursor.fetchall()

    print("\n--- FIR Records ---")
    print("ID | Name | Crime | Location | Status")
    print("--------------------------------------")

    for r in records:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]}")

    conn.close()


def delete_fir():
    conn = get_connection()
    cursor = conn.cursor()

    fir_id = input("Enter FIR ID to delete: ")

    if not fir_id.isdigit():
        print("Invalid ID!")
        return

    cursor.execute("DELETE FROM FIR WHERE FIR_ID = %s", (fir_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("FIR not found!")
    else:
        print("FIR deleted successfully!")

    conn.close()