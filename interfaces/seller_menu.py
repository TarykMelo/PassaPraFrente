import time
from rich.console import Console
from rich.panel import Panel
from utils.utils import limpar_terminal
from database.db_functions import*
from user.seller.seller_functions import*


def seller_menu(usuario):
    """
    Exibe o menu do vendedor.

    Permite registrar uma venda, ver vendas existentes, voltar ao menu principal
    ou sair do programa.
    """
    while True:
        limpar_terminal()

        console.print(Panel(
            f"Bem-vindo a area de venda {usuario[3]}\n"
            "[1] Registrar uma venda\n"
            "[2] Ver suas vendas\n"
            "[3] Voltar para o menu de usuário\n"
            "[4] Sair do programa\n",
            title="[bold white]Área do vendedor[/bold white]",
            border_style="purple"
        ))

        try:
        
            user_choice = int(input("Digite a sua opção: ").strip())

            if user_choice == 1:
                console.print("[green]Abrindo o menu para registrar a venda...[/green]")
                sell_item(usuario)
                time.sleep(1)
                continue
            elif user_choice == 2:
                console.print("[green]Acessando a suas vendas...[/green]")
                seller_products(usuario)
                time.sleep(1)
                continue
            elif user_choice == 3:
                console.print("[green]Voltando para o menu principal...[/green]")
                time.sleep(1)
                from interfaces.user_menu import user_menu  
                user_menu(usuario)
                break
            elif user_choice == 4:
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