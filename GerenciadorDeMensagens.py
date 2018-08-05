from User import *

class GerenciadorDeMensagens:
    __instance = None

    @staticmethod
    def getInstance():
        if GerenciadorDeMensagens.__instance == None: GerenciadorDeMensagens()
        return GerenciadorDeMensagens.__instance

    def __init__(self):
        if GerenciadorDeMensagens.__instance != None:
            raise Exception("Esta classe e singleton!")
        else:
            self.users = []
            GerenciadorDeMensagens.__instance = self

    def verificaExistencia(self, nome):
        for item in self.users:
            if item.getUsername() == nome:
                return True
        return False

    def adicionaUsuario(self, nome, senha):
        self.users.append(User(nome, senha))

    def verificaSenha(self, nome, senha):
        for item in self.users:
            if item.getUsername() == nome:
                if item.getPassword() == senha:
                    return True
                else: return False
        return False

    def gravaMensagem(self, usuario, nome_do_arquivo, conteudo):
        for item in self.users:
            if item.getUsername() == usuario:
                for file in item.getFiles():
                    if (file[0]==nome_do_arquivo):
                        file[1] = conteudo
                        return "S 1"
                item.addFile(nome_do_arquivo, conteudo)
                return "S 0"

    def buscaMensagem(self, nome, nome_do_arquivo):
        for item in self.users:
            if item.getUsername() == nome:
                for file in item.getFiles():
                    if (file[0]==nome_do_arquivo):
                        return "R 0 "+file[1]
                return "R -3"

    def buscaArquivos(self, nome):
        for item in self.users:
            if item.getUsername() == nome:
                if item.getFiles() == []: return "L 0"
                else: return "L 0" +item.getFileNames()

    def registro(self, msg):
        args = msg.split(" ")
        if (self.verificaExistencia(args[1]) == True):
            return "N -1"
        else:
            self.adicionaUsuario(args[1], args[2])
            return "N 0"

    def envio(self, msg):
        args = msg.split(" ")
        position = 0
        spaces = 0
        for n in msg:
            position += 1
            if (n == " ") : spaces += 1
            if (spaces == 4) : break
        conteudo = msg[position:]
        if (self.verificaExistencia(args[1])==True):
            if (self.verificaSenha(args[1], args[2])==True):
                return self.gravaMensagem(args[1], args[3], conteudo)
            else: return "S -2"
        else: return "S -1"

    def recebimento(self, msg):
        args = msg.split(" ")
        if (self.verificaExistencia(args[1])==True):
            if (self.verificaSenha(args[1], args[2])==True):
                return self.buscaMensagem(args[1], args[3])
            else: return "R -2"
        else: return "R -1"

    def lista(self, msg):
        args = msg.split(" ")
        if (self.verificaExistencia(args[1])==True):
            if (self.verificaSenha(args[1], args[2])==True):
                return self.buscaArquivos(args[1])
            else: return "L -2"
        else: return "L -1"

    def interpreta(self, msg):
        if msg[0]=='N': return self.registro(msg)
        elif msg[0]=='S': return self.envio(msg)
        elif msg[0]=='R': return self.recebimento(msg)
        elif msg[0]=='L': return self.lista(msg)
        else: return "undefined"
