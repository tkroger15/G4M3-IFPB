def main():
    matriz = []
    lista_linha = []
    lista_coluna = []
    cnt_essencia = cnt =0
    linha, coluna = input().split()
    linha = int(linha)
    coluna = int(coluna)

    for l in range(linha):
        list_coluna = [int(x) for x in input().split()] 
        matriz.append(list_coluna)
        
    for l in range(linha):
        for c in range(coluna):
            if matriz[l][c] == 1:
                cnt_essencia += 1 
                lista_coluna.append('M')
                cnt += 1
                break 
        if cnt > 0:
            cnt = 0
        else:
            lista_coluna.append('-')

    for c in range(coluna):
        for l in range(linha):
            if matriz[l][c] == 1:
                cnt_essencia += 1
                lista_linha.append('M')
                cnt += 1 
                break 
        if cnt > 0:
            cnt = 0
        else:
            lista_linha.append('-')
            
    print(cnt_essencia)

    for l in range(linha):
        print(*matriz[l], end=' ')
        print(lista_coluna[l])
    print(*lista_linha)

main()
