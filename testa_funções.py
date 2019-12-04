import time

def main(): #função pra teste, fiz apenas pra palavras faceis
    print("#######################################")
    print("######   BEM VINDO AO INICIADOR  ######")
    print("#######################################")
    print("")
    print("######          OPÇÕES           ######")
    print("")
    print("#######################################")
    print("# Adicionar/Excluir palavras aperte 1 #")
    print("#        Abrir o MENU aperte 2        #")
    print("#######################################")
    print("")
    print("")
    time.sleep(1)
    entrada = input("Opção do Usuário:\n")
    if entrada == "1":
        palavra = input("Insira a palavra: \n")
        palavra = palavra.lower()
        recebe = input("Aperte 1 para fácil \t 2 para Médio \t 3 para Difícil:\n")
        if recebe == "1":
            opt = input("Digite 1 se deseja adicionar ou 2 se deseja excluir:\n ")
            if opt == "1":
                insere_al(palavra)
                insere_fac(palavra)
            elif opt == "2":
                exclui_al(palavra)
                exclui_fac(palavra)
            else: 
                print("#        ERRO        #")
                print("#        ERRO        #")
                print("#        ERRO        #")
                time.sleep(1.5)
                main()

        elif recebe == "2":
            opt = input("Digite 1 se deseja adicionar ou 2 se deseja excluir:\n ")
            if opt == "1":
                insere_al(palavra)
                insere_med(palavra)
            elif opt == "2":
                exclui_al(palavra)
                exclui_med(palavra)
            else: 
                print("#        ERRO        #")
                print("#        ERRO        #")
                print("#        ERRO        #")
                time.sleep(1.5)
                main()

        elif recebe == "3":
            opt = input("Digite 1 se deseja adicionar ou 2 se deseja excluir:\n ")
            if opt == "1":
                insere_al(palavra)
                insere_dif(palavra)
            elif opt == "2":
                exclui_al(palavra)
                exclui_dif(palavra)
            else: 
                print("#        ERRO        #")
                print("#        ERRO        #")
                print("#        ERRO        #")
                time.sleep(1.5)
                main()
        else:
                print("#        ERRO        #")
                print("#        ERRO        #")
                print("#        ERRO        #")
                time.sleep(1.5)
                main()
        test = input("Deseja continuar? Digite 1 pra sim e 2 pra não:\n")
        if test == "1":
            main()
        elif test == "2":
            return
        else: 
            print("#        ERRO        #")
            print("#        ERRO        #")
            print("#        ERRO        #")
            time.sleep(1.5)
            main()


    elif entrada == "2":
        return
    
    else: 
        print("#        ERRO        #")
        print("#        ERRO        #")
        print("#        ERRO        #")
        time.sleep(1.5)
        main()

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

main()
