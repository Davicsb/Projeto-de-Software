import functions as fun

students = {}
courses = {}

while True:
        fun.clear_terminal()
        print("Welcome to E-Learning Platform!\nWhat do you wanna do?")
        choose = input("1 - Create, update, and manage online courses\n2 - Manage student enrollments and track their progress\n3 - Quit\n>>> ")

        if choose == "1":
            fun.clear_terminal()
            fun.option_one(courses)
        elif choose == "2":
            fun.clear_terminal()
            fun.option_two(students)
        elif choose == "3":
            print("See you soon!")
            break
        else:
            print("OPS! Invalid option!\n")