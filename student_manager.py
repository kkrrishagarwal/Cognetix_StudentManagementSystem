import csv
import os

CSV_FILE = "students.csv"
FIELDNAMES = ["id", "name", "course", "email"]

def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

def load_students():
    initialize_csv()
    students = []
    try:
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except IOError as e:
        print(f"❌ Error reading CSV file: {e}")
    return students

def save_students(students):
    try:
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(students)
    except IOError as e:
        print(f"❌ Error writing to CSV file: {e}")

def add_student():
    students = load_students()
    student_id = input("Enter Student ID (numeric): ").strip()
    if not student_id.isdigit():
        print("❌ Error: Student ID must be numeric.")
        return
    if any(s["id"] == student_id for s in students):
        print(f"❌ Error: Student ID '{student_id}' already exists.")
        return

    name = input("Enter Student Name: ").strip()
    if not name:
        print("❌ Error: Student Name cannot be empty.")
        return

    course = input("Enter Course (e.g., BCA, B.Tech, CS): ").strip()
    if not course:
        print("❌ Error: Course cannot be empty.")
        return

    email = input("Enter Email Address: ").strip()
    if "@" not in email or "." not in email:
        print("❌ Error: Please enter a valid email address containing '@'.")
        return

    students.append({
        "id": student_id,
        "name": name,
        "course": course,
        "email": email
    })
    save_students(students)
    print(f"✅ Student '{name}' (ID: {student_id}) added successfully!")

def search_student():
    students = load_students()
    student_id = input("Enter Student ID to search: ").strip()
    for s in students:
        if s["id"] == student_id:
            print("\n🔍 Student Found:")
            print(f"   ID     : {s['id']}")
            print(f"   Name   : {s['name']}")
            print(f"   Course : {s['course']}")
            print(f"   Email  : {s['email']}")
            return
    print(f"❌ No student found with ID '{student_id}'.")

def delete_student():
    students = load_students()
    student_id = input("Enter Student ID to delete: ").strip()
    updated_students = [s for s in students if s["id"] != student_id]
    if len(updated_students) == len(students):
        print(f"❌ No student found with ID '{student_id}'.")
        return
    save_students(updated_students)
    print(f"✅ Student with ID '{student_id}' deleted successfully!")

def view_all_students():
    students = load_students()
    if not students:
        print("📂 No student records found.")
        return
    print("\n" + "=" * 74)
    print(f"{'ID':<8} | {'Name':<20} | {'Course':<10} | {'Email':<28}")
    print("-" * 74)
    for s in students:
        print(f"{s['id']:<8} | {s['name']:<20} | {s['course']:<10} | {s['email']:<28}")
    print("=" * 74)

def main():
    initialize_csv()
    while True:
        print("\n==========================================")
        print("   STUDENT MANAGEMENT SYSTEM (CSV-CLI)    ")
        print("==========================================")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")
        print("------------------------------------------")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("❌ Invalid option! Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
