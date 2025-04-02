import ply.lex as lex

tokens = ['INT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE']

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caráter inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
