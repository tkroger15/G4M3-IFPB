def main():
    n, r = input().split()
    lista_de_valores = [int(x) for x in input().split()] 
    n = int(n)
    r = int(r)
    
    for c in range(n):
        if lista_de_valores[c] <= r:
            print(1)
        else:
            print(0)

if __name__ == "__main__":
  main()







