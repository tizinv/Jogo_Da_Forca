def insere_fac(palavra): #verifica se existe ou não a palavra no dicionário#
    
    file1 = open("add_fac.txt","a")
    
    if verif_fac(palavra) == False:
        file1.write(palavra+'\n')
        print("Palavra adicionada.") 
    else:
        print("A palavra já existe nos fáceis.")

    file1.close()


def exclui_fac(palavra):
    file1 = open("add_fac.txt","r")
    
    arq = transfLista(file1)
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
    file1.close()
    exclui(ifpop,arq)

def exclui(ifpop,arq):
    file = open("add_fac.txt","w")
    if ifpop == True:
        for i in range(len(arq)):
            
            file.write(arq[i])
        print("Palavra excluida.")

  
    else:
        print("Palavra nao existe para ser excluida.")


def tira_n_line(arq): #tira o \n do final da linha#
    for elem in range(len(arq)):
        arq[elem] = arq[elem].strip()
    return arq
        
        
#def verif_al(palavra):
#    file = open("add_al.txt","r")
#    arq = transfLista(file)
#    for i in arq:
#        if compararString(i,palavra)== False:
#            return False
#        else:
#            return True
#    file.close()

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


#def verif_med(palavra):
#    file = open("add_med.txt","r")
#    arq = transfLista(file)
#    for i in arq:
#        if compararString(i,palavra)== False:
#            return False
#        else:
#            return True
#    file.close()

#def verif_dif(palavra):
#    file = open("add_dif.txt","r")
#    arq = transfLista(file)
#    
#    for i in arq:
#        if compararString(i,palavra)== False:
#            return False
#        else:
#            return True
#    file.close()

def main(): #função pra teste, fiz apenas pra palavras faceis
    palavra = input("Insira qual palavra deseja adicionar: ")
    palavra = palavra.lower()
    #print("1 para fácil \t 2 para medio \t 3 para dificil")
    opt = int(input("Digite 1 se deseja adicionar ou 2 se deseja excluir: "))
    if opt == 1:    
      insere_fac(palavra)
    else:
      exclui_fac(palavra)

    test = int(input("Deseja continuar? Digite 1 pra sim e 2 pra não: "))
    if test == 1:
        main()

    
        
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
