def main():
    pes_de_limoes = int(input())
    meloes = int(input())
    num_meloes = int(input())
    
    if pes_de_limoes * num_meloes > meloes:
        print('SIM')
    else:
        print('NAO')
    
if __name__ == "__main__":
  main()
