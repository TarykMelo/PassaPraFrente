from functions.functions_main import*
import time
from rich.console import Console
from rich.panel import Panel
from utils import*
from functions.db_functions import*



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
        except ValueError, AttributeError:
            console.print("[red]Opção inválida, escolha uma das opções acima![/red]")
            time.sleep(2)
            continue


if __name__ == "__main__":
    criar_tabela()
    menu_inicial()
    product_table()        