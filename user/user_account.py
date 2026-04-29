from utils.validations import*
import time
from rich.console import Console
from rich.panel import Panel
from utils.utils import*
from database.db_functions import*
import maskpass


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
            console.print("[green]Email cadastrado com sucesso![/green]")
            time.sleep(2)
            break
        else:
            console.print("[red]Email não foi aceito, digite de acordo com o padrão pedido[/red]")
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
            console.print("[red] Erro ao ler a senha, evite caracteres com acentuação(ç, á, à...)[/red]")
            time.sleep(2)
            continue
        senha_validation , erro = validar_senha(senha)

        if senha_validation:
            try:
                confirm = maskpass.askpass("Crie uma senha: ", mask="*").strip()
            except Exception:
                console.print("[red] Erro ao ler a senha, evite caracteres com acentuação(ç, á, à...)[/red]")
                time.sleep(2)
                continue
            if confirm == senha:
                console.print("[green]Senha cadastrada![/green]")
                time.sleep(1)
                break
            else:
                console.print("[red]As senhas não são a mesma![/red]")
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
            console.print("[green]Nickname aceito![/green]")
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
                console.print("[green]Telefone aceito, conta cadastrada![/green]")
            else:
                console.print("[red]Já possui uma conta cadastrada com esse email ou nickname![/red]")
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
            from interfaces.user_menu import user_menu
            user_menu(usuario)
            break
        
        else:
            console.print(f"[red]❌ A senha não está correta![/red]")
            time.sleep(2)
            continue