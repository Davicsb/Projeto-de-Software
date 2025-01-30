import os
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from datetime import datetime
from reportlab.lib import colors

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
        progress = input("Enter the student's progress (0-100%): ")
        id = input("Enter the student's id: ")
        dictionary[name] = {"age": age, "course": course, "level": level, "progress": progress, "id" : id}
        clear_terminal()
        print(f"{name} has been successfully registered")

def track_student(dictionary):
    name = input("Enter the student's name: ")
    if name in dictionary:
        progress = dictionary[name]["progress"]
        clear_terminal()
        print(f"Current progress: {progress}%\n")  # Mostra o progresso do aluno
    else:
        clear_terminal()
        print("Student not found!\n")

def add_quiz(dictionary):
    course = input("Enter the course for the quiz: ")
    if course in dictionary:
        question = input("Enter the quiz question: ")
        answer = input("Enter the correct answer: ")
        if "quizzes" not in dictionary[course]:
            dictionary[course]["quizzes"] = []
        dictionary[course]["quizzes"].append({"question": question, "answer": answer})
        clear_terminal()
        print("Quiz added successfully!")
    else:
        clear_terminal()
        print("Course not found!\n")

def view_quizzes(dictionary):
    course = input("Enter the course for the quizzes: ")
    if course in dictionary:
        if "quizzes" in dictionary[course] and dictionary[course]["quizzes"]:
            print("\Quizzes:")
            for i, quizzes in enumerate(dictionary[course]["quizzes"], start=1):
                print(f"{i}. {quizzes}")
        else:
            print("\nNo quizzes available for this course.")
    else:
        clear_terminal()
        print("Course not found!\n")

def add_video(dictionary):
    course = input("Enter the course for the video: ")
    if course in dictionary:
        video_link = input("Enter the video URL: ")
        if "videos" not in dictionary[course]:
            dictionary[course]["videos"] = []
        dictionary[course]["videos"].append(video_link)
        clear_terminal()
        print("Video added successfully!")
    else:
        clear_terminal()
        print("Course not found!\n")

def view_videos(dictionary):
    course = input("Enter the course for the video: ")
    if course in dictionary:
        if "videos" in dictionary[course] and dictionary[course]["videos"]:
            print("\nVideos posts:")
            for i, videos in enumerate(dictionary[course]["videos"], start=1):
                print(f"{i}. {videos}")
        else:
            print("\nNo videos available for this course.")
    else:
        clear_terminal()
        print("Course not found!\n")

def add_forum_post(dictionary):
    course = input("Enter the course for the forum: ")
    if course in dictionary:
        post = input("Enter your forum post: ")
        if "forum" not in dictionary[course]:
            dictionary[course]["forum"] = []
        dictionary[course]["forum"].append(post)
        clear_terminal()
        print("Post added to the forum!")
    else:
        clear_terminal()
        print("Course not found!\n")

def view_forum(dictionary):
    course = input("Enter the course to view forum posts: ")
    if course in dictionary:
        if "forum" in dictionary[course] and dictionary[course]["forum"]:
            print("\nForum posts:")
            for i, post in enumerate(dictionary[course]["forum"], start=1):
                print(f"{i}. {post}")
        else:
            print("\nNo posts available for this course.")
    else:
        print("\nCourse not found!")


def generate_report(dictionary):
    for name, info in dictionary.items():
        print(f"Student: {name}, Progress: {info.get('progress', 'N/A')}%")

def check_course_access(dictionary):
    name = input("Enter the student's name that you wanna acess: ")
    course = input("Enter the course that you wanna check: ")
    if name in dictionary:
        if course in dictionary[name]["course"]:
            print("Access granted")
        else:
            print("Access denied")
    else:
        print("Student not found!")

def manage_payment(dictionary):
    name = input("Enter the student's name: ")
    if name in dictionary:
        paid = input("Has the student paid? (yes/no): ")
        dictionary[name]["paid"] = paid
        clear_terminal()
        print(f"Payment status for {name}: {paid}")
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

def fill_and_generate_certificate(dictionary):
    # Solicita o nome do aluno
    name = input("Enter the student's name: ")

    # Criação do PDF
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)

    # Coletando a data atual
    date = datetime.now().strftime("%B %d, %Y")

    # Definindo um fundo para o certificado
    c.setFillColor(colors.lightgrey)
    c.rect(30, 550, 550, 250, fill=1)  # Caixa de fundo
    c.setFillColor(colors.black)
    c.rect(30, 550, 550, 250, fill=0)  # Borda

    # Cabeçalho do certificado
    c.setFont("Helvetica-Bold", 20)
    c.drawString(180, 800, "Certificate of Completion")

    # Nome do estudante - Maior destaque
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 740, f"Student: {name}")

    # Nome do curso
    course_name = dictionary[name]["course"]
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 710, f"Course: {course_name}")

    # ID do estudante
    student_id = dictionary[name]["id"]
    c.setFont("Helvetica", 12)
    c.drawString(100, 680, f"Student ID: {student_id}")

    # Data de emissão
    c.setFont("Helvetica", 12)
    c.drawString(100, 650, f"Date: {date}")

    # Linha de assinatura
    c.line(100, 600, 500, 600)
    c.setFont("Helvetica-Oblique", 12)
    c.drawString(100, 590, "Instructor's Signature")

    # Salvando o conteúdo gerado
    c.save()

    # Movendo o buffer para o início
    packet.seek(0)

    # Criando o PDF com os dados preenchidos
    output_pdf = PyPDF2.PdfWriter()

    # Carregando a página gerada
    new_pdf = PyPDF2.PdfReader(packet)
    page = new_pdf.pages[0]

    # Adicionando a página ao arquivo final
    output_pdf.add_page(page)

    # Definindo o nome do arquivo de saída
    output_filename = f"{name}_certificate_filled.pdf"

    # Salvando o PDF gerado
    with open(output_filename, "wb") as output_file:
        output_pdf.write(output_file)

    return output_filename