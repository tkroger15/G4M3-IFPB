def main():
  sensores = int(input())
  total = '0'
  
  for c in range(sensores):
      armadilha = input()
      total += armadilha 
      
  print(total.count('01'))

if __name__ == "__main__":
  main()


