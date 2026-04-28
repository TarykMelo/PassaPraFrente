from utils.validations import*
import time
from rich.panel import Panel
from utils.utils import*
from functions.db_functions import*
from functions.seller_functions import*
from functions.user_functions import*
import maskpass
from functions.buyer_functions import*
    
"""
Módulo functions_main

Este módulo contém as funções principais, incluindo
cadastro de usuários, login, e menus de navegação para vendedores e compradores.
Gerencia o fluxo principal da aplicação e interações com o usuário.
"""

def cadastro():
    """
    Realiza o cadastro de um novo usuário no sistema.

    Esta função guia o usuário através do processo de cadastro, solicitando
    email institucional, senha, nickname e telefone, com validações em cada etapa.
    Salva os dados no banco se todas as validações passarem.
    """

    #Digitar email
    while True:
        limpar_terminal()
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
        try:
            senha = maskpass.askpass("Crie uma senha: ", mask="*").strip()
        except Exception:
            console.print("[red]❌ Erro ao ler a senha, evite caracteres com acentuação(ç, á, à...)[/red]")
            time.sleep(2)
            continue
        senha_validation , erro = validar_senha(senha)

        if senha_validation:
            confirm = maskpass.askpass("Confirme a sua senha: ", mask="*").strip()
            if confirm == senha:
                print("Senha cadastrada!")
                time.sleep(1)
                break
            else:
                print("As senhas não são a mesma!")
                time.sleep(2)
                continue
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
    """
    Realiza o login de um usuário existente.

    Solicita email e senha, verifica se o usuário existe e se a senha está correta.
    Se válido, direciona para o menu do usuário.
    """
    while True:
        limpar_terminal()
        console.print(Panel(
            "Insira o seu email e senha para entrar",
            title="[bold white]Área de login[/bold white]",
            border_style="green"
        ))
        email = input("Insira o seu email: ").lower().strip()

        try:
            senha = maskpass.askpass("Insira a sua senha: ", mask="*").strip()
        except Exception:
            console.print("[red]❌ Erro ao ler a senha, evite caracteres com acentuação(ç, á, à...)[/red]")
            time.sleep(2)
            continue
        usuario = buscar_usuario(email)
        
        if usuario is None:
            console.print("[red]❌ Email está incorreto![/red]")
            time.sleep(2)
            continue
        
        if senha == usuario[2]:
            console.print(f"[green]Bem-vindo, {usuario[3]}![/green] ")
            time.sleep(2)
            user_menu(usuario)
            break
        
        else:
            console.print(f"[red]❌ A senha não está correta![/red]")
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
                products_available(usuario)
                continue
            elif user_choice == 2:
                console.print("[green]Acessando as categorias disponiveis[/green]")
                time.sleep(1)
                filtrar_produto()
                continue
            elif user_choice == 3:
                console.print("[green]Acessando os produtos que você escolheu![/green]")
                time.sleep(1)
                continue
            elif user_choice == 4:
                console.print("[green]Voltando para o menu principal...[/green]")
                time.sleep(1)
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