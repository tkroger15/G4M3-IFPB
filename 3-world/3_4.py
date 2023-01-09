def main():
    fila = []
    
    while True:
        pessoa = input()
        if pessoa == 'FIM':
            break 
        
        elif pessoa == 'PROXIMO':
            print(f'PROXIMO: {fila.pop(0)}')
            
        else:
            fila.append(pessoa)
            print('FILA:', *fila )

if __name__ == "__main__":
  main()
