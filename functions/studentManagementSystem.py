students = []

subjects = ["Computer Basics", "Python Programming", "UI/UX"]

def addStudent():
    name = input("Enter the name of the student:")

    studentsMarks = {}
    total = 0

    for subject in subjects:
        markInput = input(f"Enter Subject marks for {subject}: ")
        if markInput.isdigit():
            mark = float(markInput)
            studentsMarks[subject] = mark
            total += mark


        else:
            print("Invalid input! Marks must be numbers. Student not added.")
            return

    average = total/len(subjects)

    studentLists = {
    "Name":name,
    "Marks":studentsMarks,
    "Total":total, 
    "Average":average
    }

    students.append(studentLists)
    print(f"{name} has been added.....")


def displayAllStudents():
    if len(students) == 0:
        print("No students found...")
        return 

    print("--- All students fetched successfully ---")
    for student in students:
        print(f"Name: {student['Name']}")

        print("Marks: ", end = "")
        for subject, mark in student["Marks"].items():
            print(f"{subject}: {mark} ")
            print(f" Total: {student["Total"]:.2f}, Average: {student["Average"]}")
            print("-" * 50)

def highestScoringStudent():
    if len(students):
        print("No students found....")
        return 

        topStudent = [students[0]]
        for student in students:
            if student["Total"] > topStudent["Total"]:
                topStudent = student

    print(f"\n--- Highest Scoring Student ---")
    print(f"Name: {topStudent["Name"]}")
    print(f"Total Marks: {topStudent["Total"]:.2f}")



while True:
    print("\n-------------- Student Management System --------------------")
    print("1. Add Student & Enter Marks")
    print("2. Display All Records")
    print("3. Find Highest Scoring Student")
    print("4. Exit")


    choice = input("Enter the number (1-4) you want to perform:  ")

    if choice == '1':
        addStudent()
    elif choice == '2':
        displayAllStudents()
    elif choice == '3':
        highestScoringStudent()
    elif choice == '4':
        print("Exitinggggggggggg the system !!!!!")
        break
    else:
        print("Invalid choice. Please pick a number from 1 to 4.")
    




    