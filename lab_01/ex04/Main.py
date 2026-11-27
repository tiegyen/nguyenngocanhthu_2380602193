from StudentManagement import StudentManagement

management = StudentManagement()

while (1 == 1):
    print("\nStudent Management System")
    print("1. Add student")
    print("2. Update student by ID")
    print("3. Delete student by ID")
    print("4. Find student by name")
    print("5. Sort students by average score")
    print("6. Sort students by major")
    print("7. Display student list")
    print("0. Exit")
    
    key = int(input("Enter your choice: "))
    if (key == 1):
        print("\nAdd student")
        management.inputStudent()
        print("\nStudent added successfully!")
    elif (key == 2):
        if (management.amountOfStudent() > 0):
            print("\nUpdate student by ID")
            studentId = int(input("Enter student ID to update: "))
            management.updateStudent(studentId)
        else:
            print("\nNo students available to update.")
    elif (key == 3):
        if (management.amountOfStudent() > 0):
            print("\nDelete student by ID")
            studentId = int(input("Enter student ID to delete: "))
            management.deleteByID(studentId)
        else:
            print("\nNo students available to delete.")
    elif (key == 4):
        if (management.amountOfStudent() > 0):
            print("\nFind student by name")
            name = input("Enter student name to find: ")
            found_students = management.findByName(name)
            if (len(found_students) > 0):
                print("\nFound students:")
                for st in found_students:
                    print(st)
            else:
                print("\nNo student found with name:", name)
        else:
            print("\nNo students available to find.")
    elif (key == 5):
        if (management.amountOfStudent() > 0):
            print("\nSort students by average score")
            management.sortByAverageScore()
            print("\nStudents sorted by average score:")
            management.displayStudent(management.getListStudent())
        else:
            print("\nNo students available to sort.")
    elif (key == 6):
        if (management.amountOfStudent() > 0):
            print("\nSort students by major")
            management.sortByMajor()
            print("\nStudents sorted by major:")
            management.displayStudent(management.getListStudent())
        else:
            print("\nNo students available to sort.")
    elif (key == 7):
        if (management.amountOfStudent() > 0):
            print("\nDisplay student list")
            management.displayStudent(management.getListStudent())
        else:
            print("\nNo students available to display.")
    elif (key == 0):
        print("\nExiting the program.")
        break
    else:
        print("\nInvalid choice. Please try again.")