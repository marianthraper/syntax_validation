#switch case
import ply.lex as lex
import ply.yacc as yacc

reserved = {"switch": 'SWITCH', 'print': 'PRINT'}
tokens = list(reserved.values()) + [
    'IDENTIFIER',
    'LBRACKET',
    'RBRACKET',
    'NUMBER',
    'STRING',
    'EQUALTO',
    'COMMA'
]

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACKET = r'\('
t_RBRACKET = r'\)'
t_NUMBER = r'\d+'
t_ignore = ' \t\n'
t_STRING = r'("[^"]"|\'[^\']\')'
t_EQUALTO = r'='
t_COMMA = r','



def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "IDENTIFIER")
    return t

def t_NUM(t):
    r"[0-9]+"
    t.type = reserved.get(t.value, "NUMBER")
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_S(p):
    """S : SWITCH LBRACKET A RBRACKET"""
    p[0] = "switch(" + p[3] + ")"

def p_A(p):
    """A : IDENTIFIER COMMA B"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + ', ' + p[3]

def p_B(p):
    """B : C"""
    p[0] = p[1]

def p_B1(p):
    """B : C COMMA B"""
    p[0] = p[1] + ', ' + p[3]

def p_C1(p):
    """C : STRING EQUALTO PRINT LBRACKET STRING RBRACKET"""
    p[0] = p[1] + '=' + "print(" + p[5] + ")"

def p_C2(p):
    """C : NUMBER EQUALTO PRINT LBRACKET STRING RBRACKET"""
    p[0] = p[1] + '=' + "print(" + p[5] + ")"

def p_C3(p):
    """C : STRING EQUALTO PRINT LBRACKET NUMBER RBRACKET"""
    p[0] = p[1] + '=' + "print(" + p[5] + ")"

def p_C4(p):
    """C : NUMBER EQUALTO PRINT LBRACKET NUMBER RBRACKET"""
    p[0] = p[1] + '=' + "print(" + p[5] + ")"

def p_C5(p):
    """C : STRING EQUALTO PRINT LBRACKET IDENTIFIER RBRACKET"""
    p[0] = p[1] + '=' + "print(" + p[5] + ")"

def p_C6(p):
    """C : NUMBER EQUALTO PRINT LBRACKET IDENTIFIER RBRACKET"""
    p[0] = p[1] + '=' + "print(" + p[5] + ")"

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error: missing token")

parser = yacc.yacc()


data = input("Enter expression: ")
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
result = parser.parse(data)
print("Parsed Result:",result)
