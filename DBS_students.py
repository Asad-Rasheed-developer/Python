def manage_student_database():
    student_list = []
    id_counter = 1

    while True:
        print("\nStudent Database Menu:")
        print("1. Add new students")
        print("2. Display all students")
        print("3. Search for a student")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add multiple students in one go
            while True:
                name = input("Please enter the student's name (or type 'done' to stop adding): ").strip()
                name = name.replace(",", "")  # remove commas

                if name.lower() == 'done':
                    break

                if name == "":
                    print("Name cannot be empty. Please enter a valid name.")
                    continue

                for student in student_list:
                    if student[1].lower() == name.lower():
                        print("This name is already in the list.")
                        break
                else:
                    student_list.append((id_counter, name))
                    id_counter += 1
                    print(f"Student '{name}' added successfully.")

        elif choice == "2":
            if not student_list:
                print("No students in the database.")
            else:
                print("\nComplete List of Students (Tuples):")
                print(student_list)

                print("\nList of Students with IDs:")
                for student in student_list:
                    print(f"ID: {student[0]}, Name: {student[1]}")

                print(f"\nTotal number of students: {len(student_list)}")
                total_name_length = sum(len(student[1]) for student in student_list)
                print(f"Total length of all student names combined: {total_name_length}")

                longest_name = max(student_list, key=lambda x: len(x[1]))
                shortest_name = min(student_list, key=lambda x: len(x[1]))
                print(f"The student with the longest name is: {longest_name[1]}")
                print(f"The student with the shortest name is: {shortest_name[1]}")

        elif choice == "3":
            search_name = input("Enter the name to search: ").strip()
            search_name = search_name.replace(",", "")  # remove commas

            found = False
            for student in student_list:
                if student[1].lower() == search_name.lower():
                    print(f"ID: {student[0]}, Name: {student[1]}")
                    found = True
                    break

            if not found:
                print("Student not found.")

        elif choice == "4":
            delete_name = input("Enter the name to delete: ").strip()
            delete_name = delete_name.replace(",", "")  # remove commas

            found = False
            for student in student_list:
                if student[1].lower() == delete_name.lower():
                    student_list.remove(student)
                    print("Student deleted.")
                    found = True
                    break

            if not found:
                print("Student not found.")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

manage_student_database()
