def main():
    capacidade_pulmonar = int(input())
    
    while capacidade_pulmonar > 1:
        
        print(int(capacidade_pulmonar))
        
        if capacidade_pulmonar % 2 != 0:
            capacidade_pulmonar = (capacidade_pulmonar * 3) + 1 
        
        else:
            capacidade_pulmonar = capacidade_pulmonar / 2
    
    print(int(capacidade_pulmonar))
        

if __name__ == "__main__":
  main()

