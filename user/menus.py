from rich.console import Console
from rich.panel import Panel
from utils.utils import*
from user.buyer.buyer_menu import*
from user.seller.seller_menu import*
from user.user_account import cadastro, login
from user.user_changes import*

def menu_inicial():
    while True:
        limpar_terminal()

        console.print(Panel(
            "[1] Fazer cadastro\n"
            "[2] Fazer login\n"
            "[3] Sair",
            title="[bold white]PassaPraFrente - UFRPE[/bold white]",
            border_style="green"
        ))

        try:

            user_choice = int(input("Escolha a sua opção: ").strip())

            if user_choice == 1:
                console.print("[green]Indo para a área de cadastro...[/green]")
                time.sleep(2)
                cadastro()
                continue
            elif user_choice == 2:
                console.print("[green]Indo para a área de login...[/green]")
                time.sleep(2)
                login()
                break
            elif user_choice == 3:
                console.print("[red]Fechando o programa...[/red]")
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

def user_menu(usuario):
    """
    Exibe o menu principal do usuário logado.

    Oferece opções para vender itens, comprar itens, modificar dados pessoais,
    deletar conta ou sair. Direciona para os submenus apropriados.
    """
    while True:
        limpar_terminal()
        
        console.print(Panel(
            f"Bem-vindo {usuario[3]}\n"
            "[1] Vender item\n"
            "[2] Comprar item\n"
            "[3] Modificar os dados do usuário\n"
            "[4] Deletar a conta\n"
            "[5] Sair",
            title="[bold white]Menu do usuário[/bold white]",
            border_style="green"
        ))

        try:

            user_choice = int(input("Digite a sua opção: ").strip())

            if user_choice == 1:
                console.print("[green]Vamos vender![/green]")
                time.sleep(2)
                seller_menu(usuario)
                break
            elif user_choice == 2:
                console.print("[blue]Hora de comprar![/blue]")
                time.sleep(2)
                buyer_menu(usuario)
                break
            elif user_choice == 3:
                console.print("[yellow]Indo acessar os dados pessoais...[/yellow]")
                user_modify(usuario)
                time.sleep(1)
                continue
            elif user_choice == 4:
                user_remove(usuario)
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
