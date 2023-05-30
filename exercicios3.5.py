maior = None
menor = None
while True:
    num = input("Enter a number: ")
    if num == "done":
           if maior is None:
            maior = num
            for num in maior :
             if num > maior :
              maior = num
              print(num)
    print("Maximum", maior)
    print("Minimum", menor)
        
    break
    
 
        
    


