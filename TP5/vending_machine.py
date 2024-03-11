import ply.lex as lex
import json

with open('db.json', 'r', encoding='utf-8') as file_in:
    db = json.load(file_in)    

tokens = (
    'LISTAR',
    'MOEDA',
    'SALDO',
    'SELECIONAR',
    'SAIR',
    'ID',
    'COIN',
    'COMMA'
)

states = (('moeda','exclusive'),('selecionar', 'exclusive'),)

def t_LISTAR(t):
    r'LISTAR'
    for product in db:
        print(f"< {product['id']}   {product['nome']}   {product['preco']}")
    return t

def t_MOEDA(t):
    r'MOEDA'
    t.lexer.begin('moeda')
    return t

def t_ANY_SALDO(t):
    r'SALDO'
    print(f"> SALDO = {round((t.lexer.saldo),2)}€")
    return t

def t_SELECIONAR(t):
    r'SELECIONAR'
    t.lexer.begin('selecionar')
    return t

def t_SAIR(t):
    r'SAIR'
    return t

def t_selecionar_ID(t):
    r'\d+'
    valor = 0
    for product in db:
        if product['id'] == int(t.value):
            valor = product['preco']
    if(t.lexer.saldo > valor):  
        t.lexer.saldo -= valor
    else:
        print('Saldo não suficiente')
    print(f"> SALDO = {round(t.lexer.saldo,2)}€")
    return t

def t_moeda_COIN(t):
    r'\d+c|\d+e'
    if 'e' in t.value:
        t.lexer.saldo += int(t.value[:-1])
    else:
        t.lexer.saldo += (int(t.value[:-1])/100)
    return t

def t_ANY_COMMA(t):
    r','
    pass
    
def t_ANY_newline(t):
    r'\n+'
    t.lexer.begin('INITIAL')
    t.lexer.lineno += len(t.value)

t_ANY_ignore  = ' \t'

def t_ANY_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.saldo = 0.0

try:
    while True:
        entrada = input(">> ") + '\n'
        lexer.input(entrada)
        while True:
            tok = lexer.token()
            if not tok:
                break  # Não há mais tokens
            if tok.value == 'SAIR':
                print(f"< TROCO {lexer.saldo}€")
                raise EOFError
except EOFError:
    print("VOLTE SEMPRE")