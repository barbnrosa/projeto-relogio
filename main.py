from tkinter import *
import tkinter

# importando biblioteca para obter o horário do pc
from datetime import datetime

import pyglet
pyglet.font.add_file("digital-7.ttf")

# cores
cor1 = "#89004f"  # magenta
cor2 = "#ffe0ff"  # rosa clarinho
cor3 = "#5ff4ab"  # verde
cor4 = "#f70071"  # vermelha
cor5 = "#c33b80"  # rosa escuro
cor6 = "#6bb5ff"  # azul~
cor7 = "#ff69b4"  # rosa
cor8 = "#ffa8d9"  # rosa claro

fundo = cor1
cor = cor2

janela=Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)             # não altera o tamanho da janela principal
janela.configure(bg=cor1)

# datatime

def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)                                                  
    l2.config(text=dia_semana + "   " + str(dia) + "/" + str(mes) + "/" + str(ano))


l1 = Label(janela, text="", font=("digital-7 80"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)                                 # posicionar a label dentro da janela

l2 = Label(janela, text="", font=("digital-7 20"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5) 

relogio()
janela.mainloop()