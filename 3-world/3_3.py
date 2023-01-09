def main():
    lista_meloes = []

    while True:
        meloes = input()
        
        if meloes == 'FIM':
            break 
    
        else:
            lista_meloes.append(meloes)
            print(f'{meloes} {lista_meloes.count(meloes)}')
            
main()