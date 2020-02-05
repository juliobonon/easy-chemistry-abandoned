from tkinter import *

def calc(abs, massa):
    #resultado_liquido_combinado = ( ( ( ( float(abs) * 100 ) * 25 ) / 0.2) / float(massa) ) / 2870
    print(abs)
    print(massa)

def norbixina_window():
    window = Tk()
    window.title("Calculo de norbixina")
    window.geometry("300x300")
    abs_label = Label(window, text='Digite o abs:')
    abs_label.grid(row = 0, column=1)
    abs_input = Entry(window, bd = 5)
    abs_input.grid(row = 0, column=2)
    massa_label = Label(window, text='Digite a massa:')

    massa_label.grid(row = 1, column=1)
    massa_input = Entry(window, bd = 5)
    massa_input.grid(row = 1, column=2)
    window.mainloop()

def k0h_window():
    window = Tk()
    window.title("Calculo de koh")
    window.geometry("300x300")
    titulação_label = Label(window, text='Digite a titulação:')
    titulação_label.grid(row = 0, column=1)
    titulação_input = Entry(window, bd = 5)
    titulação_input.grid(row = 0, column=2)
    
    window.mainloop()

def liquido_combinado_window():
    window = Tk()
    window.title("Calculo de liquido combinado")
    window.geometry("300x300")
    abs1_label = Label(window, text='Digite o abs:')
    abs1_label.grid(row = 0, column=1)
    abs1_input = Entry(window, bd = 5)
    abs1_input.grid(row = 0, column=2)
    massa1_label = Label(window, text='Digite a massa:')
    massa1_label.grid(row = 1, column=1)
    massa1_input = Entry(window, bd = 5)
    massa1_input.grid(row = 1, column=2)

    
    massa = massa1_input.get()
    abs = abs1_input.get()


    botao = Button(window, text= 'yeet', command=calc(abs, massa))
    botao.grid(row = 2, column = 3)

    window.mainloop()


root = Tk()
root.title('Easy Chemistry')
norbixina_name = Label(root, text='Calculo de Norbixina')
norbixina_name.pack()
bt_norbixina = Button(root, width= 20, text='Calcular!', command=norbixina_window)
bt_norbixina.pack()
k0h_name = Label(root, text='Calculo de K0H')
k0h_name.pack()
k0h_button = Button(root, width= 20, text='Calcular!', command=k0h_window)
k0h_button.pack()
liquido_combinado_name = Label(root, text='Calculo de liquido combinado')
liquido_combinado_name .pack()
liquido_combinado_name_button = Button(root, width= 20, text='Calcular!', command=liquido_combinado_window)
liquido_combinado_name_button.pack()

root.mainloop()

# Norbixina #

def Norbixina():
    abs = input("Digite a absorbancia?: ")
    massa = input("Digite o valor da massa: ")
    #print(abs)
    #print(massa)
    norbixina =  ( (float(abs) * 10000) / float(massa) ) / 2870 
    print(norbixina)

def Koh():
    titulação = input("Digite o valor da titulação:")
    resultado_KOH = ( ( float(titulação) * 56.11 ) * 100 ) / 20.000
    print(resultado_KOH)

def Liquido_combinado():
    abs = input("Digite o abs:")
    massa_abs = input("Digite o valor da massa:")
    #resultado_liquido_combinado = ( ( ( ( float(abs) * 100 ) * 25 ) / 0.2) / float(massa_abs) ) / 2870
    print(resultado_liquido_combinado)


#print("Bem vindo ao Easy Chemistry!")
#print("\n")
#print(" 1. Calculo de Norbixina")
#print(" 2. Calculo de KOH")
#print(" 3. Calculo de liquido combinado")
#print("\n")
#opt = int(input("Escolha sua opção:"))

if (opt == 1):
    Norbixina()
elif(opt == 2):
    KOH()
elif(opt == 3):
    Liquido_combinado()
else:
    print("Opção invalida!")