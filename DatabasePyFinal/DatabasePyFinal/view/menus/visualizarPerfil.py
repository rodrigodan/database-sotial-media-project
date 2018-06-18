from database.register import *
import sqlite3

connection = sqlite3.connect('database/datas/login.db')
c = connection.cursor()

db = register()

class visualizarPerfil():

    """
    Exibe o de perfil
    """
    def visualizeUser(self, email):
        sql = "SELECT * FROM usuario WHERE email = ?"

        for row in c.execute(sql, (email,)):
            if(row[2] == email):
                print("--------------------Veja seu perfil--------------------")
                print("\nNome completo: "+row[1])
                print("E-mail: "+row[2])
