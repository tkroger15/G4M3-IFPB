def main():
    cnt_beleza = 0
    verso_1 = input().split()[-1]
    verso_2 = input().split()[-1]
    verso_3 = input().split()[-1]
    verso_4 = input().split()[-1]

    for c in range(len(verso_1)):
        if verso_1[-(c+1)] == verso_3[-(c+1)]:
            cnt_beleza += 1
        else:
            break 

    for c in range(len(verso_2)):
        if verso_2[-(c+1)] == verso_4[-(c+1)]:
            cnt_beleza += 1
        else:
            break 
  
    print(cnt_beleza)
    
if __name__ == '__main__':
    main()