import time
from rich.panel import Panel
from utils import*
from functions.db_functions import todos_produtos
from functions.seller_functions import*
from functions.user_functions import*
from functions.functions_main import*


# Função para ver todos os produtos disponiveis

def products_available(usuario):
    limpar_terminal()

    produtos = todos_produtos(usuario)

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
    
    for produto in produtos:
        texto +=(
            f"[bold]#{produto[0]} - {produto[1]}[/bold]\n"
            f"Descrição: {produto[2]}\n"
            f"Preço: R${produto[3]:.2f}\n"
            f"Vendedor: {produto[5]}\n"
            f"Telefone: {produto[6]}\n"
            f"{'-' * 40}\n"
        )
    console.print(Panel(
        texto,
        title="[bold white]Área do comprador - Todos os produtos[/bold white]",
        border_style="blue"
    ))
    input("Digite ENTER para voltar")