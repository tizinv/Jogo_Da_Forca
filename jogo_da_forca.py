import tkinter as tk
from funcoes import *
# LIMPEZA
LARGE_FONT= ("Verdana", 18)



################################################
############### CLASSE (MASTER) ################
################################################
class Master(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
# AQUI É SÓ COLOCAR NESSE FOR SE QUISER ADICIONAR UMA PÁGINA NOVA
        for F in (Home, A_D_J, M_D_J, O_P_F, O_NP_F, Ajuda, P_F, Creditos, Colaboradores, Agradecimentos, R_B, Iniciar_al, Iniciar_fac, Iniciar_med, Iniciar_dif, Dificuldade, Dicionario, C_D, pal_pad, pad_al, pad_fac, pad_med, pad_dif, pal_add, add_al, add_fac, add_med, add_dif, add_pal, exc_pal):

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
        label = tk.Label(self, width=40, height= 3, text="Jogo da Forca", font=LARGE_FONT).pack(pady=10,padx=10)
        btn1 = tk.Button(self, width=40, height=3, text="Apresentação do jogo",                                                                             command=lambda: controller.show_frame(A_D_J)).pack()
        btn2 = tk.Button(self, width=40, height=3, text="Iniciar",                                                                                          command=lambda: controller.show_frame(Iniciar_al)).pack()
        btn3 = tk.Button(self, width=40, height=3, text="Dicionário de palavras",                                                                           command=lambda: controller.show_frame(Dicionario)).pack()
        btn4 = tk.Button(self, width=40, height=3, text="Ajuda",                                                                                            command=lambda: controller.show_frame(Ajuda)).pack()
        btn5 = tk.Button(self, width=40, height=3, text="Créditos",                                                                                         command=lambda: controller.show_frame(Creditos)).pack()
        btn_saida = tk.Button(self, width=15, text="Sair do jogo",                                                                                          command=lambda: quit()).pack(side="bottom", anchor="sw")
# Apresentação do jogo #
class A_D_J(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Apresentação do jogo", font=LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, text="Mecânicas do jogo",                                                                         command=lambda: controller.show_frame(M_D_J)).pack()
        btn2 = tk.Button(self, width=40, height=3, text="O que se pode fazer",                                                                       command=lambda: controller.show_frame(O_P_F)).pack()
        btn3 = tk.Button(self, width=40, height=3, text="O que não se pode fazer",                                                                   command=lambda: controller.show_frame(O_NP_F)).pack()
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                                                 command=lambda: controller.show_frame(Home)).pack (side="bottom", anchor="sw")

# Mecânicas do jogo #
class M_D_J(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Mecânicas do jogo", font=LARGE_FONT).pack(pady=10,padx=10)
        f = open("mecanicas.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self,  width=15, text="Anterior",                                                                          command=lambda: controller.show_frame(A_D_J)).pack (side="bottom", anchor="sw")

# O que pode ser feito #
class O_P_F(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="O que se pode fazer", font=LARGE_FONT).pack(pady=10,padx=10)

        f = open("o_p_f.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                         command=lambda: controller.show_frame(A_D_J)).pack (side="bottom", anchor="sw")

# O que não pode ser feito #
class O_NP_F(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="O que não se pode fazer", font=LARGE_FONT).pack(pady=10,padx=10)
        
        f = open("o_np_f.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                         command=lambda: controller.show_frame(A_D_J)).pack (side="bottom", anchor="sw")

# Jogar #

# INICIAR #
class Iniciar_al(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Iniciar", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, text="Dificuldades (Aleatório)",                                                             command=lambda: controller.show_frame(Dificuldade)).pack()
        btn2 = tk.Button(self, width=40, height=3, text="Iniciar").pack()
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                                  command=lambda: controller.show_frame(Home)).pack (side="bottom", anchor="sw")

class Iniciar_fac(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Iniciar", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, text="Dificuldades (Fácil)",                                                         command=lambda: controller.show_frame(Dificuldade)).pack()
        btn2 = tk.Button(self, width=40, height=3, text="Iniciar").pack()
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                          command=lambda: controller.show_frame(Home)).pack (side="bottom", anchor="sw")

class Iniciar_med(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Iniciar", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, text="Dificuldades (Média)",                                                         command=lambda: controller.show_frame(Dificuldade)).pack()
        btn2 = tk.Button(self, width=40, height=3, text="Iniciar").pack()
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                          command=lambda: controller.show_frame(Home)).pack (side="bottom", anchor="sw")

class Iniciar_dif(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Iniciar", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, text="Dificuldades (Difícil)",                                                       command=lambda: controller.show_frame(Dificuldade)).pack()
        btn2 = tk.Button(self, width=40, height=3, text="Iniciar").pack()                                                                      
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                          command=lambda: controller.show_frame(Home)).pack (side="bottom", anchor="sw")

# Dificuldade #
class Dificuldade(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Dificuldade", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, text="Aleatória",                                                                   command=lambda: controller.show_frame(Iniciar_al)).pack()
        btn2 = tk.Button(self, width=40, height=3, text="Fácil",                                                                       command=lambda: controller.show_frame(Iniciar_fac)).pack()
        btn3 = tk.Button(self, width=40, height=3, text="Média",                                                                       command=lambda: controller.show_frame(Iniciar_med)).pack()
        btn4 = tk.Button(self, width=40, height=3, text="Difícil",                                                                     command=lambda: controller.show_frame(Iniciar_dif)).pack()
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                         command=lambda: controller.show_frame(Iniciar_al)).pack (side="bottom", anchor="sw")


# DICIONARIO #
class Dicionario(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Dicionário", font= LARGE_FONT).pack(pady=10,padx=10)
        
        btn1 = tk.Button(self, width=40, height=3, text="Consultar Dicionário",                                                         command=lambda: controller.show_frame(C_D)).pack()
        btn2 = tk.Button(self, width=40, height=3, text="Adicionar Palavra",                                                         command=lambda: controller.show_frame(add_pal)).pack()
        btn3 = tk.Button(self, width=40, height=3, text="Excluir Palavra",                                                         command=lambda: controller.show_frame(exc_pal)).pack()
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                          command=lambda: controller.show_frame(Home)).pack (side="bottom", anchor="sw")
# ADICIONAR PALAVRA #
class add_pal(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        def op():
            v_1 = principal.get()
            if v_1 == "A" or v_1 == "a":
                palavra = word.get()
                insere_al(palavra)
            elif v_1 == "B" or v_1 == "b":
                palavra = word.get() 
                insere_fac(palavra)
            elif v_1 == "C" or v_1 == "c":
                palavra = word.get() 
                insere_med(palavra)
            elif v_1 == "D" or v_1 == "d":
                palavra = word.get() 
                insere_dif(palavra)
            else:
                op()

        label = tk.Label(self, width=40, height= 2, text="Categorias:", font= LARGE_FONT).pack()
        label1 = tk.Label(self, width=40, height= 2, text="ALEATÓRIO(A), FACEIS(B)", font= LARGE_FONT).pack()
        label2 = tk.Label(self, width=40, height= 2, text="MEDIAS(C), DIFÍCEIS(D)", font= LARGE_FONT).pack()
        principal = tk.StringVar()
        tk.Entry(self, textvariable= principal).pack()        
        label = tk.Label(self, width=40, height= 3, text="Insira a palavra a ser adicionada:", font= LARGE_FONT).pack(pady=10,padx=10)
        word = tk.StringVar()
        tk.Entry(self, textvariable = word).pack()
        btn2 = tk.Button(self, text="Confirmar", command= op).pack()
        
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                          command=lambda: controller.show_frame(Dicionario)).pack (side="bottom", anchor="sw")

# EXCLUIR PALAVRA #
class exc_pal(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def op():
            v_1 = principal.get()
            if v_1 == "A" or v_1 == "a":
                palavra = word.get()
                exclui_al(palavra)
            elif v_1 == "B" or v_1 == "b":
                palavra = word.get() 
                exclui_fac(palavra)
            elif v_1 == "C" or v_1 == "c":
                palavra = word.get() 
                exclui_med(palavra)
            elif v_1 == "D" or v_1 == "d":
                palavra = word.get() 
                exclui_dif(palavra)
            else:
                op()

        label = tk.Label(self, width=40, height= 2, text="Categorias:", font= LARGE_FONT).pack()
        label1 = tk.Label(self, width=40, height= 2, text="ALEATÓRIO(A), FACEIS(B)", font= LARGE_FONT).pack()
        label2 = tk.Label(self, width=40, height= 2, text="MEDIAS(C), DIFÍCEIS(D)", font= LARGE_FONT).pack()
        principal = tk.StringVar()
        tk.Entry(self, textvariable= principal).pack()        
        label = tk.Label(self, width=40, height= 3, text="Insira a palavra a ser excluída:", font= LARGE_FONT).pack(pady=10,padx=10)
        word = tk.StringVar()
        tk.Entry(self, textvariable = word).pack()
        btn2 = tk.Button(self, text="Confirmar", command= op).pack()
        
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                          command=lambda: controller.show_frame(Dicionario)).pack (side="bottom", anchor="sw")

       
# Consultar Dicionário #
class C_D(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Consultar Dicionário", font= LARGE_FONT).pack(pady=10,padx=10)

        btn1 = tk.Button(self, width=40, height=3, text="Palavras Padrão",                                                          command=lambda: controller.show_frame(pal_pad)).pack()
        btn2 = tk.Button(self, width=40, height=3, text="Palavras Adicionadas",                                                     command=lambda: controller.show_frame(pal_add)).pack()
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                      command=lambda: controller.show_frame(Dicionario)).pack(side="bottom", anchor="sw")

# Bloco palavras padrão #
class pal_pad(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, text="Palavras Padrão", font= LARGE_FONT).pack(pady=10, padx=10)

        btn1 = tk.Button(self, width=40, height=3, text="Categoria Aleatória",                                                         command=lambda: controller.show_frame(pad_al)).pack()
        btn2 = tk.Button(self, width=40, height=3, text="Categoria Fácil",                                                             command=lambda: controller.show_frame(pad_fac)).pack()
        btn3 = tk.Button(self, width=40, height=3, text="Categoria Média",                                                             command=lambda: controller.show_frame(pad_med)).pack()
        btn4 = tk.Button(self, width=40, height=3, text="Categoria Difícil",                                                           command=lambda: controller.show_frame(pad_dif)).pack()
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                          command=lambda: controller.show_frame(C_D)).pack(side="bottom", anchor="sw")

# Aleatórias #
class pad_al(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, text="Palavras Padrão", font= LARGE_FONT).pack(pady=10, padx=10)

        f = open("pad_al.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                  command=lambda: controller.show_frame(pal_pad)).pack(side="bottom", anchor="sw")
# Fácil #
class pad_fac(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, text="Palavras Padrão", font= LARGE_FONT).pack(pady=10, padx=10)

        f = open("pad_fac.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                  command=lambda: controller.show_frame(pal_pad)).pack(side="bottom", anchor="sw")
# Média #
class pad_med(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, text="Palavras Padrão", font= LARGE_FONT).pack(pady=10, padx=10)

        f = open("pad_med.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                  command=lambda: controller.show_frame(pal_pad)).pack(side="bottom", anchor="sw")

# Dificil #
class pad_dif(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, text="Palavras Padrão", font= LARGE_FONT).pack(pady=10, padx=10)

        f = open("pad_dif.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                  command=lambda: controller.show_frame(pal_pad)).pack(side="bottom", anchor="sw")

# Bloco palavras adicionadas #
class pal_add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, text="Categoria Aleatória", font= LARGE_FONT).pack(pady=10, padx=10)

        btn1 = tk.Button(self, width=40, height=3, text="Categoria Aleatória",                                                         command=lambda: controller.show_frame(add_al)).pack()
        btn2 = tk.Button(self, width=40, height=3, text="Categoria Fácil",                                                             command=lambda: controller.show_frame(add_fac)).pack()
        btn3 = tk.Button(self, width=40, height=3, text="Categoria Média",                                                             command=lambda: controller.show_frame(add_med)).pack()
        btn4 = tk.Button(self, width=40, height=3, text="Categoria Difícil",                                                           command=lambda: controller.show_frame(add_dif)).pack()
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                          command=lambda: controller.show_frame(Home)).pack (side="bottom", anchor="sw")

# Aleatorio #
class add_al(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, text="Palavras Padrão", font= LARGE_FONT).pack(pady=10, padx=10)

        f = open("add_al.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                  command=lambda: controller.show_frame(pal_add)).pack(side="bottom", anchor="sw")

# Facil #
class add_fac(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, text="Palavras Adicionadas", font= LARGE_FONT).pack(pady=10, padx=10)

        f = open("add_fac.txt", "r").read()
        lb = tk.Label(self, text = f).pack()

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                  command=lambda: controller.show_frame(pal_add)).pack(side="bottom", anchor="sw")

# Media #

class add_med(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, text="Palavras Adicionadas", font= LARGE_FONT).pack(pady=10, padx=10)

        f = open("add_med.txt", "r").read()
        lb = tk.Label(self, text = f).pack()

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                  command=lambda: controller.show_frame(pal_add)).pack(side="bottom", anchor="sw")

# Dificil #
class add_dif(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, text="Palavras Adicionadas", font= LARGE_FONT).pack(pady=10, padx=10)

        f = open("add_dif.txt", "r").read()
        lb = tk.Label(self, text = f).pack()

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                  command=lambda: controller.show_frame(pal_add)).pack(side="bottom", anchor="sw")

# Ajuda #
class Ajuda(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Ajuda", font= LARGE_FONT).pack(pady=10,padx=10)
        
        btn = tk.Button(self, width=40, height=3, text="Perguntas Frequentes",                                               command=lambda: controller.show_frame(P_F)).pack()
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                        command=lambda: controller.show_frame(Home)).pack (side="bottom", anchor="sw")

# Perguntas frequentes #
class P_F(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Perguntas frequentes", font=LARGE_FONT).pack(pady=10,padx=10)

        f = open("P_F.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                         command=lambda: controller.show_frame(Ajuda)).pack (side="bottom", anchor="sw")

# Creditos #
class Creditos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height=3, text="Créditos", font=LARGE_FONT).pack(pady=10,padx=10)
        
        btn2 = tk.Button(self, width=40, height=3, text="Colaboradores",                                                                                 command=lambda: controller.show_frame(Colaboradores)).pack()
        btn3 = tk.Button(self, width=40, height=3, text="Agradecimentos",                                                                                command=lambda: controller.show_frame(Agradecimentos)).pack()
        btn4 = tk.Button(self, width=40, height=3, text="Referências e bibliotecas",                                                                     command=lambda: controller.show_frame(R_B)).pack()
        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                        command=lambda: controller.show_frame(Home)).pack (side="bottom", anchor="sw")

# Colaboradores #
class Colaboradores(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Colaboradores", font=LARGE_FONT).pack(pady=10,padx=10)

        f = open("colaboradores.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                         command=lambda: controller.show_frame(Creditos)).pack (side="bottom", anchor="sw")

# Agradecimentos #
class Agradecimentos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="Agradecimentos", font=LARGE_FONT).pack(pady=10,padx=10)

        f = open("Agradecimentos.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                         command=lambda: controller.show_frame(Creditos)).pack (side="bottom", anchor="sw")

# Referências e Bibliotecas #
class R_B(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,width=40, height= 3, text="Referências e bibliotecas", font=LARGE_FONT).pack(pady=10,padx=10)
    
        f = open("R_B.txt", "r").read()
        lb = tk.Label(self, text = f).pack()                                  

        btn_saida = tk.Button(self, width=15, text="Anterior",                                                                        command=lambda: controller.show_frame(Creditos)).pack (side="bottom", anchor="sw")

# EXEMPLO DE CLASSE, CASO PRECISAR DE MAIS #
class a (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, width=40, height= 3, text="", font=LARGE_FONT).pack(pady=10,padx=10)

        btn = tk.Button(self, text="", command=lambda: controller.show_frame()).pack()
        
        btn_saida = tk.Button(self, width=15, text="Anterior", command=lambda: controller.show_frame()).pack (side="bottom", anchor="sw")







app = Master()
app.mainloop()
