for i in [5, 4, 3, 2, 1] :
    print(i)
print("Uhuul")


n = 5
while n > 0 :
    print(n)
    n = n - 1
print("Uhuul")
print(n)


friends = ['Thais', 'Anna', 'Maitê']
for friend in friends :
    print("Olá, seja bem vinda:", friend)

print("Done")

#Encontrando o maior valor

largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
        print(largest_so_far, the_num)
print("After", largest_so_far)

zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print("After:", zork )

count = 0
sum = 0
print("Before:", count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After:", count, sum, sum / count)

print("Before")
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20 :
        print("Large number:", value)
print("After")

found = False
print("Before", found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(found, value)
print("After:", found)
#Encontrar o menor numero
#None é um flag value que é um valor de bandeira para identificar nenhum valor
smallest = None
print("Before", smallest)
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print("After: ", smallest)    


tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)


if smallest is None :
     smallest = value