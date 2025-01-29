cursos = ["Phyton básico", "Java básico", "Cálculo 1"]
alunos = ["Davi", "Tenório", "Humberto"]

while True:
    print("O que deseja fazer?\n")
    num = int(input("1 - Criar, atualizar e gerenciar cursos.\n2 - Ver e gerenciar estudantes.\n3 - Sair\n"))

    if num == 1:
        choose = int(input("1 - Criar\n2 - Atualizar nome\n3 - Ver e gerenciar cursos.\n"))

        if choose == 1:
            name = input("Qual o nome do curso: ")
            cursos.append(name)
            print(f"{name} foi criado com sucesso!\n")

        elif choose == 2:
            name = input("Qual o nome do curso que deseja atualizar: ")
            if name in cursos:
                newname = input("Qual o novo nome: ")
                index = cursos.index(name)
                cursos[index] = newname
                print(f"{name} foi atualizado para {newname} com sucesso!\n")
            else:
                print("Curso não encontrado!\n")

        elif choose == 3:
            print(f"Todos os cursos: {cursos}\n")
            name = input("Qual o nome do curso que deseja gerenciar: ")

            if name in cursos:
                print("O que deseja fazer?\n")
                acao = int(input("1 - Deletar\n2 - Privar curso\n"))

                if acao == 1:
                    cursos.remove(name)
                    print(f"O curso {name} foi deletado com sucesso!\n")
                elif acao == 2:
                    print(f"O curso {name} foi privado com sucesso!\n")
                else:
                    print("Opção inválida!\n")
            else:
                print(f"O curso {name} não foi encontrado!\n")

    elif num == 2:
        choose = int(input("1 - Adicionar estudante\n2 - Deletar estudante\n"))

        if choose == 1:
            name = input("Digite o nome do estudante: ")
            idade = input("Digite a idade do estudante: ")
            curso = input("Digite o curso do estudante: ")
            
            if curso in cursos:
                alunos.append(name)
                print(f"O aluno {name} foi adicionado com sucesso! Idade: {idade}, Curso: {curso}!\n")
            else:
                print("Curso não encontrado!\n")

        elif choose == 2:
            print(f"Lista de estudantes: {alunos}\n")
            name = input("Digite o nome do estudante que deseja deletar: ")

            if name in alunos:
                alunos.remove(name)
                print(f"O aluno {name} foi deletado com sucesso!\n")
            else:
                print("Aluno não encontrado!\n")

    elif num == 3:
        print("Saindo...")
        break

    else:
        print("Opção inválida, tente novamente.")
