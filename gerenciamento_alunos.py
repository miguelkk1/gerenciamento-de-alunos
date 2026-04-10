from time import sleep
alunos = [
    {'nome': 'José', 'nota': 9},
    {'nome': 'Ana', 'nota': 7},
    {'nome': 'Carlos', 'nota': 5},
    {'nome': 'Maria', 'nota': 10}
]
def ver_alunos(alunos):
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | Nota: {aluno['nota']}") # "alunos" é uma lista de dicionários, então percorremos cada aluno
        # e acessamos os dados com aluno['nome'] e aluno['nota'].
def add_alunos(alunos):
    try:
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        novo_aluno = {'nome': nome, 'nota': nota}
        alunos.append(novo_aluno)
        print("Aluno adicionado com sucesso!")
    except ValueError:
        print("Erro: digite uma nota válida.")
def ver_alunos_reprov(alunos):
    for aluno in alunos:
        if aluno['nota'] >= 7:
            status = 'Aprovado'
        else:
            status = 'Reprovado'
        print(f"Nome: {aluno['nome']} | Nota: {aluno['nota']} | Status: {status}")
while True:
    print('=' * 55)
    print('''
                GERENCIAMENTO DE ALUNOS
    1 - Ver lista de alunos
    2 - Adicionar alunos
    3 - Ver alunos aprovados/reprovados
    4 - Sair
    ''')
    print('=' * 55)
    opcoes_menu = int(input('Olá! O que você quer fazer hoje? [1 a 4]: '))
    print('Carregando...')
    sleep(1.5)
    if opcoes_menu == 1:
        ver_alunos(alunos)
    elif opcoes_menu == 2:
        add_alunos(alunos)
    elif opcoes_menu == 3:
        ver_alunos_reprov(alunos)
    elif opcoes_menu == 4:
        break
print('Saindo...')