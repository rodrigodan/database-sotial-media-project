'''
Importa as classes
'''

from database.register import *
from view.menus.visualizarPerfil import *
from view.menus.listarAmigos import *
from view.menus.adicionarAmigo import *
from view.menus.adicionarGrupo import *
from view.menus.listarGrupos import *
from view.menus.criaGrupo import *
import sqlite3

'''
Faz conexão com o banco de dados
'''

connection = sqlite3.connect('database/datas/login.db')
c = connection.cursor()

'''
Instancia as classes
'''

adicionarGrupo = adicionarGrupo()
criaGrupo = criaGrupo()
db = register()
visualize = visualizarPerfil()
listarAmigos = listarAmigos()
adicionarAmigo = adicionarAmigo()
listarGrupos = listarGrupos()

class menu():
    option = 0
    user = []

    '''
    Exibe a tela inicial do programa
    '''
    def exibeInicio(self):
        text = "--------------------"
        print(text+"Bem vindo ao Clone do Facebook"+text+"\n\n")
        self.option = int(input("1 - Login / 2 - Registrar / 0 - Sair: "))

        if self.option > 4 or self.option < 0:
            print ("Erro, digito inválido")

        if self.option == 1:
            self.exibeLogin()
        elif self.option == 2:
            self.exibeRegister()
        elif self.option == 0:
            exit()
        else:
            print('\nDigite um valor válido\n')
            print(text+"Bem vindo ao Clone do Facebook"+text+"\n\n")
            self.option = int(input("1 - Login / 2 - Registrar: "))


    '''
    Exibe a tela para fazer login, caso dê tudo certo ela pega o metodo menu
    '''
    def exibeLogin(self):
        sql = 'SELECT * FROM usuario WHERE email = ? and senha = ?'
        loginUser = input("\nUsuário: ")
        passwordUser = input("Senha: ")
        teste = [loginUser, passwordUser]
        for row in c.execute(sql, (loginUser, passwordUser)):
            if(row[2] == loginUser and row[3] == passwordUser):
                for cont in row:
                    self.user.append(cont)
                return self.exibeMenu()

            return True

        else:
            print("Erro, usuário inválido")
            self.exibeInicio()
            return False


    '''
    EXIBE O REGISTRO, CASO de tudo certo, ele vai para o inicio
    '''
    def exibeRegister(self):
        text = "--------------------"
        print("\n"+text+"Bem vindo a tela de registro"+text+"\n")
        name = input("Digite seu nome completo: ")
        email = input("Digite a e-mail: ")
        senha = input("Digite o senha: ")
        db.registrar(name, email, senha)
        self.exibeInicio()


    '''
    Exibe o menu para escolha
    '''
    def exibeMenu(self):
        sql = 'SELECT * FROM adm_grupo WHERE id_usuario = ?'

        text = "--------------------"
        print("\n"+text+"Bem vindo "+str(self.user[1])+text+"\n")
        print("1 - Visualizar perfil")
        print("2 - Listar amigos")
        print("3 - Listar grupos")
        print("4 - adicionar grupo")
        print("5 - adicionar pessoa")
        print("6 - ver pedido de amizades pendentes")
        print("7 - Criar grupo")
        print("8 - Sair")
        for row in c.execute(sql,(self.user[0],)):
            if row[0] == self.user[0]:
                print("9 - ver pedidos para entrar no grupo")
                break


        try:
            optionFace = int(input("\nDigite a sua opção: "))
        except:
            print("Comando inválido, digite um inteiro")
            optionFace = int(input("\nDigite a sua opção: "))


        while optionFace > 10 or optionFace < 0:
            print ("Comando inválido")
            optionFace = int(input("\nDigite a sua opção: "))

        while optionFace < 10:
            if optionFace == 1:
                visualize.visualizeUser(self.user[2])
                optionFace = int(input("\nDigite a sua opção: "))

            if optionFace == 2:
                listarAmigos.listar(self.user[0])
                optionFace = int(input("\nDigite a sua opção: "))
                while optionFace == 2:
                    print("Digite outra função, a função já está aberta")
                    optionFace = int(input("\nDigite a sua opção: "))

            if optionFace == 3:
                listarGrupos.mostrarGrupos(self.user[0])
                optionFace = int(input("\nDigite a sua opção: "))
                while optionFace == 3:
                    print("Digite outra função, a função já está aberta")
                    optionFace = int(input("\nDigite a sua opção: "))

            if optionFace == 4:
                adicionarGrupo.chooseGrupo(self.user[0], self.user[1])
                optionFace = int(input("\nDigite a sua opção: "))
                while optionFace == 4:
                    print("Digite outra função, a função já está aberta")
                    optionFace = int(input("\nDigite a sua opção: "))

            if optionFace == 5:
                nameAdd = input("\nNome para adicionar: ")
                adicionarAmigo.verifyFriend(nameAdd, self.user[0])
                optionFace = int(input("\nDigite a sua opção: "))

            if optionFace == 6:
                adicionarAmigo.verifyRequest(int(self.user[0]))
                optionFace = int(input("\nDigite a sua opção: "))

            if optionFace == 7:
                criaGrupo.criarGrupo(self.user[0])
                optionFace = int(input("\nDigite a sua opção: "))

            if optionFace == 8:
                exit()

            if optionFace == 9:
                adicionarGrupo.verifyRequestGrupo(self.user[0])
                optionFace = int(input("\nDigite a sua opção: "))
