def main():
    num_nomes = int(input())
    lista_de_nomes = []
    for c in range(num_nomes):
      nome = input()
      if nome not in lista_de_nomes:
          lista_de_nomes.append(nome)
          
    for i in range(len(lista_de_nomes)):
        print(lista_de_nomes[i])

if __name__ == "__main__":
  main()
