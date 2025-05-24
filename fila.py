class Fila:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def enfileirar(self, item):
        self.items.append(item)
        print(f"Elemento '{item}' adicionado à fila.")

    def desenfileirar(self):
        if not self.esta_vazia():
            item = self.items.pop(0)
            print(f"Elemento '{item}' removido da fila.")
            return item
        else:
            print("A fila está vazia.")
            return None

    def tamanho(self):
        return len(self.items)

    def mostrar_fila(self):
        print("Fila atual:", self.items)

def main():
    fila = Fila()

    while True:
        print("\n1 - Enfileirar")
        print("2 - Desenfileirar")
        print("3 - Mostrar fila")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            item = input("Digite o elemento: ")
            fila.enfileirar(item)
        elif opcao == '2':
            fila.desenfileirar()
        elif opcao == '3':
            fila.mostrar_fila()
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
