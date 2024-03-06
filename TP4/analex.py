import ply.lex as lex
CODE = "Select id, nome, salário from empregados WHERE salário >= 820"

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'IDENTIFIER',
    'COMMA',
    'GREATER_EQUAL',
    'NUM'
)

t_COMMA = r','
t_GREATER_EQUAL = r'>='
t_IDENTIFIER = r'[A-Z_a-z]\w*'

def t_SELECT(t):
    r'[Ss][Ee][Ll][Ee][Cc][Tt]'
    t.value = t.value.upper()
    return t

def t_WHERE(t):
    r'[Ww][Hh][Ee][Rr][Ee]'
    t.value = t.value.upper()
    return t

def t_FROM(t):
    r'[Ff][Rr][Oo][Mm]'
    t.value = t.value.upper()
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
lexer.input(CODE)

for token in lexer:
    print(token)