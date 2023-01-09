def main():
    pos = 0 
    tiro = 0
    
    while True:
        campo = input().upper()
        if 'X' not in campo:
            break 
        
        else:
            if pos == 0:
                if campo[pos] == 'X':
                    print('Silêncio...')
                elif campo[pos] == 'O' and campo[pos + 1] == 'X': 
                    print('Tiro de Melão!!!')
                    tiro += 1
                elif campo[pos] == 'O' and campo[pos + 1] == 'O':
                    print(f'Correndo pro esconderijo {pos+1}!')
                    pos += 1
            
            elif pos == -1:
                if campo[pos] == 'X':
                    print('Silêncio...')
                elif campo[pos] == 'O' and campo[pos-1] == 'X': 
                    print('Tiro de Melão!!!')
                    tiro += 1
                elif campo[pos] == 'O' and campo[pos-1] == 'O':
                    print(f'Correndo pro esconderijo {pos-1}!')
                    pos -= 1
                    
            else:
                if campo[pos] == 'X':
                    print('Silêncio...') 
                elif campo[pos] == 'O' and campo[pos-1] == 'X' and campo[pos+1] == 'X':
                    print('Tiro de Melão!!!')
                    tiro += 1
                elif campo[pos] == 'O' and campo[pos-1] == 'X' and campo[pos+1] == 'O':
                    print(f'Correndo pro esconderijo {pos+1}!')
                    pos += 1 
                elif campo[pos] == 'O' and campo[pos-1] == 'O' and campo[pos+1] == 'X':
                    print(f'Correndo pro esconderijo {pos-1}!')
                    pos -= 1 
                elif campo[pos] == 'O' and campo[pos-1] == 'O' and campo[pos+1] == 'O':
                    print('Tiro de Melão!!!')
                    tiro += 1
                    
    print(f'Vitória com {tiro} melões!')

if __name__ == "__main__":
  main()
