print("Seja bem vindos ao programa de quiz da Thais")
answer_user = input("Quer começar? (S/N)")

if answer_user != "S":
    quit()

print("Começando...")    

print("Quem desenvolveu o jogo Grand Theft Auto (GTA) ? \n (A) (Rockstar Games) \n (B) (Ubisoft) \n (C) (EA) \n ")
answer1 = input(" Resposta: ")

if answer1 == "A":
    print("Correto!")
else:
    print("Incorreto!")    