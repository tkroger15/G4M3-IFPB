def main():
    limite_do_deposito = int(input())
    deposito = []
    
    while True:
        semente = int(input())
        if semente != 0:
            deposito.append(semente)
            if len(deposito) == limite_do_deposito:
                break 
        
        else:
            deposito.sort()
            print(deposito.pop())

if __name__ == "__main__":
  main()

