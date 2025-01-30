import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
  
def option_one(dictionary):
    while True:
        print("What do you wanna do?")
        choose = input("1 - Create a course\n2 - Update a course\n3 - Manage a course\n4 - Back\n>>> ")

        if choose == "1":
            add_courses(dictionary)

        elif choose == "2":
            action = input("1 - Update title\n2 - Update difficulty\n>>> ")
            if action == "1":
                update_title(dictionary)
            elif action == "2":
                update_difficulty(dictionary)
            else:
                clear_terminal()
                print("OPS! Invalid option!\n")

        elif choose == "3":
            action = input("1 - List of courses\n2 - Delete a course\n>>> ")
            if action == "1":
                if dictionary == {}:
                    clear_terminal()
                    print("Lista vazia!")
                else:
                    clear_terminal()
                    for title, info in dictionary.items():
                        print(f"Title: {title}, Difficulty: {info['difficulty']}")
            elif action == "2":
                delete_course(dictionary)
            else:
                clear_terminal()
                print("OPS! Invalid option!\n")

        elif choose == "4":
            clear_terminal()
            return
        else:
            clear_terminal()
            print("OPS! Invalid option!\n")

def option_two(dictionary):
    while True:
        print("What do you wanna do?")
        choose = input("1 - Manage a student\n2 - Track the progress of a student\n3 - Back\n>>> ")

        if choose == "1":
            action = input("1 - Register a student\n2 - Update a student\n3 - List of students\n>>> ")
            if action == "1":
                add_students(dictionary)
            elif action == "2":
                update_student(dictionary)
            elif action == "3":
                if dictionary == {}:
                    clear_terminal()
                    print("Lista vazia!")
                else:
                    clear_terminal()
                    for name, info in dictionary.items():
                        print(f"Name: {name}, ")
            else:
                clear_terminal()
                print("OPS! Invalid option!\n")

        elif choose == "2":
            track_student(dictionary)

        elif choose == "3":
            clear_terminal()
            return

        else:
            clear_terminal()
            print("OPS! Invalid option!\n")

def add_courses(dictionary):
    title = input("Enter the course title: ")
    if title in dictionary:
        clear_terminal()
        print("This course is already registered!\n")
    else:
        difficulty = input("Enter the course difficulty: ")
        dictionary[title] = {"difficulty": difficulty}
        clear_terminal()
        print(f"{title} has been successfully registered")

def delete_course(dictionary):
    title = input("Enter the title of the course that you want to delete: ")
    if title in dictionary:
        dictionary.pop(title)
        clear_terminal()
        print(f"Course '{title}' deleted successfully!\n")
    else:
        clear_terminal()
        print("Course not found!\n")

def update_title(dictionary):
    title = input("Enter the course title you want to update: ")
    if title in dictionary:
        new_title = input("Enter the new title: ")
        dictionary[new_title] = dictionary.pop(title)
        clear_terminal()
        print(f"'{title}' has been updated to '{new_title}' successfully!\n")
    else:
        clear_terminal()
        print("Course not found!\n")

def update_difficulty(dictionary):
    title = input("Enter the course title you want to update: ")
    if title in dictionary:
        new_difficulty = input("Enter the new difficulty: ")
        dictionary[title]["difficulty"] = new_difficulty
        clear_terminal()
        print(f"'{title}' difficulty has been updated successfully!\n")
    else:
        clear_terminal()
        print("Course not found!\n")

def add_students(dictionary):
    name = input("Enter the student's name: ")
    if name in dictionary:
        clear_terminal()
        print("This student is already registered!\n")
    else:
        age = input("Enter the student's age: ")
        course = input("Enter the student's course: ")
        level = input("Enter the student's level: ")
        dictionary[name] = {"age": age, "course": course, "level": level}
        clear_terminal()
        print(f"{name} has been successfully registered")

def track_student(dictionary):
    name = input("Enter the student's name: ")
    if name in dictionary:
        level = dictionary[name]["level"]
        clear_terminal()
        print(f"Current level: {level}\n")
    else:
        clear_terminal()
        print("Student not found!\n")

def update_student(dictionary):
    name = input("Enter the student's name: ")
    if name in dictionary:
        choose = input("What do you wanna update?\n1 - Name\n2 - Age\n3 - Course\n4 - Level\n>>> ")

        if choose == "1":
            new_name = input("Enter the student's new name: ")
            dictionary[new_name] = dictionary.pop(name)
            clear_terminal()
            print(f"The student '{name}' has been updated to '{new_name}'!")

        elif choose == "2":
            new_age = input("Enter the student's new age: ")
            dictionary[name]["age"] = new_age
            clear_terminal()
            print(f"The student '{name}' has been updated!")

        elif choose == "3":
            new_course = input("Enter the student's new course: ")
            dictionary[name]["course"] = new_course
            clear_terminal()
            print(f"The student '{name}' has been updated!")

        elif choose == "4":
            new_level = input("Enter the student's new level: ")
            dictionary[name]["level"] = new_level
            clear_terminal()
            print(f"The student '{name}' has been updated!")

        else:
            clear_terminal()
            print("OPS! Invalid option!\n")
    else:
        clear_terminal()
        print("Student not found!\n")
