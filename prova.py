#Exercicio 1 / Escreva um código usando o método find e divisão de strings
text = "X-DSPAM-Confidence: 0.8475"
atpos = text.find('0.8475')
host = text[atpos:]
print(float(host))
