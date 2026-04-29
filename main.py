
from database.db_functions import product_table, criar_tabela, criar_tabela_pedidos
from user.menus import menu_inicial
"""
Módulo principal

Este módulo é o principal para rodar o projeto que contém as 
funções necessárias para a criação do banco de dados
"""


if __name__ == "__main__":
    criar_tabela()
    product_table()
    criar_tabela_pedidos()
    menu_inicial()