def insere_fac(palavra): #verifica se existe ou não a palavra no dicionário#
    
    file1 = open("add_fac.txt","a")
    
    if verif_fac(palavra) == False:
        file1.write(palavra+'\n')
        print("Palavra adicionada.") 
    else:
        print("A palavra já existe nos fáceis.")

    file1.close()



def tira_n_line(myString): #tira o \n do final da linha#
    if myString[len(myString)-1] == "\n":
        myString = myString[:-1]

    return myString
    
        
        
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
    
    insere_fac(palavra)

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
