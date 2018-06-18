from database.register import *
import sqlite3

connection = sqlite3.connect('database/datas/login.db')
c = connection.cursor()

class listarAmigos():

    def __init__(self):
        mostrarAmigos = []
        self.mostrarAmigos = mostrarAmigos

    def listar(self, id):

        """
        Chama o banco de amizade e de usuario
        """
        sql = "SELECT * FROM amizade WHERE id_amigo1 = ?"
        sql2 = "SELECT * FROM usuario WHERE id_usuario = ?"

        amigos = ""

        """
        Vai procurando quantos amigos ele tem de acordo com o ID que combina com o dele
        """
        print("\n--------------------Lista de amigos--------------------\n")
        for row in c.execute(sql, (id,)):
            if row[0] == id:
                self.mostrarAmigos.append(row[1])
        for count in self.mostrarAmigos:
            for row in c.execute(sql2, (count,)):
                amigos = amigos + (row[1]+"\n")
        print (amigos)
