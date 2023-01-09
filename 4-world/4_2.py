def main():
    matriz = []
    cnt_mais = 0
    cnt_menos = 0
    cnt_o = 0 

    tamanho_matriz = int(input())
    orcs = ''

    for l in range(tamanho_matriz):
        coluna = [int(x) for x in input().split()] 
        matriz.append(coluna)

    for l in range(tamanho_matriz):
        for c in range(tamanho_matriz):
            if matriz[l][c] <= 90:
                orcs += '+'
                cnt_mais += 1
            elif matriz[l][c] > 90 and matriz[l][c] <= 100:
                orcs += 'o'
                cnt_o += 1 
            else:
                orcs += '-'
                cnt_menos += 1
        print(orcs)
        orcs = ''


    print(f'\n+: {cnt_mais}\no: {cnt_o}\n-: {cnt_menos}')
    
main()
