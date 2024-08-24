#function declaration
import ply.lex as lex
import ply.yacc as yacc

reserved = {
    "function": 'FUNCTION',
    'print("hello world")': 'PRINT'
}

tokens = list(reserved.values()) + [
    'IDENTIFIER',
    'ASSIGN',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'NUMBER',
    'STRING',
    'LCURLY',
    'RCURLY'
]

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ASSIGN = r'<-'
t_LBRACKET = r'\('
t_RBRACKET = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_COMMA = r','
t_NUMBER = r'\d+'
t_STRING = r'("[^"]*"|\'[^\']*\')'

def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = reserved.get(t.value, "IDENTIFIER")
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_program(p):
    """program : S"""
    p[0] = p[1]

def p_S(p):
    """S : IDENTIFIER A"""
    p[0] = f"{p[1]} {p[2]}"

def p_A(p):
    """A : ASSIGN B"""
    p[0] = f"{p[1]} {p[2]}"

def p_B(p):
    """B : FUNCTION C"""
    p[0] = f"{p[1]} {p[2]}"

def p_C(p):
    """C : LBRACKET D RBRACKET E"""
    p[0] = f"{p[1]} {p[2]} {p[3]} {p[4]}"

def p_E(p):
    """E : LCURLY RCURLY"""
    p[0] = f"{p[1]} {p[2]}"




def p_D_single(p):
    """D : IDENTIFIER"""
    p[0] = p[1]

def p_D_multiple(p):
    """D : D COMMA D"""
    p[0] = (p[1], p[2], p[3])

def p_D_null(p):
    """D : """
    p[0] = None



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
print("Parsed result:",result)