from utils.validations import*
import time
from rich.panel import Panel
from utils.utils import*
from functions.db_functions import*
from functions.functions_main import*

"""
Módulo seller_functions

Este módulo contém funções relacionadas às operações do vendedor
Inclui funcionalidades para cadastrar produtos para venda e gerenciar produtos já cadastrados,
como visualizar e remover produtos.
"""

# Dicionário de categorias disponíveis para produtos
CATEGORIAS = {
    "1": "Eletrônicos",
    "2": "Livros",
    "3": "Roupas",
    "4": "Móveis",
    "5": "Esportes",
    "6": "Outros"
}


def sell_item(usuario):
    """
    Permite ao vendedor cadastrar um novo produto para venda.

    Esta função guia o usuário através de um processo interativo para inserir
    detalhes do produto (nome, descrição, preço, local, categoria), valida as
    entradas, confirma os dados e salva o produto no banco de dados se aprovado.
    """
    while True:
        limpar_terminal()
        console.print(Panel(
            "Cadastre o produto que você quer vender abaixo, é necessario inserir:\n"
            "1. Nome do produto\n"
            "2. Descrição do produto\n"
            "3. Preço do produto\n"
            "4. Local de venda\n"
            "5. Categoria\n",
            title="[bold white]Área do vendedor - Vender produto[/bold white]",
            border_style="purple"
        ))
        #Nome do produto
        nome = input("Nome do produto: ").strip()
        if not nome:
            console.print("[red]❌ O nome não pode ser vazio![/red]")
            time.sleep(2)
            continue
        #Descrição do produto
        descricao = input("Coloque uma descrição do produto: ")
        if not descricao:
            console.print("[red]❌ A descrição não pode ser vazia![/red]")
            time.sleep(2)
            continue
        #Colocar o preço do produto
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

        #Colocar o local de venda    
        local_de_venda = input("Local da UFRPE e horário (exemplo: CEAGRI, 17h-18h)")

        if not local_de_venda:
            console.print("[red]Você precisa digitar alguma coisa![/red]")
            time.sleep(2)
            continue

        #Adicionar a categoria
        limpar_terminal()
        console.print(Panel(
            "Que categoria o seu produto se encaixa?\n"
            "[1] Eletrônicos\n"
            "[2] Livros\n"
            "[3] Roupas\n"
            "[4] Móveis\n"
            "[5] Esportes\n"
            "[6] Outros",
            title="[bold white]Área do vendedor - Vender produto[/bold white]",
            border_style="purple"
        ))

        escolha_cat = input("Escolha a categoria: ").strip()
        if escolha_cat not in CATEGORIAS:
            console.print("[red]Escolha uma das categorias disponíveis![/red]")
            time.sleep(2)
            continue

        categoria = CATEGORIAS[escolha_cat]

        #Confiramção do produto, sim salva no banco de dados, não volta pro menu de vendedor
        console.print(Panel(
            "Essas são as informações que você cadastrou:\n"
            f"Nome: {nome}"
            f"Descrição: {descricao}\n"
            f"Preço: R${preco:.2f}\n"
            f"Local e horário: {local_de_venda}\n"
            f"Caegoria: {categoria}",
            title="[bold white]Área do vendedor - Vender produto[/bold white]",
            border_style="purple"
        ))
        confirm = input("Os dados estão corretos?/(s ou n)")
        if confirm == "s":
            sucesso = save_product(nome, descricao, preco, local_de_venda, categoria, usuario)
            if sucesso:
                console.print("[purple]O seu produto foi colocado a venda, obrigado![/purple]")
            time.sleep(2)
            break
        elif confirm == "n":
            console.print("[red]Cancelando a venda...[/red]")
            time.sleep(2)
            break
        else:
            console.print("[red]Opção inválida! Digite s ou n[/red]")
            time.sleep(2)
            continue

def seller_products(usuario):
    """
    Exibe os produtos cadastrados pelo vendedor e permite remover produtos.

    Esta função lista todos os produtos do vendedor, oferece opções para remover
    um produto específico ou voltar ao menu anterior. Inclui validações para
    garantir que o produto existe antes de tentar removê-lo.
    """
    while True:
        limpar_terminal()
        produtos = meus_produtos(usuario)

        if not produtos:
            console.print(Panel(
                "[red]Nenhum produto cadastrado ainda![/red]",
                title="[bold white]Área do vendedor - Meus produtos[/bold white]",
                border_style="purple"
                ))
            time.sleep(3)
            break
        texto = ""
        for produto in produtos:
            texto +=(
                f"[bold]#{produto[0]} - {produto[1]}[/bold]\n"
                f"Descrição: {produto[2]}\n"
                f"Preço: R${produto[3]:.2f}\n"
                f"Local e horário: {produto[4]}\n"
                f"Categoria: {produto[5]}\n"
                f"{'-' * 40}\n"
            )
        console.print(Panel(
            texto,
            title="[bold white]Área do vendedor - Meus produtos[/bold white]",
            border_style="purple"
        ))

        console.print("[purple][1] Remover algum produto\n[/purple]" \
        "[purple][2] Voltar[/purple]")

        try:
            option = int(input("Escolha a opção: ").strip())
            
            if option == 1:
                while True:
                    console.print("Escolha qual produto você quer retirar")
                    try:

                        produto_id = int(input("Digite o # do produto que você quer remover: ").strip())

                        id_valido = [produto[0] for produto in produtos]

                        if produto_id not in id_valido:
                            console.print("[red]Produto não foi encontrado![/red]")
                            time.sleep(2)
                            continue

                        confirm = input(f"Produto encontrado! #{produto_id} Tem certeza que deseja deletar ele?(s ou n):").lower().strip()

                        if confirm == "s":
                            remove_product(produto_id, usuario)
                            console.print("[green]Produto removido com sucesso![/green]")
                            time.sleep(2)
                            break
                        elif confirm == "n":
                            console.print("[yellow]Cancelado![/yellow]")
                            time.sleep(2)
                            break
                        else:
                            console.print("Escolha s ou n")
                            time.sleep(2)

                    except ValueError:
                        print("[red]Opção inválida![/red]")
                        time.sleep(2)
                
            elif option == 2:
                console.print("[purple]Voltar para a área de vendedor[/purple]")
                time.sleep(1)
                break
            else:
                console.print("[red]Opção inválida! digite 1 ou 2[/red]")
                time.sleep(2)
                continue
        except ValueError:
            console.print("[red]Opção inválida! digite 1 ou 2[/red]")
            time.sleep(2)
            continue

