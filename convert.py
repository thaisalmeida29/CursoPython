#Convert elevator floors
#inp = input('Europe floor?')
#usf = int(inp) + 1
#print('US floor' , usf)

#Calcula o valor de horas trabalhadas
#hrs = input("Digite as horas: ")
#valor = input("Digite o valor por hora: ")
#total = float(hrs) * float(valor)
#print('Pay: ' , total)

#Trabalhando com try/except
#astr = 'Bob'
#try:
#   print('Hello')
#    istr = int(astr)
#    print('There')
#except:
#    istr = print(7)

#print('Done' , astr)


rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice Work')
else:
    print('Not a number')


