from db import get_connection

def add_officer():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter Officer Name: ")
    rank = input("Enter Officer Rank: ")

    if not name.strip():
        print("Invalid input!")
        return

    cursor.execute("INSERT INTO Officer (Name, Officer_Rank) VALUES (%s, %s)", (name, rank))
    conn.commit()

    print("Officer added successfully!")
    conn.close()


def view_officers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Officer")
    records = cursor.fetchall()

    print("\n--- Officers ---")
    print("ID | Name | Rank")
    print("----------------------")

    for r in records:
        print(f"{r[0]} | {r[1]} | {r[2]}")

    conn.close()