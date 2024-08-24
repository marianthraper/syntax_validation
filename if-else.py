#if-else ladder
import ply.lex as lex
import ply.yacc as yacc

reserved = {"if": 'IF', 'else': 'ELSE', 'print': 'PRINT'}
tokens = list(reserved.values()) + [
    'IDENTIFIER',
    'LBRACKET',
    'RBRACKET',
    'NUMBER',
    'STRING',
    'LCURLY',
    'RCURLY',
    'EQUALTO',
    'NOTEQUAL',
    'GREATER',
    'LESSER',
    'GREATEREQUAL',
    'LESSEREQUAL'
]

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LBRACKET = r'\('
t_RBRACKET = r'\)'
t_NUMBER = r'\d+'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_ignore = ' \t\n'
t_STRING = r'("[^"]*"|\'[^\']*\')'
t_EQUALTO = r'=='
t_NOTEQUAL = r'!='
t_GREATER = r'>'
t_LESSER = r'<'
t_GREATEREQUAL = r'>='
t_LESSEREQUAL = r'<='

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
    """S : IF LBRACKET A RBRACKET LCURLY B RCURLY ELSE LCURLY B RCURLY"""
    p[0] = ("if", p[3], p[6], "else", p[10])

def p_A1(p):
    """A : IDENTIFIER CMP IDENTIFIER"""
    p[0] = (p[1], p[2], p[3])

def p_A2(p):
    """A : IDENTIFIER CMP NUMBER"""
    p[0] = (p[1], p[2], p[3])

def p_A3(p):
    """A : NUMBER CMP IDENTIFIER"""
    p[0] = (p[1], p[2], p[3])

def p_A4(p):
    """A : NUMBER CMP NUMBER"""
    p[0] = (p[1], p[2], p[3])

def p_B(p):
    """B : PRINT LBRACKET D RBRACKET"""
    p[0] = ("print", p[3])

def p_D1(p):
    """D : IDENTIFIER"""
    p[0] = (p[1])

def p_D2(p):
    """D : NUMBER"""
    p[0] = (p[1])

def p_D3(p):
    """D : STRING"""
    p[0] = (p[1])

def p_CMP1(p):
    """CMP : EQUALTO"""
    p[0] = (p[1])

def p_CMP2(p):
    """CMP : NOTEQUAL"""
    p[0] = (p[1])

def p_CMP3(p):
    """CMP : GREATER"""
    p[0] = (p[1])

def p_CMP4(p):
    """CMP : LESSER"""
    p[0] = (p[1])

def p_CMP5(p):
    """CMP : GREATEREQUAL"""
    p[0] = (p[1])

def p_CMP6(p):
    """CMP : LESSEREQUAL"""
    p[0] = (p[1])

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