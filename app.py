'''
x = 5
if x < 10 :
    print('oii')
if x > 10:
    print ('uhul')

n = 3
while n > 0:
    print(n)
    n = n - 1
print('isso ai')
'''
#Get the name of the file and open it.
name = input('Enter file:')
handle = open(name)

#Count word frequemcy
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

#Find the most common word
bigcount = None
bigword = None
for word, count in counts.items() :
    if bigcount is None or count > bigcount:
        bigword = word 
        bigcount = count

#Print the output
print(bigcount)
print(bigword)