from utils.validations import*
import sqlite3
"""
Módulo db_functions

Este módulo contém todas as funções relacionadas ao banco de dados SQLite. Inclui operações para conectar ao DB, criar tabelas,
inserir, buscar, atualizar e deletar usuários e produtos.
"""
def conectar():
    """
    Conexão com o banco de dados SQLite.
    """
    return sqlite3.connect("database/passaprafrente.db")

def criar_tabela():
    """
    Cria a tabela 'usuario' no banco de dados se ela não existir.

    A tabela inclui campos para id, email, senha, nickname e telefone,
    com constraints de unicidade para email e nickname.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            nickname TEXT NOT NULL UNIQUE,
            telefone INT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def salvar_usuario(email, senha, nickname, telefone):
    """
    Insere um novo usuário no banco de dados.
    """
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuario (email, senha, nickname, telefone) VALUES (?, ?, ?, ?)",
            (email, senha, nickname, telefone)
        )
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False  
    

def buscar_usuario(email):
    """
    Busca um usuário no banco de dados pelo email.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE email = ?", (email, )
)
    usuario = cursor.fetchone()
    conn.close()
    return usuario



def product_table():
    """
    Cria a tabela 'produto' no banco de dados se ela não existir.

    A tabela inclui campos para id, nome, descricao, preco, local_de_venda,
    categoria, vendedor_id, vendedor_nickname, vendedor_telefone.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            preco REAL NOT NULL,
            local_de_venda TEXT NOT NULL,
            categoria TEXT NOT NULL,
            vendedor_id INTEGER NOT NULL,
            vendedor_nickname TEXT NOT NULL,
            vendedor_telefone TEXT NOT NULL,
            FOREIGN KEY (vendedor_id) REFERENCES usuarios(id)
            )
        """)
    conn.commit()
    conn.close()


def save_product(nome, descricao, preco, local_de_venda, categoria, usuario):
    """
    Insere um novo produto no banco de dados.
    """
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
                "INSERT INTO produto(nome, descricao, preco, local_de_venda, categoria, vendedor_id, vendedor_nickname, vendedor_telefone) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (nome, descricao, preco, local_de_venda, categoria, usuario[0], usuario[3], usuario[4])
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"[red]Erro ao salvar o produto: {e}[/red]")
        return False
    

def meus_produtos(usuario):
    """
    Busca todos os produtos de um vendedor específico.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produto WHERE vendedor_id = ?", (usuario[0],))
    produtos = cursor.fetchall()
    conn.close()
    return produtos


def remove_product(produto_id ,usuario):
    """
    Remove um produto específico do banco de dados.
    Apenas o vendedor dono do produto pode removê-lo.
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM produto WHERE id= ? AND vendedor_id= ?",
        (produto_id, usuario[0]))
    conn.commit()
    conn.close()


def remove_user(usuario):
    """
    Remove um usuário e todos os seus produtos do banco de dados.
    """
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produto WHERE vendedor_id = ?",
                    (usuario[0],))
        cursor.execute("DELETE FROM usuario WHERE id = ?",
                    (usuario[0],))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao deletar a conta {e}")
        return False


def todos_produtos(usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM produto 
        WHERE vendedor_id != ?
        AND id NOT IN (
            SELECT produto_id FROM pedidos WHERE comprador_id = ?
        )
    """, (usuario[0], usuario[0]))
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def criar_tabela_pedidos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            produto_nome TEXT NOT NULL,
            produto_preco REAL NOT NULL,
            comprador_id INTEGER NOT NULL,
            comprador_nickname TEXT NOT NULL,
            vendedor_id INTEGER NOT NULL,
            vendedor_nickname TEXT NOT NULL,
            vendedor_telefone TEXT NOT NULL,
            FOREIGN KEY (produto_id) REFERENCES produtos(id),
            FOREIGN KEY (comprador_id) REFERENCES usuarios(id)
        )
    """)
    conn.commit()
    conn.close()

def fazer_pedido(produto, usuario):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO pedidos (produto_id, produto_nome, produto_preco, comprador_id, comprador_nickname, vendedor_id, vendedor_nickname, vendedor_telefone) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (produto[0], produto[1], produto[3], usuario[0], usuario[3], produto[5], produto[6], produto[7])
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        console.print(f"[red]Erro ao salvar pedido: {e}[/red]")
        return False

def produto_ja_pedido(produto_id, usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM pedidos WHERE produto_id = ? AND comprador_id = ?",
        (produto_id, usuario[0])
    )
    pedido = cursor.fetchone()
    conn.close()
    return pedido is not None