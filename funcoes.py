def exclui_al(palavra):
    file = open("add_al.txt","r")
    arq = transfLista(file)
    arq = tira_n_line(arq)
    ifpop = False
    size = len(arq)
    cont = 0
    while cont < size:    
        if compararString(arq[cont],palavra) == True:
            removido = arq.pop(cont)
            size -= 1
            ifpop = True
            
        cont += 1    
    for i in range(len(arq)):
        arq[i] += '\n'
    
    file.close()
    return exclui0(ifpop,arq)

def exclui0(ifpop,arq):
    file = open("add_al.txt","w")
    if ifpop == True:
        for i in range(len(arq)):
            
            file.write(arq[i])
        return True

  
    else:
        return False
        
def exclui_fac(palavra):
    file = open("add_fac.txt","r")
    
    arq = transfLista(file)
    arq = tira_n_line(arq)
    ifpop = False
    size = len(arq)
    cont = 0
    while cont < size:
        
        if compararString(arq[cont],palavra) == True:
            removido = arq.pop(cont)
            size -= 1
            ifpop = True
            
        cont += 1    
    for i in range(len(arq)):
        arq[i] += '\n'
    
    file.close()
    return exclui1(ifpop,arq)

def exclui1(ifpop,arq):
    file = open("add_fac.txt","w")
    if ifpop == True:
        for i in range(len(arq)):
            
            file.write(arq[i])
        return True

  
    else:
        return False

def exclui_med(palavra):
    file = open("add_med.txt","r")
    
    arq = transfLista(file)
    arq = tira_n_line(arq)
    ifpop = False
    size = len(arq)
    cont = 0
    while cont < size:
        
        if compararString(arq[cont],palavra) == True:
            removido = arq.pop(cont)
            size -= 1
            ifpop = True
            
        cont += 1    
    for i in range(len(arq)):
        arq[i] += '\n'
    
    file.close()
    return exclui2(ifpop,arq)

def exclui2(ifpop,arq):
    file = open("add_med.txt","w")
    if ifpop == True:
        for i in range(len(arq)):
            
            file.write(arq[i])
        return True

  
    else:
        return False

def exclui_dif(palavra):
    file = open("add_dif.txt","r")
    
    arq = transfLista(file)
    arq = tira_n_line(arq)
    ifpop = False
    size = len(arq)
    cont = 0
    while cont < size:
        
        if compararString(arq[cont],palavra) == True:
            removido = arq.pop(cont)
            size -= 1
            ifpop = True
            
        cont += 1    
    for i in range(len(arq)):
        arq[i] += '\n'
    
    file.close()
    return exclui3(ifpop,arq)

def exclui3(ifpop,arq):
    file = open("add_dif.txt","w")
    if ifpop == True:
        for i in range(len(arq)):
            
            file.write(arq[i])
        return True

  
    else:
        return False

###############################################################
###############################################################
def insere_al(palavra): #verifica se existe ou não a palavra no dicionário# 
    file1 = open("add_al.txt","a")
    
    if verif_add_al(palavra) == False:
        file1.write(palavra+'\n')
        return False
    else:
        return True

    file1.close()
        
def insere_fac(palavra): #verifica se existe ou não a palavra no dicionário#
    
    file1 = open("add_fac.txt","a")
    
    if verif_add_fac(palavra) == False:
        file1.write(palavra+'\n')
        return False 
    else:
        return True

    file1.close()

def insere_med(palavra): #verifica se existe ou não a palavra no dicionário#
    
    file1 = open("add_med.txt","a")
    
    if verif_add_med(palavra) == False:
        file1.write(palavra+'\n')
        return False 
    else:
        return True

    file1.close()
    
def insere_dif(palavra): #verifica se existe ou não a palavra no dicionário#
    
    file1 = open("add_dif.txt","a")
    
    if verif_add_dif(palavra) == False:
        file1.write(palavra+'\n')
        return False
    else:
        return True

    file1.close()
        
def verif_add_al(palavra):
    file = open("add_al.txt","r")
    arq = transfLista(file)
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    for i in arq:
        if compararString(i,palavra) == True:
            file.close()
            return True
    return False

def verif_add_fac(palavra):    
    file = open("add_fac.txt","r")
    arq = transfLista(file)
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    for i in arq:
        if compararString(i,palavra) == True:
            file.close()
            return True
    return False

def verif_add_med(palavra):
    file = open("add_med.txt","r")
    arq = transfLista(file)
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    for i in arq:
        if compararString(i,palavra) == True:
            file.close()
            return True
    return False

def verif_add_dif(palavra):
    file = open("add_dif.txt","r")
    arq = transfLista(file)
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    for i in arq:
        if compararString(i,palavra) == True:
            file.close()
            return True
    return False

def verif_pad_al(palavra):
    file = open("pad_al.txt","r")
    arq = transfLista(file)
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    for i in arq:
        if compararString(i,palavra) == True:
            file.close()
            return True
    return False

def verif_pad_fac(palavra):    
    file = open("pad_fac.txt","r")
    arq = transfLista(file)
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    for i in arq:
        if compararString(i,palavra) == True:
            file.close()
            return True
    return False

def verif_pad_med(palavra):
    file = open("pad_med.txt","r")
    arq = transfLista(file)
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    for i in arq:
        if compararString(i,palavra) == True:
            file.close()
            return True
    return False

def verif_pad_dif(palavra):
    file = open("pad_dif.txt","r")
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
