import time
from rich.panel import Panel
from utils.utils import*
from functions.db_functions import*
from functions.seller_functions import*
from functions.user_functions import*
from functions.functions_main import*

"""
Módulo buyer_functions

Este módulo contém funções relacionadas às operações do comprador.
Inclui funcionalidades para visualizar todos os produtos disponíveis e filtrar produtos por categoria.
"""

def products_available(usuario):
    """
    Exibe todos os produtos disponíveis para o comprador.

    Esta função limpa o terminal, busca todos os produtos disponíveis para o usuário
    e os exibe em um painel formatado. Se não houver produtos, mostra uma mensagem
    de aviso.
    """
    limpar_terminal()

    produtos = todos_produtos(usuario)

    # Caso não haja produto disponivel
    if not produtos:
        console.print(Panel(
            "[red]Nenhum produto cadastrado ainda![/red]",
            title="[bold white]Área do vendedor - Meus produtos[/bold white]",
            border_style="blue"
            ))
        time.sleep(2)
        input("Digite ENTER para voltar")
        return
    texto = ""
    
    # Caso tenha produto, uma lista de todos os produtos disponíveis
    for produto in produtos:
        texto +=(
            f"[bold]#{produto[0]} - {produto[1]}[/bold]\n"
            f"Descrição: {produto[2]}\n"
            f"Preço: R${produto[3]:.2f}\n"
            f"Local e horário: {produto[4]}\n"
            f"Categoria: {produto[5]}"
            f"Vendedor: {produto[7]}\n"
            f"Telefone: {produto[8]}\n"
            f"{'-' * 40}\n"
        )
    console.print(Panel(
        texto,
        title="[bold white]Área do comprador - Todos os produtos[/bold white]",
        border_style="blue"
    ))
    input("Digite ENTER para voltar")

# Função para filtrar a categoria e ver os produtos disponíveis de lá

def filtrar_produto():
    """
    Permite ao comprador filtrar produtos por categoria.

    Esta função exibe um menu de categorias, solicita a escolha do usuário,
    consulta o banco de dados com base na categoria selecionada e exibe os
    produtos filtrados em um painel. Se não houver produtos na categoria,
    mostra uma mensagem apropriada.
    """
    limpar_terminal()
    console.print(Panel(
        "[1] Eletrônicos\n"
        "[2] Livros\n"
        "[3] Roupas\n"
        "[4] Móveis\n"
        "[5] Esportes\n"
        "[6] Outros\n"
        "[7] Todos",
        title="[bold white]Área do comprador - Filtros[/bold white]",
        border_style="blue"
    ))

    escolha = input("Escolha uma categoria: ").strip()

    conn = conectar()
    cursor = conn.cursor()

    if escolha == "7":
        cursor.execute("SELECT * FROM produto")
    elif escolha in CATEGORIAS:
        cursor.execute("SELECT * FROM PRODUTO WHERE categoria = ?",
                       (CATEGORIAS[escolha],)
        )
    else:
        console.print("[red]Escolha uma das categorias disponíveis![/red]")
        time.sleep(2)
        return
    
    produtos = cursor.fetchall()
    conn.close()

    if not produtos:
        console.print(Panel(
            "Nenhum produto nessa categoria!",
            title="[bold white]Área do comprador - Filtros[/bold white]",
            border_style="blue"
        ))
        input("Pressione ENTER para voltar")
        return
    
    texto = ""
    for produto in produtos:
            texto +=(
                f"[bold]#{produto[0]} - {produto[1]}[/bold]\n"
                f"Descrição: {produto[2]}\n"
                f"Preço: R${produto[3]:.2f}\n"
                f"Local e horário: {produto[4]}\n"
                f"Categoria: {produto[5]}"
                f"Vendedor: {produto[7]}\n"
                f"Telefone: {produto[8]}\n"
                f"{'-' * 40}\n"
            )
    console.print(Panel(
        texto,
        title="[bold white]Área do comprador - Filtros[/bold white]",
        border_style="blue"
    ))
    input("Pressione ENTER para voltar")