hrs = input("Enter Hours:")
tx = input("Enter Rate:")

def computepay(h, r):
    hrs = float(h)
    tx = float(r)

    if hrs <= 40:
        salario = hrs * tx
    else:
        txextra = hrs - 40
        salario = 40*tx+(txextra*(1.5*tx))
    return salario
   
p = computepay(hrs , tx)
print("Pay", p)