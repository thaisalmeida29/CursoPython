
hrs = input("Enter Hours:")
vlr = input("Enter Rate:")
try:
    h = float(hrs) 
    v = float(vlr)
except:
    print("Digite um número valido: ")
    quit()

print(h, v)

if h > 40 :
    tot = h * v
    t = (v - 40.0) * (h * 0.5)
    xp = tot + t
else:
    xp = h * v
print("Pay: " , xp)