from validations import*
import time
from rich.panel import Panel
from utils import*
from functions.functions_main import*
from functions.db_functions import*
from functions.seller_functions import*

# Remover usuário
def user_remove(usuario):
    
    while True:
        limpar_terminal()
        console.print(Panel(
            "Voce tem certeza que deseja deletar a conta?(s/n)\n"
            "Digite a sua senha para confirmar",
            title = "[bold white]Menu do usuário - Remover conta[/bold white]",
            border_style= "red"
        ))
        
        confirm = input("Você tem certeza?")
        
        if confirm == "s":
            password = input("Senha: ")
            valid_password = usuario[2]

            if password not in valid_password:
                console.print("[red]Senha não está correta![/red]")
                time.sleep(2)
                continue
            else:
                remove_user(usuario)
                console.print("[red]Usuário removido, adeus...[/red]")
                time.sleep(3)
                break
        elif confirm == "n":
            console.print("[yellow]Obrigado por desistir de deletar a conta![/yellow]")
            time.sleep(1)
            break
        else:
            console.print("[red]Opção inválida, digite somente s ou n[/red]")
            time.sleep(1)
            continue

            