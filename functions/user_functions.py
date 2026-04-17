from validations import validar_senha, validar_tel
import time
from rich.panel import Panel
from utils import*
from functions.functions_main import*
from functions.db_functions import*
from functions.seller_functions import*
import maskpass

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


#Modificar o usuário
def user_modify(usuario):

    while True:
        limpar_terminal()
        console.print(Panel(
            "Dados atuais:\n"
            f"email: {usuario[1]}\n"
            f"Nickname: {usuario[3]}\n"
            f"Número de telefone: {usuario[4]}\n"
            f"[green]{'-' * 50}[/green]\n"
            "O que você deseja modificar da sua conta?\n"
            "[1] Nickname\n"
            "[2] Número de telefone\n"
            "[3] Senha\n"
            "[4] Voltar para o menu principal",
            title = "[bold white]Menu do usuário - Modificar dados[/bold white]",
            border_style= "green"
        ))
        try:

            user_choice = int(input("Digite a sua opção: ").strip())

            if user_choice == 1:
                nickname_modify(usuario)
                time.sleep(2)
                continue
            elif user_choice == 2:
                tel_modify(usuario)
                time.sleep(2)
                continue
            elif user_choice == 3:
               password_modify(usuario)
               continue
            elif user_choice == 4:
                console.print("[yellow]Voltando para o menu principal[/yellow]")
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

#Função para modificar a senha
def password_modify(usuario):
    while True:
        limpar_terminal()
        console.print(Panel(
            "Hora de criar a senha, ela precisa ter no mínimo:\n"
            "  • 8 caracteres\n"
            "  • 1 letra maiúscula (A-Z)\n"
            "  • 1 símbolo (@#$%...)\n"
            "  • 1 número (0-9)",
            title="[bold white]Menu do usuário - Modificar senha[/bold white]",
            border_style="green"
        ))
        
        senha_atual = maskpass.askpass("Digite a sua senha atual: ", mask="*").strip()
        valid_password = usuario[2]
        
        if senha_atual != valid_password:
            console.print("[red]Senha atual errada![/red]")
            time.sleep(2)
            continue
        
        nova_senha = maskpass.askpass("Digite a nova senha: ", mask="*").strip()
        senha_validation , erro = validar_senha(nova_senha)

        if senha_validation:
            confirm_senha = maskpass.askpass("Confirme a senha: ", mask="*").strip()
            
            if confirm_senha == nova_senha:
                confirm = input("Voce tem certeza que deseja colocar essa senaha nova?(s/n) ")
                if confirm == "s":
                    
                    #Abrindo o banco de dados para modificar a senha
                    conn = conectar()
                    cursor = conn.cursor()
                    cursor.execute("UPDATE usuario SET senha = ? WHERE id = ?",
                    (nova_senha, usuario[0]))
                    linhas_afetadas = cursor.rowcount # Entrar no banco de dados e ver se possui alguma mudança
                    conn.commit()
                    conn.close()
                    
                    if linhas_afetadas > 0:
                        console.print("[green]Senha atualizada com sucesso![/green]")
                        time.sleep(2)
                    else:
                        console.print("[red]Não foi possível atualizar a senha![/red]")
                    time.sleep(3)
                    return buscar_usuario(usuario[1])

                elif confirm == "n":
                    console.print("[yellow]Senha não foi modificada![/yellow]")
                    time.sleep(2)
                    break
                
                else:
                    console.print("[red]Somente s ou n é válido[/red]")
                    time.sleep(2)
                    continue
            else:
                console.print("[red]Senhas não coincidem![/red]")
                time.sleep(2)
                continue
        else:
            console.print(erro)
            time.sleep(2)
            continue

#Função para modificar o telefone
def tel_modify(usuario):
    while True:
        telefone = input("Digite o seu novo número de telefone: ")
        tel_validation, erro = validar_tel(telefone)

        if tel_validation:
            confirm = input(f"Voce tem certeza que esse é o telefone novo? - {telefone} (s/n) ")
            if confirm == "s":
                #Entrar no banco de dados para atualizar o telefone
                conn = conectar()
                cursor = conn.cursor()
                cursor.execute("UPDATE usuario SET telefone = ? WHERE id = ?",
                (telefone, usuario[0]))
                linhas_afetadas = cursor.rowcount # Entrar no banco de dados e ver se possui alguma mudança
                conn.commit()
                conn.close()
                
                if linhas_afetadas > 0:
                    console.print("[green]Número de telefone atualizado com sucesso![/green]")
                    time.sleep(2)
                else:
                    console.print("[red]Deu algum erro ao tentar modificar o número de telfone[/red]")
                time.sleep(3)
                return buscar_usuario(usuario[1])
            elif confirm == "n":
                console.print("[yellow]Telefone não foi modificado![/yellow]")
                time.sleep(2)
                break
            
            else:
                console.print("[red]Somente s ou n é válido[/red]")
                time.sleep(2)
                continue
        else:
            print(erro)
            time.sleep(2)
            continue

#Modificar o nickname do usuário
def nickname_modify(usuario):
    while True:
        nick = input("Digite o seu novo nickname: ").strip()

        if nick:
            confirm = input(f"Você quer colocar esse nickname mesmo? - {nick} (s/n) ")
            if confirm == "s":
                try:
                    #Entrar no banco de dados para atualizar o telefone
                    conn = conectar()
                    cursor = conn.cursor()
                    cursor.execute("UPDATE usuario SET nickname = ? WHERE id = ?",
                    (nick, usuario[0]))
                    linhas_afetadas = cursor.rowcount # Entrar no banco de dados e ver se possui alguma mudança
                    conn.commit()
                    conn.close()
                    
                    if linhas_afetadas > 0:
                        console.print("[green]Nickname atualizado com sucesso![/green]")
                        time.sleep(2)
                        break
                    
                    else:
                        console.print("[red]Deu algum erro ao tentar modificar o nickname[/red]")
                    time.sleep(3)
                    return buscar_usuario(usuario[1])
                
                except sqlite3.IntegrityError:
                    console.print("[red]Esse nickname já existe, tente outro por favor.[/red]")
                    time.sleep(2)
                    continue
            
            elif confirm == "n":
                console.print("[yellow]Nickname não foi modificado![/yellow]")
                time.sleep(2)
                break
            
            else:
                console.print("[red]Somente s ou n é válido[/red]")
                time.sleep(2)
                continue
        else:
            console.print("[red]Nickname não válido[/red]")
            time.sleep(2)
            continue