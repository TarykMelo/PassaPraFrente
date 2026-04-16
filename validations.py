import re
import time
"""
Validação de email
"""
def validar_email(email):
    email_padrao = r"^[a-zA-Z]+\.[a-zA-Z]+@ufrpe\.br$"
    return re.match(email_padrao, email)


"""
Validação de senha
"""
def validar_senha(senha):
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

#Requisitos da senha
def senha_min():
    return print("""
Hora de criar a senha, ela precisa ter no mínimo:
    • 8 caracteres
    • 1 letra maiúscula (A-Z)
    • 1 símbolo (@#$%...)
    • 1 número (0-9)""")

"""
Validação de usuário
"""

def validar_user(user):
    erros = []
    if re.search(r"\s", user):
        erros.append("❌ O user não pode ter espaços, se quiser colocar um espaço use _")
    if erros:
        return False, "\n".join(erros)
    else:
        return True, None
    
"""
Validação de telefone
"""

def validar_tel(tel):
    erros = []
    if not re.search(r"^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$", tel):
        erros.append("❌Telefone não é válido, precisa ser igual do padrão acima")
    if erros:
        return False, "\n".join(erros)
    else:
        return True, None