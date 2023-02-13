import random

def print_line(size):
    print("\n" + "-=" * size + "\n")

def main():
    # Leitura dos valores de X e Y
    x = int(input("Digite o tamanho do primeiro vetor: "))
    y = int(input("Digite o tamanho do segundo vetor: "))
    
    # Inicialização dos vetores X e Y com números aleatórios não repetitivos
    max_value = x + y + 1
    x_list = random.sample(range(max_value), x)
    y_list = random.sample(range(max_value), y)
    
    # Impressão dos vetores X e Y
    print_line(30)
    print("Vetor X: ", x_list)
    print("Vetor Y: ", y_list)
    print_line(30)
    
    # Impressão dos números exclusivos do vetor X
    x_set = set(x_list)
    x_unique = list(x_set.difference(set(y_list)))
    print("Números exclusivos do vetor X: ", x_unique)
    print_line(30)
    
    # Impressão dos números exclusivos do vetor Y
    y_set = set(y_list)
    y_unique = list(y_set.difference(set(x_list)))
    print("Números exclusivos do vetor Y: ", y_unique)
    print_line(30)
    
    # Impressão dos números existentes nos dois vetores
    common = list(x_set.intersection(y_set))
    print("Números existentes nos vetores X e Y: ", common)

if __name__ == '__main__':
    main()
