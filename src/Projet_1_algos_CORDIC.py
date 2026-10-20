import math
import Projet_1_exo1 as pr
import matplotlib.pyplot as plt

# logarithme néperien de 2
def ln2(p):
    n1 = 0
    d = 0
    n2 = 1
    i = 1
    while abs(n2 - n1) > (10**(-p)):
        n1 = n2
        i += 1
        d += pr.delta_somme(n2, ((-1)**(i + 1)) / i, p)
        n2 = n2 + ((-1)**(i + 1)) / i
    return n2, d


# algorithme CORDIC du logarithme néperien
def ln(x):
    k = 0
    y = 0
    p = 1
    while k <= 6:
        while x >= p + p * 10**(-k):
            y += math.log(1 + 10 ** (-k))
            p += p * 10**(-k)
        k += 1
    return y + (x / p - 1)


# algorithme CORDIC de la fonction exponentielle
def exp(x):
    k = 0
    y = 1
    while k <= 6:
        while x >= math.log(1 + 10 ** (-k)):
            x += -math.log(1 + 10 ** (-k))
            y += y * 10 ** (-k)
        k += 1
    return y + y * x


# algorithme CORDIC de la fonction arctangeante
def arctan(x):
    k = 0
    y = 1
    r = 0
    
    while k <= 4:
        while x < y * 10 ** (-k):
            k += 1
        xp = x - y * 10**(-k)
        y += x * 10**(-k)
        x = xp
        r += math.atan(10**(-k))
    return r + (x / y)


# algorithme CORDIC de la fonction tangeante
def tan(x):
    k = 0
    n = 0
    d = 1
    while k <= 4:
        while x >= math.atan(10**(-k)):
            x -= math.atan(10**(-k))
            np = n + d * 10**(-k)
            d -= n * 10**(-k)
            n = np
        k += 1
    return (n + x * d) / (d - x * n)


# graphique du calcul de ln(2) selon la précision demandée
def aff_graphe_delta_ln2():
    Y_x=[]
    Y_delta_ln=[]
    for p in range(1,5):
        l = ln2(p)
        Y_x.append(l[0])
        Y_delta_ln.append(l[1])
    plt.title("Delta ln(2)")
    plt.plot(range(1,5),Y_delta_ln)
    plt.xlabel('Precision of values')
    plt.ylabel('Error in calculations')
    plt.legend()
    plt.show()
    return


# graphique du calcul de ln(x) sous différentes précisions en fonction des erreurs
def aff_graphe_delta_ln():
    for p in range(12, 17):
        i = 0
        Y_x=[]
        Y_delta_ln=[]
        plt.title("Delta ln")
        for y in range(5, 20):
            Y_x.append(pr.rp(math.log(y), p))
            Y_delta_ln.append(pr.rp(ln(y), p))
            Y_delta_ln[i] = (Y_delta_ln[i] - Y_x[i]) / Y_delta_ln[i]
            i += 1
        plt.plot(Y_x,Y_delta_ln,label="p="+str(p))
    plt.xlabel('Logarithmic value of integers from 5 to 20')
    plt.ylabel('Error in calculations')
    plt.legend()
    plt.show()
    return


# graphique du calcul de exp(x) sous différentes précisions en fonction des erreurs
def aff_graphe_delta_exp():
    for p in range(12,17):
        i = 0
        Y_x=[]
        Y_delta_exp=[]
        plt.title("Delta exp")
        for y in range(5, 20):
            Y_x.append(pr.rp(math.exp(y), p))
            Y_delta_exp.append(pr.rp(exp(y), p))
            Y_delta_exp[i] = (Y_x[i] - Y_delta_exp[i]) / Y_x[i]
            i += 1
        plt.plot(Y_x,Y_delta_exp,label="p="+str(p))
    plt.xlabel('Exponential value of integers from 5 to 20')
    plt.ylabel('Error in calculations')
    plt.legend()
    plt.show()
    return

# graphique du calcul de tan(x) sous différentes précisions en fonction des erreurs
def aff_graphe_delta_tan():
    for p in range(11,17):
        i = 0
        Y_x=[]
        Y_delta_tan=[]
        plt.title("Delta tan")
        for y in range(5, 20):
            Y_x.append(pr.rp(math.tan(y), p))
            Y_delta_tan.append(pr.rp(tan(y), p))
            Y_delta_tan[i] = (Y_x[i] - Y_delta_tan[i]) / Y_x[i]
            i += 1
        plt.plot(Y_x,Y_delta_tan,label="p="+str(p))
    plt.xlabel('Tangent value of integers from 5 to 20')
    plt.ylabel('Error in calculations')
    plt.legend()
    plt.show()
    return

# graphique du calcul de arctan(x) sous différentes précisions en fonction des erreurs
def aff_graphe_delta_atan():
    for p in range(12,17):
        i = 0
        Y_x=[]
        Y_delta_atan=[]
        plt.title("Delta arctan")
        for y in range(5, 20):
            Y_x.append(pr.rp(math.atan(y), p))
            Y_delta_atan.append(pr.rp(arctan(y), p))
            Y_delta_atan[i] = (Y_x[i] - Y_delta_atan[i]) / Y_x[i]
            i += 1
        plt.plot(Y_x,Y_delta_atan,label="p="+str(p))
    plt.xlabel('Arctangent value of integers from 5 to 20')
    plt.ylabel('Error in calculations')
    plt.legend()
    plt.show()
    return

#test fonctions
print(math.log(2), ln2(3))
print(math.log(5), ln(5))
print(math.exp(5), exp(5))
print(math.tan(5), tan(5))
print(math.atan(5), arctan(5))

#test ln(2)
aff_graphe_delta_ln2()

#graph ln() cordic
aff_graphe_delta_ln()

#graph exp() cordic
aff_graphe_delta_exp()

#graph tan() cordic
aff_graphe_delta_tan()

#graph atan() cordic
aff_graphe_delta_atan()