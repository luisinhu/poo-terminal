from funcoes import *
from classes import *
import os

limpar_terminal()
print('Seja bem-vindo ao nosso sistema\nEscolha uma das opções abaixo')

login_ou_cadastro = int(input('[1] - Login\n[2] - Cadastro\n'))
limpar_terminal()
while login_ou_cadastro != 1 and login_ou_cadastro != 2:
    limpar_terminal()
    print('Você digitou algo incorretamente')
    login_ou_cadastro = int(input('[1] - Login\n[2] - Cadastro\n'))

if login_ou_cadastro == 1:  # LOGIN
    print('Você irá Logar como?')
    aluno_ou_prof = int(input('[1] - Aluno\n[2] - Professor\n'))

    while aluno_ou_prof != 1 and aluno_ou_prof != 2:
        limpar_terminal()
        print('Você digitou algo incorretamente')
        aluno_ou_prof = int(input('[1] - Aluno\n[2] - Professor'))

    if aluno_ou_prof == 1:  # LOGIN -> ALUNO
        limpar_terminal()
        print('Insira seus dados')
        input_mat_login_aluno = int(input('Matrícula: '))
        input_senha_login_aluno = input('Senha: ')
        login(input_mat_login_aluno, input_senha_login_aluno, aluno_ou_prof)

    if aluno_ou_prof == 2:  # LOGIN -> PROFESSOR
        limpar_terminal()
        print('Insira seus dados')
        input_mat_login_prof = int(input('Matrícula: '))
        input_senha_login_prof = input('Senha: ')
        login(input_mat_login_prof, input_senha_login_prof, aluno_ou_prof)

elif login_ou_cadastro == 2:  # CADASTRO
    aluno_ou_prof = int(input('[1] - Aluno\n[2] - Professor'))
    if aluno_ou_prof == 1:
        limpar_terminal()
        print("Bem-vindo(a)")
        nome_aluno = input("Digite seu nome: ")
        sexo_aluno = input("Digite seu sexo: ")
        matricula_aluno = int(input("Digite sua matrícula: "))
        senha_aluno = input("Digite sua senha: ")

        # Dicionário de turmas
        turmas = {
            1: '1 INFO A',
            2: '1 INFO B',
            3: '1 ELET A',
            4: '1 ELET B',
            5: '1 EDIF A',
            6: '1 EDIF B',
            7: '1 QUIM A',
            8: '1 QUIM B',
            9: ' 2 INFO M',
            10: '2 INFO V',
            11: '2 ELET M',
            12: '2 ELET V',
            13: '2 EDIF M',
            14: '2 EDIF V',
            15: '2 QUIM M',
            16: '2 QUIM V',
            17: '3 INFO M',
            18: '3 INFO V',
            19: '3 ELET M',
            20: '3 ELET V',
            21: '3 EDIF M',
            22: '3 EDIF V',
            23: '3 QUIM M',
            24: '3 QUIM V',
        }
        print("Turmas disponíveis:")
        for key, value in turmas.items():
            print(f"{key} - {value}")

        num_turma_aluno = int(input("Escolha o número da turma desejada: "))
        if num_turma_aluno in turmas:
            turma_aluno = turmas[num_turma_aluno]
            cadastrar_aluno(nome_aluno, sexo_aluno, matricula_aluno, senha_aluno, turma_aluno)
        else:
            print("Turma não encontrada. O aluno não foi cadastrado.")
        
    else:
        limpar_terminal()
        print("Bem-vindo(a)")
        nome_prof = input("Digite seu nome: ")
        sexo_prof = input("Digite seu sexo: ")
        matricula_prof = int(input("Digite sua matrícula: "))
        senha_prof = input("Digite sua senha: ")
        cadastrar_professor(nome_prof, sexo_prof, matricula_prof, senha_prof)
