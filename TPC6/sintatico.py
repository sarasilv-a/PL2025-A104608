import ply.yacc as yacc
import sys
from lexico import tokens

def p_start(p):
    """
    Start : ExprAS
    """
    print("Expression value:", p[1])

def p_expr_add(p):
    """
    ExprAS : ExprAS PLUS ExprMD
    """
    p[0] = p[1] + p[3]

def p_expr_sub(p):
    """
    ExprAS : ExprAS MINUS ExprMD
    """
    p[0] = p[1] - p[3]

def p_expr_base(p):
    """
    ExprAS : ExprMD
    """
    p[0] = p[1]

def p_expr_mul(p):
    """
    ExprMD : ExprMD TIMES Factor
    """
    p[0] = p[1] * p[3]

def p_expr_div(p):
    """
    ExprMD : ExprMD DIVIDE Factor
    """
    p[0] = p[1] / p[3]

def p_exprmd_base(p):
    """
    ExprMD : Factor
    """
    p[0] = p[1]

def p_factor_num(p):
    """
    Factor : INT
    """
    p[0] = p[1]

def p_error(p):
    print("Erro sintático:", p)
    parser.success = False

parser = yacc.yacc()

for linha in sys.stdin:
    parser.success = True
    parser.parse(linha)
    if parser.success:
        print("Valid:", linha.strip())
    else:
        print("Invalid sentence.")