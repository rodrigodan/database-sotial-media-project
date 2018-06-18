import sqlite3

connection = sqlite3.connect('database/datas/login.db')
c = connection.cursor()

'''
Cria as tabelas do banco de dados
'''
class register():

    def criar():
        c.execute("CREATE TABLE IF NOT EXISTS usuario(id_usuario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                                                        nome_usuario VARCHAR(100) NOT NULL,\
                                                        email VARCHAR(100)  NOT NULL,\
                                                        senha VARCHAR(100) NOT NULL)")

        c.execute('CREATE TABLE IF NOT EXISTS amizade(id_amigo1 INTEGER NOT NULL,\
                                                        id_amigo2 INTEGER NOT NULL,\
                                                        data_amizade DATE NOT NULL,\
                                                         PRIMARY KEY(id_amigo1,id_amigo2),\
                                                         FOREIGN KEY(id_amigo1) REFERENCES usuario(id_usuario) ON DELETE CASCADE,\
	                                                     FOREIGN KEY(id_amigo2) REFERENCES usuario(id_usuario) ON DELETE CASCADE)')

        c.execute('CREATE TABLE IF NOT EXISTS solicitacao(\
                                                    id_solicitante INTEGER NOT NULL,\
	                                                id_solicitado INTEGER NOT NULL,\
	                                                estado BOOLEAN NOT NULL,\
	                                                PRIMARY KEY(id_solicitante,id_solicitado),\
	                                                FOREIGN KEY(id_solicitante) REFERENCES usuario(id_usuario) ON DELETE CASCADE,\
	                                                FOREIGN KEY(id_solicitado) REFERENCES usuario(id_usuario) ON DELETE CASCADE)')

        c.execute('CREATE TABLE IF NOT EXISTS grupo(id_grupo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                                                	nome_grupo VARCHAR(100) NOT NULL)')

        c.execute('CREATE TABLE IF NOT EXISTS grupo_usuario(\
	                                               id_grupo INTEGER NOT NULL,\
	                                               id_usuario INTEGER NOT NULL,\
                                                	PRIMARY KEY(id_grupo,id_usuario),\
                                                	FOREIGN KEY(id_grupo) REFERENCES grupo(id_grupo) ON DELETE CASCADE, \
                                                	FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE)')

        c.execute('CREATE TABLE IF NOT EXISTS adm_grupo(\
                                                	id_usuario INTEGER NOT NULL,\
                                                	id_grupo INTEGER NOT NULL,\
                                                	PRIMARY KEY(id_usuario,id_grupo),\
                                                	FOREIGN KEY(id_usuario) REFERENCES usuario(id_usario) ON DELETE CASCADE,\
                                                	FOREIGN KEY(id_grupo) REFERENCES grupo(id_grupo) ON DELETE CASCADE)')

        c.execute('CREATE TABLE IF NOT EXISTS solicitacao_grupo(\
                                                	id_usuario_solicitante INTEGER NOT NULL,\
                                                	id_grupo INTEGER NOT NULL,\
                                                	estado BOOLEAN NOT NULL,\
                                                	PRIMARY KEY(id_usuario_solicitante,id_grupo),\
                                                	FOREIGN KEY(id_usuario_solicitante) REFERENCES usuario(id_usuario) ON DELETE CASCADE, \
                                                	FOREIGN KEY(id_grupo) REFERENCES grupo(id_grupo) ON DELETE CASCADE)')

        c.execute('CREATE TABLE IF NOT EXISTS posts(\
                                            id_post INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
	                                        id_usuario INTEGER,/* esse campo pode ser null caso a postagem seja feita em um grupo */\
	                                        id_grupo INTEGER,/* esse campo pode ser null caso a postagem seja feita em um perfil de pessoa */\
	                                        data_post DATE NOT NULL,\
	                                        conteudo TEXT, /* texto da postagem */\
	                                        visibilidade BOOLEAN, /* pública = true, privada = false */\
	                                        FOREIGN KEY(id_usuario) REFERENCES usuario(id_usario) ON DELETE CASCADE,\
	                                        FOREIGN KEY(id_grupo) REFERENCES grupo(id_grupo) ON DELETE CASCADE)')

        c.execute('CREATE TABLE IF NOT EXISTS comentarios(\
	                                       id_comentario INTEGER NOT NULL,\
	                                       id_post INTEGER NOT NULL,\
	                                       data_coment DATE NOT NULL,\
	                                       conteudo_coment TEXT,\
	                                       PRIMARY KEY(id_comentario, id_post),\
	                                       FOREIGN KEY(id_post) REFERENCES posts(id_post) ON DELETE CASCADE)')
        return True


    '''
    Método em que ele chama as tabelas primeiro, para poder criar e depois ele insere o usuario pq na outra classe ele chama essa
    '''
    def registrar(self, name, email, password):
        register.criar()
        c.execute("INSERT INTO usuario (nome_usuario, email, senha) VALUES (?,?,?)", (name, email, password))
        connection.commit()
        return True
