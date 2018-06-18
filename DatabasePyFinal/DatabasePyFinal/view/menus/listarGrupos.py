from database.register import *
import sqlite3

connection = sqlite3.connect('database/datas/login.db')
c = connection.cursor()

class listarGrupos():

    """
    Abre o banco de dados de grupo e só exibe
    """
    def mostrarGrupos(self, id):
        grupos = []
        sql0 = "SELECT * FROM grupo WHERE id_grupo = ?"
        sql = "SELECT * FROM grupo_usuario WHERE id_usuario = ?"

        print("\n--------------------Lista de grupos--------------------\n")
    
        for row in c.execute(sql,(id,)):
            grupos.append(row[0])

        for count in grupos:
            for rowTwo in c.execute(sql0, (count,)):
                print(rowTwo[1])
