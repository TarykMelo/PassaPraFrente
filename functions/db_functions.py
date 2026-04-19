from functions.functions_main import*
from validations import*
import sqlite3
from rich.console import Console
""""Banco de dados"""
#conectar com o banco de dados
def conectar():
    return sqlite3.connect("passaprafrente.db")

#Criar uma tabela caso não exista
def criar_tabela():
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

#Salvar usuário pro banco
def salvar_usuario(email, senha, nickname, telefone):
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
        return False  # email ou nickname já cadastrado
    
#Descobrir se o usuário existe na aba de login

def buscar_usuario(email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario WHERE email = ?", (email, )
)
    usuario = cursor.fetchone()
    conn.close()
    return usuario


# Criar banco de dados para cadastro de produtos

def product_table():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            preco REAL NOT NULL,
            vendedor_id INTEGER NOT NULL,
            vendedor_nickname TEXT NOT NULL,
            vendedor_telefone TEXT NOT NULL,
            FOREIGN KEY (vendedor_id) REFERENCES usuarios(id)
            )
        """)
    conn.commit()
    conn.close()

#função para salvar o produto no banco de dados

def save_product(nome, descricao, preco, usuario):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
                "INSERT INTO produto(nome, descricao, preco, vendedor_id, vendedor_nickname, vendedor_telefone) VALUES (?, ?, ?, ?, ?, ?)",
                (nome, descricao, preco, usuario[0], usuario[3], usuario[4])
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"[red]Erro ao salvar o produto: {e}[/red]")
        return False
    
# Buscar produtos do banco de dados

def meus_produtos(usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produto WHERE vendedor_id = ?", (usuario[0],))
    produtos = cursor.fetchall()
    conn.close()
    return produtos

# Função para deletar o produto do banco de dados caso o vendedor queira

def remove_product(produto_id ,usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM produto WHERE id= ? AND vendedor_id= ?",
        (produto_id, usuario[0]))
    conn.commit()
    conn.close()

# Remover usuário do banco de dados

def remove_user(usuario):
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

# Acessar todos os produtos disponiveis a venda

def todos_produtos(usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produto")
    produtos = cursor.fetchall()
    conn.close()
    return produtos