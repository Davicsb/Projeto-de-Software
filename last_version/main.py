import functions as fun

students = {}
courses = {}

while True:
        fun.clear_terminal()
        print("Welcome to E-Learning Platform!\nWhat do you wanna do?")
        choose = input("1 - Create, update, and manage online courses\n2 - Manage student enrollments and track their progress\n3 - Interactive learning tools\n4 - Video streaming\n5 - Foruns and chats\n6 - Emit certificate\n7 - Analytics and reporting\n8 - Access control\n9 - Payment and subscription\n10 - Quit\n>>> ")

        if choose == "1":
            fun.clear_terminal()
            fun.option_one(courses)
        elif choose == "2":
            fun.clear_terminal()
            fun.option_two(students)
        elif choose == "3":
            fun.clear_terminal()
            fun.add_quiz(courses)
        elif choose == "4":
            fun.clear_terminal()
            fun.add_video(courses)
        elif choose == "5":
            fun.clear_terminal()
            fun.add_forum_post(courses)
        elif choose == "6":
            fun.clear_terminal()
            fun.fill_and_generate_certificate(students)
        elif choose == "7":
            fun.clear_terminal()
            fun.generate_report(students)
        elif choose == "8":
            fun.check_course_access(students)
        elif choose == "9":
            fun.manage_payment(students)
        elif choose == "10":
            print("See you soon!")
            break
        else:
            print("OPS! Invalid option!\n")