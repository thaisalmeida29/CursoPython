pontuacao = input("Digite uma pontuação: ")

try:
    p = float(pontuacao)
except:
    print("Digite números válidos entre 0.0 e 1.0")
    quit()

if p < 0.0 :
    print("Pontuação Inválida")
if p > 1.0 :
    print("Pontuação Inválida")

elif p >= 0.9 :
    print("A")

elif p >= 0.8 :
    print("B")

elif p >= 0.7 :
    print("C")

elif p >= 0.6 :
    print("D")

elif p < 0.6 :
    print("F")
