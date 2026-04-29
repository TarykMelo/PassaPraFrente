import time
from rich.console import Console
from rich.panel import Panel
from utils.utils import limpar_terminal
from database.db_functions import*
from user.buyer.buyer_functions import*

def buyer_menu(usuario):
    """
    Exibe o menu do comprador.

    Oferece opções para ver todos os produtos, filtrar por categoria,
    ver produtos selecionados (não implementado), voltar ao menu principal
    ou sair.
    """
    while True:
        limpar_terminal()

        console.print(Panel(
            f"Bem-vindo a area de venda {usuario[3]}\n"
            "[1] Ver todos os produtos disponiveis\n"
            "[2] Filtrar para uma categoria especifica\n"
            "[3] Ver os produtos selecionados\n"
            "[4] Voltar para o menu de usuário\n"
            "[5] Sair do programa\n",
            title="[bold white]Área do comprador[/bold white]",
            border_style="blue"
        ))

        try:
        
            user_choice = int(input("Digite a sua opção: ").strip())

            if user_choice == 1:
                console.print("[green]Acessando os produtos disponiveis...[/green]")
                time.sleep(1)
                comprar_produto(usuario)
                continue
            elif user_choice == 2:
                console.print("[green]Acessando as categorias disponiveis[/green]")
                time.sleep(1)
                filtrar_produto(usuario)
                continue
            elif user_choice == 3:
                console.print("[green]Acessando os produtos que você escolheu![/green]")
                time.sleep(1)
                ver_meus_pedidos(usuario)
                continue
            elif user_choice == 4:
                console.print("[green]Voltando para o menu principal...[/green]")
                time.sleep(1)
                from user.menus import user_menu  
                user_menu(usuario)
                break
            elif user_choice == 5:
                console.print("[red]Saindo...[/red]")
                time.sleep(2)
                break
            else:
                console.print("[red]Opção inválida, escolha uma das opções acima![/red]")
                time.sleep(2)
                continue
        except ValueError:
            console.print("[red]Opção inválida, escolha uma das opções acima![/red]")
            time.sleep(2)
            continue