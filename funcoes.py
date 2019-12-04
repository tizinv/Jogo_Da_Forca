from random import randint
def master():
    print("1 - Mecânicas do Jogo")
    print("2 - Iniciar")
    print("3 - Dicionário")
    print("4 - Ajuda")
    print("5 - Créditos")
    print("0 - Sair")

    while True:
        try:
            opt = int(input("Informe:   "))
            break
        except:
            print("Comando inválido")
            
    if opt == 1:
        mec_jogo()
    elif opt == 2:
        iniciar()
    elif opt == 3:
        main_dic()
    elif opt == 4:
        ajuda()
    elif opt == 5:
        creditos()
    elif opt == 0:
        print("Obrigado por jogar.")
    else:
        print("Comando inválido.")
    while True:
        try:
            if_cont = int(input("Digite 1 se deseja continuar ou qualquer coisa se deseja sair "))
            break
        except:
            print("Comando inválido")
            
    if if_cont == 1:
        master()
    else:
        print("Obrigado por jogar.")


def iniciar():
    print("Escolha uma dentre as dificuldades. \n1- Aleatório \n2- Fácil \n3- Média \n4- Difícil")
    while True:
        try:
            dific = int(input("Informe: "))
            if dific != 1 and dific != 2 and dific != 3 and dific != 4:
                print("Comando inválido.")
            else:
                break
        except:
            print("Comando inválido.")
            
    print("Escolha 1 para palavras padrão ou 2 para palavras que foram adicionadas pelos usuários.")  
    while True:
        try:
            dic = int(input("Informe: "))
            if dic != 1 and dic != 2:
                print("Comando inválido.")
            else:
                break
        except:
            print("Comando inválido.")
    
    if dific == 1 and dic == 1: #Aleatório e Padrão
        palavra = escolhe_pad_al()
        

        pal_list = pal_em_lista(palavra)
        new_list = list_em_traco(pal_list)
        
        jogar(pal_list,new_list)

    elif dific == 2 and dic == 1: #Fácil e Padrão
        palavra = escolhe_pad_fac()
        

        pal_list = pal_em_lista(palavra)
        new_list = list_em_traco(pal_list)
        
        jogar(pal_list,new_list)
        
    elif dific == 3 and dic == 1: #Médio e Padrão
        palavra = escolhe_pad_med()
        

        pal_list = pal_em_lista(palavra)
        new_list = list_em_traco(pal_list)
        
        jogar(pal_list,new_list)

    elif dific == 4 and dic == 1: #Difícil e Padrão
        palavra = escolhe_pad_dif()
        

        pal_list = pal_em_lista(palavra)
        new_list = list_em_traco(pal_list)
        
        jogar(pal_list,new_list)

    elif dific == 1 and dic == 2: #Aleatório e Adicionadas
        palavra = escolhe_add_al()
        

        pal_list = pal_em_lista(palavra)
        new_list = list_em_traco(pal_list)
        
        jogar(pal_list,new_list)
        
    elif dific == 2 and dic == 2: #Fácil e Adicionadas
        palavra = escolhe_add_fac()
        

        pal_list = pal_em_lista(palavra)
        new_list = list_em_traco(pal_list)
        
        jogar(pal_list,new_list)

    elif dific == 3 and dic == 2: #Médias e Adicionadas
        palavra = escolhe_add_med()
        

        pal_list = pal_em_lista(palavra)
        new_list = list_em_traco(pal_list)
        
        jogar(pal_list,new_list)

    elif dific == 4 and dic == 2: #Difíceis e Adicionadas
        palavra = escolhe_add_dif()
        

        pal_list = pal_em_lista(palavra)
        new_list = list_em_traco(pal_list)
        
        jogar(pal_list,new_list)
        
def pal_em_lista(palavra): ################# >>>>>> TRANSFORMA PALAVRA EM LISTA DE PALAVRAS
    tamanho = len(palavra) -1
    pal_list = [0]*(len(palavra)-1)
    for i in range (tamanho):
        pal_list[i] = palavra[i]
    
    return pal_list


def list_em_traco(pal_list): #################### >>>>> TRANSFORMA LISTA DE PALAVRAS EM TRAÇOS
    new_list = list(pal_list)
    for i in range (len(new_list)):
        new_list[i] = "_"
    
    return new_list
    
    
def escolhe_dic():
    from random import randint
    return randint(0,1)

############################################################  RANDOM PALAVRAS# #######################################################
def escolhe_pad_al():   
    arq = open("pad_al.txt","r")
    lista = transfLista(arq)
    opt = randint(0,len(lista))

    return lista[opt]

def escolhe_pad_fac():
    arq = open("pad_fac.txt","r")
    lista = transfLista(arq)
    opt = randint(0,len(lista))

    return lista[opt]
    
def escolhe_pad_med():
    arq = open("pad_med.txt","r")
    lista = transfLista(arq)
    opt = randint(0,len(lista))

    return lista[opt]

def escolhe_pad_dif():
    arq = open("pad_dif.txt","r")
    lista = transfLista(arq)
    opt = randint(0,len(lista))

    return lista[opt]

def escolhe_add_al():
    arq = open("add_al.txt","r")
    lista = transfLista(arq)
    opt = randint(0,len(lista))

    return lista[opt]

def escolhe_add_fac():
    arq = open("add_fac.txt","r")
    lista = transfLista(arq)
    opt = randint(0,len(lista))

    return lista[opt]

def escolhe_add_med():
    arq = open("add_med.txt","r")
    lista = transfLista(arq)
    opt = randint(0,len(lista))

    return lista[opt]

def escolhe_add_dif():
    arq = open("add_dif.txt","r")
    lista = transfLista(arq)
    opt = randint(0,len(lista))

    return lista[opt]

####################################################################  JOGAR  ##########################################################

def jogar(pal_list, new_list):
    printalista(pal_list)
    printalista(new_list)
    erro = 0
    while erro < 6:
        while True:
            try:
                letra = input("Informe um caracter: ")
                if len(letra) > 1:
                    print("Só um caracter.")
                else:
                    break
            except:
                print("Comando inválido.")
                
        mudou = False
        for i in range(len(new_list)):     
            if letra == pal_list[i]:
                new_list[i] = letra
                mudou = True

        if mudou == False:
            erro += 1
            print("Você errou.",erro,"erros.")
            if erro == 6:
                print("Você perdeu.")
                master()
        printalista(new_list)

        if verif_ganhou(new_list) == True:
            print("Parabéns! Você ganhou!")
            master()
        

def verif_ganhou(new_list):
    for i in range(len(new_list)):
        if new_list[i] == "_":
            return False
            break
    return True
            
            
            
                

    
        
    
        
          























def main_dic(): #função pra teste, fiz apenas pra palavras faceis
    palavra = input("Insira a palavra: ")
    palavra = palavra.lower()
    print("1 para fácil \t 2 para medio \t 3 para dificil", end ='\t')
    recebe = int(input(':'))
    if recebe == 1:
        opt = int(input("Digite 1 se deseja adicionar ou 2 se deseja excluir: "))
        if opt == 1:
            insere_al(palavra)
            insere_fac(palavra)
        else:
            exclui_al(palavra)
            exclui_fac(palavra)
    elif recebe == 2:
        opt = int(input("Digite 1 se deseja adicionar ou 2 se deseja excluir: "))
        if opt == 1:
            insere_al(palavra)
            insere_med(palavra)
        else:
            exclui_al(palavra)
            exclui_med(palavra)
    elif recebe == 3:
        opt = int(input("Digite 1 se deseja adicionar ou 2 se deseja excluir: "))
        if opt == 1:
            insere_al(palavra)
            insere_dif(palavra)
        else:
            exclui_al(palavra)
            exclui_dif(palavra)

    test = int(input("Deseja continuar? Digite 1 pra sim e 2 pra não: "))
    if test == 1:
        main_dic()

###################################################################
###################################################################
        
def exclui_al(palavra):
    file = open("add_al.txt","r")
    
    arq = transfLista(file)
    print (arq)
    arq = tira_n_line(arq)
    print (arq)
    ifpop = False
    size = len(arq)
    cont = 0
    while cont < size:
        
        if compararString(arq[cont],palavra) == True:
            removido = arq.pop(cont)
            print(arq)
            size -= 1
            ifpop = True
            
        cont += 1    
    for i in range(len(arq)):
        arq[i] += '\n'
    
    print (arq)
    file.close()
    exclui0(ifpop,arq)

def exclui0(ifpop,arq):
    file = open("add_al.txt","w")
    if ifpop == True:
        for i in range(len(arq)):
            
            file.write(arq[i])
        print("Palavra excluida das aleatórias.")

  
    else:
        print("Palavra nao existe nas aleatórias para ser excluida.")
        
def exclui_fac(palavra):
    file = open("add_fac.txt","r")
    
    arq = transfLista(file)
    print (arq)
    arq = tira_n_line(arq)
    print (arq)
    ifpop = False
    size = len(arq)
    cont = 0
    while cont < size:
        
        if compararString(arq[cont],palavra) == True:
            removido = arq.pop(cont)
            print(arq)
            size -= 1
            ifpop = True
            
        cont += 1    
    for i in range(len(arq)):
        arq[i] += '\n'
    
    print (arq)
    file.close()
    exclui1(ifpop,arq)

def exclui1(ifpop,arq):
    file = open("add_fac.txt","w")
    if ifpop == True:
        for i in range(len(arq)):
            
            file.write(arq[i])
        print("Palavra excluida das fáceis.")

  
    else:
        print("Palavra nao existe nas fáceis para ser excluida.")

def exclui_med(palavra):
    file = open("add_med.txt","r")
    
    arq = transfLista(file)
    print (arq)
    arq = tira_n_line(arq)
    print (arq)
    ifpop = False
    size = len(arq)
    cont = 0
    while cont < size:
        
        if compararString(arq[cont],palavra) == True:
            removido = arq.pop(cont)
            print(arq)
            size -= 1
            ifpop = True
            
        cont += 1    
    for i in range(len(arq)):
        arq[i] += '\n'
    
    print (arq)
    file.close()
    exclui2(ifpop,arq)

def exclui2(ifpop,arq):
    file = open("add_med.txt","w")
    if ifpop == True:
        for i in range(len(arq)):
            
            file.write(arq[i])
        print("Palavra excluida das médias.")

  
    else:
        print("Palavra nao existe nas médias para ser excluida.")

def exclui_dif(palavra):
    file = open("add_dif.txt","r")
    
    arq = transfLista(file)
    print (arq)
    arq = tira_n_line(arq)
    print (arq)
    ifpop = False
    size = len(arq)
    cont = 0
    while cont < size:
        
        if compararString(arq[cont],palavra) == True:
            removido = arq.pop(cont)
            print(arq)
            size -= 1
            ifpop = True
            
        cont += 1    
    for i in range(len(arq)):
        arq[i] += '\n'
    
    print (arq)
    file.close()
    exclui3(ifpop,arq)

def exclui3(ifpop,arq):
    file = open("add_dif.txt","w")
    if ifpop == True:
        for i in range(len(arq)):
            
            file.write(arq[i])
        print("Palavra excluida nas difíceis.")

  
    else:
        print("Palavra nao existe nas difíceis para ser excluida.")

###############################################################
###############################################################
def insere_al(palavra): #verifica se existe ou não a palavra no dicionário#
    
    file1 = open("add_al.txt","a")
    
    if verif_al(palavra) == False:
        file1.write(palavra+'\n')
        print("Palavra adicionada nos aleatórios.") 
    else:
        print("A palavra já existe nos aleatórios.")

    file1.close()
        
def insere_fac(palavra): #verifica se existe ou não a palavra no dicionário#
    
    file1 = open("add_fac.txt","a")
    
    if verif_fac(palavra) == False:
        file1.write(palavra+'\n')
        print("Palavra adicionada nas fáceis.") 
    else:
        print("A palavra já existe nas fáceis.")

    file1.close()

def insere_med(palavra): #verifica se existe ou não a palavra no dicionário#
    
    file1 = open("add_med.txt","a")
    
    if verif_med(palavra) == False:
        file1.write(palavra+'\n')
        print("Palavra adicionada nas médias.") 
    else:
        print("A palavra já existe nas médias.")

    file1.close()
    
def insere_dif(palavra): #verifica se existe ou não a palavra no dicionário#
    
    file1 = open("add_dif.txt","a")
    
    if verif_dif(palavra) == False:
        file1.write(palavra+'\n')
        print("Palavra adicionada nas difíceis.") 
    else:
        print("A palavra já existe nas difíceis.")

    file1.close()
        
def verif_al(palavra):
    file = open("add_al.txt","r")
    arq = transfLista(file)
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    for i in arq:
        if compararString(i,palavra) == True:
            file.close()
            return True
    return False

def verif_fac(palavra):    
    file = open("add_fac.txt","r")
    arq = transfLista(file)
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    for i in arq:
        if compararString(i,palavra) == True:
            file.close()
            return True
    return False

def verif_med(palavra):
    file = open("add_med.txt","r")
    arq = transfLista(file)
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    for i in arq:
        if compararString(i,palavra) == True:
            file.close()
            return True
    return False

def verif_dif(palavra):
    file = open("add_dif.txt","r")
    arq = transfLista(file)
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    for i in arq:
        if compararString(i,palavra) == True:
            file.close()
            return True
    return False

#####################################################################
#####################################################################

def tira_n_line(arq): #tira o \n do final da linha#
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    return arq    
        
def compararString(i, palavra): #compara string recebida pelo usuário com o elemento da lista#
  if i == palavra:
    compara = True
  else:
    compara = False
  return compara    
                
    
def transfLista(arq): #transforma as linhas em elementos de uma lista#
    
    arq.seek(0,0)
    arq = arq.readlines()
    return arq
def printalista(lista):
    for i in range(len(lista)):
        print(lista[i], end='\t')
    print()
        
master()
