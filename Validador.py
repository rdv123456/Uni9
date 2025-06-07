expressoes = [
    "(a+b)*(c-d)",     # Válida
    "((x+y)*(z/2))",   # Válida
    "(a+b)*c)",        # Inválida - parêntese a mais
    "((a+b)*(c-d)",    # Inválida - parêntese a menos
    "a++b",            # Inválida - operador duplicado
    "a+b*(c/d)",       # Válida
]

def validar_expressao(expressao: str) -> bool:
    pilha = []
    operadores = set("+-*/")
    operandos = set("abcdefghijklmnopqrstuvwxyz0123456789")
    ultimo = None  # 'op', 'num', '(', ')'

    for i, char in enumerate(expressao):
        if char == ' ':
            continue
        elif char == '(':
            pilha.append(char)
            ultimo = '('
        elif char == ')':
            if not pilha or pilha[-1] != '(':
                return False
            pilha.pop()
            if ultimo in ['op', '(']:
                return False
            ultimo = ')'
        elif char in operandos:
            if ultimo in ['num', ')']:
                return False
            ultimo = 'num'
        elif char in operadores:
            if ultimo not in ['num', ')']:
                return False
            ultimo = 'op'
        else:
            return False  # símbolo inválido

    return len(pilha) == 0 and ultimo not in ['op', None]

for exp in expressoes:
    print(f"{exp}: {'Válida' if validar_expressao(exp) else 'Inválida'}")
