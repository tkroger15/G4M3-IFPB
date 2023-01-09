def main():
    meloes_roubados = 0
    goblins_resgatados = 0
    forca_populacao = int(input())
    
    while True:
        forca_horda,  meloes_a_roubar, goblins_a_resgatar = input().split()
        forca_horda = int(forca_horda)
        meloes_a_roubar = int(meloes_a_roubar)
        goblins_a_resgatar = int(goblins_a_resgatar)
        
        if forca_horda == 0 and meloes_a_roubar == 0 and goblins_a_resgatar == 0:
            break 
        elif forca_horda > forca_populacao:
                meloes_roubados += meloes_a_roubar
                goblins_resgatados += goblins_a_resgatar 
        
        print(f'Meloes roubados: {meloes_roubados}\nGoblins resgatados: {goblins_resgatados}\n---')
        
if __name__ == "__main__":
  main()



