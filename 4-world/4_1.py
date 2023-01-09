def main():
    numero = int(input())
    lista_de_numeros = [numero]
  
    while numero > 1:
      numero = numero // 2
      lista_de_numeros.append(numero)
      
    print(len(lista_de_numeros))

if __name__ == "__main__":
  main()


