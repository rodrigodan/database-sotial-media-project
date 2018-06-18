from database.register import *
import sqlite3
import datetime
import time

connection = sqlite3.connect('database/datas/login.db')
c = connection.cursor()

'''
Classe para verificar e adicionar
'''
class adicionarAmigo():

    def __init__(self):
        id_friend = None
        self.id_friend = id_friend

    '''
    Verifica o id do solicitante
    '''
    def verifyIdFriend(self, nome):
        sql = "SELECT * FROM usuario WHERE nome_usuario = ?"

        for row in c.execute(sql,(nome, )):
            if row[1] == nome:
                self.id_friend = row[0]
                break

        return self.id_friend

    """
    chama o de verificar solicitante e compara com o solicitado, se tudo der ok, ele insere na tabela de solicitacao
    """
    def verifyFriend(self, nome, id_user):
        self.verifyIdFriend(nome)
        sql = "SELECT * FROM amizade WHERE id_amigo2 = ?"

        for row in c.execute(sql,(self.id_friend, )):
            if row[1] == self.id_friend and row[0] == id_user:
                print("Vocês já são amigos")
                break

        change = input("Deseja adicionar "+nome+"? (Resposta com S/N): ")

        if change == "S":
            try:
                c.execute("INSERT INTO solicitacao (id_solicitante, id_solicitado, estado) VALUES (?,?,?)", (id_user, self.id_friend, 1))
                connection.commit()
            except:
                print("\nPessoa não existe")
        else:
            exit()

    """
    Mostra pessoas que desejam lhe adicionar
    """
    def verifyRequest(self, user):
        pessoas = []
        inserir = []
        sql = "SELECT * FROM solicitacao WHERE id_solicitado = ?"
        sql1 = "SELECT * FROM usuario WHERE id_usuario = ?"
        sql2 = "SELECT * FROM usuario WHERE nome_usuario = ?"

        for row in c.execute(sql,(user, )):
            if row[1] == user and row[2] == 1:
                inserir.append(row[0])

        for count in inserir:
            for rowTwo in c.execute(sql1,(count,)):
                if rowTwo[0] == count:
                    pessoas.append(rowTwo[1])

        if pessoas:
            for count in pessoas:
                print(count + " quer adicionar você")

            date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%D'))
            choose = input("Quem deseja adicionar? (Digite o nome igual) ")

            for row in c.execute(sql2,(choose, )):
                if row[1] == choose:
                    c.execute("DELETE FROM solicitacao WHERE (? and ?)",(row[0], user))
                    connection.commit()
                    c.execute("INSERT INTO amizade (id_amigo1, id_amigo2, data_amizade) VALUES (?,?,?)", (user, row[0], date))
                    c.execute("INSERT INTO amizade (id_amigo1, id_amigo2, data_amizade) VALUES (?,?,?)", (row[0], user, date))
                    connection.commit()
                    c.execute("INSERT INTO solicitacao (id_solicitante, id_solicitado, estado) VALUES (?,?,?)", (row[0], user, 0))
                    connection.commit()
                    print ("Adicionado com sucesso")

                else:
                    print("Usuário não adicionado")
                    choose = input("Quem deseja adicionar? (Digite o nome igual) ")

        else:
            print("Nenhum amigo para ser adicionado")
