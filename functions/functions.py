import os
from validations import*
import time
from rich.panel import Panel
from utils import*
from functions.db_functions import*
from functions.seller_functions import*
    


def cadastro():
    limpar_terminal()

    #Digitar email
    while True:
        console.print(Panel(
            "Digite seu email institucional e crie uma senha para se cadastrar.",
            title="[bold green]Área de cadastro[/bold green]",
            border_style="green"
        ))
        email = input("Email institucional(nome.sobrenome@ufrpe.br): ").lower().strip()
        validation = validar_email(email)

        if validation:
            print("Email cadastrado com sucesso!")
            time.sleep(2)
            break
        else:
            print("Email não foi aceito, digite de acordo com o padrão pedido")
            time.sleep(2)


    #digitar senha        
    while True:
        limpar_terminal()
        console.print(Panel(
            "Hora de criar a senha, ela precisa ter no mínimo:\n"
            "  • 8 caracteres\n"
            "  • 1 letra maiúscula (A-Z)\n"
            "  • 1 símbolo (@#$%...)\n"
            "  • 1 número (0-9)",
            title="[bold white]Área de cadastro[/bold white]",
            border_style="green"
        ))
        senha = input("Crie uma senha: ").strip()
        senha_validation , erro = validar_senha(senha)

        if senha_validation:
            confirm = input("Confirme a sua senha: ").strip()
            if confirm == senha:
                print("Senha cadastrada!")
                time.sleep(1)
                break
            else:
                print("As senhas não são a mesma!")
                time.sleep(2)
        else:
            print(erro)
            time.sleep(2)
            continue

    #Digitar o nickname
    while True:
        limpar_terminal()
        console.print(Panel(
            "Escolha o seu nickname",
            title="[bold green]Área de cadastro[/bold green]",
            border_style="green"
        ))
        user = input("Crie um nickname: ").strip()
        user_confirm , erro = validar_user(user)

        if user_confirm:
            print("Nickname aceito!")
            time.sleep(1)
            break
        else:
            print(erro)
            time.sleep(2)
            continue

    #Digitar o telefone
    while True:
        limpar_terminal()
        console.print(Panel(
            "Digite o número do seu telefone(ex : (81)12344 5678)",
            title="[bold white]Área de cadastro[/bold white]",
            border_style="green"    
        ))
        
        tel = input("Número de telefone: ")
        tel_confirm, erro = validar_tel(tel)

        if tel_confirm:
            # salvar o cadastro no banco de dados
            success = salvar_usuario(email, senha, user, tel)
            if success:
                print("Telefone aceito, conta cadastrada!")
            else:
                print("Já possui uma conta cadastrada com esse email ou nickname!")
            time.sleep(2)
            break
        else:
            print(erro)
            time.sleep(2)
            continue

def login():
    while True:
        limpar_terminal()
        console.print(Panel(
            "Insira o seu email e senha para entrar",
            title="[bold white]Área de login[/bold white]",
            border_style="green"
        ))
        email = input("Insira o seu email: ").lower().strip()
        senha = input("Insira a sua senha: ").strip()

        usuario = buscar_usuario(email)
        
        if usuario is None:
            console.print("[red]❌ Email está incorreto![/red]")
            time.sleep(2)
            continue
        
        senha_hash = usuario[2]

        if bcrypt.checkpw(senha.encode(), senha_hash):
            console.print(f"[green]Bem-vindo, {usuario[3]}![/green] ")
            time.sleep(2)
            user_menu(usuario)
            break
        else:
            console.print(f"[red]❌ A senha não está correta![/red]")
            time.sleep(2)
            continue


#Menu do usuário

def user_menu(usuario):
    while True:
        limpar_terminal()
        
        console.print(Panel(
            f"Bem-vindo {usuario[3]}\n"
            "[1] Vender item\n"
            "[2] Comprar item\n"
            "[3] Modificar os dados do usuário\n"
            "[4] Sair",
            title="[bold white]Menu do usuário[/bold white]",
            border_style="green"
        ))

        user_choice = int(input("Digite a sua opção: "))

        if user_choice == 1:
            console.print("[green]Vamos vender![/green]")
            seller_menu(usuario)
            time.sleep(2)
            break
        elif user_choice == 2:
            console.print("[green]Hora de comprar![/green]")
            time.sleep(2)
            break
        elif user_choice == 3:
            console.print("[green]Indo acessar os dados pessoais...[/green]")
            time.sleep(2)
            break
        elif user_choice == 4:
            console.print("[red]Saindo...[/red]")
            time.sleep(2)
            break
        else:
            console.print("[red]Opção inválida, escolha uma das opções acima![/red]")
            time.sleep(2)
            continue


#Menu do vendedor

def seller_menu(usuario):
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

        user_choice = int(input("Digite a sua opção: "))

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