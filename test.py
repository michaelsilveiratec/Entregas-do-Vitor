import json
import os

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def salvar_em_json(self, arquivo):
        dados = {
            "login": self.login,
            "senha": self.senha
        }
        with open(arquivo, "w") as f:
            json.dump(dados, f, indent=4)
        print("Dados salvos com sucesso!")

    @classmethod
    def carregar_de_json(cls, arquivo):
        with open(arquivo, "r") as f:
            dados = json.load(f)
        return cls(dados["login"], dados["senha"])

    @staticmethod
    def criar_novo_perfil(arquivo):
        if os.path.exists(arquivo):
            with open(arquivo, "r") as f:
                usuarios = json.load(f)
        else:
            usuarios = {}

        login = input("Digite o nome de usuário: ")
        if login in usuarios:
            print("Erro: Nome de usuário já está em uso.")
            return

        senha = input("Digite a senha: ")
        confirmar_senha = input("Confirme a senha: ")

        if senha != confirmar_senha:
            print("Erro: As senhas não coincidem.")
            return

        usuarios[login] = senha
        with open(arquivo, "w") as f:
            json.dump(usuarios, f, indent=4)
        print("Usuário criado com sucesso!")

# Exemplo de uso
arquivo_usuarios = "usuarios.json"
Usuario.criar_novo_perfil(arquivo_usuarios)
