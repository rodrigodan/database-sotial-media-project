from database.register import *
import sqlite3

connection = sqlite3.connect('database/datas/login.db')
c = connection.cursor()

class criaGrupo():

    def testDB(self):
        c.execute('SELECT * FROM grupo')
        data = c.fetchall()
        if data is None:
            print(true)
            return True
        else:
            return False

    def criarGrupo(self, id):
        nomeDoGrupo = ""
        self.nomeDoGrupo = nomeDoGrupo
        sql = 'SELECT * FROM usuario WHERE id_usuario = ?'
        sql2 = 'SELECT * FROM grupo WHERE id_grupo = ?'
        text = "--------------------"
        print(text+"Criação de grupo"+text+"\n")
        nameGrupo =  input("Nome do grupo: ")
        self.nomeDoGrupo = nameGrupo

        if self.testDB:
            for rowTwo in c.execute(sql,(id, )):
                if rowTwo[0] == id:
                    c.execute('INSERT INTO grupo (nome_grupo) VALUES (?)',([self.nomeDoGrupo]))
                    connection.commit()
                    for row in c.execute(sql2,(rowTwo[0], )):
                            c.execute('INSERT INTO grupo_usuario (id_grupo, id_usuario) VALUES (?, ?)', (row[0], rowTwo[0]))
                            c.execute('INSERT INTO adm_grupo (id_usuario, id_grupo) VALUES (?, ?)', (rowTwo[0], row[0]))
                            connection.commit()
                            print("Grupo criado com sucesso!!\n")

                    return True
        else:
            for row in c.execute(sql2, (nameGrupo, )):
                if row[0] == nameGrupo:
                    print("Nome já usado\n")
                    return False
                else:
                    for rowTwo in c.execute(sql,(id, )):
                        if rowTwo[0] == id:
                            c.execute('INSERT INTO grupo (nome_grupo, id_usuario) VALUES (?, ?)', (nameGrupo, rowTwo[0]))
                            connection.commit()
                            c.execute('INSERT INTO grupo_usuario (id_grupo, id_usuario) VALUES (?, ?)', (row[1], rowTwo[0]))
                            c.execute('INSERT INTO adm_grupo (id_usuario, id_grupo) VALUES (?, ?)', (rowTwo[0], row[1]))
                            connection.commit()
                            print("Grupo criado com sucesso!!\n")
                            return True
