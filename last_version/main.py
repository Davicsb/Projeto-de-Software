import functions as fun

students = {}
courses = {}

while True:
        print("\nWelcome to E-Learning Platform!\nWhat do you wanna do?")
        choose = input("1 - Create, update, and manage online courses\n2 - Manage student enrollments and track their progress\n3 - Interactive learning tools\n4 - Video streaming\n5 - Foruns and chats\n6 - Emit certificate\n7 - Analytics and reporting\n8 - Access control\n9 - Payment and subscription\n10 - Quit\n>>> ")

        if choose == "1":
            fun.clear_terminal()
            fun.option_one(courses)
        elif choose == "2":
            fun.clear_terminal()
            fun.option_two(students)
        elif choose == "3":
            action = input("1 - Add a quiz\n2 - View videos\n")
            if action == "1":
                fun.clear_terminal()
                fun.add_quiz(courses)
            elif action == "2":
                fun.clear_terminal()
                fun.view_quizzes(courses)
        elif choose == "4":
            action = input("1 - Add a video\n2 - View videos\n")
            if action == "1":
                fun.clear_terminal()
                fun.add_video(courses)
            if action == "2":
                fun.clear_terminal()
                fun.view_videos(courses)
        elif choose == "5":
            action = input("1 - Post\n2 - View posts\n")
            if action == "1":
                fun.clear_terminal()
                fun.add_forum_post(courses)
            elif action == "2":
                fun.clear_terminal()
                fun.view_forum(courses)
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