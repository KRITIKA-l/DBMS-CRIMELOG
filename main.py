from fir import add_fir, view_fir, delete_fir
from officer import add_officer, view_officers
from case import assign_case, view_cases, update_case_status
from db import get_connection

# ===== UI HELPERS =====
def print_header(title):
    print("\n" + "=" * 50)
    print(f"{title.center(50)}")
    print("=" * 50)

def print_menu():
    print_header("Crime Record Management System")
    print("1.  Add FIR")
    print("2.  View FIR")
    print("3.  Delete FIR")
    print("4.  Add Officer")
    print("5.  View Officers")
    print("6.  Assign Case")
    print("7.  View Cases")
    print("8.  Update Case Status")
    print("9.  View Audit Logs")
    print("10. Exit")
    print("-" * 50)


def view_audit_logs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Audit_Log")
    records = cursor.fetchall()

    print_header("Audit Logs")

    print(f"{'LogID':<6} {'Action':<10} {'Table':<15} {'RecordID':<10} {'Timestamp'}")
    print("-" * 50)

    for r in records:
        print(f"{r[0]:<6} {r[1]:<10} {r[2]:<15} {r[3]:<10} {r[4]}")

    if not records:
        print("No logs available.")

    conn.close()


# ===== MAIN LOOP =====
while True:
    print_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        print_header("Add FIR")
        add_fir()

    elif choice == "2":
        print_header("View FIR")
        view_fir()

    elif choice == "3":
        print_header("Delete FIR")
        delete_fir()

    elif choice == "4":
        print_header("Add Officer")
        add_officer()

    elif choice == "5":
        print_header("View Officers")
        view_officers()

    elif choice == "6":
        print_header("Assign Case")
        assign_case()

    elif choice == "7":
        print_header("View Cases")
        view_cases()

    elif choice == "8":
        print_header("Update Case Status")
        update_case_status()

    elif choice == "9":
        view_audit_logs()

    elif choice == "10":
        print("\nExiting system... Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")