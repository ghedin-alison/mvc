from db import _executar


class Produto:
    def __init__(self, nome, preco, id=None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.status = 1  # Ativo = 1, Inativo = 0

        # Se a tabela produtos não existir, criar.
        query = "CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL, status NUMERIC)"
        _executar(query)

    def salvar(self):
        query = f"INSERT INTO produtos (nome, preco, status) VALUES ({self.nome}, " \
                f"{float(self.preco)}, {int(self.status)})"
        _executar(query)

    def atualizar(self):
        query = f"UPDATE produtos SET status={int(self.status)} WHERE ID={int(self.id)}"
        _executar(query)

    def deletar(self):
        query = f"DELETE FROM produtos WHERE ID={int(self.id)}"
        _executar(query)

    @staticmethod
    def get_produtos():
        query = "SELECT * FROM produtos"
        produtos = _executar(query)
        return produtos

    @staticmethod
    def get_produto(id):
        query = f"SELECT * FROM produtos WHERE ID={int(id)}"
        produto = _executar(query)[0]
        produto = Produto(id=produto[0], nome=produto[1], preco=produto[2])
        return produto


