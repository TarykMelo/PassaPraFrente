## 📌 Sobre o projeto

O **PassaPraFrente** é uma plataforma desenvolvida em **Python** com o objetivo de facilitar a compra e venda de produtos entre estudantes e membros da **Universidade Federal Rural de Pernambuco (UFRPE)**.

Diferente de marketplaces abertos, o sistema é **fechado para o núcleo da universidade**, promovendo um ambiente mais seguro, confiável e acessível para negociações.

## 🎯 Objetivo

Criar um espaço digital onde usuários possam:

* 💰 Vender produtos de forma simples
* 🛍️ Comprar itens de outros usuários
* 🔒 Negociar dentro de um ambiente restrito à universidade
* ♻️ Facilidade para vender produto de forma segura e rápida

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* SQlite3

## 🏗️ Estrutura do Projeto

```bash
PassaPraFrente/
│
├── main.py                    # Arquivo principal
├── requirements.txt           # Dependências
├── README.md                  # Documentação
│
├── database/
│   ├── db_functions.py        # Operações do banco de dados
│   └── passaprafrente.db      # Banco SQLite
│
├── user/
│   ├── menus.py               # Menus principais
│   ├── user_account.py        # Cadastro e login
│   ├── user_changes.py        # Alteração de dados
│   │
│   ├── buyer/
│   │   ├── buyer_menu.py      # Menu do comprador
│   │   └── buyer_functions.py # Funções de compra
│   │
│   └── seller/
│       ├── seller_menu.py     # Menu do vendedor
│       └── seller_functions.py# Funções de venda
│
└── utils/
    ├── utils.py               # Funções utilitárias
    └── validations.py         # Validação de dados
```
## ⚙️ RELEASE 1.0

* 👤 Sistema de cadastro e login de usuários
* 📦 Cadastro de produtos para venda
* 🔍 Busca e visualização de produtos
* 🛒 Sistema de compra
* 📂 Organização por categorias
* 🔐 Acesso restrito a usuários da UFRPE

## 📚 Bibliotecas utilizadas

* rich -> Estilização do projeto inteiro
* time -> Controle do tempo que permanece na tela os avisos
* sqlite3 -> Banco de dados utilizado no projeto
* re -> Validação dos dados (email, senha, telefone)
* maskpass -> Ocultação de dados importantes do usuário
* os -> Biblioteca para interação com o sistema operacional

▶️ Como Executar
Clone o repositório:
```
git clone https://github.com/TarykMelo/PassaPraFrente.git
cd PassaPraFrente
```
Instale as dependências:
```
pip install -r requirements.txt
```
Execute:
```
python main.py
```

## 🔐 Público-alvo

Este sistema é destinado exclusivamente a:

🎓 Estudantes e membros da **UFRPE**



## 💡 RELEASE 2.0

* 🔧 Mais opções de personalização para o vendedor
* 🌐 Lançamento de um site
* ⭐ Sistema de avaliação de vendedores
* 💬 Chat entre compradores e vendedores
* 🛍️ Histórico de venda ou compra do produto


## 👨‍💻 Autor

Desenvolvido por **Taryk Melo**

* GitHub: https://github.com/TarykMelo

---
📌 Link do Fluxograma, planilha e video

https://drive.google.com/drive/u/2/folders/1hqp1vxdU2zF_4JHbeKrq4hTMdvCL3JUF
https://www.youtube.com/watch?v=-m3AzsgBPsk
