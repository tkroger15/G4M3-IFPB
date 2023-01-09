def main():
    n, e = input().split()
    n = int(n)
    e = int(e)
    sum = 0 
    
    for c in range(n):
        qnt = int(input())
        sum += qnt 
    
    if sum >= e:
        print(' NADA PREOCUPANTE')
    elif sum >= e - 5:
        print('POUCO PREOCUPANTE')
    else:
        print('MUITO PREOCUPANTE')
    
if __name__ == "__main__":
  main()

