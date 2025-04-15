students = []
def create_students():
    num = int(input("How many students do you want to add? "))
    for _ in range(num):
        name = input("Enter name: ")
        roll = int(input("Enter roll number: "))
        marks = tuple(map(int, input("Enter marks in 3 subjects separated by space: ").split()))
        grade = input("Enter grade: ")
        students.append((name, roll, marks, grade))
    print(f"\n{num} students added successfully.\n")
def display_all_students():
    if not students:
        print("No student records found.\n")
        return
    print("\n--- All Student Records ---")
    for student in students:
        print(f"Name: {student[0]}, Roll No: {student[1]}, Marks: {student[2]}, Grade: {student[3]}")
    print()
def add_new_student():
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = tuple(map(int, input("Enter marks in 3 subjects separated by space: ").split()))
    grade = input("Enter grade: ")
    students.append((name, roll, marks, grade))
    print("Student added successfully.\n")
def search_student():
    roll = int(input("Enter roll number to search: "))
    for student in students:
        if student[1] == roll:
            print(f"Student found: Name: {student[0]}, Marks: {student[2]}, Grade: {student[3]}\n")
            return
    print("Student not found.\n")
def calculate_total_marks():
    print("\n--- Total Marks ---")
    for student in students:
        total = sum(student[2])
        print(f"Name: {student[0]}, Roll No: {student[1]}, Total Marks: {total}")
    print()
def update_grade():
    roll = int(input("Enter roll number to update grade: "))
    for i in range(len(students)):
        if students[i][1] == roll:
            new_grade = input("Enter new grade: ")
            students[i] = (students[i][0], students[i][1], students[i][2], new_grade)
            print("Grade updated successfully.\n")
            return
    print("Student not found.\n")
def remove_student():
    roll = int(input("Enter roll number to remove: "))
    for i in range(len(students)):
        if students[i][1] == roll:
            del students[i]
            print("Student removed successfully.\n")
            return
    print("Student not found.\n")
def menu():
    while True:
        print("----- Student Data Management -----")
        print("1. Create Students")
        print("2. Display All Students")
        print("3. Add New Student")
        print("4. Search Student by Roll Number")
        print("5. Calculate Total Marks")
        print("6. Update Grade")
        print("7. Remove Student")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            create_students()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            add_new_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            calculate_total_marks()
        elif choice == '6':
            update_grade()
        elif choice == '7':
            remove_student()
        elif choice == '8':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.\n")
menu()
