# syntax_validation
Syntax Validation of some R constructs using PLY tools in Python. AFLL Projects Ssem-3)
# Custom Language Parser and Interpreter

## Project Overview
This project focuses on developing a custom language parser and interpreter using Python's PLY (Python Lex-Yacc) library. The primary goal is to design a simple programming language with essential control structures, data types, and expressions. The parser and interpreter support fundamental constructs such as function declarations, list handling, conditional statements (if-else), loops (for), and switch-case statements.

## Key Features

### 1. Function Declaration
- Parse and interpret custom function declarations, including handling parameters and function bodies.

### 2. List Declaration
- Support for declaring lists with numeric, string, and null values, along with basic list operations.

### 3. Conditional Statements
- Implementation of if-else ladders to handle conditional logic within the custom language.

### 4. Loops
- Support for `for` loops, enabling iterative execution of code blocks.

### 5. Switch-Case Statements
- Implement switch-case constructs for multi-way branching, allowing different code paths based on specific conditions.

## Technical Details

- **Lexical Analysis:** Tokenization of input strings using PLY's lexer to identify keywords, identifiers, operators, and literals.
- **Syntax Analysis:** Parsing of tokenized input using PLY's parser to construct a syntax tree, defining the structure and semantics of the custom language.
- **Error Handling:** Basic error detection and handling for illegal characters and syntax errors.
- **Modularity:** Separate modules for each language feature, making the codebase easy to extend and maintain.

## Applications
This project serves as a foundational exercise in language design and compiler construction. It can be extended with more complex features such as additional data types, advanced control structures, and a runtime environment. The project is an excellent learning tool for understanding the principles of parsers, interpreters, and compiler design.

## Requirements

- Python 3.x
- PLY (Python Lex-Yacc)

---

*This project is a practical exploration of language design and compiler theory, implemented using Python.*
