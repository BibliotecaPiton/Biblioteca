#!/usr/bin/env python
# -- coding: utf-8 --

from datetime import datetime
from datetime import date
import os.path
import re

print('''PROJETO SISTEMA DE BIBLIOTECA ------- PAULO E JAMERSON -------- INÍCIO'''.center(88))

print()

usuario1 = {}
livros = {}
emp = {}
devolvidos = {}
bloq = {}
maisEmp = {}

def enviaEmail(cpf, npatrimonio, dia, mes, ano):

    # !/usr/bin/env python
    # -- coding: utf-8 --

    # Script criado por @kmiokande
    import smtplib

    # Informe suas credenciais abaixo.
    remetente = "emaildabiblioteca123@gmail.com"
    senha = "biblioteca123"

    # Destinatario e informações da mensagem.
    destinatario = usuario1[cpf][3]
    assunto = 'Confirmação de Emprestimos.'
    texto = "Olá, prezado(a) "+usuario1[cpf][0]+" foi realizado o empréstimo do livro: "+livros[npatrimonio][0]+"\nNeste dia "+str(dia)+"/"+str(mes)+"/"+str(ano)+".\nA data de entrega é no dia "+validaTempoEstimado()

    # Preparando a mensagem
    msg = '\r\n'.join([
        'From: %s' % remetente,
        'To: %s' % destinatario,
        'Subject: %s' % assunto,
        '',
        '%s' % texto
    ])

    # Enviando o email SMTP esta configurado para o remetete usar Gmail.
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(remetente, senha)
    server.sendmail(remetente, destinatario, msg.encode('utf-8'))
    server.quit()

def validaTempoEstimado():
	hj = date.today()
	return str(date.fromordinal(hj.toordinal()+12))

def recuperar_usuario():
    with open('usuarios.txt', 'r+') as Arquivo:
        for k in Arquivo:
            read = k.split('|')
            read.pop(len(read) - 1)
            usuario1[read[2]] = read[:]

def grava_usuario():
    conteudo = ''
    with open('usuarios.txt', 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in usuario1:
            for k in range(len(usuario1[i])):
                conteudo += str(usuario1[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()

def recuperar_livros():
    try:
        with open('livros.txt', 'r+') as Arquivo:
            for k in Arquivo:
                read = k.split('|')
                read.pop(len(read) - 1)
                livros[read[3]] = read[:]
    except:
        print()
def gravar_livros():

        conteudo = ''
        with open('livros.txt', 'a+') as arquivo:
            arquivo.seek(0)
            arquivo.truncate()
            for i in livros:
                for k in range(len(livros[i])):
                    conteudo += str(livros[i][k]) + '|'
                conteudo += '\n'
            arquivo.writelines(conteudo)
        arquivo.close()
def recuperar_emprestimos():
        with open('emprestimos.txt', 'r+') as Arquivo:
            for k in Arquivo:
                read = k.split('|')
                read.pop(len(read) - 1)
                emp[read[4]] = read[:]
def gravar_emprestimos():
    conteudo = ''
    try:
        with open('emprestimos.txt', 'a+') as arquivo:
            arquivo.seek(0)
            arquivo.truncate()
            for i in emp:
                for k in range(len(emp[i])):
                    conteudo += str(emp[i][k]) + '|'
                conteudo += '\n'
            arquivo.writelines(conteudo)
        arquivo.close()
    except:
        print()
def recuperar_devolvidos():
    try:
        with open('devolvidos.txt', 'r+') as Arquivo:
            for k in Arquivo:
                read = k.split('|')
                read.pop(len(read) - 1)
                devolvidos[read[3]] = read[:]
    except:
        print()
def gravar_devolvidos():
    conteudo = ''
    with open('devolvidos.txt', 'a+') as arquivo:
        arquivo.seek(0)
        arquivo.truncate()
        for i in livros:
            for k in range(len(devolvidos[i])):
                conteudo += str(devolvidos[i][k]) + '|'
            conteudo += '\n'
        arquivo.writelines(conteudo)
    arquivo.close()

def validanome(nome):
    if re.match("[^0-9][A-Za-z-ãõçóéúáí ]{3,}", nome):
        return True
    else:
        return False

def apagar():
    print("\n"*20)

def valida_cpf(cpf):
    if len(cpf) != 11:
        return False
    else:
        if not cpf.isdigit():
            return False
        cpf = list(cpf)
        for a in range(len(cpf)):
            cpf[a] = int(cpf[a])
        mult = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        mult2 = [11] + mult
        soma = 0
        soma2 = 0
        for a in range(len(mult)):
            soma += cpf[a] * mult[a]
        d1 = 11 - (soma % 11)
        if d1 == 10 or d1 == 11:
            d1 = 0
        cpf.append(d1)
        for a in range(len(mult2)):
            soma2 += cpf[a] * mult2[a]
        d2 = 11 - (soma2 % 11)
        if d2 == 10 or d2 == 11:
            d2 = 0
        cpf.append(d2)
        return bool(d1 == cpf[9] and d2 == cpf[10])

def validaEmail(email):
    if len(email) > 11 and (email.find("@") != -1) and (email.find(".") != -1):
        return True
    else:
        return False

def validaTelefone(telefone):
    if not telefone.isdigit():
        return False
    telefone = list(telefone)
    if len(telefone) == 11 or len(telefone) == 9 or len(telefone) == 8:
        return True
    else:
        return False

def cadastraUsuario():
    nome = input("Digite o nome completo: ")
    while not validanome(nome):
        print('digite apenas letras')
        nome = input('Digite o nome completo  ')
    telefone = input("Digite seu telefone. Ex: 99998888 ou 999998888 ou 00999998888: ")
    while not validaTelefone(telefone):
        print()
        print('erro')
        print()
        print('digite novamente')
        print()
        telefone = input("Digite seu telefone: ")
    cpf = input("Digite seu CPF: Ex: 12312312300: ")
    while not valida_cpf(cpf):
        print('Erro')
        cpf = input("Digite seu cpf: ")
    email = input('digite seu email: Ex: seuemail@servidor.com ')
    while not validaEmail(email):
        print('Erro')
        print('Digite novamente !')
        email = input("Digite o email : ")
    cidade = input("Digite sua cidade: ")
    while not validanome(cidade):
        print('Digite apenas letras: ')
        cidade = input('Digite sua cidade: ')
    usuario1[cpf] = [nome, telefone, cpf, email, cidade]
    grava_usuario()
    print("USUÁRIO CADASTRADO!")
    print(usuario1)

def atualizaUsuario():
    cpf = input('Digite o CPF do usuario a atualizar: ')
    while not valida_cpf(cpf):
        print('Erro')
        cpf = input("Digite seu cpf: ")
    print(usuario1)
    if cpf in usuario1:
        print('O que deseja atualizar?')
        print()
        print('1 - Telefone: ')
        print('2 - Email: ')
        print('3 - Cidade: ')
        opcao1 = input('Qual sua opção ? ')
        if opcao1 == '1':
            novtelefone = input('Digite o novo telefone: ')
            if validaTelefone(novtelefone):
                usuario1[cpf][1] = novtelefone
                print('Telefone atualizado com sucesso')
            else:
                print("Número inválido!")
                print()
        elif opcao1 == '2':
            novoemail = input('Digite o novo email: ')
            if validaEmail(novoemail):
                usuario1[cpf][3] = novoemail
                print('Email atualizado com sucesso!')
            else:
                print("Email inválido!")
        elif opcao1 == '3':
            novacid = input('Digite uma nova cidade:')
            usuario1[cpf][4] = novacid
            grava_usuario()
            print('Cidade atualizada com sucesso!')
    else:
        print('Usuario não existe.')

def apagaUsuario():
    apagarusuario = input('Digite o CPF do usuário deseja apagar? ')
    if apagarusuario in usuario1:
        del usuario1[apagarusuario]
        print(apagarusuario, 'foi apagado com sucesso!')
        grava_usuario()
    else:
        print('Usuario não encontrado.')

def recuperaUsuario():
    cpf = input('Digite o usuario a procurar: ')
    while not valida_cpf(cpf):
        print('Erro')
        cpf = input("Digite seu cpf: ")
    if cpf in usuario1:
        print("Nome: ", usuario1[cpf][0])
        print('Fone: ', usuario1[cpf][1])
        print('CPF: ', usuario1[cpf][2])
        print('E-mail: ', usuario1[cpf][3])
        print('Cidade: ', usuario1[cpf][4])
    else:
        print('Usuario não encontrado! ')

def cadastraLivro():
    titulo = input("Digite o título do livro: ")
    edicao = input("Digite a edição do livro: ")
    isbn = input("Digite o ISBN: ")
    validaISBN(isbn)
    npatrimonio = input("Digite o numero do patrimonio/codigo exemplar: ")
    validaPatrimonio(npatrimonio)
    livros[npatrimonio] = [titulo, edicao, isbn, npatrimonio]
    gravar_livros()
    print("Livro cadastrado! ")

def apagaLivro():
    npatrimonio = input("Digite o n do patrimonio  do livro no qual deseja apagar: ")
    validaPatrimonio(npatrimonio)
    if npatrimonio in livros:
        del livros[npatrimonio]
        print(npatrimonio, "Este livro foi removido. ")
        gravar_livros()
    else:
        print('Livro não encontrado! ')

def vizulizaLivroDisponivel():
    titulo = input('Digite o titulo a procurar: ')
    npatrimonio = input('Código do livro: ')
    validaPatrimonio(npatrimonio)
    existe = False
    for titulo in emp:
        if livros[npatrimonio][0].find(titulo):
            existe = True
            print('Livro', titulo, 'disponível.')
    if not existe:
        print('Livro', titulo, 'não disponível.')

def recuperaLivro():
    npatrimonio = input('digite o numero de patrimonio do livro : ')
    validaPatrimonio(npatrimonio)
    if npatrimonio in livros:
        print('Título;', livros[npatrimonio][0])
        print('Edição;', livros[npatrimonio][1])
        print('ISBN;', livros[npatrimonio][2])
    else:
        print('Livro não encontrado')

def realizaEmprestimo():
    cpf = input('Digite seu CPF: ')
    while not valida_cpf(cpf):
        print('Erro.')
        cpf = input('Digite novamente: ')
    if cpf in usuario1:
        npatrimonio = input("digite o numero do patrimonio: ")
        validaPatrimonio(npatrimonio)
        if npatrimonio in livros:
                print("Emprestimo feito com sucesso ")
                now = datetime.now()
                dia = now.day
                mes = now.month
                ano = now.year
                emp[npatrimonio] = [cpf, dia, mes, ano, npatrimonio]
                print("Nome do usuario: ", usuario1[cpf][0])
                print("Nome do Livro: ", livros[npatrimonio][0])
                enviaEmail(cpf, npatrimonio, dia, mes, ano)
                gravar_emprestimos()
        else:
            print("Numero de patrimonio não encontrado!")
    else:
        print("CPF não encontrado.")

def devolverLivro():
    npatrimonio = input("Digite o n do patrimonio: ")
    validaPatrimonio(npatrimonio)
    if npatrimonio in emp:
        cpf = input("Digite o CPF: ")
        while not valida_cpf(cpf):
            print("Erro")
            cpf = input("Digite seu CPF: ")
        if cpf in emp:
            titulo = input("Digite o titulo do livro: ")
            if titulo in emp:
                del emp[npatrimonio]
                print("Emprestimo apagado com sucesso. ")
                now = datetime.now()
                dia = now.day
                mes = now.month
                ano = now.year
                devolvidos[npatrimonio] = [cpf, titulo, dia, mes, ano]
            gravar_devolvidos()
        else:
            print("CPF não encontrado.")
    else:
        print("Impossivel apagar emprestimo.")

def renovarEmprestimos():
    print("")

def emprestimosPendentes():
    cpf = input("Digite o CPF do usuario a procurar os emprestimos pendentes: ")
    while not valida_cpf(cpf):
        print('Erro')
        cpf = input("Digite seu cpf: ")
    if cpf in emp:
        for cpf in emp:
            print(emp[cpf])

def bloquearUsuariosPendentes():
    print("")

def titulosMaisLocados():
    maisemp = {}
    for npatrimonio in devolvidos:
        if npatrimonio in maisemp:
            maisemp[npatrimonio] += 1
        else:
            maisemp[npatrimonio] = 1
    print(maisemp)

def usuariosMaisFrequente():
    print("")

def historicoDoUsuario():
    print("")

def buscarUsuarioComLivro():
    achou = False
    npatrimonio = input("Digite o numero do patrimonio: ")
    validaPatrimonio(npatrimonio)
    for emprestimo in emp:
        if emprestimo[emp][1] == npatrimonio:
            cpf = emprestimo[emp][0]
            achou = True
        if not achou:
            print("Usuário", usuario1[cpf][0])

def validaISBN(isbn):
    while bool(re.match("[0-9]{13}", isbn)) is False:
        isbn = input("ISBN inválido!\nInforme um ISBN válido. Ex: 0000000000000: ")

def validaPatrimonio(npatrimonio):
    while bool(re.match("[0-9]{6}", npatrimonio)) is False:
        npatrimonio= input("Patrimonio inválido!\nInforme um Patrimonio válido. Ex: 000000: ")

def menu1():
    print("----------CADASTRAMENTO DE PESSOA----------".center(80))
    print()
    print("1 - Cadastrar-se.")
    print('2 - Atualizar dados')
    print("3 - Excluir cadastro.")
    print('4 - Recuperar dados')
    op = input("Digite sua opção: ")
    print()
    if op == '1':
        cadastraUsuario()
    elif op == '2':
        atualizaUsuario()
    elif op == '3':
        apagaUsuario()
    elif op == '4':
        recuperaUsuario()

def menu2():
    print("-------CADASTRO DE LIVROS---------".center(80))
    print()
    print("----------- MENU -----------")
    print("".center(80))
    print("1 - Cadastramento de livros.")
    print("".center(80))
    print("2 - Remoção de livros.")
    print("".center(80))
    print("3 - Visualizar livros disponíveis.")
    print("".center(80))
    print('4 - Recuperar Livros.')

    novaop = input("Digite a opção desejada: ")
    apagar()
    if novaop == '1':
        cadastraLivro()
    elif novaop == '2':
        apagaLivro()
    elif novaop == '3':
        vizulizaLivroDisponivel()
    elif novaop == '4':  # ver se ta ok
        recuperaLivro()

def menu3():
    print("-----------MENU DE EMPRÉSTIMOS-----------".center(88))
    print()
    print('1 - Realizar emprestimos.')
    print('2 - Devolver livro.')
    print('3 - Renovar emprestimos.')
    print('4 - Emprestimos pendentes.')
    print('5 - Bloquear Usuarios pendentes.')
    print('6 - Titulos mais Locados.')
    print('7 - Usuario mais frequentes.')
    print('8 - Historico de usuario.')
    print('9 - Buscar usuario com livro.')
    op4 = input('Digite a opção: ')
    if op4 == '1':
        realizaEmprestimo()
    elif op4 == '2':
        devolverLivro()
    elif op4 == '3':
        renovarEmprestimos()
    elif op4 == '4':
        emprestimosPendentes()
    elif op4 == '5':
        bloquearUsuariosPendentes()
    elif op4 == '6':
        titulosMaisLocados()
    elif op4 == '7':
        usuariosMaisFrequente()
    elif op4 == '8':
        historicoDoUsuario()
    elif op4 == '9':
        buscarUsuarioComLivro()

def menu4():
    print(' RELATORIOS DE LIVROS LOCADOS !')
    print('Volume de emprestimos em...')
    print('1 - Dia')
    print('2 - Semana')
    print('3 - Mês')
    print('4 - Semestre')
    print('5 - Ano')
    opcao5 = input('Digite o periodo desejado de Relatorios : ')
    if opcao5 == '1':
        print()
    elif opcao5 == '2':
        print()
    elif opcao5 == '3':
        print()
    elif opcao5 == '4':
        print()
    elif opcao5 == '5':
        print()
    else:
        print("Opção inválida.")

recuperar_usuario()
recuperar_livros()
recuperar_emprestimos()
recuperar_devolvidos()

opcao = '0'
print("----------- ÁREA PRINCIPAL -------------".center(80))
print("".center(80))
while opcao != '10':
    print("1 - MENU DO USUÁRIO.")
    print("".center(80))
    print("2 - MENU DOS LIVROS.")
    print("".center(80))
    print("3 - MENU DE EMPRÉSTIMOS.")
    print()
    print("4 - MENU DE RELATÓRIOS. ")
    print()
    print("0 - SAIR PARA SALVAR DADOS. ")
    opcao = input("Digite aqui sua opção: ")

    apagar()  # ajeitar
    if opcao == '1':
        menu1()
    elif opcao == '2':
        menu2()
    elif opcao == '3':
        menu3()
    elif opcao == '4':
        menu4()
    elif opcao == '0':
        print('Finalizado. Volte sempre!')
        break
    else:
        print("Opção inválida !")
        print('Digite novamente !')
        print()
        print(usuario1)

# grava_usuario(usuario1)
# gravar_livros(livros)
# gravar_emprestimos(emp)
# gravar_devolvidos(devolvidos)
#-------------------------------------
# procurar livro com usuario opção 9
# mais locados opção 6
# veja a opcao de renovar emprestimo
# emprestimos pendentes
# bloquear usuarios
# enviar email quando devolver
# enviar quando devolver relatorios
# mesmo com o cpf em emprestimo, nos devolvidos aparece que nao tem
# verificar cada etapa se existe
# verificar se o cpf já está cadastrado
# renovar emprestimos
# usuarios frequentes