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


# Função para filtrar a categoria e ver os produtos disponíveis de lá

def filtrar_produto(usuario):  
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
        cursor.execute("""
            SELECT * FROM produto
            WHERE vendedor_id != ?
            AND id NOT IN (
                SELECT produto_id FROM pedidos WHERE comprador_id = ?
            )
        """, (usuario[0], usuario[0]))

    elif escolha in CATEGORIAS:
        cursor.execute("""
            SELECT * FROM produto
            WHERE categoria = ?
            AND vendedor_id != ?
            AND id NOT IN (
                SELECT produto_id FROM pedidos WHERE comprador_id = ?
            )
        """, (CATEGORIAS[escolha], usuario[0], usuario[0]))

    else:
        console.print("[red]❌ Escolha uma das categorias disponíveis![/red]")
        time.sleep(2)
        return

    produtos = cursor.fetchall()
    conn.close()
    limpar_terminal()

    if not produtos:
        console.print(Panel(
            "Nenhum produto disponível nessa categoria!",
            title="[bold white]Área do comprador - Filtros[/bold white]",
            border_style="blue"
        ))

    texto = ""
    for p in produtos:
        texto += (
            f"[bold]#{p[0]} — {p[1]}[/bold]\n"
            f"Descrição: {p[2]}\n"
            f"Preço: R$ {p[3]:.2f}\n"
            f"Categoria: {p[4]}\n"
            f"Vendedor: {p[6]}\n"
            f"Telefone: {p[7]}\n"
            f"{'-' * 40}\n"
        )

    console.print(Panel(
        texto,
        title="[bold white]Área do comprador - Filtros[/bold white]",
        border_style="blue"
    ))
    try:
        escolha = int(input("Digite o # do produto que deseja (0 para voltar): ").strip())

        if escolha == 0:
            return

        # verifica se o produto existe na lista
        produto_escolhido = next((p for p in produtos if p[0] == escolha), None)

        if produto_escolhido is None:
            console.print("[red]❌ Produto não encontrado![/red]")
            time.sleep(2)
            return

        # confirma o pedido
        limpar_terminal()
        console.print(Panel(
            f"Produto: {produto_escolhido[1]}\n"
            f"Descrição: {produto_escolhido[2]}\n"
            f"Preço: R$ {produto_escolhido[3]:.2f}\n"
            f"Categoria: {produto_escolhido[4]}\n"
            f"Vendedor: {produto_escolhido[6]}\n"
            f"Telefone: {produto_escolhido[7]}",
            title="[bold green]Confirmar pedido[/bold green]",
            border_style="green"
        ))

        confirm = input("Deseja salvar esse pedido? (s/n): ").lower().strip()

        if confirm == "s":
            sucesso = fazer_pedido(produto_escolhido, usuario)
            if sucesso:
                console.print(
                    f"[green]✅ Pedido salvo!\n"
                    f"Entre em contato com o vendedor: {produto_escolhido[7]}[/green]"
                )
            time.sleep(3)
            return
        elif confirm == "n":
            console.print("[yellow]Pedido cancelado.[/yellow]")
            time.sleep(2)
            return
        else:
            console.print("[red] Digite s ou n![/red]")
            time.sleep(2)
            return

    except ValueError:
        console.print("[red] Digite um número válido![/red]")
        time.sleep(2)
        return


def comprar_produto(usuario):
    """
    Exibe todos os produtos disponíveis para o comprador.

    Esta função limpa o terminal, busca todos os produtos disponíveis para o usuário
    e os exibe em um painel formatado. Se não houver produtos, mostra uma mensagem
    de aviso.
    """
    while True:
        limpar_terminal()
        produtos = todos_produtos(usuario)

        if not produtos:
            console.print(Panel(
                "Nenhum produto disponível no momento!",
                title="[bold green]Comprar produto[/bold green]",
                border_style="green"
            ))
            input("Pressione Enter para voltar...")
            return

        texto = ""
        for p in produtos:
            texto += (
                f"[bold]#{p[0]} — {p[1]}[/bold]\n"
                f"Descrição: {p[2]}\n"
                f"Preço: R$ {p[3]:.2f}\n"
                f"Categoria: {p[4]}\n"
                f"Vendedor: {p[6]}\n"
                f"Telefone: {p[7]}\n"
                f"{'-' * 40}\n"
            )

        console.print(Panel(
            texto,
            title="[bold green]Produtos disponíveis[/bold green]",
            border_style="green"
        ))

        try:
            escolha = int(input("Digite o # do produto que deseja (0 para voltar): ").strip())

            if escolha == 0:
                return

            # verifica se o produto existe na lista
            produto_escolhido = None
            for p in produtos:
                if p[0] == escolha:
                    produto_escolhido = p
                    break

            if produto_escolhido is None:
                console.print("[red]❌ Produto não encontrado![/red]")
                time.sleep(2)
                continue

            # confirma o pedido
            limpar_terminal()
            console.print(Panel(
                f"Produto: {produto_escolhido[1]}\n"
                f"Descrição: {produto_escolhido[2]}\n"
                f"Preço: R$ {produto_escolhido[3]:.2f}\n"
                f"Categoria: {produto_escolhido[4]}\n"
                f"Vendedor: {produto_escolhido[6]}\n"
                f"Telefone: {produto_escolhido[7]}",
                title="[bold green]Confirmar pedido[/bold green]",
                border_style="green"
            ))

            confirm = input("Deseja salvar esse pedido? (s/n): ").lower().strip()

            if confirm == "s":
                sucesso = fazer_pedido(produto_escolhido, usuario)
                if sucesso:
                    console.print(
                        f"[green]✅ Pedido salvo!\n"
                        f"Entre em contato com o vendedor: {produto_escolhido[7]}[/green]"
                    )
                time.sleep(3)
                return
            elif confirm == "n":
                console.print("[yellow]Pedido cancelado.[/yellow]")
                time.sleep(2)
                continue
            else:
                console.print("[red] Digite s ou n![/red]")
                time.sleep(2)
                continue

        except ValueError:
            console.print("[red] Digite um número válido![/red]")
            time.sleep(2)
            continue

def ver_meus_pedidos(usuario):
    limpar_terminal()
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM pedidos WHERE comprador_id = ?", (usuario[0],)
    )
    pedidos = cursor.fetchall()
    conn.close()

    if not pedidos:
        console.print(Panel(
            "Você ainda não fez nenhum pedido!",
            title="[bold green]Meus pedidos[/bold green]",
            border_style="green"
        ))
        input("Pressione Enter para voltar...")
        return

    texto = ""
    for p in pedidos:
        texto += (
            f"[bold]#{p[0]} — {p[2]}[/bold]\n"
            f"Preço: R$ {p[3]:.2f}\n"
            f"Vendedor: {p[7]}\n"
            f"Telefone: {p[8]}\n"
            f"{'-' * 40}\n"
        )

    console.print(Panel(
        texto,
        title="[bold green]Meus pedidos[/bold green]",
        border_style="green"
    ))
    input("Pressione Enter para voltar...")