import re
import time
"""
Módulo de validações

Este módulo contém funções para validar diferentes tipos de entrada de usuário,
como emails, senhas, nomes de usuário e números de telefone, seguindo padrões específicos.
"""

def validar_email(email):
    """
    Valida um endereço de email.

    Verifica se o email segue o padrão específico da Universidade Federal Rural de Pernambuco (UFRPE):
    nome.sobrenome@ufrpe.br
    """
    email_padrao = r"^[a-zA-Z]+\.[a-zA-Z]+@ufrpe\.br$"
    return re.match(email_padrao, email)



def validar_senha(senha):
    """
    Valida uma senha com base em critérios específicos.

    A senha deve ter pelo menos 8 caracteres, incluir uma letra maiúscula, um número,
    um símbolo e não pode conter espaços ou caracteres acentuados.
    """
    erros = []
    if re.search(r"\s", senha):
        erros.append("❌ A senha não pode ter espaços")
    if re.search(r"[À-ÿ]", senha):
        erros.append("❌ A senha não pode ter caracteres acentuados")
    if not re.search(r"[A-Z]", senha):
        erros.append("❌ A senha precisa ter pelo menos uma letra maiúscula")
    if not re.search(r"[0-9]", senha):
        erros.append("❌ A senha precisa ter pelo menos um número")
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", senha):
        erros.append("❌ A senha precisa de pelo menos um símbolo")
    if len(senha) < 8:
        erros.append("❌ A senha precisa de pelo menos 8 caracteres")
    if erros:
        return False, "\n".join(erros)
    else:
        print("Senha válida, muito bom!")
        return True, None

def senha_min():
    """
    Exibe os requisitos mínimos para uma senha válida.

    Imprime uma mensagem informativa sobre os critérios de senha.
    """
    return print("""
Hora de criar a senha, ela precisa ter no mínimo:
    • 8 caracteres
    • 1 letra maiúscula (A-Z)
    • 1 símbolo (@#$%...)
    • 1 número (0-9)""")


def validar_user(user):
    """
    Valida um nome de usuário.

    O nome de usuário não pode conter espaços; use '_' se necessário.
    """
    erros = []
    if re.search(r"\s", user):
        erros.append("❌ O user não pode ter espaços, se quiser colocar um espaço use _")
    if erros:
        return False, "\n".join(erros)
    else:
        return True, None
    

def validar_tel(tel):
    """
    Valida um número de telefone brasileiro.

    O formato aceito é: (81) XXXXX-XXXX ou variações com espaços ou sem parênteses.
    """

    erros = []
    if not re.search(r"^\(?81\)?[\s-]?\d{4,5}-?\d{4}$", tel):
        erros.append("❌Telefone não é válido, precisa ser igual do padrão acima")
    if erros:
        return False, "\n".join(erros)
    else:
        return True, None