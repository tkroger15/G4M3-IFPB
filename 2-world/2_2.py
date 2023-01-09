def main():
    cnt_fadas = 0
    versos = int(input())
    
    for c in range(versos):
        atual_verso = input().lower()
        if 'fada' in atual_verso:
            cnt_fadas += 1 
    
    print(cnt_fadas)
    
if __name__ == "__main__":
  main()