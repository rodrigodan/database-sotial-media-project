from database.register import *
import sqlite3

connection = sqlite3.connect('database/datas/login.db')
c = connection.cursor()

class adicionarGrupo():

    def chooseGrupo(self, id, nome):
        sql = 'SELECT * FROM grupo WHERE nome_grupo = ?'

        text = "-------------------"
        print("\n"+text+"Entre em um grupo"+text)
        choose = input("\n Digite o nome do grupo: ")

        for row in c.execute(sql, (choose, )):
            if row[1] == choose:
                chooseAnother = input("Deseja entrar no grupo "+choose+"? (S/N): ")
                if chooseAnother == "S":
                    c.execute('INSERT INTO solicitacao_grupo (id_usuario_solicitante, id_grupo, estado) VALUES (?, ?, ?)',(id, row[0], 1))
                    connection.commit()
                    return True
                else:
                    print("Obrigado por tentar entrar em algum grupo")
                    return True
            else:
                print("Grupo não existe")
                return False


    def verifyRequestGrupo(self, id):
        pessoas = []
        sql0 = 'SELECT * FROM grupo WHERE nome_grupo = ?'
        sql = 'SELECT * FROM adm_grupo WHERE id_usuario = ?'
        sql2 = 'SELECT * FROM grupo WHERE id_grupo = ? '
        sql3 = 'SELECT * FROM solicitacao_grupo WHERE id_grupo = ?'
        sql4 = 'SELECT * FROM usuario WHERE id_usuario = ?'
        sql5 = 'SELECT * FROM usuario WHERE nome_usuario = ?'
        sql6 = 'SELECT * FROM solicitacao_grupo WHERE id_usuario_solicitante = ?'

        idDoGrupo = 0
        self.idDoGrupo = idDoGrupo
        countPessoas = 0
        print("---------------------Grupos que você gerencia----------------------")

        for row in c.execute(sql, (id,)):
            for count in c.execute(sql2, (row[1],)):
                print ("\n"+count[1]+"\n")
                continue


        choose = input("Digite o grupo que você quer gerenciar: ")

        ''''Verificar o id do grupo'''

        for row in c.execute(sql0, (choose, )):
            if row[1] == choose:
                self.idDoGrupo = row[0]
                ''''Verificar o tamanho da solicitação de pessoas através do Id do grupo'''
                for rowTwo in c.execute(sql3, (self.idDoGrupo, )):
                    pessoas.append(rowTwo[0])
                    countPessoas+= 1
            else:
                print("Grupo não encontrado")
                return False

        for count in pessoas:
            for rowUser in c.execute(sql4, (count, )):
                for rowVerify in c.execute(sql3,(self.idDoGrupo,)):
                    if rowVerify[2] == 1:
                        print(rowUser[1]," quer entrar no grupo")

        for count in range(countPessoas):
            chooseAnother = input("Quem você deseja adicionar? (0 para sair) ")
            if chooseAnother == "0":
                return False
            else:
                for rowUser in c.execute(sql5, (chooseAnother, )):
                    for rowUserInSolicitacao in c.execute(sql6, (rowUser[0], )):
                        c.execute ("DELETE FROM solicitacao_grupo WHERE (? and ?)", (rowUser[0], self.idDoGrupo))
                        connection.commit()
                        c.execute("INSERT INTO solicitacao_grupo VALUES (?, ?, ?)",(rowUser[0], self.idDoGrupo, 0))
                        c.execute("INSERT INTO grupo_usuario VALUES (?, ?)", (self.idDoGrupo, rowUser[0]))
                        connection.commit()
                        continue
