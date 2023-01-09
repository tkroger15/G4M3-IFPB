def main():
    criptografada = input()
    retire = 'P'
    
    for c in range(len(retire)):
        if 'PPP' not in criptografada:
            criptografada = criptografada.replace(retire[c], '')
        else:
            criptografada = criptografada.replace('PPP', '--')
            criptografada = criptografada.replace(retire[c], '')
    
    criptografada = criptografada.replace('--', 'P')
    print(criptografada)

if __name__ == "__main__":
  main()