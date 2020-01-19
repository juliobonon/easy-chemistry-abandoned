import tkinter as tk


# Norbixina #

abs = input("Digite a absorbancia?: ")
massa = input("Digite o valor da massa: ")

print(abs)
print(massa)

constante = 2870
ml_do_balão = 10000

resultado =  ( (float(abs) * ml_do_balão) / float(massa) ) / constante 

print(resultado)

# KOH #

titulação = input("Digite o valor da titulação:")
constante2 = 56.11

