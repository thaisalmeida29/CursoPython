largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        if largest is not None:
         print("Maximum is", largest)
        if smallest is not None:
         print("Minimum is", smallest)
        break
    try:
        num = int(num)
        if largest is None or num > largest:
          largest = num
        if smallest is None or num < smallest:
         smallest = num
    except:
     print("Invalid Input")
     
   
  
   
    