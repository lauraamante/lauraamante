def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def main():
    print("Calculadora simples em Python")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", soma(a, b))
    elif escolha == '2':
        print("Resultado:", subtracao(a, b))
    elif escolha == '3':
        print("Resultado:", multiplicacao(a, b))
    elif escolha == '4':
        print("Resultado:", divisao(a, b))
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
