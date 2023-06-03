# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
     if not line.startswith("X-DSPAM-Confidence:") :    
      continue
     if line.startswith('X-DSPAM-Confidence:') :
       words = line.split()
       for word in words:
            if '.' in word:       
             value = float(word)
             total += value
             count += 1


if count > 0:
    average = total / count


# Print output
print('Average spam confidence:', average)

      

