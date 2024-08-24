#for loop
import ply.lex as lex
import ply.yacc as yacc

reserved = {'for': 'FOR', 'in': 'IN', 'print': 'PRINT'}
tokens = list(reserved.values()) + [
    'IDENTIFIER',
    'LBRACKET',
    'RBRACKET',
    'NUMBER',
    'STRING',
    'LCURLY',
    'RCURLY',
    'COLON',
    'MINUS'
]

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACKET = r'\('
t_RBRACKET = r'\)'
t_NUMBER = r'\d+'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_ignore = ' \t\n'
t_STRING = r'("[^"]*"|\'[^\']*\')'
t_COLON = r':'
t_MINUS = r'-'


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


def p_S1(p):
    """S : FOR LBRACKET IDENTIFIER IN NUMBER COLON NUMBER RBRACKET LCURLY B RCURLY"""
    p[0] = ('for', p[3], 'in', (p[5], p[6], p[7]), p[8], p[9], p[10],p[11])  # Include both numbers and the colon
def p_S2(p):
    """S : FOR LBRACKET IDENTIFIER IN MINUS NUMBER COLON NUMBER RBRACKET LCURLY B RCURLY"""
    p[0] = ('for', p[3], 'in', (p[5], p[6], p[7]), p[8], p[9], p[10],p[11])

def p_S3(p):
    """S : FOR LBRACKET IDENTIFIER IN NUMBER COLON MINUS NUMBER RBRACKET LCURLY B RCURLY"""
    p[0] = ('for', p[3], 'in', (p[5], p[6], p[7]), p[8], p[9], p[10],p[11])

def p_S4(p):
    """S : FOR LBRACKET IDENTIFIER IN MINUS NUMBER COLON MINUS NUMBER RBRACKET LCURLY B RCURLY"""
    p[0] = ('for', p[3], 'in', (p[5], p[6], p[7]), p[8], p[9], p[10],p[11])

def p_B1(p):
    """B : S"""
    p[0] = p[1]  # Pass the result up the tree


def p_B2(p):
    """B : C"""
    p[0] = p[1]  # Pass the result up the tree


def p_C(p):
    """C : PRINT LBRACKET D RBRACKET"""
    p[0] = ('print', p[3])  # Return a tuple with parsed information


def p_D1(p):
    """D : IDENTIFIER"""
    p[0] = ( p[1])  # Return a tuple with parsed information


def p_D2(p):
    """D : NUMBER"""
    p[0] = ( p[1])  # Return a tuple with parsed information


def p_D3(p):
    """D : STRING"""
    p[0] = ( p[1])  # Return a tuple with parsed information


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
print("Parsed Result:", result)