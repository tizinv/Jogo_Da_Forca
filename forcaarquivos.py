def dicio():
    referencia = {
        "p1":None,
        "p2":None,
        "p3":'bum',
        "p4":'xuxa',
        "p5":'None',
        "p6":None,
        "p7":None,
    }
    return referencia
def path():
    import os
    path = os.getcwd()
    return path
def cria():
    palavras = open(path() + "/palavras.txt","a")
    return palavras
def inseri(word):
    palavras = open(path() + "/palavras.txt","a")
    palavras.write(word + "\n")
    palavras.close
def conta():
    linhas=0
    palavras = open(path() + "/palavras.txt","r")
    for line in palavras:
        linhas+=1
    palavras.close()
    return linhas
def verifica():
    lista = []
    
    palavras = open(path() + "/palavras.txt","r")
    
    referencia = dicio()
    for word in palavras:
        lista.append(word.strip())
    print(lista)
    linhas = len(lista)
    contadoradd=0
    for cont in range (0,linhas,1):
        if ( lista[cont] in referencia.values()):
            chave = True
            print("deu certo",cont)
        else:
            print(palavras.readline())
            chave = False
            contadoradd+=1
            print("deu errado")
            referencia["p"+str(contadoradd+7)]= lista[cont]
            
            #for i in referencia:
                #print(referencia[i])
    print(referencia)
    return(lista)
def sorteio():
    import random
    lista = []
    lista = verifica()    
    sortword = random.choice(lista)
    return sortword
def dichava():
    palavra = sorteio()
    lista = []
    for letra in palavra:
        lista.append(letra)
    return lista
def forcacompara():
    lista = dichava()
    listaprint = []
    listaposi = []
    for i in range(len(lista)):
            listaprint.append("x")
    print(listaprint)
    while(lista!=listaprint):
        letra = str(input("inserir a letra:"))
        if(letra in lista):
            for l in range(len(lista)):
                if(letra in lista[l]):
                    listaposi.append(l)
            print(listaposi)
            print("deucerto")
            for posi in listaposi:
                listaprint[posi]=letra
        print(listaprint)
        print(lista)
        listaposi = []
    print(lista)
    


    
#cria()
#inseri(input("palavra:"))
#conta()
#verifica()
#sorteio()
#dichava()
forcacompara()
