import matplotlib.pyplot as plt

def rp(x,p):
    str_x = str(x)
    leng_str = len(str_x)
    index_debut = 0
    new_x = 0
    s = 1
    nmb_zero = 0
    virgule = False #voir si on a vu toute la partie entière

    #savoir si negatif
    if str_x[0] ==  "-":
        s = -1
        str_x = str_x[1:]
        leng_str -= 1
    #calcul des zeros après la virgule
    while ((str_x[index_debut] == "0") or (str_x[index_debut] == ".")):
        index_debut += 1
        if str_x[index_debut] == ".":
            virgule = True
            nmb_zero -= index_debut
        else:
            nmb_zero += 1

    i = index_debut
    compteur=i
    
    #recupérer les chiffres significatifs
    while compteur < (p+index_debut) and i < leng_str:
        if str_x[i] == ".":
            compteur-=1
            virgule = True
        else:
            new_x = (new_x * 10 + int(str_x[i]))
            if virgule == True:
                nmb_zero += 1
        i+=1
        compteur += 1
    #arrondi au superieur /!\ pas virgule
    if i< leng_str and str_x[i] == ".":
        i+=1
        virgule=True
    if i< leng_str and int(str_x[i]) >= 5:
        new_x+=1

    #rajouter les zeros si nous n'avons pas atteind la virgule
    if i< leng_str and not(virgule):
        while str_x[i] != "." and i < len(str_x)-1:
            new_x *= 10
            i+=1
    return s*new_x*10**(-nmb_zero)


def delta_somme(x,y,p):
    x_machine = rp(x,p)
    y_machine = rp(y,p)
    return abs(x+y - (x_machine + y_machine))/abs(x+y)

def delta_prod(x,y,p):
    x_machine = rp(x,p)
    y_machine = rp(y,p)
    return abs(x*y - (x_machine * y_machine))/abs(x*y)

def aff_graphe_delta_s(x):
    plt.figure()
    plt.title("Delta somme")
    for p in range(2,6):
        Y_x=[]
        Y_delta_s=[]
        for y in range (50000,51000):
            Y_x.append(y/10000)
            Y_delta_s.append(delta_somme(x,y/10000,p))
        plt.plot(Y_x,Y_delta_s,label="p="+str(p))
    plt.legend()
    plt.show()
    return

def aff_graphe_delta_p(x):
    plt.figure()
    plt.title("Delta produit")
    for p in range(2,6):
        Y_x=[]
        Y_delta_s=[]
        for y in range (50000,51000):
            Y_x.append(y/10000)
            Y_delta_s.append(delta_prod(x,y/10000,p))
        plt.plot(Y_x,Y_delta_s,label="p="+str(p))
    plt.legend()
    plt.show()
    return


#test_rp
#print(rp(3.141592658,4)); print(rp(3.141592658,6))
#print(rp(10507.1823,4)); print(rp(10507.1823,6))
#print(rp(0.0001857563,4)); print(rp(0.0001857563,6))
#print(rp(1.5,1)); print(rp(1.8,3))

#test_delta
#print(delta_somme(3.141592658,10507.1823,4));print(delta_somme(3.141592658,10507.1823,6))
#print(delta_prod(3.141592658,10507.1823,4));print(delta_prod(3.141592658,10507.1823,6))

#test_graphe_s
aff_graphe_delta_s(10.26)

#test_graphe_p
aff_graphe_delta_p(10.26)
