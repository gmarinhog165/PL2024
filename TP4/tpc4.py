# SELECT id,nome,salara
# from empregados
# where salario >= 820

# SPACES, OPERATOR, VAR, CONDS, INT

import ply.lex as lex

tokens = (
    'OPERATOR',
    'VAR',
    'CONDS',
    'INT',
)

t_OPERATOR = r'\b(?i:select)\b|\b(?i:from)\b|\b(?i:where)\b'
t_INT = r'\d+'
t_VAR =  r'\w+'
t_CONDS = r'[\<\>]=?'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = """
SELECT id,nome,salarios
from empregados
Where salario >= 820"""

lexer.input(data)

for tok in lexer:
    #print(tok)
    print( tok.value, tok.lexpos, tok.lineno)