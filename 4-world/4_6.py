def main():
    tropa = [int(x) for x in input().split()]
    contar_turnos = 0
    
    while True:
        if tropa.count(1) == len(tropa):
            break
        else:
            for c in range(len(tropa)):
                if tropa[c] % 2 == 0 and tropa[c] > 1:
                    tropa[c] /= 2 
                elif tropa[c] % 2 != 0 and tropa[c] > 1:
                    tropa[c] += 1
                    
        contar_turnos += 1
    
    print(contar_turnos)

main()