from validations import*
import time
from rich.panel import Panel
from utils import*
from functions.db_functions import*
from functions.functions import*

# CADASTRAR O PRODUTO PARA VENDER

def sell_item(usuario):
    while True:
        limpar_terminal()
        console.print(Panel(
            "Cadastre o produto que você quer vender abaixo, é necessario inserir:\n"
            "Nome do produto\n"
            "Descrição do produto\n"
            "Preço do produto\n",
            title="[bold white]Área do vendedor - Vender produto[/bold white]",
            border_style="purple"
        ))
        nome = input("Nome do produto: ").strip()
        if not nome:
            console.print("[red]❌ O nome não pode ser vazio![/red]")
            time.sleep(2)
            continue
        
        descricao = input("Coloque uma descrição do produto: ")
        if not descricao:
            console.print("[red]❌ A descrição não pode ser vazia![/red]")
            time.sleep(2)
            continue
        
        try:
            preco = float(input("Coloque o preço do produto que você quer vender: R$ ").replace(",", "."))
            if preco <=0:
                console.print("O preço do produto precisa ser maior que 0")
                time.sleep(2)
                continue
        except ValueError:
            console.print("[red]Preço inválido, use números (exemplo R45.50[/red]")
            time.sleep(3)
            continue

        console.print(Panel(
            "Essas são as informações que você cadastrou:\n"
            f"{nome}"
            f"{descricao}\n"
            f"R${preco}",
            title="[bold white]Área do vendedor - Vender produto[/bold white]",
            border_style="purple"
        ))
        confirm = input("Deseja colocar o produto a venda?/(s ou n)")
        if confirm == "s":
            sucesso = save_product(nome, descricao, preco, usuario)
            if sucesso:
                console.print("[purple]O seu produto foi colocado a venda, obrigado![/purple]")
            time.sleep(2)
            break
        elif confirm == "n":
            console.print("[red]Cancelando a venda...[/red]")
            time.sleep(2)
            continue
        else:
            console.print("[red]Opção inválida! Digite s ou n[/red]")
            time.sleep(2)
            continue
