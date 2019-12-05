import tkinter as tk
from funcoes import *
from string import ascii_lowercase
from tkinter import messagebox
import random
# LIMPEZA
LARGE_FONT= ("Verdana", 18)



################################################
############### CLASSE (MASTER) ################
################################################
class Master(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.title("Jogo da Forca")
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
# AQUI É SÓ COLOCAR NESSE FOR SE QUISER ADICIONAR UMA PÁGINA NOVA
        for F in (Home, A_D_J, M_D_J, O_P_F, O_NP_F, Ajuda, P_F, Creditos, Colaboradores, Agradecimentos, R_B, Iniciar_al, Iniciar_fac,
                  Iniciar_med, Iniciar_dif, Dificuldade, Dicionario, C_D, pal_pad, pal_add, add_pal,
                  exc_pal, Jogar_al, Jogar_fac, Jogar_med, Jogar_dif):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

# FUNÇÃO QUE MUDA O FRAME
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

################################################
############## CLASSES(SUB) ####################
##############   (PÁGINAS)  ####################
################################################

# Home #    
class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Jogo da Forca", font=LARGE_FONT).pack(pady=10,padx=10)
        
        btn1 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Apresentação do jogo",
                         command=lambda: controller.show_frame(A_D_J)).pack()
        
        btn2 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Iniciar",
                         command=lambda: controller.show_frame(Iniciar_al)).pack()
        
        btn3 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Dicionário de palavras",
                         command=lambda: controller.show_frame(Dicionario)).pack()
        
        btn4 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Ajuda",
                         command=lambda: controller.show_frame(Ajuda)).pack()
        
        btn5 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Créditos",
                         command=lambda: controller.show_frame(Creditos)).pack()
        
        btn_saida = tk.Button(self, width=25, height=2, bg="indianred" , fg="Black", text="Sair do jogo",
                         command=lambda: quit()).pack()
        
# Apresentação do jogo #
class A_D_J(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Apresentação do jogo", font=LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Mecânicas do jogo",
                         command=lambda: controller.show_frame(M_D_J)).pack()
        
        btn2 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="O que se pode fazer",
                         command=lambda: controller.show_frame(O_P_F)).pack()
        
        btn3 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="O que não se pode fazer",
                         command=lambda: controller.show_frame(O_NP_F)).pack()
        
        btn_saida = tk.Button(self, width=25, height=2, text="Anterior", bg="indianred", fg="black",
                         command=lambda: controller.show_frame(Home)).pack()

# Mecânicas do jogo #
class M_D_J(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Mecânicas do jogo", font=LARGE_FONT).pack(pady=10,padx=10)
        f = open("mecanicas.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self,  width=25, height=2, text="Anterior", bg="indianred", fg="black",
                        command=lambda: controller.show_frame(A_D_J)).pack(side="bottom", anchor="sw")

# O que pode ser feito #
class O_P_F(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="O que se pode fazer", font=LARGE_FONT).pack(pady=10,padx=10)

        f = open("o_p_f.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=25, height=2, text="Anterior", bg="indianred", fg="black",
                              command=lambda: controller.show_frame(A_D_J)).pack (side="bottom", anchor="sw")

# O que não pode ser feito #
class O_NP_F(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="O que não se pode fazer", font=LARGE_FONT).pack(pady=10,padx=10)
        
        f = open("o_np_f.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=25, height=2, text="Anterior", bg="indianred", fg="black",
                              command=lambda: controller.show_frame(A_D_J)).pack (side="bottom", anchor="sw")

###########

# INICIAR #
class Iniciar_al(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Iniciar", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Dificuldades (Aleatório)",
                         command=lambda: controller.show_frame(Dificuldade)).pack()
        btn2 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Iniciar",
                         command=lambda: controller.show_frame(Jogar_al)).pack()
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                         command=lambda: controller.show_frame(Home)).pack ()

class Iniciar_fac(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Iniciar", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Dificuldades (Fácil)",
                         command=lambda: controller.show_frame(Dificuldade)).pack()
        
        btn2 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Iniciar",
                         command=lambda: controller.show_frame(Jogar_fac)).pack()
        
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                         command=lambda: controller.show_frame(Home)).pack ()

class Iniciar_med(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Iniciar", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Dificuldades (Média)",
                         command=lambda: controller.show_frame(Dificuldade)).pack()
        
        btn2 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Iniciar",
                         command=lambda: controller.show_frame(Jogar_med)).pack()
        
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                              command=lambda: controller.show_frame(Home)).pack()

class Iniciar_dif(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Iniciar", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Dificuldades (Difícil)",
                         command=lambda: controller.show_frame(Dificuldade)).pack()
        
        btn2 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Iniciar",
                         command=lambda: controller.show_frame(Jogar_dif)).pack()
        
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                         command=lambda: controller.show_frame(Home)).pack ()

# Dificuldade #
class Dificuldade(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, relief="groove", height= 3, text="Dificuldade", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Aleatória",
                         command=lambda: controller.show_frame(Iniciar_al)).pack()
        
        btn2 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Fácil",
                         command=lambda: controller.show_frame(Iniciar_fac)).pack()
        
        btn3 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Média",
                         command=lambda: controller.show_frame(Iniciar_med)).pack()
        
        btn4 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Difícil",
                         command=lambda: controller.show_frame(Iniciar_dif)).pack()
        
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                         command=lambda: controller.show_frame(Iniciar_al)).pack()
#   JOGAR    #
class Jogar_al(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        arq_pad = open("pad_al.txt","r")
        arq_add = open("add_al.txt","r")
        
        lista_pad = transfLista(arq_pad)
        lista_add = transfLista(arq_add)
        
        lista = list(lista_pad) + list(lista_add)
        lista_palavras_al = tira_n_line(lista)
        
        
        photos = [tk.PhotoImage(file="0_erro.png"),tk.PhotoImage(file="1_erro.png"),tk.PhotoImage(file="2_erro.png"),
                  tk.PhotoImage(file="3_erro.png"),tk.PhotoImage(file="4_erro.png"),tk.PhotoImage(file="5_erro.png"),
                  tk.PhotoImage(file="6_erro.png")]

        def newGame():
            global palavra_underline_al
            global erros
            erros = 0
            imgLabel.config(image=photos[0])
            palavra = random.choice(lista_palavras_al)
            
            palavra_underline_al = " ".join(palavra)
            lblWord.set(" ".join("_"*len(palavra)))

        def guess(letter):
            global erros
            if erros<6:
                txt = list(palavra_underline_al)
                letra = list(lblWord.get())
                if palavra_underline_al.count(letter)>0:
                    for i in range(len(txt)):
                        if txt[i] == letter:
                            letra[i] = letter
                        lblWord.set("".join(letra))
                        if lblWord.get() == palavra_underline_al:
                            resposta = messagebox.askyesno(title="Você Adivinhou!", message="PARABÉNS!!! Deseja voltar para o menu?") 
                            if resposta == True:
                                controller.show_frame(Iniciar_al)
                                newGame()
                        
                else:
                    erros += 1
                    imgLabel.config(image= photos[erros])
                    if erros == 6:
                        resposta = messagebox.askyesno(title="Você Perdeu! D:", message="Desesja voltar para o menu?")  
                        if resposta == True:
                            controller.show_frame(Iniciar_al)
                            newGame()

                               
                   
        imgLabel= tk.Label(self)
        imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
        imgLabel.config(image=photos[0])

        lblWord = tk.StringVar()
        tk.Label(self, textvariable = lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)


        n=0
        for c in ascii_lowercase:
            tk.Button(self, text=c, command=lambda c=c: guess(c), font= ("Helvetica 18"), width=6).grid(row= 1+n//9, column=n%9, columnspan=1, rowspan=1,padx=10)
            n += 1


        tk.Button(self, text= "Novo\nJogo", command=lambda: newGame(), font= ("Helvetica 10 bold")).grid(row=3, column=8, columnspan=2,rowspan=1, sticky="NSWE")
        newGame()

class Jogar_fac(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        arq_pad = open("pad_fac.txt","r")
        arq_add = open("add_fac.txt","r")
        
        lista_pad = transfLista(arq_pad)
        lista_add = transfLista(arq_add)
        
        lista = list(lista_pad) + list(lista_add)
        lista_palavras_fac = tira_n_line(lista)
        
        
        
        photos = [tk.PhotoImage(file="0_erro.png"),tk.PhotoImage(file="1_erro.png"),tk.PhotoImage(file="2_erro.png"),
                  tk.PhotoImage(file="3_erro.png"),tk.PhotoImage(file="4_erro.png"),tk.PhotoImage(file="5_erro.png"),
                  tk.PhotoImage(file="6_erro.png")]

        def newGame():
            global palavra_underline_fac
            global erros
            erros = 0
            imgLabel.config(image=photos[0])
            palavra = random.choice(lista_palavras_fac)
            
            palavra_underline_fac = " ".join(palavra)
            lblWord.set(" ".join("_"*len(palavra)))

        def guess(letter):
            global erros
            if erros<6:
                txt = list(palavra_underline_fac)
                letra = list(lblWord.get())
                if palavra_underline_fac.count(letter)>0:
                    for i in range(len(txt)):
                        if txt[i] == letter:
                            letra[i] = letter
                        lblWord.set("".join(letra))
                        if lblWord.get() == palavra_underline_fac:
                            resposta = messagebox.askyesno(title="Você Adivinhou!", message="PARABÉNS!!! Deseja voltar para o menu?") 
                            if resposta == True:
                                controller.show_frame(Iniciar_fac)
                                newGame()
                        
                else:
                    erros += 1
                    imgLabel.config(image= photos[erros])
                    if erros == 6:
                        resposta = messagebox.askyesno(title="Você Perdeu! D:", message="Desesja voltar para o menu?")  
                        if resposta == True:
                            controller.show_frame(Iniciar_fac)
                            newGame()

                        
                   
        imgLabel= tk.Label(self)
        imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
        imgLabel.config(image=photos[0])

        lblWord = tk.StringVar()
        tk.Label(self, textvariable = lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)


        n=0
        for c in ascii_lowercase:
            tk.Button(self, text=c, command=lambda c=c: guess(c), font= ("Helvetica 18"), width=6).grid(row= 1+n//9, column=n%9, columnspan=1, rowspan=1)
            n += 1


        tk.Button(self, text= "Novo\nJogo", command=lambda: newGame(), font= ("Helvetica 10 bold")).grid(row=3, column=8, columnspan=2,rowspan=1, sticky="NSWE")
        newGame()


class Jogar_med(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        arq_pad = open("pad_med.txt","r")
        arq_add = open("add_med.txt","r")
        
        lista_pad = transfLista(arq_pad)
        lista_add = transfLista(arq_add)
        
        lista = list(lista_pad) + list(lista_add)
        lista_palavras_med = tira_n_line(lista)
        
        
        
        photos = [tk.PhotoImage(file="0_erro.png"),tk.PhotoImage(file="1_erro.png"),tk.PhotoImage(file="2_erro.png"),
                  tk.PhotoImage(file="3_erro.png"),tk.PhotoImage(file="4_erro.png"),tk.PhotoImage(file="5_erro.png"),
                  tk.PhotoImage(file="6_erro.png")]

        def newGame():
            global palavra_underline_med
            global erros
            erros = 0
            imgLabel.config(image=photos[0])
            palavra = random.choice(lista_palavras_med)
            
            palavra_underline_med = " ".join(palavra)
            lblWord.set(" ".join("_"*len(palavra)))

        def guess(letter):
            global erros
            if erros<6:
                txt = list(palavra_underline_med)
                letra = list(lblWord.get())
                if palavra_underline_med.count(letter)>0:
                    for i in range(len(txt)):
                        if txt[i] == letter:
                            letra[i] = letter
                        lblWord.set("".join(letra))
                        if lblWord.get() == palavra_underline_med:
                            resposta = messagebox.askyesno(title="Você Adivinhou!", message="PARABÉNS!!! Deseja voltar para o menu?") 
                            if resposta == True:
                                controller.show_frame(Iniciar_med)
                                newGame()
                        
                else:
                    erros += 1
                    imgLabel.config(image= photos[erros])
                    if erros == 6:
                        resposta = messagebox.askyesno(title="Você Perdeu! D:", message="Desesja voltar para o menu?")  
                        if resposta == True:
                            controller.show_frame(Iniciar_med)
                            newGame()
                        
                   
        imgLabel= tk.Label(self)
        imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
        imgLabel.config(image=photos[0])

        lblWord = tk.StringVar()
        tk.Label(self, textvariable = lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)


        n=0
        for c in ascii_lowercase:
            tk.Button(self, text=c, command=lambda c=c: guess(c), font= ("Helvetica 18"), width=6).grid(row= 1+n//9, column=n%9, columnspan=1, rowspan=1)
            n += 1


        tk.Button(self, text= "Novo\nJogo", command=lambda: newGame(), font= ("Helvetica 10 bold")).grid(row=3, column=8, columnspan=2,rowspan=1, sticky="NSWE")
        newGame()


class Jogar_dif(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        arq_pad = open("pad_dif.txt","r")
        arq_add = open("add_dif.txt","r")
        
        lista_pad = transfLista(arq_pad)
        lista_add = transfLista(arq_add)
        
        lista = list(lista_pad) + list(lista_add)
        lista_palavras_dif = tira_n_line(lista)
        
        
        
        photos = [tk.PhotoImage(file="0_erro.png"),tk.PhotoImage(file="1_erro.png"),tk.PhotoImage(file="2_erro.png"),
                  tk.PhotoImage(file="3_erro.png"),tk.PhotoImage(file="4_erro.png"),tk.PhotoImage(file="5_erro.png"),
                  tk.PhotoImage(file="6_erro.png")]

        def newGame():
            global palavra_underline_dif
            global erros
            erros = 0
            imgLabel.config(image=photos[0])
            palavra = random.choice(lista_palavras_dif)
            
            palavra_underline_dif = " ".join(palavra)
            lblWord.set(" ".join("_"*len(palavra)))

        def guess(letter):
            global erros
            if erros<6:
                txt = list(palavra_underline_dif)
                letra = list(lblWord.get())
                if palavra_underline_dif.count(letter)>0:
                    for i in range(len(txt)):
                        if txt[i] == letter:
                            letra[i] = letter
                        lblWord.set("".join(letra))
                        if lblWord.get() == palavra_underline_dif:
                            resposta = messagebox.askyesno(title="Você Adivinhou!", message="PARABÉNS!!! Deseja voltar para o menu?") 
                            if resposta == True:
                                controller.show_frame(Iniciar_dif)
                                newGame()
                        
                else:
                    erros += 1
                    imgLabel.config(image= photos[erros])
                    if erros == 6:
                        resposta = messagebox.askyesno(title="Você Perdeu! D:", message="Desesja voltar para o menu?")  
                        if resposta == True:
                            controller.show_frame(Iniciar_dif)
                            newGame()
                        
                   
        imgLabel= tk.Label(self)
        imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
        imgLabel.config(image=photos[0])

        lblWord = tk.StringVar()
        tk.Label(self, textvariable = lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)


        n=0
        for c in ascii_lowercase:
            tk.Button(self, text=c, command=lambda c=c: guess(c), font= ("Helvetica 18"), width=6).grid(row= 1+n//9, column=n%9, columnspan=1, rowspan=1)
            n += 1


        tk.Button(self, text= "Novo\nJogo", command=lambda: newGame(), font= ("Helvetica 10 bold")).grid(row=3, column=8, columnspan=2,rowspan=1, sticky="NSWE")
        newGame()


# DICIONARIO #
class Dicionario(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Dicionário", font= LARGE_FONT).pack(pady=10,padx=10)
        
        btn1 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Consultar Dicionário",
                         command=lambda: controller.show_frame(C_D)).pack()
        
        btn2 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Adicionar Palavra",
                         command=lambda: controller.show_frame(add_pal)).pack()
        
        btn3 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Excluir Palavra",
                         command=lambda: controller.show_frame(exc_pal)).pack()
        
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                         command=lambda: controller.show_frame(Home)).pack()

# ADICIONAR PALAVRA #
class add_pal(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        def op():
            v_1 = principal.get()
            if v_1 == "A" or v_1 == "a":
                palavra = word.get()
                palavra = palavra.lower()
                if insere_al(palavra)== False:
                    messagebox.showinfo("Sucesso","Palavra Adicionada")
                else:
                    messagebox.showinfo("Erro","Palavra ja existe nas palavras adicionadas")
                    
            elif v_1 == "B" or v_1 == "b":
                palavra = word.get()
                palavra = palavra.lower()
                if insere_fac(palavra)== False:
                    messagebox.showinfo("Sucesso","Palavra Adicionada")
                else:
                    messagebox.showinfo("Erro","Palavra ja existe nas palavras adicionadas")
                    

            elif v_1 == "C" or v_1 == "c":
                palavra = word.get()
                palavra = palavra.lower()
                if insere_med(palavra)== False:
                    messagebox.showinfo("Sucesso","Palavra Adicionada")
                else:
                    messagebox.showinfo("Erro","Palavra ja existe nas palavras adicionadas")
                    
            elif v_1 == "D" or v_1 == "d":
                palavra = word.get()
                palavra = palavra.lower()
                if insere_dif(palavra)== False:
                    messagebox.showinfo("Sucesso","Palavra Adicionada")
                else:
                    messagebox.showinfo("Erro","Palavra ja existe nas palavras adicionadas")

            else:
                messagebox.showinfo("Erro","Categoria não identificada")

        label = tk.Label(self, width=40, height= 2, relief="solid", text="Categorias:", font= LARGE_FONT).pack()
        label1 = tk.Label(self, width=40, height= 2, text="ALEATÓRIO(A), FACEIS(B)", font= LARGE_FONT).pack()
        label2 = tk.Label(self, width=40, height= 2, text="MEDIAS(C), DIFÍCEIS(D)", font= LARGE_FONT).pack()
        principal = tk.StringVar()
        tk.Entry(self, textvariable= principal).pack()        
        label = tk.Label(self, width=40, height= 3, text="Insira a palavra a ser adicionada:", font= LARGE_FONT).pack(pady=10,padx=10)
        word = tk.StringVar()
        tk.Entry(self, textvariable = word).pack()
        btn2 = tk.Button(self, text="Confirmar", command= op).pack()
        
        btn_saida = btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                              command=lambda: controller.show_frame(Dicionario)).pack (side="bottom", anchor="sw")

# EXCLUIR PALAVRA #
class exc_pal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def op():
            v_1 = principal.get()
            if v_1 == "A" or v_1 == "a":
                palavra = word.get()
                palavra = palavra.lower()
                if exclui_al(palavra)== True:
                    messagebox.showinfo("Sucesso","Palavra Excluída")
                else:
                    messagebox.showinfo("Erro","Palavra não existe para ser excluida")
                    
            elif v_1 == "B" or v_1 == "b":
                palavra = word.get()
                palavra = palavra.lower()
                if exclui_fac(palavra)== True:
                    messagebox.showinfo("Sucesso","Palavra Excluída")
                else:
                    messagebox.showinfo("Erro","Palavra não existe para ser excluida")
                    

            elif v_1 == "C" or v_1 == "c":
                palavra = word.get()
                palavra = palavra.lower()
                if exclui_med(palavra)== True:
                    messagebox.showinfo("Sucesso","Palavra Excluída")
                else:
                    messagebox.showinfo("Erro","Palavra não existe para ser excluida")
                    
            elif v_1 == "D" or v_1 == "d":
                palavra = word.get()
                palavra = palavra.lower()
                if exclui_dif(palavra)== True:
                    messagebox.showinfo("Sucesso","Palavra Excluída")
                else:
                    messagebox.showinfo("Erro","Palavra não existe para ser excluida")

            else:
                messagebox.showinfo("Erro","Categoria não identificada")
                

        label = tk.Label(self, width=40, height= 2, relief="solid", text="Categorias:", font= LARGE_FONT).pack()
        label1 = tk.Label(self, width=40, height= 2, text="ALEATÓRIO(A), FACEIS(B)", font= LARGE_FONT).pack()
        label2 = tk.Label(self, width=40, height= 2, text="MEDIAS(C), DIFÍCEIS(D)", font= LARGE_FONT).pack()
        principal = tk.StringVar()
        tk.Entry(self, textvariable= principal).pack()        
        label = tk.Label(self, width=40, height= 3, text="Insira a palavra a ser excluída:", font= LARGE_FONT).pack(pady=10,padx=10)
        word = tk.StringVar()
        tk.Entry(self, textvariable = word).pack()
        btn2 = tk.Button(self, text="Confirmar", command= op).pack()
        
        btn_saida = btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                              command=lambda: controller.show_frame(Dicionario)).pack (side="bottom", anchor="sw")

       
# Consultar Dicionário #
class C_D(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Consultar Dicionário", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Palavras Padrão",
                         command=lambda: controller.show_frame(pal_pad)).pack()
        
        btn2 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Palavras Adicionadas",
                         command=lambda: controller.show_frame(pal_add)).pack()
        
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                         command=lambda: controller.show_frame(Dicionario)).pack()

# Bloco palavras padrão #
class pal_pad(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def op():
            palavra = word.get()
            verif_1(palavra)
            verif_2(palavra)
            verif_3(palavra)
            verif_4(palavra)
            
        def verif_1(palavra):
            if verif_pad_al(palavra) == True:
                messagebox.showinfo("","Palavra já existe nos aleatórios")
            else:
                messagebox.showinfo("","Palavra não existe nos aleatórios")
                
        def verif_2(palavra):
            if verif_pad_fac(palavra) == True:
                messagebox.showinfo("","Palavra já existe nos fáceis")
            else:
                messagebox.showinfo("","Palavra não existe nos fáceis")
                
        def verif_3(palavra):
            if verif_pad_med(palavra) == True:
                messagebox.showinfo("","Palavra já existe nas médios")
            else:
                messagebox.showinfo("","Palavra não existe nas médios")
                
        def verif_4(palavra):
            if verif_pad_dif(palavra) == True:
                messagebox.showinfo("","Palavra já existe nos dificeis")
            else:
                messagebox.showinfo("","Palavra não existe nos dificeis")

        label = tk.Label(self, width=40, height= 2, relief="solid",text="Palavras Padrão", font= LARGE_FONT).pack()
        
                
        label2 = tk.Label(self, width=40, height= 3, text="Insira a palavra a ser consultada:", font= LARGE_FONT).pack(pady=10,padx=10)
        word = tk.StringVar()
        tk.Entry(self, textvariable = word).pack()
        btn2 = tk.Button(self, text="Confirmar", command= op).pack()
        
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                              command=lambda: controller.show_frame(C_D)).pack (side="bottom", anchor="sw")


# Bloco palavras adicionadas #
class pal_add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def op():
            palavra = word.get()
            verif_1(palavra)
            verif_2(palavra)
            verif_3(palavra)
            verif_4(palavra)
            
        def verif_1(palavra):
            if verif_add_al(palavra) == True:
                messagebox.showinfo("","Palavra já existe nos aleatórios")
            else:
                messagebox.showinfo("","Palavra não existe nos aleatórios")
                
        def verif_2(palavra):
            if verif_add_fac(palavra) == True:
                messagebox.showinfo("","Palavra já existe nos fáceis")
            else:
                messagebox.showinfo("","Palavra não existe nos fáceis")
                
        def verif_3(palavra):
            if verif_add_med(palavra) == True:
                messagebox.showinfo("","Palavra já existe nas médios")
            else:
                messagebox.showinfo("","Palavra não existe nas médios")
                
        def verif_4(palavra):
            if verif_add_dif(palavra) == True:
                messagebox.showinfo("","Palavra já existe nos dificeis")
            else:
                messagebox.showinfo("","Palavra não existe nos dificeis")

        label = tk.Label(self, width=40, height= 2, relief="solid", text="Palavras Adicionadas", font= LARGE_FONT).pack()
        
                
        label2 = tk.Label(self, width=40, height= 3, text="Insira a palavra a ser consultada:", font= LARGE_FONT).pack(pady=10,padx=10)
        word = tk.StringVar()
        tk.Entry(self, textvariable = word).pack()
        btn2 = tk.Button(self, text="Confirmar", command= op).pack()
        
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                              command=lambda: controller.show_frame(C_D)).pack (side="bottom", anchor="sw")

# Ajuda #
class Ajuda(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Ajuda", font= LARGE_FONT).pack(pady=10,padx=10)
        
        btn = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Perguntas Frequentes",
                        command=lambda: controller.show_frame(P_F)).pack()
        
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                        command=lambda: controller.show_frame(Home)).pack()

# Perguntas frequentes #
class P_F(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Perguntas frequentes", font=LARGE_FONT).pack(pady=10,padx=10)

        f = open("P_F.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                              command=lambda: controller.show_frame(Ajuda)).pack (side="bottom", anchor="sw")

# Creditos #
class Creditos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, relief="groove", text="Créditos", font=LARGE_FONT).pack(pady=10,padx=10)
        
        btn2 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Colaboradores",
                         command=lambda: controller.show_frame(Colaboradores)).pack()
        
        btn3 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Agradecimentos",
                         command=lambda: controller.show_frame(Agradecimentos)).pack()
        
        btn4 = tk.Button(self, width=40, height=3, bg="lightBlue" , fg="Black", text="Referências e bibliotecas",
                         command=lambda: controller.show_frame(R_B)).pack()
        
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                         command=lambda: controller.show_frame(Home)).pack()

# Colaboradores #
class Colaboradores(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Colaboradores", font=LARGE_FONT).pack(pady=10,padx=10)

        f = open("colaboradores.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                        command=lambda: controller.show_frame(Creditos)).pack (side="bottom", anchor="sw")

# Agradecimentos #
class Agradecimentos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, relief="groove", text="Agradecimentos", font=LARGE_FONT).pack(pady=10,padx=10)

        f = open("Agradecimentos.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                        command=lambda: controller.show_frame(Creditos)).pack (side="bottom", anchor="sw")

# Referências e Bibliotecas #
class R_B(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,width=40, height= 3, relief="groove", text="Referências e bibliotecas", font=LARGE_FONT).pack(pady=10,padx=10)
    
        f = open("R_B.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black",
                        command=lambda: controller.show_frame(Creditos)).pack (side="bottom", anchor="sw")

# EXEMPLO DE CLASSE, CASO PRECISAR DE MAIS #
class a (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="", font=LARGE_FONT).pack(pady=10,padx=10)

        btn = tk.Button(self, text="", command=lambda: controller.show_frame()).pack()
        
        btn_saida = tk.Button(self, width=25, height = 2, text="Anterior", bg="indianred", fg="black", command=lambda: controller.show_frame()).pack (side="bottom", anchor="sw")







app = Master()
app.mainloop()
