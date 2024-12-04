# Função para calcular a expressão
def calcular_expressao(expressao):
    expressao = expressao.replace("+", " + ")
    expressao = expressao.replace("-", " - ")
    expressao = expressao.replace("/", " / ")
    expressao = expressao.replace("*", " * ")

    partes = expressao.split()
    
    
    n1 = float(partes[0])
    op = partes[1]
    n2 = float(partes[2])
    
    
    if  op == '+':
        return n1 + n2
    elif op  == '-':
        return n1 - n2
    elif op  == '*':
        return n1 * n2
    elif op  == '/':
        if  n2 != 0:
            return n1 / n2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"

expressao = input("Digite a expressão (ex: 5 + 3): ")


resultado = calcular_expressao(expressao)
print("Resultado:", resultado)