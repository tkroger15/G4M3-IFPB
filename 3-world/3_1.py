def main():
    pessoas_precisando_de_ajuda = int(input())
    lista_de_pessoas = []

    for c in range(pessoas_precisando_de_ajuda):
        pessoa = int(input())
        lista_de_pessoas.append(pessoa)

    lista_de_pessoas.sort()

    for c in range(len(lista_de_pessoas)):
        print(lista_de_pessoas[c])
    
if __name__ == '__main__':
    main()